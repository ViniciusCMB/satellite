# Auditoria Crítica — Mission Report Helike #213 (LASC 2026)

**Data:** 05-ago-2026 · **Artefato auditado:** `docs/mission-report/main.pdf` (15 pág., compilado 05-ago 23:02) · **Skill:** paper-auditor v1.3.0 + `references/helike_mission_report_audit.md`
**Método:** pdftotext no main.pdf; grep com nº de linha nos `.tex`; verificação contra a cadeia da verdade (mission-report-truth.md → 4_PU.md → src/config.h + src/main.cpp → notebook `01_simulacao_dedalo.ipynb` + resultados → manual SCSM E07 R01.pdf local → artigo ENMC).

---

## 1. Notas por dimensão (1–5)

| Dimensão | Nota | Justificativa |
|---|---|---|
| D1 · Clareza do objetivo | **4** | Objetivos primário/secundário/suporte claros e hierarquizados; narrativa coerente (SRAB central, LoRa como suporte). Penalizado pela contradição "no critical single points of failure" vs. "losing a single wing is a mission-critical degradation" (A-9). |
| D2 · Rigor metodológico | **2** | Modelo bem descrito (Newton-Euler 4ª ordem, BEM, correção LEV, RocketPy) e firmware verificado contra o código real — mas a seção "Experimental Drop Tests" apresenta valores SIMULADOS (ENMC: "parâmetros simulados dos Testes 1 e 2"; Teste 3 = simulação a 1000 m) como campanhas instrumentadas de queda; "1000 m drop" sem evidência (C-2). REC 10.1.5 ignorado (C-1). |
| D3 · Validade estatística | **2** | MC com 100 iterações (< 1000 recomendado para P95 — pitfall 4) sem menção de limitação; MC rotulado "atmospheric dispersion" quando varia tolerâncias de fabricação/modelo (A-6); "confirming the 1.5 safety factor" contradito pelo próprio CSV (max 14.24 m/s → FS real 1.40; P95 13.87 → 1.44) (A-5). P5/P95/σ verificados corretos contra `mc_srab_dedalo.csv`. |
| D4 · Reprodutibilidade e transparência | **2** | Valores do relatório não batem com o notebook definitivo salvo (apogeu 1520/1520.5 vs 1516/1515.6; drift 184.3 vs 181.6; tempo 111.4 vs 110.8; raio 79.7 vs 79.2 mm; posições de impacto; coordenadas de lançamento). Célula MC do notebook está desabilitada (CSV existe). Positivo: pendências honestas (Test 4, PCB, estrutura, bench de autonomia). |
| D5 · Coerência interna | **2** | Contradições seção-a-seção: drift SRAB 184.3 m (Stage 3) vs 131.2 m (tabela de comparação) (C-3); autonomia "about 9 h / >2×" vs ">5 h / ≈2×" (A-16); "two" vs "three" campanhas de drop test (A-10); buzzer como mitigação vs "planned" (A-11); "(PASS, FS 1.5)" vs veredito "REPROVADO" do notebook (A-18). |
| D6 · Qualidade das referências | **2** | [1] ano errado (2025 → manual diz "Effective: 22 March 2026", verificável no PDF local); atribuições de [2]/[4]/[5]/[6] com forte indício de citação trocada; sem DOIs; "et al." com 4 autores ([3]) fora do estilo AIAA estrito. [1], [3], [7], [8] verificáveis; demais "não verificáveis" (PDFs ausentes). |
| D7 · Contribuição e originalidade | **3** | Aplicação genuinamente original (autorrotação de samara → PocketQube 1P passivo) com integração real RocketPy + módulos SRAB, MC e benchmark vs paraquedas; porém a contribuição é enfraquecida pela superdeclaração da base experimental e pelas inconsistências numéricas. |

---

## 2. Vieses

