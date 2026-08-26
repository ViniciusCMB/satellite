"""
Exporta artefatos da simulacao Helike/Dedalo para a landing page do GitHub Pages.

Roda headless (sem display), re-executa a simulacao com GFS e gera:
  - data/landing.json                 -> KPIs (apogeu, drift, area, GFS metadata)
  - data/trajectory_3d.json           -> Plotly trace (ascent + parachute + SRAB)
  - data/trajectory_topdown.geojson   -> Polylines vista superior (Leaflet)

Target launch: 2026-09-04 09:00 BRT (UTC-03) = 2026-09-04 12:00 UTC.
A simulacao e re-rodada com GFS mais recente para essa data/hora.

Uso:
    python export_landing_data.py
"""
from __future__ import annotations

import json
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")

# Paths (this script: extras/wing-analysis/scripts/export_landing_data.py)
SCRIPT_DIR = Path(__file__).resolve().parent
NB_DIR = SCRIPT_DIR.parent / "notebooks"
WING_SRC = SCRIPT_DIR.parent / "src"
GEOMETRY = SCRIPT_DIR.parent / "geometry"
OUT_DIR = SCRIPT_DIR.parent.parent.parent / "docs" / "landing" / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WING_SRC))

# Launch parameters (LASC 2026, Helike mission #213)
LAT = -21.9430528
LON = -48.9540861
ELEV = 478
LAUNCH_LOCAL_STR = "2026-09-04T09:00:00-03:00"
LAUNCH_UTC = datetime(2026, 9, 3, 12, 0, 0, tzinfo=timezone.utc)

RAIL_LENGTH = 4.0
INCLINATION = 85
HEADING = 0
PAYLOAD_MASS = 0.200  # kg (PocketQube 1P)

# SRAB
VF_MAX = 20.0
SAFETY_FACTOR = 1.5
VF_TARGET = VF_MAX / SAFETY_FACTOR  # 13.33 m/s

# Wing DXF (same as notebook 01_simulacao_dedalo.ipynb)
DXF_FILE = "Asa3.DXF"
N_WINGS = 2


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_environment():
    from rocketpy import Environment

    env = Environment(latitude=LAT, longitude=LON, elevation=ELEV)
    env.set_date(LAUNCH_UTC)
    env.set_atmospheric_model(type="Forecast", file="GFS")
    return env


def load_motor():
    from rocketpy import SolidMotor
    import pandas as pd

    motor_data = pd.read_csv(NB_DIR / "motor.csv")
    with open(NB_DIR / "dedalo_motor.json") as f:
        cfg = json.load(f)

    return SolidMotor(
        thrust_source=motor_data,
        dry_mass=cfg["dry_mass"],
        dry_inertia=cfg["dry_inertia"],
        nozzle_radius=cfg["nozzle_radius"],
        grain_number=cfg["grain_number"],
        grain_density=cfg["grain_density"],
        grain_outer_radius=cfg["grain_outer_radius"],
        grain_initial_inner_radius=cfg["grain_initial_inner_radius"],
        grain_initial_height=cfg["grain_initial_height"],
        grain_separation=cfg["grain_separation"],
        grains_center_of_mass_position=cfg["grains_center_of_mass_position"],
        center_of_dry_mass_position=cfg["center_of_dry_mass_position"],
        nozzle_position=cfg["nozzle_position"],
        burn_time=motor_data["Time(s)"].iloc[-1],
        throat_radius=cfg["throat_radius"],
        coordinate_system_orientation=cfg["coordinate_system_orientation"],
    )


