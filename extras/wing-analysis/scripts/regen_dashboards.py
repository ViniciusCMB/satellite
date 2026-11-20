#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate dashboard images for mission report in English."""

import sys
from pathlib import Path

# Add src to path
SRC = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC))

from samara_pq_simulation import PocketQubeSamaraWing
from rocketpy_samara.srab_recovery import SRABRecovery
from rocketpy_samara.plotting import plot_lrr_dashboard
from rocketpy import Environment
from datetime import datetime, timedelta

# Parameters for Asa3 (final mission configuration)
DXF_PATH = Path(__file__).resolve().parent.parent / "geometry" / "Asa3.DXF"
OUT_DIR = Path(__file__).resolve().parent.parent.parent / "docs" / "mission-report" / "figures"

print("=" * 60)
print("  Regenerating mission report dashboards (English)")
print("=" * 60)

# Create wing
wing = PocketQubeSamaraWing(
    dxf_path=str(DXF_PATH),
    n_wings=2,
    mass=0.200,  # 200 g
    f_factor=0.3,
    cd0=1.0,
    rho=1.225,
    beta_deg=5.0,
)

print(f"\n  Wing parameters:")
print(f"    DXF: {DXF_PATH}")
print(f"    Wings: {wing.n_wings}")
print(f"    Mass: {wing.mass * 1000:.0f} g")
print(f"    Radius: {wing.radius * 100:.2f} cm")

# Use same conditions as notebook
LAT, LON, ELEV = -21.942472, -48.952111, 478
env = Environment(latitude=LAT, longitude=LON, elevation=ELEV)
env.set_date(datetime.now() + timedelta(days=1))
env.set_atmospheric_model(type="forecast", file="GFS")

srab = SRABRecovery(
    wing, env=env,
    dxf_path=str(DXF_PATH),
    n_wings=2,
    mass_kg=0.200,
    theta_deg=0.0,
    theta_dot_0=0.0,
    phi_dot_0=0.1,
    v0_0=0.0,
    beta_deg=5.0,
    cd0=1.0,
    f_factor=0.3,
    rho=1.225,
    t_max=300.0,
    max_step=0.2,
    optimize=True,
    target_vf=13.33,  # 20/1.5
    safety_factor=1.5,
)

# Simulate from apogee (1520.5 m) using basic simulate method
print("\n  Running simulation...")
# Initial conditions: altitude=1520.5m, v_z=0 (apogee), theta=0, phi_dot=0.1 rad/s
initial_conditions = [1520.5, 0.0, 0.0, 0.0, 0.1]  # [z, v_z, theta, theta_dot, phi_dot]
sol = srab.simulate(initial_conditions=initial_conditions)

print(f"\n  Results:")
print(f"    Impact velocity: {sol.v_impact:.2f} m/s")
print(f"    Descent time: {sol.t_impact:.1f} s")
print(f"    Equilibrium angle: {sol.theta_eq:.1f}°")
print(f"    Spin at impact: {sol.spin_impact_rpm:.1f} RPM")

# Generate dashboard
print("\n  Generating LRR dashboard...")
fig = plot_lrr_dashboard(sol)
output_path = OUT_DIR / "fig_asa3_lrr.png"
fig.savefig(str(output_path), dpi=150, bbox_inches="tight")
print(f"  Saved: {output_path}")

print("\n" + "=" * 60)
print("  DONE")
print("=" * 60)