- **Viés de confirmação / cherry-picking:** o relatório afirma "certifies the recovery", "(PASS, FS 1.5)" e "confirming the 1.5 safety factor" enquanto o próprio notebook imprime "13.34 m/s EXCEDEU … REPROVADO" (comparação estrita 13.336 > 13.333) e o MC max dá FS 1.40. Números favoráveis são citados; os desfavoráveis, omitidos.
- **Superdeclaração da base experimental (pitfall 16):** simulação apresentada como "drop tests instrumentados"; "1000 m drop" atribuído a um teste que, na fonte (ENMC), é simulação (Parte A) com instrumentação validada em bancada a 20 Hz.
- **Viés de omissão/seleção:** REC 10.1.5 (limite de 1500 m AGL + detachability) ausente do documento inteiro; status real do REC 10.2.1 (LASC não encaminha e-mails; follow-up pendente) suavizado; limitação das 100 iterações MC omitida.
- **Viés de otimismo (mitigado):** os trade-offs abertos (Test 4, bench de autonomia, validação dos kill switches) são declarados honestamente — ponto positivo.
- **Conflito de interesse:** nenhum aplicável (relatório de competição estudantil); não há declaração de financiamento, mas também não é obrigatório no template.

---

## 3. Verificação de citações [1]–[8]

| Ref | Verificação | Classificação |
|---|---|---|
| [1] LASC SCSM E07 R01, **2025** | Manual local: "Edition 7 \| Revision 1", "Effective: 22 March 2026". Conteúdo usado (PQB/ECS/REC) **fiel**; **ano errado** (2025 → 2026) | Parcialmente fiel (erro verificável em sec-references.tex:10) |
| [2] Norberg 2002, J. Morphology | PDF não disponível no repo. Usada para "parachute is a critical failure point in miniaturized satellites" (sec-introduction.tex:36) — artigo de morfologia de voo animal; o suporte mais plausível seria [6] McConnell & Das (recovery de small sats). **Não verificável** + forte indício de citação trocada | Não verificável (indício de mismatch) |
| [3] Lentink et al. 2009, Science | PDF local presente; conteúdo "LEV doubles lift" confere com a alegação do texto (Acer rubrum ✓). Verificada | **Fiel** |
| [4] Pennycuick 2008, Modelling the Flying Bird | PDF não disponível. Citada para "LEV doubles the effective lift" (sec-introduction.tex:67) — deveria ser [3] Lentink. **Não verificável** + indício de troca com [5] | Não verificável (indício de mismatch) |
| [5] Yasuda & Azuma 1997, J. Theor. Biol. | PDF não disponível. Citada para "mathematical modelling of animal flight" (sec-introduction.tex:72) — deveria ser [4] Pennycuick. **Não verificável** + indício de troca | Não verificável (indício de mismatch) |
| [6] McConnell & Das 2023, SSC | PDF não disponível. Citada para "descent rate substantially lower than the ballistic terminal velocity" (sec-computational-simulation.tex:18) — física de samara; o suporte natural seria [5] Yasuda & Azuma. **Não verificável** + indício de mismatch | Não verificável (indício de mismatch) |
| [7] RocketPy 2024 | Software realmente importado/executado no notebook (`rocketpy_samara`, rocketpy) ✓ | Fiel |
| [8] Serra Rocketry, ENMC 2026 | Artigo existe no repo (`extras/wing-analysis/docs/telemetria_enmc_latex/`) e os valores de Test 1/2/3 citados no relatório (306.8/13.5°, 306.9/24.4°, 372.0/17.2°, 12.90 m/s, 78.03 s, 99.15%) conferem com o artigo | Fiel |

**Nota:** como os PDFs de [2], [4], [5], [6] não estão no workspace, o conteúdo exato não pôde ser confirmado — nada foi inventado; a classificação é "não verificável" com indício forte de numeração trocada (os quatro pontos suspeitos formam um padrão sistemático).

---

## 4. Conformidade SCSM E07 R01 (cláusulas verificadas no PDF local do manual)