def build_rocket(motor, with_payload: bool):
    from rocketpy import Rocket

    with open(NB_DIR / "dedalo_data.json") as f:
        cfg = json.load(f)

    mass = cfg["mass"] + (PAYLOAD_MASS if with_payload else 0.0)
    rocket = Rocket(
        radius=cfg["radius"],
        mass=mass,
        inertia=cfg["inertia"],
        power_off_drag=str(NB_DIR / "power_off_drag.csv"),
        power_on_drag=str(NB_DIR / "power_on_drag.csv"),
        center_of_mass_without_motor=cfg["center_of_mass_without_motor"],
        coordinate_system_orientation=cfg["coordinate_system_orientation"],
    )
    rocket.add_motor(motor, position=1.65)
    rocket.add_nose(
        length=cfg["nose_length"],
        kind=cfg["nose_type"],
        position=cfg["nose_position"],
    )
    rocket.add_trapezoidal_fins(
        n=cfg["n_aletas"],
        root_chord=cfg["root_chord"],
        tip_chord=cfg["tip_chord"],
        span=cfg["span"],
        position=cfg["position"],
        cant_angle=cfg["cant_angle"],
    )
    if not with_payload:
        # Parachute parameters match the notebook Stage 2
        def apogee_acc_trigger(_pressure, _height, state_vector, u_dot):
            vz = state_vector[5]
            az = u_dot[5]
            return abs(vz) < 1.0 and az < -0.1

        rocket.add_parachute(
            "Main",
            cd_s=1.5,
            trigger=apogee_acc_trigger,
            sampling_rate=105,
            lag=1.5,
            radius=0.6,
            noise=(0, 8.3, 0.5),
        )
    return rocket


def run_ascent(env, rocket_full):
    from rocketpy import Flight
    return Flight(
        rocket=rocket_full,
        environment=env,
        rail_length=RAIL_LENGTH,
        inclination=INCLINATION,
        heading=HEADING,
        terminate_on_apogee=True,
        verbose=False,
    )


def run_parachute_descent(env, rocket_empty, ascent):
    from rocketpy import Flight
    return Flight(
        rocket=rocket_empty,
        environment=env,
        rail_length=RAIL_LENGTH,
        inclination=INCLINATION,
        heading=HEADING,
        initial_solution=ascent,
        verbose=False,
        max_time=600,
    )


def run_srab(env, ascent):
    from rocketpy_samara.srab_recovery import SRABRecovery
    from samara_pq_simulation import PocketQubeSamaraWing

    wing = PocketQubeSamaraWing(
        dxf_path=str(GEOMETRY / DXF_FILE),
        n_wings=N_WINGS,
        mass=PAYLOAD_MASS,
    )
    srab = SRABRecovery(
        wing=wing,
        env=env,
        optimize=True,
        target_vf=VF_TARGET,
        safety_factor=SAFETY_FACTOR,
        n_wings=N_WINGS,
    )
    sol = srab.simulate_from_flight(ascent, target_vf=VF_TARGET)
    return srab, sol


