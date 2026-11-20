# Roteiro de Apresentação — Missão Helike #213 (LASC 2026)

**A mensagem em uma frase** (se a banca lembrar de uma coisa só, é esta):
> "Nós trocamos o paraquedas por uma semente, e ela desce mais rápido, mais perto e sem ponto único de falha."

3 apresentadores, 10 minutos, 13 slides. Alvo: 8:45 falado, ~1:15 de folga.

| Quem | Blocos | Tempo |
|---|---|---|
| Vinicius | Fio condutor: abertura, SRAB, teoria, simulações, fechamento | 5:00 |
| Pablo | Complementos de hardware e RF/LoRa | 1:20 |
| Barizon | Complementos de operação, benchmark, testes | 2:25 |

Formato: no máximo 2 vozes por slide, entrada sempre marcada pelo domínio ("Na operação...", "E o firmware..."). Se a dinâmica não engatar no ensaio, o complemento vira fala única do dono do slide. Nada mais muda.

---

## Arco da apresentação (3 pontos, o mais forte primeiro)

1. **A semente** (slides 3–5): a natureza já resolveu esse problema há milhões de anos; nós só parametrizamos. É o gancho e o material mais forte: abre com ele.
2. **Os números** (slides 6–8): a simulação previu, o Monte Carlo confirmou, o Dédalo acopla.
3. **A máquina** (slides 9–13): 50 gramas de eletrônica que sobrevivem a 477 RPM, mais o benchmark que decide.

Fecho: volta da semente no slide 14. "A semente que a gente achou no chão do parque" reaparece na última frase.

---

## Slide 2 — Título / Apresentação da Equipe *(Vinicius · 0:40)*

Fala:
> "Bom dia. Antes do satélite, uma pergunta: quando você solta uma semente de samara da mão, ela não cai. Ela desce girando, devagar, e pousa de pé. A gente passou um ano perguntando: e se um satélite caísse do mesmo jeito? Eu sou o Vinicius, Mission Leader, da Serra Rocketry, do IPRJ-UERJ. Comigo estão o Pablo, Technology Manager, e o Barizon, Operations Manager. E essa é a Helike, número 213."

Pontos-chave:
- O gancho é a samara na mão, pergunta retórica respondida pelo slide 3.
- Apresentar os três em uma frase. Não ler dados do evento.

---

## Slide 3 — The Recovery Paradigm *(Vinicius · 0:45)*

Fala:
> "Por que substituir o paraquedas? Porque ele é o elo fraco. Sequenciador de deploy, pirotecnia, linha que enrola. Cada item dessa lista é um ponto único de falha. A gente já perdeu payload por menos. A samara não tem nada disso. É 100% passiva: a energia da queda vira giro estável. Sem atuador, sem pirotecnia, sem linha. O hardware que menos pode falhar é o que não existe."

Pontos-chave:
- Contraste dor × elegância. A frase-fechamento ("o hardware que menos pode falhar é o que não existe") é a tese.
- "A gente já perdeu payload por menos": usar só se for verdade na história da equipe; senão cortar.

---

## Slide 4 — Aerodynamic Foundations *(Vinicius · 0:45)*

Fala:
> "Mas a semente faz uma coisa que a aerodinâmica clássica dizia ser impossível: gera sustentação além do estol. O truque é o Leading-Edge Vortex — um vórtice que gruda na borda de ataque e eleva o coeficiente de sustentação local para 2 a 5. O desafio era enfiar isso em 50 milímetros. As asas da Asa3 foram parametrizadas em volta dessa restrição: β de 5 graus, 200 gramas."

Pontos-chave:
- LEV em uma frase: "vórtice que gruda na asa e dá sustentação extra".
- Form factor 1P como restrição, geometria desenhada em volta dela.

---

## Slide 5 — Preliminary Validation *(Vinicius + Barizon · 0:50)*

Fala (Vinicius · 0:35):
> "Teoria bonita sem chão é só bonita. Então fomos para o chão: queda de 20 metros, três ciclos de teste. Resultado: 12% mais área deram 81,6% mais conicidade. O modelo previu, o experimento confirmou."

Fala (Barizon · 0:15):
> "E esses testes são da minha rotina de operações. Medir conicidade, ajustar geometria, soltar de novo. Ciclo curto, erro rápido."

Pontos-chave:
- Vinicius fecha a teoria, Barizon atesta a operação.
- Números: 20 m, 12% de área, 81,6% de conicidade.

---

## Slide 6 — Steady-State Autorotation *(Vinicius · 0:50)*