| Requisito | Linha manual | Alegação do relatório | Veredito |
|---|---|---|---|
| PQB 7.1.9 (≥2 kill switches) | 945 | SW1/SW2 (Z axis) ✓ | Atende (7.1.11 sem evidência explícita — A-21) |
| PQB 7.1.10 (só eixo Z) | 947 | "Z axis" ✓ | Atende |
| PQB 7.1.11 (não obstruir ejeção) | 953 | alegado "meeting PQB 7.1.9–7.1.11" sem declaração | Sem evidência (A-21) |
| ECS 9.1.3 (≥4 h autonomia) | 994 | >5 h (~9 h) ✓ | Atende (inconsistência de valores — A-16) |
| ECS 9.1.5–9.1.7 (RBF) | 1000–1003 | RBF série corta tudo; removido pós-integração ✓ | Atende |
| ECS 9.2.4 (frequências legais) | 1016 | 915 MHz (banda das Américas/Brasil); autorização "in progress" ✓ | Atende (declarado honestamente) |
| REC 10.1.1 (independência do foguete) | 1036 | sem conexão elétrica fixa; power-on na ejeção ✓ | Atende |
| REC 10.1.5 (deploy ≤1500 m AGL) | 1050 | **NUNCA citado**; deploy simulado a 1520.5 m AGL (notebook: 1515.6) — acima do limite; "target descent rate … e.g., 20–45 m/s" apresentado como "LASC 20 m/s limit" | **NÃO atende / não declarado (C-1)** |
| REC 10.1.5 (facilmente destacável) | 1047 | não mencionado | Não declarado (C-1) |
| REC 10.2.1 (notificação + keep apprised) | 1064 | "notification was sent on 19 April 2026, although formalization … pending" | Apresentado como enviado; LASC não encaminha e-mails; follow-up pendente (A-7) |

---

## 5. Achados priorizados

### CRITICAL

**C-1 · REC 10.1.5: limite de 1500 m AGL violado e nunca declarado**
- Localização: `sec-computational-simulation.tex:135` e `:145` (release 1520.5 m AGL); `:109` (apogeu 1520 m AGL); nenhuma ocorrência de "10.1.5", "1500 m" ou "detachab" em todo o documento (grep).
- Explicação: o manual (linha 1050) exige "deployment event … at or lower than 1,500 m AGL". O deploy simulado ocorre a 1520.5 m AGL (e até o valor do notebook, 1515.6 m AGL, excede o limite). O relatório não cita REC 10.1.5 em lugar nenhum e não reconhece a excedência; também não aborda a cláusula de destacabilidade (linha 1047). É decisão da equipe — **não corrigir unilateralmente**, mas a omissão atual é inaceitável.
- Correção sugerida (EN): "Add an explicit REC 10.1.5 compliance discussion in §4/§5: the passive ejection occurs at the Dédalo apogee (~1520 m AGL), which exceeds the 1500 m AGL deployment limit; state the deviation, its root cause, and the planned mitigation (e.g., LASC coordination, deployment delay, or apogee reduction), and address the 'easily detachable' clause."

**C-2 · Base experimental superdeclarada: simulações apresentadas como "drop tests instrumentados"**
- Localização: `sec-computational-simulation.tex:208` ("Three instrumented drop-test campaigns validated the model"), `:225` e `:238–239` ("1000 m drop … reached steady autorotation at 12.90 m/s in 78.03 s", "SRAB instrumented to record rotation with the flight IMU"); tabela de Testes 1–3 (v_impact 10.33/10.05/12.90 m/s); Figura 4 caption "measured descent profile" (figura = `fig_test2_sim.png`).
- Explicação: pelo artigo ENMC (fonte dos dados consolidados): Testes 1 e 2 = quedas livres QUALITATIVAS de ~20 m (drone); todos os números quantitativos são "parâmetros simulados dos Testes 1 e 2"; Teste 3 (Parte A) = SIMULAÇÃO a 1000 m (12.90 m/s, 78.03 s, θeq 17.22°, 371.98 rpm, 99.15%); instrumentação validada em BANCADA a 20 Hz. Não há evidência de queda física de 1000 m com IMU embarcado.
- Correção sugerida (EN): "Relabel §4: physical drop tests (Tests 1–2) were qualitative (~20 m drone); all quantitative values are simulation results (Test 3 = 1000 m simulation, ENMC Part A); onboard electronics were bench-validated at 20 Hz. Remove 'instrumented drop-test campaigns' and '1000 m drop'; state the planned quantitative test (Test 4) as the remaining evidence."

