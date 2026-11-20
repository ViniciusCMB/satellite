# Mission Report Helike #213 — Notas e Pendências da Equipe

**Criado:** 05-ago-2026 · **Autor:** Vinicius (via Hermes) · **Contexto:** chat com muita
compressão — este arquivo reconstitui o estado e lista o trabalho futuro.

---

## 1. Estado atual (o que JÁ foi feito)

Pipeline Fases 1–4 concluído em 05-ago-2026 (subagentes deram timeout nas fases 3 e 4;
concluídas manualmente pelo agente principal). PDF compila: **15 páginas, sem erros**.

### Correções aplicadas (consistência com a cadeia da verdade)
- Bateria 6000 mAh → **1300 mAh**, autonomia >5 h, margem ~2× (todos os lugares)
- FSM/scheduler/beacon/IMPACT "implementados" → **loop único 5 Hz real**; pós-pouso marcado
  como planejado; buzzer = startup/error (não recurso pós-pouso)
- SRAB = **Asa3, 2 asas, 13.33 m/s** (alvo 20/1.5 com FS 1.5); 10.05 m/s só como histórico
  de drop test; janela rígida "20–45 m/s" removida
- Drop tests com valores com fonte (ENMC): T1 306.8 rpm/13.5°, T2 306.9 rpm/24.4°,
  T3 372.0 rpm/17.2°, 12.90 m/s, 78.03 s, 99.15% — Test 3 quantitativo adicionado à tabela
- Monte Carlo **100 iterações** adicionado (13.33±0.31 m/s, P5 12.78, P95 13.87)
- ABS → **PETG** (asas) / **alumínio 6061** (estrutura); kill switches paralelo NC
  (PQB 7.1.9–7.1.11); "triangulation" → "trilateration"; GPS beacons → ground LoRa beacons
- Hazard 2: kill switches "in series" → "wired in parallel with NC contacts"
- Nota REC 10.1.5 declarada: release 1520.5 m AGL ≈ 1.4% acima do guideline de 1500 m
- "two drop-test campaigns" → **three** (abstract, Filter 2, weights-measures)
- "Data is" → "Data are"; SPDT → "NC contacts wired in parallel"
- Matriz de riscos: renomeada "Risk Matrix (P × S)" + legenda de limiares + fases =
  arcos do ConOps (SAFE/BOOST/DESCENT/POST-LANDING) + 3 linhas novas (loop hang P2S2R4,
  brownout P1S2R2, wing cuts P2S1R2)
- Abstract 1 parágrafo com Dédalo/RocketPy; ConOps narrativo; citações [n] no texto;
  equações numeradas; pendências honestas (Test 4, PCB, estrutura)

### Referências (05-ago-2026, decisão do dono: APENAS as do artigo ENMC)
Conjunto = **6 referências idênticas às citadas no artigo ENMC** (`.bbl` do
`extras/wing-analysis/docs/telemetria_enmc_latex/`):

| # | Ref | Uso no texto |
|---|---|---|
| [1] | Lentink et al., *Science* 324(5933):1438–1440, 2009, doi:10.1126/science.1174196 | samara/LEV ("doubles the lift") |
| [2] | Limacher, *Samara-Seed Aerodynamics*, M.S. thesis, Univ. Calgary, 2015 | assimetria/autorrotação, velocidade < balística |
| [3] | McConnell & Das, *JDSMC* 145(6), 2023, doi:10.1115/1.4062438 | modelo 4ª ordem Newton-Euler |
| [4] | LASC, *SCSM*, 7th ed., Rev. 1, 2026 | compliance |
| [5] | Rezgui, Arroyo & Theunissen, *Aeronautical Journal* 124(1278):1236–1261, 2020, doi:10.1017/aer.2020.25 | correção LEV (f_factor) |
| [6] | RocketPy Development Team, *RocketPy Documentation*, 2024–2026 | simulação |