Fala:
> "Com o modelo validado, rodamos a simulação completa: Runge-Kutta de 5ª ordem. O sistema se estabiliza sozinho em cerca de 10 segundos, depois da dispensa a 938 metros. E a partir daí é regime: 13,33 m/s de descida, conicidade de 8,6 graus, 477 RPM. Soltou, girou, estabilizou — sem ninguém tocando em nada."

Pontos-chave:
- O destaque é o "sozinho": equilíbrio em ≈ 10 s sem comando.
- 13,33 m/s, 8,6°, 477 RPM.

---

## Slide 7 — Parametric Robustness *(Vinicius + Barizon · 1:05)*

Fala (Vinicius · 0:50):
> "A pergunta que toda banca faz: e a tolerância de fabricação? Rodamos 100 iterações de Monte Carlo variando massa, passo β, arrasto parasita e fator de forma. Deu 13,32 ± 0,31 m/s, variação abaixo de 2,5%. A velocidade terminal fica invariante até com ±20% no C_d0."

Fala (Barizon · 0:15):
> "Traduzindo para a bancada: as imperfeições do PETG impresso em 3D não derrubam a previsibilidade. A gente viu isso na impressora."

Pontos-chave:
- Monte Carlo, 100 iterações.
- Vinicius dá o número, Barizon traduz para a manufatura real.

---

## Slide 8 — 6-DOF Trajectory *(Vinicius + Barizon · 1:00)*

Fala (Vinicius · 0:35):
> "Agora o sistema completo: a descida do SRAB acoplada ao perfil de subida real do Dédalo #11, com vento GFS via RocketPy. Descida rápida, janela de deriva menor."

Fala (Barizon · 0:25):
> "E é aqui que a operação agradece. O CEP de recolhimento encola: menos área para procurar, menos tempo de payload exposto ao vento. É a diferença entre procurar um satélite e ir buscá-lo."

Pontos-chave:
- Vinicius dá a simulação, Barizon traduz para campo.
- A frase de fecho dele ("procurar um satélite vs ir buscá-lo") é a imagem que fica.

---

## Slide 9 — Hardware Architecture *(Pablo + Vinicius · 1:00)*

Fala (Pablo · 0:35):
> "E a eletrônica, que é a minha frente: MCU, IMU, sensor ambiental, GPS e LoRa em 50 gramas dentro do 1P. O núcleo é um ESP32-C3 com escalonamento cooperativo. Barramentos segregados: I2C para os sensores a 20 Hz, SPI com chip selects dedicados para LoRa e microSD, UART exclusiva para o GPS."

Fala (Vinicius · 0:25):
> "E o firmware que roda nisso passou pela minha mão: loop determinístico de 50 ms, telemetria por LoRa, gravação dupla em SD e LittleFS. Segurança física: kill switches no eixo Z e pino RBF. A Helike só liga quando a gente decide que ela liga."

Pontos-chave:
- Pablo fala de PCB e barramentos, Vinicius de firmware e segurança.
- "Só liga quando a gente decide que ela liga": a frase fica na cabeça da banca e é verdadeira.

---

## Slide 10 — Systems Engineering: 3-Filter *(Barizon · 0:45)*

Fala:
> "E para nada disso quebrar em campo, o software foi desenhado esperando o pior. A metodologia tem três filtros: compliance com os manuais da LASC; design defensivo via FMECA, com rejeição de NaN em nível de hardware e armazenamento duplo; e viabilidade temporal: um loop de 50 ms em vez de máquinas de estado complexas. A regra da equipe é simples: se pode dar errado, já está tratado."

Pontos-chave:
- 3 filtros: SCSM / Murphy (FMECA) / viabilidade.
- NaN em hardware + redundância SD+LittleFS; loop de 50 ms.

---

## Slide 11 — Secondary Mission: GPS-Denied *(Pablo · 0:40)*

Fala:
> "E se o GPS morrer no momento crítico? A missão não morre com ele. A missão secundária é localização sem GPS: trilateração de RSSI via LoRa com três beacons terrestres independentes. O satélite não precisa saber onde está — os beacons sabem onde ele está."

Pontos-chave:
- Pablo: RF/LoRa é a especialidade dele.
- A frase de fecho ("os beacons sabem onde ele está") vende o diferencial sem a palavra "diferencial".

---

## Slide 12 — Benchmark: SRAB vs Parachute *(Barizon + Vinicius · 1:10)*

Fala (Barizon · 0:40):
> "Este slide resume a missão. Comparação honesta: paraquedas circular de 200 mm contra o SRAB de 2 asas, ambos a 200 g, do apogeu do Dédalo, 938 metros. Deu 69,9 segundos contra 110. E a deriva horizontal, 339 metros contra 534."