**C-3 · Inconsistência numérica interna + divergência sistemática vs. notebook definitivo**
- Localização: drift SRAB 184.3 m (`sec-computational-simulation.tex:150`) vs 131.2 m na tabela de comparação (`:179`); paraquedas 204.6 m (`:179`) vs notebook 264.6 m; release 1520.5 m AGL (`:145`) vs notebook 1515.6; tempo de descida 111.4 s (`:147`) vs notebook 110.8 e vs própria média MC 110.97 (`:202`); raio 79.7 mm (`:144`) vs notebook 79.2 mm; Stage 2: 17.8 m/s e x=−139.7 m (`:125`, `:127`) vs notebook 18.8 m/s e x=−114.7; Stage 1: apogeu 1520 m AGL/1996 m ASL e acel. 106.7 m/s² (`:109`–`110`) vs notebook 1516/1991 e 108.1; coordenadas de lançamento −21.94305/−48.95409 vs notebook −21.94093/−48.95318.
- Explicação: o notebook `01_simulacao_dedalo.ipynb` é a fonte definitiva (mission-report-truth.md); os valores salvos nas saídas divergem do relatório em ~12 números (5–35% em drift/posições), e o relatório se contradiz internamente (184.3 vs 131.2 m para a MESMA descida SRAB). Nenhum dos valores do relatório é reproduzível do artefato salvo.
- Correção sugerida (EN): "Re-run and save `01_simulacao_dedalo.ipynb` with the final GFS, capture its outputs, and use exactly those values in every table; make the SRAB drift in the parachute comparison equal to the Stage 3 value (or state different wind conditions explicitly). Add the run timestamp/GFS file to §4 for reproducibility."

### MAJOR

**A-4 · "LASC 20 m/s limit" não existe no manual — é alvo exemplificado**
- Localização: `sec-introduction.tex:148`; `sec-architecture.tex:50`; `sec-computational-simulation.tex:152, 192, 204, 250`; `sec-appendix-drawings.tex:42`.
- Explicação: REC 10.1.5 (linha 1050–1052) diz "target descent rate … (e.g., between 20-45 m/s)" — alvo exemplificado, não limite duro. O relatório cita "LASC 20 m/s limit" 6+ vezes.
- Correção (EN): "Replace 'LASC 20 m/s limit' with 'SCSM REC 10.1.5 target descent rate (e.g., 20–45 m/s), interpreted conservatively as 20 m/s with FS 1.5'."

**A-5 · "confirming the 1.5 safety factor" contradito pelo próprio MC**
- Localização: `sec-computational-simulation.tex:204`.
- Explicação: CSV (100 iters): max v_impact 14.24 m/s → FS real 20/14.24 = 1.40; P95 13.87 → 1.44. O alvo FS 1.5 (13.33) é excedido pelo P95. "Every iteration below the 20 m/s LASC limit, confirming the 1.5 safety factor" superdeclara.
- Correção (EN): "State the MC dispersion explicitly: 13.33±0.31 m/s (P5 12.78, P95 13.87, max 14.24), all below 20 m/s, implying a margin of 1.40–1.5×; do not claim the 1.5 safety factor is confirmed."

**A-6 · MC rotulado "atmospheric dispersion", mas varia tolerâncias de fabricação/modelo**
- Localização: `sec-computational-simulation.tex:200`.
- Explicação: a célula MC do notebook varia mass_kg (200±10 g), beta_deg, cd0 (1.0±0.10) e f_factor (0.3±0.03) — sem variação de atmosfera/vento.
- Correção (EN): "Describe the MC as varying manufacturing tolerances and model parameters (mass, β, CD0, f_factor), not atmospheric dispersion; add a wind-sensitivity study or reword."

**A-7 · REC 10.2.1 ainda apresentado como enviado/fechado**
- Localização: `sec-introduction.tex:98` ("the notification was sent on 19 April 2026"); tabela de §3 ("Sent 19 Apr 2026; formalization pending"); conclusões (`sec-conclusions.tex:13` — "caught the non-parachute notification requirement" como sucesso).
- Explicação: verdade conhecida — LASC respondeu que NÃO encaminha e-mails ao board; revisão interna de jun/2026 ainda "NÃO ENVIADA — AÇÃO URGENTE"; sem follow-up ("keep LASC apprised"). O relatório suaviza para "formalization pending".
- Correção (EN): "Present REC 10.2.1 as an open action: 'notification attempted by e-mail on 19 Apr 2026; LASC does not forward e-mails to the review board; formal submission and follow-up to keep LASC apprised are pending'."

**A-8 · Rótulo "FMECA" sem estrutura FMECA**
- Localização: `sec-appendix-risk.tex:11` ("Risk Matrix (FMECA)").
- Explicação: a matriz tem #, Failure Mode, Phase, P, S, R, Level — sem colunas de efeito/detecção/RPN; a metodologia interna (regra-dos-tres-filtros, Filtro 2) exige FMECA. Legenda P/S existe (linha 6–7), mas sem limiares de nível (R=6→Critical, R=4→High, R=3→Medium, R=2→Low implícitos).
- Correção (EN): "Either add FMECA columns (failure effect, detection method, RPN/action) or rename to 'Risk Matrix'; define and state the P×S level thresholds."

