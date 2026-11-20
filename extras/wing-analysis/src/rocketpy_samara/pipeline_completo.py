#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pipeline completo: GFS + otimização única + Monte Carlo 1000 iterações
+ trajetória 3D + mapa satélite + dashboard LRR + dispersão.

Uso:
    python pipeline_completo.py

Requer: rocketpy, folium, ezdxf, matplotlib, numpy, scipy
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

_SRC = Path(__file__).resolve().parent.parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from samara_pq_simulation import PocketQubeSamaraWing
from rocketpy_samara.srab_recovery import SRABRecovery
from rocketpy_samara.monte_carlo import SRABMonteCarlo
from rocketpy_samara.plotting import (
    plot_lrr_dashboard,
    plot_dispersion,
    plot_trajectory_map,
    _plot_srab_only,
)

# =============================================================================
# Parâmetros do usuário (mesmos do CLI de referência)
# =============================================================================
DXF = _SRC.parent / "geometry" / "Asa3.DXF"

params = dict(
    dxf_path=str(DXF),
    n_wings=2,
    mass_kg=0.200,
    altitude_m=1000.0,
    theta_deg=0.0,
    theta_dot_0=0.0,
    phi_dot_0=0.0,
    v0_0=0.0,
    beta_deg=5.0,
    cd0=1.0,
    f_factor=0.3,
    rho=1.225,
    t_max=600.0,
    max_step=0.2,
    optimize=True,
    target_vf=20.0,
    safety_factor=1.5,
)

# Coordenadas de lançamento (LASC / Tatuí-SP)
LAT, LON, ELEV = -21.942472, -48.952111, 478

# Número de iterações Monte Carlo
N_MC = 1000

# Diretório de saída
OUT = _SRC.parent.parent / "results"
OUT.mkdir(parents=True, exist_ok=True)

# =============================================================================
# 1. Ambiente GFS (densidade + vento realistas)
# =============================================================================
print("=" * 65)
print("  [1/5] Configurando ambiente GFS...")
print("=" * 65)

from rocketpy import Environment  # noqa: E402

env = Environment(latitude=LAT, longitude=LON, elevation=ELEV)
env.set_date(datetime.now() + timedelta(days=1))
env.set_atmospheric_model(type="forecast", file="GFS")
print(f"  ρ(0) = {env.density.get_value_opt(0):.4f} kg/m³")
print(f"  ρ(1000 m) = {env.density.get_value_opt(1000):.4f} kg/m³")

# =============================================================================
# 2. Otimização única (encontra o raio ideal)
# =============================================================================
print("\n" + "=" * 65)
print("  [2/5] Otimização única do raio aerodinâmico...")
print("=" * 65)

wing = PocketQubeSamaraWing(
    dxf_path=params["dxf_path"],
    n_wings=params["n_wings"],
    mass=params["mass_kg"],
    f_factor=params["f_factor"],
    cd0=params["cd0"],
    rho=params["rho"],
    beta_deg=params["beta_deg"],
)

vf_target = params["target_vf"] / params["safety_factor"]
opt_params = dict(params)
opt_params["target_vf"] = vf_target

recovery_opt = SRABRecovery(wing, env=env, **opt_params)

# Força re-otimização mesmo se wing já tiver radius otimizado
sol_ref = recovery_opt.simulate()

print(f"\n  Resultado da otimização:")
print(f"  Raio aerodinâmico: {wing.radius * 100:.2f} cm")
print(f"  v_impacto:         {sol_ref.v_impact:.2f} m/s (alvo: {vf_target:.2f})")
print(f"  t_descida:         {sol_ref.t_impact:.1f} s")
print(f"  Spin impacto:      {sol_ref.spin_impact_rpm:.1f} RPM")
print(f"  Deriva:            ({sol_ref.x_impact:.1f}, {sol_ref.y_impact:.1f}) m")

# =============================================================================
# 3. Monte Carlo (1000 iterações, sem otimização — raio fixo)
# =============================================================================
print("\n" + "=" * 65)
print("  [3/5] Monte Carlo — 1000 iterações...")
print("=" * 65)

mc_params = dict(params)
mc_params["optimize"] = False

recovery_mc = SRABRecovery(wing, env=env, **mc_params)

mc = SRABMonteCarlo(recovery_mc, n=1000, seed=42)

mc.add_param("mass_kg", "normal", (0.200, 0.010))
mc.add_param("beta_deg", "normal", (5.0, 0.5))
mc.add_param("cd0", "normal", (1.0, 0.15))
mc.add_param("n_wings", "discrete", (2, 4))

mc.run(verbose=True)
mc.print_summary()
mc.export_csv(str(OUT / "mc_pipeline_1000.csv"))

stats = mc.process()
print(f"\n  CEP radius:          {stats['cep_radius']:.2f} m")
print(f"  LASC pass rate:      {stats['lasc_window_pass_rate'] * 100:.1f}%")

# =============================================================================
# 4. Plot 3D da trajetória
# =============================================================================
print("\n" + "=" * 65)
print("  [4/5] Gerando plots...")
print("=" * 65)

fig3d = _plot_srab_only(sol_ref)
fig3d.savefig(str(OUT / "trajetoria_3d_gfs.png"), dpi=150, bbox_inches="tight")
print(f"  3D plot: {OUT / 'trajetoria_3d_gfs.png'}")

# Dashboard LRR
fig_lrr = plot_lrr_dashboard(sol_ref)
fig_lrr.savefig(str(OUT / "lrr_dashboard_gfs.png"), dpi=150, bbox_inches="tight")
print(f"  LRR dashboard: {OUT / 'lrr_dashboard_gfs.png'}")

# Dispersão MC
fig_disp = plot_dispersion(mc)
fig_disp.savefig(str(OUT / "dispersao_mc_1000.png"), dpi=150, bbox_inches="tight")
print(f"  Dispersão MC: {OUT / 'dispersao_mc_1000.png'}")

# =============================================================================
# 5. Mapa satélite HTML (folium)
# =============================================================================
print("\n" + "=" * 65)
print("  [5/5] Gerando mapa satélite HTML...")
print("=" * 65)

plot_trajectory_map(
    sol_ref,
    lat=LAT,
    lon=LON,
    filename=str(OUT / "mapa_descida_gfs.html"),
    zoom=15,
)

# =============================================================================
# Sumário final
# =============================================================================
print("\n" + "=" * 65)
print("  PIPELINE COMPLETO — RESUMO")
print("=" * 65)
print(f"  Raio otimizado:       {wing.radius * 100:.2f} cm")
print(f"  v_impacto (nominal):  {sol_ref.v_impact:.2f} m/s")
print(f"  t_descida (nominal):  {sol_ref.t_impact:.1f} s")
print(f"  MC iterações:         {mc.n}")
print(f"  v_impacto médio MC:   {stats['v_impact_mean']:.2f} ± {stats['v_impact_std']:.2f} m/s")
print(f"  CEP radius:           {stats['cep_radius']:.2f} m")
print(f"  LASC pass rate:       {stats['lasc_window_pass_rate'] * 100:.1f}%")
print(f"  Saída:                {OUT}/")
print("=" * 65)
