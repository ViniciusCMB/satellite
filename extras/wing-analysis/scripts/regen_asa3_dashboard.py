#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate Asa3 LRR dashboard with current English script."""

import sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')

SRC = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC))

from samara_pq_simulation import PocketQubeSamaraWing
from rocketpy_samara.srab_recovery import SRABRecovery
from rocketpy_samara.plotting import plot_lrr_dashboard
from rocketpy import Environment
from datetime import datetime, timedelta

DXF_PATH = Path(__file__).resolve().parent.parent / "geometry" / "Asa3.DXF"
OUT_DIR = Path(__file__).resolve().parent.parent.parent / "docs" / "mission-report" / "figures"

print("=" * 60)
print("  Regenerating Asa3 LRR dashboard (English)")
print("=" * 60)

wing = PocketQubeSamaraWing(
    dxf_path=str(DXF_PATH),
    n_wings=2,
    mass=0.200,
    f_factor=0.3,
    cd0=1.0,
    rho=1.225,
    beta_deg=5.0,
)

print(f"  Wings: {wing.n_wings}, Radius: {wing.radius*100:.2f} cm")

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
    target_vf=13.33,
    safety_factor=1.5,
)

# Use simulate() with explicit initial conditions
# [theta, theta_dot, phi_dot, v0, z_alt]
initial_conditions = [0.0, 0.0, 0.1, 0.0, 1520.5]
print("\n  Running simulation...")
sol = srab.simulate(initial_conditions=initial_conditions)

print(f"\n  Results:")
print(f"    Impact velocity: {sol.v_impact:.2f} m/s")
print(f"    Descent time: {sol.t_impact:.1f} s")
print(f"    Equilibrium angle: {sol.theta_eq:.1f}°")
print(f"    Spin at impact: {sol.spin_impact_rpm:.1f} RPM")

# Generate and save dashboard
print("\n  Generating LRR dashboard...")
fig = plot_lrr_dashboard(sol)
output_path = OUT_DIR / "fig_asa3_lrr.png"
fig.savefig(str(output_path), dpi=150, bbox_inches="tight")
print(f"  Saved: {output_path}")

print("\n" + "=" * 60)
print("  DONE")
print("=" * 60)