**A-9 · Contradição: "no critical single points of failure" vs. perda de asa única = mission-critical**
- Localização: `sec-introduction.tex:148` vs `sec-architecture.tex:54`.
- Correção (EN): "Reword the primary objective: '…with a predicted terminal velocity meeting the 20/1.5 m/s target and no critical single points of failure in the actuation/deployment chain'; acknowledge single-wing loss as an accepted residual risk."

**A-10 · "two" vs "three" drop-test campaigns**
- Localização: `sec-frontmatter.tex:17` (abstract), `sec-weights-measures.tex:32`, `sec-introduction.tex:109` (two) vs `sec-computational-simulation.tex:208`, `sec-appendix-hazard.tex:56`, `sec-appendix-risk.tex:38` (three).
- Explicação: campanhas físicas = 2 (qualitativas); Teste 3 é simulação (ver C-2). Contagem inconsistente e superdimensionada.
- Correção (EN): "Use a consistent count everywhere: 'two qualitative physical drop-test campaigns (Tests 1–2) plus a simulated 1000 m test (Test 3, ENMC Part A)'."

**A-11 · Buzzer usado como mitigação de risco mas não existe no firmware de voo**
- Localização: `sec-appendix-risk.tex:53–54` ("three ground LoRa beacons plus the buzzer give the recovery team several ways to find it") vs `sec-architecture.tex` ("Impact detection, the buzzer and the low-power beacon mode are planned for a future firmware revision"; firmware real: buzzer só toca startup/error — verificado em main.cpp).
- Correção (EN): "Reference the ground LoRa beacons and GPS as the recovery means; state the buzzer as planned, not available in the current flight software."

### MINOR

**A-12 · Referência [1] com ano errado** — `sec-references.tex:10`: "2025" → manual local: "Effective: 22 March 2026". Fix: "change the year to 2026."
**A-13 · Indícios de citações trocadas ([2]/[4]/[5]/[6])** — ver §3. Fix: "Re-map citations: LEV-doubles-lift → Lentink [3]; modelling of animal flight → Pennycuick [4]; parachute failure in small sats → McConnell & Das [6]; samara descent-rate physics → Yasuda & Azuma [5] (verify against each PDF)."
**A-14 · Referências sem DOI e "et al." com 4 autores** — `sec-references.tex:14` ([3] "D. Lentink et al."). Fix: "Add DOIs (e.g., Lentink 10.1126/science.1174196); list all authors (AIAA allows 'et al.' only beyond ten) or follow the template example."
**A-15 · Captions "Figure N:" fora do padrão AIAA** — template (`main_backup.tex:339`) exige "Fig. 1." e citação no texto como "Fig.". Fix: "Use 'Fig. N. caption' in captions and 'Fig.' when citing in text."
**A-16 · Autonomia inconsistente entre seções** — `sec-introduction.tex:94` ("about 9 h … margin of more than two times") vs `sec-weights-measures.tex:69–71` (">5 h" / "≈2×"). Fix: "Unify: '≈9 h predicted (1300 mAh / ~145 mA), margin ≈2× vs the ≥4 h requirement'; keep >5 h as the conservative lower bound."
**A-17 · "99.15% dissipada" sem rótulo de configuração** — `sec-weights-measures.tex:47`: valor é do Teste 3 Asa3 4-asas (ENMC). Fix: "Label it '(Test 3, Asa3 4-wing, ENMC)'."
**A-18 · "(PASS, FS 1.5)" vs veredito do notebook "REPROVADO"** — `sec-computational-simulation.tex:152`: simulação dá 13.336 m/s vs alvo estrito 13.333 (0.003 m/s; célula 28 do notebook imprime "EXCEDEU/REPROVADO"). Fix: "Report '13.34 m/s vs 13.33 m/s target (numerical residual of 0.02%)' or use one consistent rounding."
**A-19 · Nomenclature sem unidades** — `sec-frontmatter.tex`: símbolos (θ, ϕ̇, CL, …) sem unidades (AIAA exige, ex.: θ [deg], ϕ̇ [rpm]); entrada "F S" com espaçamento estranho. Fix: "Add units to all nomenclature entries; use \mathit{FS}."
**A-20 · Matriz de riscos: cobertura incompleta** — `sec-appendix-risk.tex`: Hazard 3 (sharp edges) sem linha na matriz; sem linhas para loop-hang/watchdog ou brownout (SPoFs citados no texto do Filtro 2); sem limiares de nível. Fix: "Add rows for personnel injury (sharp edges), firmware loop-hang (watchdog), and brownout; define level thresholds."
**A-21 · PQB 7.1.11 alegado sem evidência** — `sec-introduction.tex` (citação "meeting PQB 7.1.9–7.1.11") sem declaração de não-obstrução da ejeção. Fix: "Add one sentence on kill-switch placement not obstructing ejection (per PQB 7.1.10a/b)."