*(pausa de 2 segundos, deixar a banca ler a tabela)*

Fala (Vinicius · 0:30):
> "36% menos tempo, 36% menos deriva, e 100% dos modos de falha de deploy ativo eliminados. O paraquedas é mais simples de explicar. O SRAB é mais simples de confiar."

Pontos-chave:
- Barizon aponta a tabela, pausa, Vinicius dá a leitura de engenharia.
- A frase final do Vinicius é a mais importante da apresentação. Ensaiar até sair natural.

---

## Slide 13 — Flight Test Objectives *(Barizon · 0:40)*

Fala:
> "E o lançamento não é praça de prova aberta: tem critério. Velocidade de impacto dentro de ±5% da previsão. Tempo de descida dentro de ±3%. Telemetria a 20 Hz sem perder amostra. Se o voo real fechar com a simulação, o modelo está pronto para escalar."

Pontos-chave:
- Não é "lançar para ver se funciona", é experimento com critérios.
- ±5% velocidade, ±3% tempo, telemetria 20 Hz sem perdas.

---

## Slide 14 — Referências / Encerramento *(Vinicius · 0:30)*

Fala:
> "Para fechar, voltando à semente do começo: ela virou um sistema que cai mais rápido, mais perto e sem pirotecnia. A simulação rodou no RocketPy com as nossas próprias equações, as referências estão aqui. E o QR Code leva para a página da missão, com a contagem regressiva para o lançamento. A natureza levou milhões de anos para aperfeiçoar a queda. A gente só precisou de um ano. Obrigado!"

Pontos-chave:
- Callback ao gancho do slide 2 (a samara na mão).
- Uma frase de crédito técnico (RocketPy + equações próprias).
- QR Code, apontar para ele.
- Nota: se o gancho do slide 2 for ajustado no ensaio, ajustar a volta da semente junto. O par precisa bater.

Encerramento (não conta): slide 15 "Thank you!" em tela durante o Q&A. Vinicius modera e direciona: SRAB/simulação/firmware para ele; PCB/barramentos/LoRa para o Pablo; operação/testes/recolhimento para o Barizon.

---

## Preparação de entrega (a parte que faz diferença)

**Ritmo:**
- Apresentação formal: 100–120 palavras por minuto. A fala mais longa aqui (slide 3) tem ~90 palavras, o que dá 50 s falando devagar. Se no ensaio cronometrado alguém estourar, é velocidade, não texto.
- Respire na pontuação. Pausa entre slides: os 2 segundos de silêncio são conteúdo, não atraso.
- Filler words (é..., tipo..., então...) são o inimigo do minuto de 120 palavras. Gravar uma vez e ouvir revela todos.

**Ensaio (fora do espelho):**
1. Rodada 1: cronômetro, notas em ponto, um ouvinte. Depois perguntar ao ouvinte: "qual foi o ponto principal?" Se a resposta não for "SRAB desce mais rápido e sem falha", a mensagem não aterrissou.
2. Rodada 2: só as trocas mescladas (slides 5, 7, 8, 9, 12), repetir até a entrada do segundo ser automática.
3. Rodada 3: gravar em vídeo, ouvir uma vez, corrigir ritmo e monotonia.
4. No dia: chegar cedo, testar cliques, água na mesa.

**Regras de dinâmica:**
- Sinal de troca: meio passo à frente e começa a falar. Sem se olhar.
- Quem fala não opera: Pablo nos cliques, ou um quarto membro.
- Se a dinâmica mesclada não engatar, plano B: cada complemento vira fala única do dono do slide. Nada mais muda.
- Números em voz alta só os essenciais: 13,33 m/s, 938 m, 69,9 contra 110 s, ±5%. O resto está no slide.
- Se estourar o tempo, cortar do slide 5 e 11. Nunca do 12.

---

# English Version — Speech Script

**The one-sentence message** (if the panel remembers one thing):
> "We swapped the parachute for a seed, and it comes down faster, closer, and with no single point of failure."

3 speakers, 10 minutes, 13 content slides. Target: 9:00 spoken (English runs ~10% longer than Portuguese), ~1:00 slack.

Rule: max 2 voices per slide; each speaker enters with their own domain ("On the operations side...", "And the firmware..."). If the mixed dynamics doesn't click in rehearsal, each complement becomes a solo line by the slide owner. Nothing else changes.

---

## Slide 2 — Title / Team Introduction *(Vinicius · 0:40)*