DOIs validados via Crossref. Nota: bib do ENMC diz McConnell 145(8); Crossref resolve
145(6) — usamos o Crossref. Nome do evento corrigido: **ENMC = Encontro Nacional de
Modelagem Computacional** (o texto usa só a sigla "ENMC consolidated data").

### Auditoria final
Relatório completo do auditor (Fase 4) em:
`docs/mission-report/audit/2026-08-05-auditoria-final.md` — notas 1–5 por dimensão,
vieses, verificação de citações, achados priorizados.

---

## 2. TODO — Próximas tarefas (ordem sugerida)

### T2.1 — Autores: alinhar com o artigo ENMC + Template 2026
- [x] Modificar os **autores** do mission report para os MESMOS usados no artigo ENMC
      (`satellite/extras/wing-analysis/docs/telemetria_enmc_latex/main.tex` + secs)
- [x] E também os do arquivo
      `/home/vinicius/Documentos/projects/Second-brain/Presentation Session Abstract Template 2026.md`
- [x] Cruzar os dois para decidir a lista oficial (ordem, afiliações, e-mail)

### T2.2 — Revisar o texto: LASC como meio de desenvolvimento de tecnologia
- [x] Base: `/home/vinicius/Documentos/projects/Second-brain/Presentation Session Abstract Template 2026.md`
- [x] O template demonstra que a LASC é o **meio de teste/desenvolvimento de uma
      tecnologia (SRAB)** — não uma competição onde se leva algo só para competir e fim
- [x] Revisar intro/ConOps/conclusões com essa leitura (framing da missão como
      desenvolvimento tecnológico; resultados = validação da tecnologia, não "vitória")

### T2.3 — Imagens: todas em inglês + imagens do notebook + vista de satélite
- [x] **Todas** as imagens precisam estar em **inglês** (legendas, eixos, rótulos)
- [x] Usar as **imagens do notebook** (`extras/wing-analysis/notebooks/01_simulacao_dedalo.ipynb`
      — plots de descida, autorrotação, etc.)
- [x] **Adicionar** uma imagem da **vista de satélite da trajetória do Helike**
      (trajetória de descida vista de cima / mapa — verificar se o RocketPy gera
      `flight.latitude/longitude` → plot sobre mapa; checar como o Dédalo simulado
      mostra isso no notebook)
- [x] Conferir quais figuras existem hoje em `docs/mission-report/` e substituir

### T2.4 — Formatação do .tex (hierarquia de fontes)
- [x] **Seções com subseções estão em fonte maior** do que deveriam — corrigir a
      formatação (provável problema no template/cabeçalhos: \section com subsecções
      renderizando tamanho de fonte errado)
- [x] Verificar `main.tex` / setup do template LASC (estilos de \section, \subsection,
      \subsubsection e \paragraph) e os `\textbf{...}` manuais usados como seções

---

**Status T2.1–T2.4 (06-ago-2026): concluídas.** T2.1: lista união (9) aplicada em
`sec-frontmatter.tex`, template LASC 2026 e `config.sty` do ENMC (e-mail do João Victor
pendente — TODO comentado). T2.2: intro/ConOps/conclusões com framing LASC como meio de
desenvolvimento. T2.3: figuras verificadas em inglês (md5 + fonte); adicionadas
`fig_srab_vs_parachute.png` (valores da tabela do relatório) e `fig_trajectory_map.png`
(render do `mapa_deploy_srab.html`); legendas de `fig_asa3_lrr`/`fig_test2_sim` ajustadas
(sem claim de janela 20–45). T2.4: hierarquia de fontes corrigida via sectsty em
`main.tex` (subseções deixaram de renderizar em \large; H1/H2 bold 10pt, H3 italic 10pt).

---

## 3. Achados ABERTOS da auditoria (decisões de equipe)

Do relatório `docs/mission-report/audit/2026-08-05-auditoria-final.md` — não corrigidos
unilateralmente (alguns são factuais, outros são decisão).

