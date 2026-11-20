#!/usr/bin/env python3
"""Asa3.DXF + 4 asas, SEM otimização de raio. GFS + plots + geometria + mapa."""

import sys
from datetime import datetime, timedelta
from pathlib import Path

_SRC = Path(__file__).resolve().parent.parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from samara_pq_simulation import PocketQubeSamaraWing, plot_wing_geometry_views
from rocketpy_samara.srab_recovery import SRABRecovery
from rocketpy_samara.plotting import plot_lrr_dashboard, plot_trajectory_map, _plot_srab_only

DXF = _SRC.parent / "geometry" / "Asa3.DXF"

params = dict(
    dxf_path=str(DXF),
    n_wings=4,
    mass_kg=0.200,
    altitude_m=1000.0,
    theta_deg=0.0,
    phi_dot_0=0.0,
    v0_0=0.0,
    beta_deg=5.0,
    cd0=1.0,
    f_factor=0.3,
    rho=1.225,
    t_max=600.0,
    max_step=0.2,
    optimize=False,
)

LAT, LON, ELEV = -21.942472, -48.952111, 478
OUT = _SRC.parent.parent / "results"
OUT.mkdir(parents=True, exist_ok=True)

print("=" * 65)
print("  Asa3.DXF + 4 asas — SEM otimização")
print("=" * 65)

from rocketpy import Environment
env = Environment(latitude=LAT, longitude=LON, elevation=ELEV)
env.set_date(datetime.now() + timedelta(days=1))
env.set_atmospheric_model(type="forecast", file="GFS")
print(f"  ρ(0) = {env.density.get_value_opt(0):.4f} kg/m³")
print(f"  ρ(1000 m) = {env.density.get_value_opt(1000):.4f} kg/m³")

wing = PocketQubeSamaraWing(
    dxf_path=params["dxf_path"],
    n_wings=params["n_wings"],
    mass=params["mass_kg"],
    f_factor=params["f_factor"],
    cd0=params["cd0"],
    rho=params["rho"],
    beta_deg=params["beta_deg"],
)

recovery = SRABRecovery(wing, env=env, **params)
sol = recovery.simulate()

print(f"\n  Raio DXF original:   {wing.radius * 100:.2f} cm")
print(f"  r0 → rf:             {wing.r0 * 1e3:.1f} → {wing.rf * 1e3:.1f} mm")
print(f"  Área total asas:     {wing.n_wings * wing.wing_area_one_m2 * 1e4:.1f} cm²")
print(f"  v_impacto:           {sol.v_impact:.2f} m/s")
print(f"  t_descida:           {sol.t_impact:.1f} s")
print(f"  θ_eq:                {sol.theta_eq:.1f}°")
print(f"  Spin impacto:        {sol.spin_impact_rpm:.1f} RPM")
print(f"  Deriva:              ({sol.x_impact:.1f}, {sol.y_impact:.1f}) m")

plot_wing_geometry_views(wing, theta_eq_deg=sol.theta_eq, output_dir=str(OUT))

_plot_srab_only(sol).savefig(str(OUT / "trajetoria_3d_asa3_4w_sem_otim.png"), dpi=150, bbox_inches="tight")
plot_lrr_dashboard(sol).savefig(str(OUT / "lrr_dashboard_asa3_4w_sem_otim.png"), dpi=150, bbox_inches="tight")
plot_trajectory_map(sol, lat=LAT, lon=LON, filename=str(OUT / "mapa_descida_asa3_4w_sem_otim.html"), zoom=15)

print("\n" + "=" * 65)
print("  CONCLUÍDO")
print(f"  Saída: {OUT}/")
print("=" * 65)