> "Good morning. Before the satellite, a question: when you drop a samara seed from your hand, it doesn't fall. It spins down, slowly, and lands upright. We spent a year asking: what if a satellite came down the same way? I'm Vinicius, Mission Leader, from Serra Rocketry, IPRJ-UERJ. With me are Pablo, our Technology Manager, and Barizon, our Operations Manager. And this is Helike, number 213."

Key points:
- The hook is the seed in the hand; slide 3 answers the question.
- Introduce all three in one sentence. Don't read event data.

---

## Slide 3 — The Recovery Paradigm *(Vinicius · 0:45)*

> "Why replace the parachute? Because it's the weak link. Deployment sequencers, pyrotechnics, lines that tangle. Every item on that list is a single point of failure. The samara has none of that. It's fully passive: falling energy becomes stable spin. No actuators, no pyrotechnics, no lines. The hardware least likely to fail is the hardware that doesn't exist."

Key points:
- Contrast pain × elegance. The closing line is the thesis.
- Note: if the team has actually lost payloads to less, say so here; otherwise cut.

---

## Slide 4 — Aerodynamic Foundations *(Vinicius · 0:45)*

> "But the seed does something classical aerodynamics called impossible: it generates lift beyond stall. The trick is the Leading-Edge Vortex — a vortex that clings to the leading edge and pushes the local lift coefficient to 2 to 5. The challenge was fitting that into 50 millimeters. The Asa3 wings were parameterized around that constraint: 5 degrees of pitch, 200 grams."

Key points:
- LEV in one sentence: "a vortex that clings to the wing and adds lift".
- The 1P form factor is the constraint; the geometry was drawn around it.

---

## Slide 5 — Preliminary Validation *(Vinicius + Barizon · 0:50)*

Vinicius (0:35):
> "A pretty theory with no ground truth is just pretty. So we went to the ground: 20-meter drops, three test cycles. Result: 12% more area gave 81.6% more coning. The model predicted it, the experiment confirmed it."

Barizon (0:15):
> "And those tests are part of my operations routine. Measure coning, adjust the geometry, drop again. Short cycle, fail fast."

Key points:
- Vinicius closes the theory, Barizon vouches for the operations.
- Numbers: 20 m, 12% area, 81.6% coning.

---

## Slide 6 — Steady-State Autorotation *(Vinicius · 0:50)*

> "With the model validated, we ran the full simulation: fifth-order Runge-Kutta. The system stabilizes itself in about 10 seconds after release from 938 meters. Then it's all steady state: 13.33 m/s descent, 8.6 degrees of coning, 477 RPM. Released, spinning, stable — with nobody touching anything."

Key points:
- The point to stress is "by itself": equilibrium in ~10 s with no commands.
- 13.33 m/s, 8.6°, 477 RPM.

---

## Slide 7 — Parametric Robustness *(Vinicius + Barizon · 1:05)*

Vinicius (0:50):
> "The question every panel asks: what about manufacturing tolerance? We ran 100 Monte Carlo iterations, perturbing mass, pitch, parasitic drag, and form factor. We got 13.32 ± 0.31 m/s, variation under 2.5%. Terminal velocity stays invariant even with ±20% on C_d0."

Barizon (0:15):
> "On the shop floor, that means the imperfections of 3D-printed PETG don't hurt predictability. We saw it at the printer."

Key points:
- Monte Carlo, 100 iterations.
- Vinicius gives the number, Barizon translates it to real manufacturing.

---

## Slide 8 — 6-DOF Trajectory *(Vinicius + Barizon · 1:00)*

Vinicius (0:35):
> "Now the full system: the SRAB descent coupled to the real ascent profile of Dédalo #11, with GFS winds through RocketPy. Faster descent, narrower drift window."

Barizon (0:25):
> "And this is where operations says thank you. The recovery CEP shrinks: less area to search, less time with the payload exposed to wind. It's the difference between searching for a satellite and going to pick it up."

Key points:
- Vinicius gives the simulation, Barizon translates it to the field.
- His closing line ("searching vs picking it up") is the image that sticks.

---

## Slide 9 — Hardware Architecture *(Pablo + Vinicius · 1:00)*

Pablo (0:35):
> "The electronics, which is my front: MCU, IMU, environmental sensor, GPS, and LoRa in 50 grams inside the 1P. The core is an ESP32-C3 with cooperative scheduling. Segregated buses: I2C for sensors at 20 Hz, SPI with dedicated chip selects for LoRa and microSD, a dedicated UART for GPS."

Vinicius (0:25):
> "And the firmware running on it went through my hands: a deterministic 50 ms loop, LoRa telemetry, dual logging to SD and LittleFS. Physical safety: Z-axis kill switches and an RBF pin. Helike only powers up when we decide it powers up."