def downsample(t, x, y, z, max_points=200):
    n = len(t)
    if n <= max_points:
        return t, x, y, z
    step = max(1, n // max_points)
    return t[::step], x[::step], y[::step], z[::step]


def compute_impact_zone(parachute_xy, srab_xy, landing_uncert_m=200):
    """Impact ellipse: combines parachute point + SRAB + GFS uncertainty."""
    import numpy as np
    pts = np.array([parachute_xy, srab_xy])
    cx, cy = pts.mean(axis=0)
    semi_a = max(np.linalg.norm(pts[0] - pts[1]) / 2 + landing_uncert_m, landing_uncert_m)
    semi_b = landing_uncert_m
    return {
        "center_x_m": float(cx),
        "center_y_m": float(cy),
        "semi_axis_a_m": float(semi_a),
        "semi_axis_b_m": float(semi_b),
        "area_km2": float(np.pi * semi_a * semi_b / 1e6),
    }


def main():
    import numpy as np

    print(f"[{now_utc_iso()}] Starting landing page export...")
    print(f"  Target launch: {LAUNCH_LOCAL_STR} (12:00 UTC)")

    print("[1/6] Loading Environment (GFS forecast)...")
    env = load_environment()

    print("[2/6] Building Dedalo (with payload + without payload)...")
    motor = load_motor()
    rocket_full = build_rocket(motor, with_payload=True)
    rocket_empty = build_rocket(motor, with_payload=False)

    print("[3/6] Ascent (Stage 1) to apogee...")
    ascent = run_ascent(env, rocket_full)
    apogee_agl = float(ascent.apogee - env.elevation)
    apogee_asl = float(ascent.apogee)
    apogee_time = float(ascent.apogee_time)
    print(f"      Apogee: {apogee_agl:.0f} m AGL / {apogee_asl:.0f} m ASL @ t={apogee_time:.1f}s")

    print("[4/6] Parachute descent (Stage 2)...")
    parachute = run_parachute_descent(env, rocket_empty, ascent)
    parachute_impact = (float(parachute.x_impact), float(parachute.y_impact))
    parachute_time = float(parachute.t_final)
    print(f"      Parachute impact: ({parachute_impact[0]:.1f}, {parachute_impact[1]:.1f}) m @ t={parachute_time:.1f}s")

    print("[5/6] SRAB descent (Stage 3)...")
    srab, srab_sol = run_srab(env, ascent)
    srab_impact = (float(srab_sol.x_impact), float(srab_sol.y_impact))
    srab_time = float(srab_sol.t_impact)
    srab_v_impact = float(srab_sol.v_impact)
    srab_spin_rpm = float(srab_sol.spin_impact_rpm)
    srab_drift = float(np.hypot(*srab_impact))
    print(f"      SRAB impact: ({srab_impact[0]:.1f}, {srab_impact[1]:.1f}) m, |v|={srab_v_impact:.2f} m/s")

    print("[6/6] Generating JSON/GeoJSON artifacts...")

    # Impact lat/lon (simple geodesic offset)
    dlat = srab_impact[0] / 111320.0
    dlon = srab_impact[1] / (111320.0 * 0.85)
    impact_lat = LAT + dlat
    impact_lon = LON + dlon

    area = compute_impact_zone(parachute_impact, srab_impact, landing_uncert_m=200)

    # Trajectories
    t_asc = np.linspace(0, apogee_time, 60)
    x_asc = np.array([float(ascent.x(t)) for t in t_asc])
    y_asc = np.array([float(ascent.y(t)) for t in t_asc])
    z_asc = np.array([float(ascent.z(t)) - env.elevation for t in t_asc])

    t_par = np.linspace(0, parachute_time, 80)
    x_par = np.array([float(parachute.x(t)) for t in t_par])
    y_par = np.array([float(parachute.y(t)) for t in t_par])
    z_par = np.array([float(parachute.z(t)) - env.elevation for t in t_par])

    t_srab = np.array(srab_sol.t)
    z_srab = np.array(srab_sol.altitude)
    x_srab = np.array(srab_sol.x)
    y_srab = np.array(srab_sol.y)
    t_srab_ds, x_srab_ds, y_srab_ds, z_srab_ds = downsample(t_srab, x_srab, y_srab, z_srab, max_points=200)

    # Main JSON (KPIs)
    landing = {
        "generated_at_utc": now_utc_iso(),
        "launch": {
            "datetime_local_brt": LAUNCH_LOCAL_STR,
            "datetime_utc": LAUNCH_UTC.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "latitude": LAT,
            "longitude": LON,
            "elevation_m": ELEV,
            "rail_length_m": RAIL_LENGTH,
            "inclination_deg": INCLINATION,
            "heading_deg": HEADING,
        },
        "atmospheric_model": {
            "type": "GFS",
            "gfs_run_date_utc": LAUNCH_UTC.strftime("%Y-%m-%d"),
            "note": "GFS forecast for 2026-09-04 12:00 UTC. Updated every 6h (00/06/12/18Z).",
        },
        "ascent": {
            "apogee_m_agl": apogee_agl,
            "apogee_m_asl": apogee_asl,
            "apogee_time_s": apogee_time,
            "out_of_rail_velocity_m_s": float(ascent.out_of_rail_velocity),
            "max_speed_m_s": float(ascent.max_speed),
            "max_mach": float(ascent.max_mach_number),
            "max_acceleration_m_s2": float(ascent.max_acceleration),
            "max_acceleration_g": float(ascent.max_acceleration) / 9.80665,
        },
        "parachute_descent": {
            "impact_x_m": parachute_impact[0],
            "impact_y_m": parachute_impact[1],
            "drift_m": float(np.hypot(*parachute_impact)),
            "descent_time_s": parachute_time,
        },
        "srab_descent": {
            "impact_x_m": srab_impact[0],
            "impact_y_m": srab_impact[1],
            "drift_m": srab_drift,
            "descent_time_s": srab_time,
            "impact_velocity_m_s": srab_v_impact,
            "impact_spin_rpm": srab_spin_rpm,
            "target_velocity_m_s": VF_TARGET,
            "lasc_limit_m_s": VF_MAX,
        },
        "impact_zone": {
            **area,
            "impact_lat": float(impact_lat),
            "impact_lon": float(impact_lon),
        },
    }
    (OUT_DIR / "landing.json").write_text(json.dumps(landing, indent=2))
    print(f"  -> landing.json")

    # Plotly 3D
    traj3d = {
        "ascent": {
            "t": t_asc.tolist(),
            "x": x_asc.tolist(),
            "y": y_asc.tolist(),
            "z": z_asc.tolist(),
        },
        "parachute": {
            "t": (t_par + apogee_time).tolist(),
            "x": x_par.tolist(),
            "y": y_par.tolist(),
            "z": z_par.tolist(),
        },
        "srab": {
            "t": (t_srab_ds + apogee_time).tolist(),
            "x": x_srab_ds.tolist(),
            "y": y_srab_ds.tolist(),
            "z": z_srab_ds.tolist(),
        },
        "apogee_point": {
            "x": float(ascent.x(apogee_time)),
            "y": float(ascent.y(apogee_time)),
            "z": apogee_agl,
        },
    }
    (OUT_DIR / "trajectory_3d.json").write_text(json.dumps(traj3d))
    print(f"  -> trajectory_3d.json")

    # Top-down GeoJSON
    def to_lonlat(x_m, y_m):
        return [LON + y_m / (111320.0 * 0.85), LAT + x_m / 111320.0]

    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "Ascent (Stage 1)", "color": "#ff6b35", "stage": "ascent"},
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[LON, LAT]] + [to_lonlat(x, y) for x, y in zip(x_asc, y_asc)],
                },
            },
            {
                "type": "Feature",
                "properties": {"name": "Parachute descent (Stage 2)", "color": "#3498db", "stage": "parachute"},
                "geometry": {
                    "type": "LineString",
                    "coordinates": [to_lonlat(x, y) for x, y in zip(x_par, y_par)],
                },
            },
            {
                "type": "Feature",
                "properties": {"name": "SRAB descent (Stage 3)", "color": "#9b59b6", "stage": "srab"},
                "geometry": {
                    "type": "LineString",
                    "coordinates": [to_lonlat(x, y) for x, y in zip(x_srab_ds, y_srab_ds)],
                },
            },
            {
                "type": "Feature",
                "properties": {"name": "Estimated impact zone", "stage": "impact"},
                "geometry": {"type": "Point", "coordinates": [float(impact_lon), float(impact_lat)]},
            },
            {
                "type": "Feature",
                "properties": {"name": "Launch pad", "stage": "launch"},
                "geometry": {"type": "Point", "coordinates": [LON, LAT]},
            },
        ],
    }
    (OUT_DIR / "trajectory_topdown.geojson").write_text(json.dumps(geojson))
    print(f"  -> trajectory_topdown.geojson")

    print(f"\n[OK] Done. Output at: {OUT_DIR}")
    print(f"     Apogee: {apogee_agl:.0f} m AGL")
    print(f"     SRAB impact velocity: {srab_v_impact:.2f} m/s (LASC limit: {VF_MAX})")
    print(f"     Estimated area: {area['area_km2']:.3f} km²")


if __name__ == "__main__":
    main()
