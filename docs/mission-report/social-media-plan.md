# Plano de Postagens — Missão Helike (#213, LASC 2026)

**Período:** segunda-feira, 24/08 → domingo, 30/08 (Semana 1 — 7 dias, 1 post/dia)
**Canais:** Instagram **OU** LinkedIn por dia (conteúdo direcionado à plataforma)
**Extras fora da semana:** 02/09 (abertura da LASC) + dia do lançamento (**04/09**, confirmado)
**Janela de publicação sugerida:** 18h–20h (BRT)
**Tom:** PT-BR, voz técnico-narrativa (sem hype inflado), primeira pessoa quando for relato pessoal (Vinicius)
**Hashtags core (usar em todos):** `#Helike213` `#LASC2026` `#SerraRocketry` `#PocketQube` `#SRAB` `#RocketPy`

---

## Identidade Visual da Missão Helike

Para garantir consistência e reconhecimento imediato, todos os posts seguirão uma identidade visual unificada, inspirada no briefing de telemetria da Serra Rocketry, mas adaptada para a missão Helike como um todo.

### 1. Direção de Arte & Moodboard

**Background:** fundo escuro preto `#0D0D0D` (preto do mission patch) com uma malha quadriculada sutil ao fundo (opacidade de 8–12%, cor `#1A1425`) — estilo blueprint de engenharia ou radar tecnológico, remetendo a diagramas de trajetória e dados de voo.

**Paleta de cores — mission patch (v2, substitui a paleta neon anterior):**

- **Preto (fundo):** `#0D0D0D` — base de todos os slides.
- **Roxo profundo:** `#2D1959` — bordas de card em destaque, elementos estruturais, grid.
- **Roxo claro:** `#907ABF` — destaques secundários, números-chave, subtítulos.
- **Laranja claro:** `#F28749` — destaque primário: títulos de ênfase, linhas do marcador, CTAs.
- **Laranja-marrom:** `#8C4F2B` — acentos terciários (uso pontual).
- **Texto corrido:** branco puro `#FFFFFF`; texto apagado `#8A85A0`.