Key points:
- Pablo covers PCB and bus architecture, Vinicius covers firmware and safety.
- "Only powers up when we decide it powers up": memorable and true.

---

## Slide 10 — Systems Engineering: 3-Filter *(Barizon · 0:45)*

> "And to keep none of this breaking in the field, the software was designed expecting the worst. The methodology has three filters: compliance with the LASC manuals; defensive design through FMECA, with hardware-level NaN rejection and dual storage; and temporal viability: a 50 ms loop instead of complex state machines. The team rule is simple: if it can go wrong, it's already handled."

Key points:
- 3 filters: SCSM / Murphy (FMECA) / viability.
- Hardware-level NaN + SD+LittleFS redundancy; 50 ms loop.

---

## Slide 11 — Secondary Mission: GPS-Denied *(Pablo · 0:40)*

> "And if GPS dies at the critical moment? The mission doesn't die with it. The secondary mission is GPS-denied localization: RSSI trilateration over LoRa with three independent ground beacons. The satellite doesn't need to know where it is — the beacons know where it is."

Key points:
- Pablo: RF/LoRa is his specialty.
- The closing line sells the edge without saying "differentiator".

---

## Slide 12 — Benchmark: SRAB vs Parachute *(Barizon + Vinicius · 1:10)*

Barizon (0:40):
> "This slide is the mission in one table. An honest comparison: a 200 mm circular parachute against the 2-wing SRAB, both 200 g, from Dédalo's apogee, 938 meters. That's 69.9 seconds versus 110. And horizontal drift: 339 meters versus 534."

*(2-second pause, let the panel read the table)*

Vinicius (0:30):
> "36% less descent time, 36% less drift, and 100% of active deployment failure modes eliminated. The parachute is simpler to explain. The SRAB is simpler to trust."

Key points:
- Barizon points at the table, pauses, Vinicius gives the engineering read.
- Vinicius's final line is the most important sentence of the talk. Rehearse until it sounds natural.

---

## Slide 13 — Flight Test Objectives *(Barizon · 0:40)*

> "And the launch isn't an open proving ground: there are acceptance criteria. Impact velocity within ±5% of prediction. Descent time within ±3%. Telemetry at 20 Hz with zero sample loss. If the real flight closes with the simulation, the model is ready to scale."

Key points:
- Not "launch and see", it's an experiment with criteria.
- ±5% velocity, ±3% time, lossless 20 Hz telemetry.

---

## Slide 14 — References / Closing *(Vinicius · 0:30)*

> "To close, back to the seed from the start: it became a system that falls faster, closer, and without pyrotechnics. The simulation ran on RocketPy with our own samara dynamics equations; the references are here. And the QR code takes you to the mission page, with the countdown to launch. Nature took millions of years to perfect the fall. It took us one year. Thank you!"

Key points:
- Callback to the slide 2 hook (the samara in the hand).
- One technical credit line (RocketPy + own equations).
- QR code, point at it.
- Note: if the slide 2 hook changes in rehearsal, change this closing too. The pair must match.

Closing (not counted): slide 15 "Thank you!" stays on screen during Q&A. Vinicius moderates and routes: SRAB/simulation/firmware to himself; PCB/buses/LoRa to Pablo; operations/testing/recovery to Barizon.

---

## Delivery prep (the part that makes the difference)

**Pace:**
- Formal presentation: 100–120 words per minute. The longest line here (slide 3) is ~75 words, about 45 s spoken slowly. If a timed rehearsal runs over, it's pace, not text.
- Breathe at punctuation. The 2-second silence between slide 12's halves is content, not delay.
- Filler words are the enemy of the 120-word minute. Record once and listen; they all show up.

**Rehearsal (no mirrors):**
1. Round 1: timer, point-form notes, one listener. Then ask the listener: "what was the main point?" If the answer isn't "the SRAB descends faster with no single point of failure", the message didn't land.
2. Round 2: only the mixed transitions (slides 5, 7, 8, 9, 12), repeating until the second speaker's entry is automatic.
3. Round 3: record on video, listen once, fix pace and monotone.
4. On the day: arrive early, test the clicker, water on the table.

**Dynamics rules:**
- Handoff signal: half step forward and start talking. No eye-contact negotiation, no waiting.
- Whoever speaks doesn't drive slides: Pablo clicks, or a fourth member.
- If mixed dynamics doesn't click, plan B: each complement becomes a solo line by the slide owner. Nothing else changes.
- Say only the essential numbers out loud: 13.33 m/s, 938 m, 69.9 vs 110 s, ±5%. The rest is on the slide.
- If time runs over, cut from slides 5 and 11. Never from 12.