---

## 6. Itens da Fase 3 validados (sem achado novo)

- Bateria 1300 mAh, >5 h, margem ~2× — consistente em spec table, §2, §3 (4_PU ✓); resíduo apenas na dupla "~9 h/>5 h" (A-16).
- FSM/scheduler/beacon/IMPACT → loop único 5 Hz real (config.h: SAMPLE_INTERVAL_MS 200; main.cpp sem FSM) ✓; watchdog TWDT 5 s real (config.h:107) ✓; pós-pouso "planned" ✓.
- SRAB Asa3 2 asas, 13.33 m/s (20/1.5) — consistente em spec table, §2, §4, apêndices ✓; 10.05 m/s só como "historical" ✓.
- "APROVADO (13.33<13.33)" removido ✓ (resíduo: "PASS, FS 1.5" — A-18).
- RPM/cone dos drop tests: T1 306.8/13.5°, T2 306.9/24.4°, T3 372.0/17.2° ✓ (conferem com ENMC: 306.77/13.46, 306.89/24.44, 371.98/17.22).
- PETG (asas)/alumínio 6061 (estrutura) ✓; kill switches paralelo NC ✓ (4_PU); "trilateration" ✓; beacons de solo LoRa ✓.
- Citações [1]–[8] presentes; equações numeradas ✓; MC 100 iterações consistente (só em §4; **não corrigir para 1000** — reportar como limitação metodológica: pitfall 4, ver A-5/A-6); parâmetros LoRa (SF7, 125 kHz, 20 dBm, sync 0xF3, CRC) ✓ verificados em config.h/LoRaModule.cpp; 5 Hz ✓.
- Test 4 pendente (~200 m), PCB/estrutura "In progress" ✓ honestos.
- Buzzer: §2/ConOps corretos (startup/error apenas; impacto/buzzer/beacon futuros) ✓; contradição apenas na mitigação A-11.
- Nomenclature: FSM removido ✓; símbolos usados ✓ (resíduo: unidades — A-19).
- 17.8 J ✓ (notebook 17.79); 477 RPM ✓; θ_eq 8.6° ✓; 926 N/95 pts/2.82 s ✓; massas 5.100/4.900/0.200 kg ✓; Ø106 mm ✓; 0.47 s @ 18.9 m/s ✓; elevação 478 m ✓.

---

## 7. Veredito final

**NÃO PRONTO para submissão LASC 2026.**

O relatório está estruturalmente bom (objetivos claros, honestidade sobre pendências, firmware alinhado ao código real, requisitos PQB/ECS majoritariamente verificados), mas os três achados CRITICAL bloqueiam a submissão: (C-1) não conformidade com REC 10.1.5 (1500 m AGL) não declarada — decisão da equipe, mas a omissão atual é inaceitável; (C-2) base experimental superdeclarada (simulação como "drop tests instrumentados", "1000 m drop" sem evidência); (C-3) inconsistências numéricas internas (184.3 vs 131.2 m) e divergência sistemática vs. notebook definitivo. Somam-se 8 achados MAJOR (framing do "20 m/s limit", sobre-alegação do FS 1.5, MC mal descrito, REC 10.2.1 ainda otimista, FMECA sem estrutura, contradição de SPoF, contagem de campanhas, buzzer como mitigação).

**Caminho para aprovação:** resolver C-1 (declarar a excedência + mitigação), C-2 (re-rotular testes conforme ENMC), C-3 (re-executar/salvar o notebook e adotar exatamente seus valores), e os MAJORs A-4..A-11; então recompilar e re-auditar. Com isso, o documento fica "pronto com ressalvas" (as pendências Test 4/PCB/bench são aceitáveis se declaradas).