**Ícones:** [Heroicons](https://heroicons.com) (outline, MIT) renderizados na cor de destaque — link/cadeia no post da cadeia de falhas, raio na capa, olho no contexto, calendário na agenda, check/xmark nas comparações.

**Barra inferior de logos (todos os slides, exceto CTA):** linha horizontal em roxo profundo a ~94% da altura, com os 3 logos: Serra Rocketry (esquerda, versão branca), mission patch (centro) e logo LASC 2026 (direita). Assets em `docs/assets/` (`mission_patch.png`, `lasc_logo.png`).

**Última página (CTA):** mission patch e logo LASC lado a lado na base, abaixo do QR code do repo.

**Composição visual:**

**Tratamento de imagens:** todas as fotos devem ser colocadas dentro de “cards” ou molduras com:

- Cantos arredondados (raio de 12 px).
- Leve sobreposição entre slides consecutivos, para criar profundidade.
- Contorno colorido de 2 px em laranja claro (`#F28749`) para integrar ao fundo escuro.
- Drop shadow sutil (`0px 4px 12px rgba(0,0,0,0.3)`) para destacar o conteúdo do fundo.

**Espaçamento:**

- Margem interna mínima de 24 px dentro dos cards.
- Espaçamento de 16 px entre elementos, seguindo a base do grid de 8 px.

### 2. Padronização de textos na arte

Cada slide do carrossel seguirá esta estrutura, quando houver texto na imagem:

**Marcador (canto superior esquerdo):**

```text
MISSÃO HELIKE - #213
[linha horizontal fina de 1 px, comprimento de 60 px, cor #F28749]
```

**Título principal:** fonte forte (Space Grotesk Bold ou similar), caixa alta, tamanho adaptado ao slide, cor `#FFFFFF`.

**Subtítulo:** aplicar a cor `#907ABF` (roxo claro do patch) com efeito de brilho suave.

**Elementos de destaque:** usar `#F28749` (laranja claro) para números-chave, unidades e termos técnicos que devam ser destacados.

**Rodapé opcional (canto inferior direito):**

- Patch oficial da LASC (2026) — 24 × 24 px, sempre presente.
- Logo pequeno da Serra Rocketry, se disponível — 20 × 20 px, opcional.

### 3. Exemplos de aplicação

**Slide de abertura (Dia 1):**

- Background: `#0D0D0D` com grid `#1A1425`.
- Marcador: “MISSÃO HELIKE - #213” + linha roxa.
- Título: “E SE A RECUPERAÇÃO NÃO TIVESSE COMO FALHAR?”.
- Subtítulo: “SEM SERVO. SEM PIROTECNIA. SEM SOFTWARE DECIDINDO NADA.”.
- Imagem: `Helike_complete_assy_render.JPG` dentro de card com borda laranja.
- Rodapé: Patch LASC + logo Serra, se houver.

**Slide de dados (Dia 6):**

- Background: mesmo padrão.
- Marcador + título/subtítulo conforme o padrão.
- Corpo: tabela comparativa com linhas em `#F28749`, texto em `#FFFFFF` e números-chave em `#907ABF`.
- Imagem: `test2_randon_record.jpg` em card com borda laranja.
- Rodapé: Patch LASC.

---

## Estratégia de Canais (Revisada — 1 post/dia, plataforma por conteúdo)

| Aspecto           | Especificação                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| Formato do slide  | **1080 × 1080 (quadrado)** — funciona nativamente no Instagram e no LinkedIn                      |
| Identidade visual | Segue rigorosamente a seção “Identidade Visual da Missão Helike” acima                            |
| Tipografia        | [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) — Bold títulos, Regular corpo; números em [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono); fallback IBM Plex Sans |
| Tema              | Dark com grid elétrico — consistência absoluta em toda a semana                                   |
| Quantidade        | 5–6 slides por post (1 capa + 3–4 de conteúdo + 1 CTA)                                            |
| Autossuficiência  | Cada slide funciona sozinho (alcance isolado no Instagram) e em sequência (narrativa)             |

### Divisão Instagram vs. LinkedIn (critério)

- **Instagram** → conteúdo visual/emocional/educativo: história, bioinspiração, hardware com foto real, bastidores do time, countdown do lançamento. Caption curta (3–5 linhas).
- **LinkedIn** → conteúdo técnico/profissional: números de validação, arquitetura, lições de engenharia, recuperação passiva como decisão de design. Caption longa (800–1500 palavras).

---

## Visão Semanal (24–30/08) — _Números atualizados conforme o MR final_

| Data      | Dia | Plataforma | Tema                                                               | Gancho                                                                                      |
| --------- | --- | ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **24/08** | Seg | LinkedIn   | O satélite que se recupera sozinho (conceito do SRAB)             | “E se a recuperação não tivesse como falhar?”                                               |
| **25/08** | Ter | LinkedIn   | O que é um PocketQube 1P (50 × 50 × 50 mm)                         | “Um satélite inteiro dentro de um cubo de 5 cm.”                                            |
| **26/08** | Qua | Instagram  | A biologia por trás: sementes de samara + LEV                      | “A natureza resolveu a queda estável há milhões de anos. A gente só copiou.”                |
**27/08** | Qua | Instagram  | Da semente ao código: SRAB → modelo BEM/LEV → simulação Samara_PQ (samara_pq_simulation.py)    | “A natureza inventou, a gente escreveu como equação, a equação virou código.”
| **28/08** | Sex | Instagram  | O TIME: quem construiu o Helike                                    | “Quem fez o Helike?”                                                                        |
| **29/08** | Sáb | LinkedIn   | Simulamos o voo inteiro: pipeline RocketPy + ODE própria           | “Não existe add_autorotating_wing() no RocketPy. Então a gente escreveu uma.”               |
| **30/08** | Dom | Instagram  | COUNTDOWN: o dia do lançamento                                     | “04/09 o Helike sobe no Dédalo. Acompanhe ao vivo — e veja a simulação atualizando sozinha a cada 6h.” _(data confirmada)_ |

> **Nota:** os posts de segunda (conceito), terça (formato) e sábado (simulação) são técnicos e densos → LinkedIn. Os posts de quarta, quinta, sexta e domingo são visuais/narrativos → Instagram. A segunda abre a semana pela pergunta de engenharia ("e se a recuperação não tivesse como falhar?"), e a experiência de 2025 entra no slide 3 como contexto técnico, não como abertura emocional.

---

## Extras (fora da semana)

### EXTRA 1 — Dia 02/09 (abertura da LASC) → **Instagram**

_(Placeholder de data/hora dos eventos oficiais — preencher quando sair a agenda da LASC.)_

1. **Capa:** título “ESTAMOS EM IACANGA” / subtítulo “LASC 2026 COMEÇA HOJE”.
2. **Slide de contexto:** o que a equipe leva (Helike #213 no deployer, integração no Dédalo).
3. **Foto real da chegada/montagem do stand** _(placeholder de asset)_.
4. **Agenda da equipe nos dias 02–05** _(preencher quando confirmado)_.
5. **CTA:** “Acompanhe nos stories — lançamento no dia 04/09”.

**Caption IG curta:** manter o tom “estamos aqui”, sem números novos.

### EXTRA 2 — Dia de LANÇAMENTO (04/09) → **Instagram + LinkedIn simultaneamente**

_(Post preparado ANTES, publicado logo após o voo — nunca durante; placeholder `[DATA_LANCAMENTO]` em todo o texto.)_

#### Etapa nova — “Simulação D-1” (rodar na noite anterior ao voo)

Quando a data for confirmada, rodar o pipeline com a data real do lançamento:

```bash
cd extras/wing-analysis
# editar env.set_date() em src/rocketpy_samara/pipeline_completo.py
#   de: datetime.now() + timedelta(days=1)
#   para: datetime(2026, 9, 4, hora_prevista)  <- data/hora real do voo
python src/rocketpy_samara/pipeline_completo.py
```

O GFS *forecast* cobre a janela do dia 04/09, então a simulação passa a usar **o vento e a densidade previstos para o dia real** — não mais a média genérica usada no MR. Isso gera assets novos e exclusivos:

- Mapa satélite atualizado do ponto de impacto previsto (folium)
- Dashboard LRR com o perfil de descida daquele dia
- Números do dia: apogeu previsto, tempo de descida, deriva

**Como usar nos posts:**

| Momento | Conteúdo da simulação |
|---|---|
| **Countdown (30/08)** | Se a data já estiver confirmada, rodar a D-1 adiantada e postar o mapa de impacto previsto: “é AQUI que ele vai pousar” *(slide extra opcional)* |
| **Véspera / manhã do voo** | Rodar a simulação com data+hora reais e publicar nos STORIES: previsão do dia (impacto, deriva) — conteúdo exclusivo que ninguém mais tem |
| **Pós-voo (post do lançamento)** | Comparação lado a lado: previsto vs. realizado (primeiro dado real vs. mapa da D-1) |

> **Regra:** a simulação D-1 é previsão, não promessa — caption sempre com “previsto para”. E se a comparação previsto × realizado mostrar divergência grande, isso vira o gancho do post-mortem (“onde o modelo errou”), mantendo a honestidade do plano.

#### Estrutura do post (inalterada)

1. **Capa:** “O VOO ACONTECEU” ou, se falhar, versão alternativa pronta.
2. **Primeira imagem/dado real disponível:** foto do lançamento, primeiro pacote LoRa recebido etc.
3. **Status honesto em 3 bullets:** recuperamos? Telemetria? Dados?
4. **Bônus (se houver tempo):** slide “previsto × realizado” com o mapa da D-1.
5. **CTA:** “Post-mortem técnico completo na próxima semana”.

**Caption IG curta + caption LinkedIn longa:** ambas escritas em duas versões (sucesso/falha parcial), escolhidas em campo. A regra do plano original vale em dobro: **relato honesto > hype**.

### EXTRA 3 — Dia 06/09 (encerramento/agradecimento) → **Instagram**

_(Post de fechamento da participação. Fotos da equipe no evento — placeholder de asset até o dia. Fundo escuro.)_

#### Estrutura do carrossel (4 slides)

1. **Capa:** "OBRIGADO, LASC 2026." / foto da equipe no stand
2. **A equipe em pessoa:** foto segurando a asa (asset já existe) + "seis pessoas, dois anos, um cubo de 5 cm"
3. **Agradecimentos:** LASC (oportunidade de voo) · Alba Orbital (frame 1P) · IPRJ-UERJ (apoio) · comunidade (torcida) — adicionar patrocinadores quando houver
4. **O que vem depois:** post-mortem técnico com os dados + SRAB segue como tecnologia para futuras missões PocketQube + link do repo

#### Caption Instagram

> Acabou a LASC 2026 — e a gente volta pra casa com muito mais do que foi. Obrigado à organização pelo voo, à Alba Orbital pelo frame, ao IPRJ-UERJ pelo apoio e a cada um que acompanhou a semana toda. O post-mortem técnico com os dados do voo vem aí. A Serra Rocketry segue.
>
> · #Helike213 #LASC2026 #SerraRocketry #PocketQube #SRAB

> **Nota:** publicar no dia 06/09, após o encerramento do evento. Fotos reais da equipe na LASC são obrigatórias — capturar durante os dias 02–05.

---

# Segunda-feira — “O satélite que se recupera sozinho”

_(Todos os slides seguem a identidade visual definida acima.)_

> **Mudança em relação à versão anterior:** a história de 2025 continua sendo a origem, mas agora entra no slide 3 como *contexto técnico*, não como abertura emocional. A semana começa pela pergunta de engenharia que o Helike responde.

### Carrossel unificado (6 slides)

#### 1. Capa (gancho)

- Background: `#0D0D0D` + grid `#1A1425`.
- Marcador: “MISSÃO HELIKE - #213” + linha `#F28749`.
- Título: “E SE A RECUPERAÇÃO NÃO TIVESSE COMO FALHAR?”.
- Subtítulo: “SEM SERVO. SEM PIROTECNIA. SEM SOFTWARE DECIDINDO NADA.” (`#907ABF` nos três “sem”).
- Imagem: `Helike_complete_assy_render.JPG` em card com borda laranja (12 px de raio, borda de 2 px `#F28749`).
- Rodapé: Patch LASC.

#### 2. O problema

- Título: “TODO MECANISMO DE RECOVERY É UMA CADEIA”.
- Corpo: diagrama horizontal de cadeia com 4 elos, cada elo um card:
  `sensor decide → atuador dispara → energia disponível → paraquedas abre`
  - Elo quebrado = perda total (elo do meio riscado em `#F28749`).
- Subtítulo: “QUEBROU UM ELO, PERDEU O SATÉLITE”.

#### 3. Contexto (a lição de 2025, comprimida)

- Título: “O QUE APRENDEMOS COM A LASC 2025?”.
- Corpo: 2 bullets em branco:
  - “Apogeu atingido, comunicação perdida, voo balístico.”
  - “Sem telemetria suficiente, nem dá pra saber o que falhou.”

#### 4. A resposta: eliminar a classe de falha

- Título: “O SRAB NÃO MELHORA A CADEIA. ELE A ELIMINA.”
- Subtítulo: “Recuperação por aerodinâmica, não por decisão”.
- Corpo: contraste lado a lado:
  - ❌ Paraquedas: sequenciador + atuador + energia + tecido (4 modos de falha)
  - ✅ SRAB: asas abertas por física na ejeção (0 atuadores, 0 mecanismo)
- Destaque em `#907ABF`: “zero pontos únicos de falha na classe deployment”.

#### 5. O que vem na semana

- Título: “ESTA SEMANA: COMO A GENTE CONSTRUIU ISSO”.
- Corpo: mini-agenda em cards (um por linha):
  - Ter — o formato 1P (50 × 50 × 50 mm)
  - Qua — a física da autorrotação
  - Qui — da semente ao código
  - Sex — o time
  - Sáb — os números da validação
  - Dom — countdown do lançamento

#### 6. CTA

- Título: “SEGUE PARA ACOMPANHAR CADA PASSO”.
- Corpo: seta estática apontando para baixo.
- Imagem: fundo com elementos técnicos leves (circuitos, órbitas).
- Rodapé: Patch LASC + “@SerraRocketry” em tamanho pequeno.

### Caption Instagram (curta — caso seja adaptado para IG)

> Todo sistema de recuperação é uma corrente: sensor decide, atuador dispara, paraquedas abre. Quebre um elo e perdeu o satélite. O Helike #213 elimina a corrente inteira: as asas abrem por física, na ejeção, sem nenhum comando. Esta semana a gente mostra como.
>
> · #Helike213 #LASC2026 #SerraRocketry #PocketQube #SRAB #RocketPy #EngenhariaBrasileira

### Caption LinkedIn (longa)

> Antes de contar como construímos o Helike #213, vale explicar a pergunta que originou o projeto: **existe um mecanismo de recuperação que não tenha como falhar?**
>
> **O problema.** Todo recovery convencional é uma cadeia de dependências: um sensor decide a hora de abrir, um atuador (servo ou pirotecnia) executa, energia precisa estar disponível naquele instante exato, e o paraquedas precisa inflar. Cada elo tem sua probabilidade de falha — e elas se multiplicam. Um satélite com um único mecanismo de deployment carrega todos esses modos de falha de uma vez.
>
> **A origem.** Aprendemos isso da pior forma no LASC 2025: dois projetos (SR Couto #100 e SR Coutinho #261), dois anos de trabalho, zero redundância. O voo bateu o apogeu previsto, mas a comunicação caiu, o paraquedas não abriu, e tudo terminou balístico. Sem telemetria suficiente, nem dá pra saber se a causa foi mecânica ou eletrônica.
>
> **A resposta.** O SRAB (Sistema de Recuperação Autorrotativo Bioinspirado) não tenta melhorar cada elo da cadeia: ele remove a cadeia. Não há sequenciador, não há atuador, não há software decidindo nada. As asas ficam recolhidas durante a subida e abrem passivamente na ejeção do deployer; a partir dali, a recuperação é aerodinâmica, com o satélite autorrotando como uma semente de bordo até o solo. Um paraquedas tem quatro modos de falha em série; o SRAB tem zero atuadores. A classe de falha "deployment" sai do projeto inteira, não recebe backup.
>
> Essa é a regra de design que governa todo o Helike: **redundância por classe, não por componente** — 2 kill switches + RBF pin para energia, SD card com fallback automático para LittleFS, 3 beacons LoRa + GPS para localização. Se uma classe de falha existe, precisa de duas mitigações independentes. Se não pode ter duas, a classe não entra.
>
> Repo público com esquemáticos, firmware e dados de teste: github.com/ViniciusCMB/satellite
>
> Nos próximos posts: a física da autorrotação, o modelo computacional e os números da validação. Qual elo da sua cadeia de projeto você eliminaria se pudesse?

---

# Terça-feira, 25/08 — “O que é um PocketQube 1P” → **LinkedIn**

_(Fundo claro #F2F2F2, logo preto. Post educativo: apresenta o formato do satélite e justifica a escolha. Script: helike_ter.js)_

### Carrossel (4 slides)

1. **Capa:** "O QUE É UM POCKETQUBE 1P?" / imagem do frame Alba Orbital (desenho técnico) / "50 × 50 × 50 mm · ~200 g" / "O menor formato padronizado de satélite que existe."
2. **Por que 1P e não CubeSat?** — 3 cards comparando:
   - CanSat: sem envelope padronizado, sem herança de deployer
   - 1U CubeSat: 10 cm, ~1 kg — consumiria o payload do Dédalo inteiro
   - **1P PocketQube**: 5 cm, ~200 g — cabe na classe de 800 g com folga (destaque, borda roxo profundo)
   - Rodapé: "Frame de voo doado pela Alba Orbital no LASC 2025 — estrutura de alumínio com backplate de FRP. A estrutura veio pronta; o esforço foi todo no SRAB."
3. **O Helike #213 em specs:** tabela de 6 linhas — RECUPERAÇÃO (SRAB · 2 asas · passiva) / VELOCIDADE FINAL (13.33 m/s, limite 20, SF 1.5) / CÉREBRO (ESP32-C3 · telemetria 5 Hz) / RÁDIO (LoRa 915 MHz + GPS) / ARMAZENAMENTO (SD + LittleFS) / ENERGIA (1300 mAh · ~8 h, req. 4 h). Fechamento: "Nada importante depende de uma coisa só."
4. **CTA:** "AMANHÃ: A FÍSICA DA AUTORROTAÇÃO" + link do repo

### Caption LinkedIn (longa)

> Um satélite inteiro dentro de um cubo de 5 cm. Parece pouco — e é exatamente esse o ponto.
>
> O Helike #213 é um PocketQube 1P: o menor formato padronizado de satélite que existe. 50 × 50 × 50 mm, ~200 g. Para comparar, um CubeSat 1U tem o dobro do lado e cinco vezes a massa.
>
> **Por que escolhemos o menor?** Porque a missão é validar o SRAB — o sistema de recuperação autorrotativa — e o 1P é o único formato que equilibra três coisas:
>
> - **Cabe no deployer** com herança de voo (diferente de um CanSat, que não tem envelope padronizado nenhum)
> - **Não devora o payload do foguete** — o Dédalo #11 tem classe de 800 g; um 1U comeria a margem inteira, um 1P deixa folga
> - **Exerce o problema real de recuperação** — 200 g caindo de 1520 m precisam de uma solução de verdade, não de um paraquedas de brinquedo
>
> **E tem um detalhe que fez diferença:** o frame de voo foi doado pela Alba Orbital durante o LASC 2025. Estrutura de alumínio com backplate de FRP (material não-condutivo que simplifica o projeto elétrico). Sem isso, teríamos gastado meses projetando e qualificando estrutura em vez de focar no que define a missão: o SRAB.
>
> As specs do Helike: recuperação SRAB com 2 asas, impacto previsto de 13.33 m/s (limite LASC de 20 m/s com fator de segurança de 1.5), cérebro ESP32-C3 com telemetria de 5 Hz, rádio LoRa de 915 MHz com GPS, armazenamento duplo SD + LittleFS e bateria de 1300 mAh dando ~8 h de autonomia (o requisito é 4 h).
>
> Repo público: github.com/ViniciusCMB/satellite
>
> Amanhã: a física da autorrotação — por que girar segura a queda.

---

# Quarta-feira, 26/08 — “A biologia: samara + LEV” → **Instagram**

_(Fundo escuro. Post visual/educativo: o conceito biológico por trás do SRAB. Script: helike_qua.js. Pode reaproveitar os slides 1–2 do post de quinta se quiser mais profundidade.)_

> **Base científica (conteúdo extra p/ slides e stories):** Lentink et al., *Science* 324 (2009) mostrou que a samara gera um **vórtice de borda de ataque (LEV) estável** — a mesma estrutura aerodinâmica que insetos em hover usam — que **dobra a sustentação** em relação a uma asa fixa equivalente. Estudos posteriores (Ulrich & Lei, *J. Bionic Eng.* 2014, com *Acer palmatum*) mediram queda típica de ~1,2 m/s a ~1.250 RPM, com ângulo de cone ~22° — ou seja: a natureza já fez o "controle de descida" que precisávamos. A autorrotação é um **equilíbrio intrínseco estável** (Niu et al., *Phys. Rev. E* 2022): sem controle ativo, a semente sozinha encontra o regime de queda estável — exatamente a classe de falha que o SRAB elimina.

### Carrossel (4 slides)

1. **Capa:** foto superior da samara em card / "A NATUREZA RESOLVEU ISSO HÁ MILHÕES DE ANOS." / "A gente só copiou."
2. **O conceito:** 2 cards lado a lado — "PESO DE UM LADO" (o centro de massa fica numa ponta da semente) / "SUSTENTAÇÃO NO OUTRO" (a asa gera sustentação na ponta oposta; o desequilíbrio faz a semente girar em queda). Fechamento: "Girando, a asa gera sustentação extra: é isso que segura a queda. O vórtice de borda de ataque (LEV) dobra esse efeito."
3. **Do conceito ao satélite:** foto da asa do Helike ao lado de várias sementes / "asa do Helike ao lado das sementes que a inspiraram" / "Sem motor. Sem comando. Só aerodinâmica." _(números de story opcionais: semente cai a ~1,2 m/s girando a ~1.250 RPM; o Helike desce a 13,33 m/s a ~470 RPM — escala de satélite)_
4. **CTA:** "AMANHÃ: DA SEMENTE AO CÓDIGO" + link do repo

### Caption Instagram

> A natureza resolveu a queda estável há milhões de anos — a semente de bordo gira porque o peso fica de um lado e a sustentação do outro. Girando, ela gera um vórtice que dobra a sustentação e segura a queda (Lentink et al. demonstraram isso na Science em 2009: o LEV da samara é o mesmo que insetos usam para voar parado). O SRAB do Helike copia exatamente isso: sem motor, sem comando, só aerodinâmica — e a rotação é autoestável, como na semente. Amanhã: como transformamos biologia em código.
>
> · #Helike213 #LASC2026 #SerraRocketry #PocketQube #SRAB #Bioinspiracao

---


# Quinta-feira, 27/08 — “Da semente ao código” → **Instagram**

_(Carrossel com identidade visual padrão. Post técnico mas LEVE: mostra o caminho natureza → modelo → código sem entrar em derivação matemática. A equação aparece só como "textura visual", sem exigir leitura.)_

### Carrossel (5 slides)

1. **Capa:** título “DE UMA SAMARA A UM SATÉLITE” / subtítulo “NATUREZA → EQUAÇÃO → CÓDIGO”.
2. **O conceito:** foto/render da asa ao lado de uma samara real: “centro de peso numa ponta, sustentação na outra → gira estável ao cair”. Destaque em `#907ABF`: “girando, a asa gera sustentação extra — é isso que segura a queda”.
3. **A iteração:** Asa1 → Asa2 → Asa3 (fotos lado a lado) + um número por asa (7.68 → 8.04 → 12.90 m/s). Mensagem: “cada queda de drone gerava dados; cada dado gerava a próxima asa”.
4. **O código:** pseudocódigo estilizado da simulação em card escuro estilo editor — **sem callouts densos**, só 2 destaques simples: “integrada passo a passo, milhares de vezes por segundo” · “cada força da natureza vira um termo”. Legenda: “a equação que descreve a semente roda até o pouso” _(base: `samara_pq_simulation.py`, extras/wing-analysis)_.
5. **CTA:** “O resultado? O satélite desce girando a ~470 RPM até pousar. Amanhã: quem construiu.”

> **Regra deste post:** zero equações legíveis, zero jargão de API. Quem quiser a profundidade encontra no repo (link na bio) e no post de sábado no LinkedIn.

### Caption Instagram

> Como você transforma uma semente de bordo em equação? A gente escreveu a física da autorrotação como código: cada força do voo virou um termo, cada estado da descida virou uma linha, e o computador integra tudo passo a passo até o pouso. Três gerações de asas depois, a simulação e os testes de queda concordam. Amanhã: o time por trás disso.
>
> · #Helike213 #LASC2026 #SerraRocketry #PocketQube #SRAB #Python #ComputationalFluidDynamics

---

# Sexta-feira, 28/08 — “O TIME” → **Instagram**

_(Carrossel com identidade visual padrão. Post focado na estrutura de liderança exigida pela LASC — Mission Leader + 3 Managers — mais agradecimento geral à equipe estendida. Fotos reais em cards com borda laranja — placeholder de asset até ter as fotos.)_

### Estrutura de liderança (exigência LASC)

| Papel | Quem |
|---|---|
| **Mission Leader** | Vinicius Monnerat |
| **Operations Manager** | João Barizon |
| **Technology Manager** | Pablo |
| **Security Manager** | Steffany Ouverney |

### Carrossel (6 slides)

1. **Capa:** título “QUEM FEZ O HELIKE?” / subtítulo “QUATRO POSTOS, UMA EQUIPE”.
2. **O organograma:** 4 cards (grade 2×2 ou linha), um por papel — foto + nome + breve descrição:
   - **Vinicius Monnerat — Mission Leader:** visão da missão, SRAB e decisões técnicas de último nível.
   - **João Barizon — Operations Manager:** operação, testes e coordenação — do banco de testes à rampa.
   - **Pablo — Technology Manager:** arquitetura eletrônica, PCBs e miniaturização do 1P.
   - **Steffany Ouverney — Security Manager:** análise de riscos, FMECA e compliance de segurança.
3. **E a equipe inteira:** “um satélite não se constrói a quatro” — agradecimento aos demais que desenvolveram o Helike: Gabriel (telemetria/ground station), Heitor (mecânica), Lorena (software), Felipe, Júlia e todo o time da Serra Rocketry. Foto coletiva em card _(placeholder)_.
4. **Slide “Como começou”:** time universitário (IPRJ-UERJ), autofinanciado, aprendendo fazendo.
5. **Slide de bastidor:** uma foto real de bancada/teste de drop com drone.
6. **CTA:** “Quer ver esse cubo caindo e girando? Siga — lançamento dia 04/09.”

### Caption Instagram

> O Helike #213 tem uma estrutura de liderança de quatro postos: Vinicius na liderança da missão, Barizon na operação, Pablo na tecnologia e Steffany na segurança. Mas nenhum satélite voa com quatro pessoas — essa semana inteira foi construída por um time inteiro da Serra Rocketry (IPRJ-UERJ), dividindo estrutura, eletrônica, firmware, simulação e muitos testes de queda com drone. Obrigado a cada um. Lançamento no LASC 2026, dia 04/09.
>
> · #Helike213 #LASC2026 #SerraRocketry #PocketQube #SRAB

---

# Sábado, 29/08 — “Simulamos o voo inteiro antes dele existir” → **LinkedIn**

_(Números conforme o Mission Report final. Post sobre o pipeline RocketPy, mas em tom narrativo: a profundidade técnica fica na estrutura da história, não em jargão. Carrossel segue o mesmo padrão visual; caption longa porém acessível.)_

> **Base técnica (conteúdo extra p/ slides e stories):**
> - RocketPy é um simulador **6-DOF open source** publicado no *Journal of Aerospace Engineering* (Ceotto et al., 2021) e **validado com voos reais de universidades** (EPFL, Notre Dame): desvio de apogeu da ordem de **1%** (ex.: Bella Lui — erro de 0,45%; NDRT — 0,75%). Não é "um simulador qualquer": é ferramenta com paper e validação.
> - O modelo de atmosfera que usamos é o **GFS** (Global Forecast System, NOAA), importado diretamente pelo RocketPy via servidor THREDDS/OPeNDAP da UCAR: perfil completo de vento e densidade por altitude para o local e hora do voo.
> - O Monte Carlo do RocketPy usa **Multivariate Rejection Sampling (MRS)** para reamostrar dispersões sem rodar tudo de novo — o nosso teste de estresse de 100 cenários segue essa mesma filosofia: variar tolerâncias de fabricação e incertezas do modelo, e verificar se o limite de impacto continua respeitado.

### Estrutura do carrossel (5 slides)

1. **Capa:** título “SIMULAMOS O VOO INTEIRO ANTES DELE EXISTIR” / subtítulo “E QUANDO O SIMULADOR NÃO TINHA O QUE A GENTE PRECISAVA, ESCREVEMOS”.
2. **O obstáculo:** simulador de foguetes (RocketPy) sabe simular subida e paraquedas — mas não sabe simular um satélite girando como semente. Destaque: “não tinha botão pra isso”.
3. **A solução:** diagrama simples de 3 blocos: `SUBIDA do Dédalo` → `APOGEU 1520 m` → `DESCIDA do Helike (equação própria)`. Subtítulo: “o satélite 'herda' a posição exata onde o foguete o largou”.
4. **O resultado:** apogeu 1520 m · descida de 111 s · impacto 13.33 m/s — exatamente o alvo (limite 20 m/s ÷ 1.5) · teste de estresse com 100 cenários: todos dentro do limite.
5. **CTA:** repo público + “post-mortem completo depois do voo”.

### Caption LinkedIn (longa)

> Quando decidimos recuperar o Helike #213 sem paraquedas, a recuperação ficou mais confiável, mas apareceu um problema inesperado: **nosso simulador não sabia simular isso**.
>
> Usamos o RocketPy, uma ferramenta open source consagrada para simular voos de foguete. Ele faz muito bem duas coisas: a subida propelida e a descida sob paraquedas. O problema é que o Helike não desce sob paraquedas. Ele desce girando, como uma semente de bordo, e autorrotação é um problema de dinâmica diferente. Forçar isso numa ferramenta feita para outra coisa produz números bonitos e enganosos.
>
> **A saída foi acoplar os dois mundos.** A subida do Dédalo roda no simulador padrão, que para exatamente no apogeu: ~1520 m de altitude, velocidade zero vertical. A partir desse ponto, entra uma equação de movimento que escrevemos especificamente para descrever a autorrotação do SRAB — ela "herda" a posição e velocidade exatas do apogeu e integra a descida até o solo, passo a passo.
>
> Dois detalhes que importam:
>
> - A descida usa a **mesma atmosfera** da subida, com densidade e vento reais previstos para o dia. O desvio que aparece na trajetória entre 1500 e 2000 m não é ruído: é a mesma camada de vento que o foguete cruzou na subida.
> - Como a descida nasce diretamente do resultado da subida, qualquer mudança no foguete (massa, motor) atualiza a previsão de queda automaticamente.
>
> **Os números:** descida de 111 segundos, impacto previsto em 13.33 m/s — exatamente nosso alvo de projeto (o limite da LASC é 20 m/s; projetamos com fator de segurança de 1.5). Rodamos 100 variações de cenário — tolerâncias de fabricação e incertezas do modelo — e todas ficaram abaixo do limite.
>
> Por que confiar na parte de subida? O RocketPy não é um simulador amador: foi publicado no Journal of Aerospace Engineering e validado contra voos reais de equações universitárias (EPFL, Notre Dame), com erro de apogeu abaixo de 1%. A atmosfera da simulação é o forecast GFS do NOAA, importado direto do servidor da UCAR — o mesmo perfil de vento que o foguete vai cruzar no dia 04/09.
>
> E a simulação não parou depois do post: ela roda sozinha a cada 6 horas num GitHub Action no nosso repositório — busca o GFS mais recente, refaz a trajetória e atualiza a landing page pública com o novo ponto de impacto. O mapa que está lá agora é o resultado do último ciclo GFS, não de uma simulação congelada de semanas atrás.
>
> Tudo open source: github.com/ViniciusCMB/satellite
>
> No dia 04/09, essa simulação encontra o voo real no LASC 2026.

---

# Domingo, 30/08 — “Countdown” → **Instagram**

_(Data confirmada: lançamento em 04/09. Hora segue placeholder até sair a janela de voo — a landing page pública usa 09:00 BRT como referência do countdown.)_

### Conteúdo extra — a simulação que conta os dias junto

O countdown não é só um post: é **infraestrutura rodando de verdade**. Um GitHub Action no repositório (`sim-refresh.yml`) dispara sozinho **a cada 6 horas**, alinhado com os ciclos de release do GFS (00/06/12/18 UTC). A cada disparo ele:

1. Instala o ambiente e roda o pipeline RocketPy completo (subida do Dédalo + descida autorrotativa do SRAB);
2. Busca o forecast GFS mais recente para o local/hora do voo;
3. Regenera os artefatos (trajetória 3D, GeoJSON top-down, números da descida);
4. Commita os novos dados e publica no GitHub Pages.

Resultado prático p/ o post: a landing page (link na bio) tem um **countdown ao vivo para 04/09** e um **mapa de impacto previsto que se atualiza sozinho** conforme os forecasts do NOAA melhoram na semana do voo. Quanto mais perto do dia, melhor o GFS — e mais preciso o mapa. Isso é o slide 5 (bônus) do carrossel.

### Carrossel (5 slides)

1. **Capa:** marcador “MISSÃO HELIKE - #213” / título “04/09” em destaque gigante (`#907ABF`) / subtítulo “O HELIKE VOA”.
2. **Contexto:** o foguete Dédalo #11 leva o Helike a ~1520 m; na ejeção, as asas abrem sozinhas.
3. **O que assistir:** 111 s de descida girando; telemetria LoRa ao vivo na ground station.
4. **Onde acompanhar:** stories da Serra Rocketry + transmissão oficial da LASC _(link quando sair)_. + countdown ao vivo na landing page.
5. **Slide bônus:** mapa satélite da simulação D-1 com o ponto de impacto previsto — “é AQUI que ele vai pousar” _(print direto da landing page — ela já se atualiza sozinha a cada 6h via GitHub Action)_.
6. **CTA:** “Ative as notificações. Dia 04/09, às [HORA].” _(hora placeholder até sair a janela de voo)_.

### Caption Instagram

> Está marcado: 04/09, o Helike #213 sobe no foguete Dédalo no LASC 2026. A ~1520 m de altitude, o satélite é ejetado, as asas abrem sem nenhum comando, e ele desce girando como uma semente de bordo, transmitindo telemetria o tempo todo. Toda a validação que mostramos essa semana vai ser testada de verdade. O countdown está ao vivo no link da bio — e o mapa de impacto previsto lá se atualiza sozinho a cada 6h com o forecast mais recente. Nos vemos lá.
>
> · #Helike213 #LASC2026 #SerraRocketry #PocketQube #SRAB

---


# Anexos Operacionais (Revisados)

## A. Checklist de assets por post — _Com tratamento visual especificado_

| Dia              | Asset base                                                                     | Tratamento visual obrigatório                                                        |
| ---------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **Seg (24/08)**  | `Helike_complete_assy_render.JPG`, `fig_srab_vs_parachute.png`                 | Card com borda laranja; cadeia de 4 elos como cards com o do meio riscado em `#F28749`            |
| **Ter (25/08)**  | `Helike_complete_assy_render.JPG`, `1P_ALBA_ORBITAL_frame_p1.png`              | Ambos em cards com borda laranja; frame 1P pode ter destaque em `#907ABF` nas dimensões          |
| **Qua (26/08)**  | `Asa2_dxf_p1.png`, `fig_test2_geometry.png`                                    | Cards com borda laranja; destacar área +12% em `#907ABF` e setas de tendência                    |
| **Qui (27/08)**  | Fotos Asa1/Asa2/Asa3 + pseudocódigo da simulação (`extras/wing-analysis/src/samara_pq_simulation.py`) em card escuro estilo editor _(placeholder)_ | Código em card escuro estilo editor, callouts em `#907ABF`           |
| **Sex (28/08)**  | Fotos reais dos 6 membros + foto de bancada/drop _(placeholder até ter fotos)_ | Cards com borda laranja individuais; nome + função em branco                                     |
| **Sáb (29/08)**  | `fig_full_trajectory.png`, `fig_mc_sensitivity.png`, `Asa3.DXF` (render CAD)   | Cards com borda laranja; diagrama de 3 estágios com setas em `#F28749`, números em `#907ABF`     |
| **Dom (30/08)**  | `Helike_complete_assy_render.JPG` ou render do deployer                        | Card com borda laranja; data gigante em `#907ABF` na capa                                         |
| **Extra 02/09**  | Foto real da chegada/montagem _(placeholder)_                                  | Card com borda laranja                                                                            |
| **Extra launch** | Foto do lançamento / primeiro pacote LoRa _(capturar no dia)_                  | Card com borda laranja; versões de sucesso + falha preparadas antes                               |

> **Notas críticas:**
>
> - Os assets de sexta-feira (fotos do time) e dos extras dependem de captura nova — agendar sessão de fotos **antes de 28/08**.
> - O post de domingo (countdown) já pode ser produzido com a data confirmada (04/09); a hora do CTA segue placeholder até sair a janela de voo.

## B. Workflow de produção — _Com passo de identidade visual_

### 1. Seg–Sex (noite anterior)

- Escrever/atualizar a caption do LinkedIn no Google Docs/Notion.
- Confirmar quais assets base serão usados (ver checklist A).

### 2. Sábado de manhã

- Abrir o template Figma/Canva da identidade visual Helike.
- Importar os assets base do dia.
- Aplicar tratamento de card (12 px de raio, borda de 2 px `#F28749`, sombra sutil).
- Adicionar marcador padrão (canto superior esquerdo), títulos/subtítulos seguindo a hierarquia.
- Incluir rodapé obrigatório (patch LASC + logo Serra, se houver).
- Exportar 5–6 slides como PNG (para Instagram) + PDF multipágina (para LinkedIn).

### 3. Sábado à tarde

- Revisar a consistência visual entre os slides (cores, espaçamento e alinhamento).
- Agendar a publicação para domingo às 18h.

### 4. Domingo, 18h

- Publicação automática.
- Monitorar comentários nas primeiras 2h (responder perguntas técnicas no LinkedIn e engajar no Instagram).

### 5. Segunda-feira de manhã

- Responder comentários técnicos do LinkedIn.
- Responder DMs do Instagram com perguntas específicas.
- Arquivar as métricas do dia anterior.

---

## C. Variações de copy — _Inalteradas, mas agora com identidade visual aplicada aos stories/reels_

- “Um satélite inteiro em 5 × 5 × 5 cm. Sem paraquedas.”
- “A gente copiou a queda de uma semente.”
- “O que aprendemos com a LASC 2025? Nada importante depende de uma coisa só.”
- “13.33 m/s caindo, sem paraquedas. Como?”

**CTAs alternativos (para A/B — inalterados):**

- “Comenta o que você faria diferente.”
- “Salva para mostrar para o time.”
- “Marca um amigo que trabalha com hardware.”
- “Compartilha se isso é relevante para o seu projeto.”

---

## D. Métricas para acompanhar (semanal) — _Inalteradas_

- Alcance por post (Instagram) e impressões (LinkedIn).
- Taxa de salvamento (Instagram) — indicador de valor percebido.
- Comentários técnicos vs. elogios genéricos (LinkedIn) — filtro de qualidade da audiência.
- Cliques no link do repo (somando LinkedIn).
- DMs de outros times/universidades pedindo _spec sheet_ — sinal de impacto real.

---

## E. Riscos do plano — _Atualizado com consideração de identidade visual_

- **Risco baixo:** viralizar antes da competição e vazar detalhes de projeto.
  **Mitigação:** posts são sobre conceitos e arquitetura, não sobre parâmetros de voo secretos (canal LoRa, IDs etc. já são públicos no repo).

- **Risco médio:** comparação com paraquedas pode soar como crítica a quem usa.
  **Mitigação:** ênfase sempre em “escolha nossa”, nunca em “errado vs. certo”.

- **Risco médio:** janela de voo (hora) não confirmada a tempo do post de domingo.
  **Mitigação:** data já confirmada (04/09); publicar o countdown com “04/09” e complementar a hora nos stories quando sair a janela.

- **Risco médio:** post do dia do lançamento depender do resultado.
  **Mitigação:** duas versões prontas antes do voo (sucesso/falha parcial), escolhidas em campo; nunca postar durante o voo.

- **Risco baixo:** falta de fotos do time para o post de sexta-feira, 28/08.
  **Mitigação:** agendar sessão de fotos até 27/08; fallback = fotos de bancada/drop já existentes + nomes/funções sem retrato individual.

- **Risco novo (baixo):** inconsistência na aplicação da identidade visual.
  **Mitigação:** criar e bloquear um template Figma/Canva com todos os elementos fixos (marcadores, rodapé, estilos de texto); designer ou responsável pela arte utiliza somente esse template.

---

## F. Próximos passos depois da Semana 1

- **31/08–01/09:** preparar os posts dos extras (02/09 e dia do lançamento), incluindo as duas versões do post de voo.
- **Semana da LASC (02–05/09):** cobertura diária em stories (Instagram) + post de abertura (02/09) + post de lançamento no dia do voo.
- **Pós-LASC:** post-mortem técnico completo (sucessos + falhas + dados) — Instagram curto + LinkedIn longo, com telemetria real vs. simulação.

---

## G. Sugestões em aberto

1. **Reel do drop test como conteúdo âncora da quinta.** O post "da semente ao código" ganha muito mais com um vídeo curto (10–15 s) do drone soltando o protótipo e ele girando, com o número de RPM animado na tela. Reel alcança muito mais que carrossel no IG; o carrossel vira o post principal e o reel vira teaser no mesmo dia. Os clipes dos Testes 1–3 já existem.
2. **Pin nos destaques.** Fixar no perfil: post de segunda (conceito), sábado (simulação) e, depois do voo, o resultado. Quem chegar no perfil pela LASC vê a história em ordem.
3. **Colaboração com a RocketPy.** O post de sábado é essencialmente um case study de uso da ferramenta. Mencionar @RocketPy no LinkedIn/IG custa nada e pode gerar repost pra uma audiência técnica grande. Se der, oferecer um guest post curto pro blog/newsletter deles pós-voo.
4. **Story com enquete na véspera.** "Que velocidade você acha que vai bater? Menos de 13 m/s / mais de 13" — barato de fazer, gera engajamento pré-voo e dá gancho pronto pro resultado.