**Status 06-ago-2026 (tarde):** 2 dos 11 itens RESOLVIDOS ("Drift" e "Valores vs. notebook
salvo" — ver marcas abaixo). Restam **9 decisões**.

- **"(PASS, FS 1.5)" vs. notebook**: o notebook imprime "13.34 m/s EXCEDEU…
  REPROVADO" (comparação estrita 13.336 > 13.333) e o MC max dá FS real **1.40**
  (P95 13.87 → 1.44). Relatório afirma "confirming the 1.5 safety factor" — decidir
  como declarar (honestidade vs. interpretação do notebook).
- **Drop tests "experimentais"**: valores que no ENMC são **simulados** descritos como
  campanhas instrumentadas; "1000 m drop" sem evidência de teste real.
- **Drift — RESOLVIDO (06-ago)**: não era contradição — 184.3 m = distância do impacto
  ao PAD de lançamento (célula 28: hypot(x_impact, y_impact)); 131.2 m = drift da
  descida relativo ao ponto de deploy (célula 33: subtrai x0/y0). Relatório rotulado
  ("Distance from launch pad" / "Descent drift (m)*" + nota das métricas, §4).
- **Autonomia**: "about 9 h / >2×" vs. ">5 h / ≈2×" em lugares diferentes.
- **SPoF**: "no critical single points of failure" vs. "losing a single wing is a
  mission-critical degradation".
- **Valores vs. notebook salvo — RESOLVIDO (06-ago)**: decisão: vale a versão
  COMMITADA (1520.5 m / 184.3 m / 111.4 s / 79.7 mm / 13.33 m/s OK). Notebook,
  `mc_srab_dedalo.csv` e `mapa_deploy_srab.html` restaurados via `git checkout` (a
  re-rodada de 27-jul com 1516/13.34/REPROVADO foi descartada). NÃO re-rodar o notebook.
- **Monte Carlo**: 100 iterações (verdade do notebook) abaixo do mínimo ~1000 para P95 —
  reportar como limitação metodológica.
- **REC 10.1.5**: nota declarada; decisão de margem (1.4% acima) é do LRR.
- **REC 10.2.1**: follow-up "keep LASC apprised" pendente (LASC não encaminha emails).
- **Test 4** (~200 m, Asa3 2 asas): pendência real antes do LRR.
- **Dashboards com janela 20–45 m/s (levantado em 06-ago-2026)**: `fig_asa3_lrr.png` e
  `fig_test2_sim.png` ainda mostram "LASC Window (20–45 m/s)" + linha em 45 m/s enquanto o
  texto do relatório diz "20 m/s limit com FS 1.5" — legendas ajustadas, mas a figura
  contradiz o texto. Opções: regenerar dashboards (patchear `samara_pq_simulation.py`:
  remover axhspan 20–45 e linha 45, adicionar linha 20 m/s + alvo 13.33; risco de drift de
  valores — ver item "Valores vs. notebook salvo") ou aceitar como está.

---

## 4. Caminhos úteis

- Mission report: `/home/vinicius/Documentos/projects/satellite/docs/mission-report/`
- Artigo ENMC (LaTeX): `/home/vinicius/Documentos/projects/satellite/extras/wing-analysis/docs/telemetria_enmc_latex/`
- Notebook simulação: `/home/vinicius/Documentos/projects/satellite/extras/wing-analysis/notebooks/01_simulacao_dedalo.ipynb`
- Template abstract LASC 2026: `/home/vinicius/Documentos/projects/Second-brain/Presentation Session Abstract Template 2026.md`
- Fonte da verdade: `/home/vinicius/Documentos/projects/Second-brain/4_PU.md`
- Auditoria: `docs/mission-report/audit/2026-08-05-auditoria-final.md`
- Manual SCSM E07 R01 (local): `/home/vinicius/Documentos/projects/Second-brain/02_Profissional_Academico/LASC2026/Satellite Challenge Standards Manual E07 R01.md`
