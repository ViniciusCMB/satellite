#!/usr/bin/env python3
"""Generate Helike presentation audio via edge-tts, one segment per speech line.
Differentiates the 3 speakers with rate/pitch on the single male pt-BR voice."""
import asyncio, os, subprocess, sys
import edge_tts

OUT = os.path.dirname(os.path.abspath(__file__))
TMP = os.path.join(OUT, "segments")
os.makedirs(TMP, exist_ok=True)

SPEAKERS = {
    "vinicius": dict(voice="pt-BR-AntonioNeural", rate="-4%", pitch="-8Hz"),
    "pablo":    dict(voice="pt-BR-AntonioNeural", rate="+2%", pitch="+22Hz"),
    "barizon":  dict(voice="pt-BR-AntonioNeural", rate="+6%", pitch="+38Hz"),
}

# (speaker, label, text) — speech lines only, PT-BR
SCRIPT = [
    ("vinicius", "02-abertura", "Bom dia. Antes do satélite, uma pergunta: quando você solta uma semente de samara da mão, ela não cai. Ela desce girando, devagar, e pousa de pé. A gente passou um ano perguntando: e se um satélite caísse do mesmo jeito? Eu sou o Vinicius, Mission Leader, da Serra Rocketry, do IPRJ-UERJ. Comigo estão o Pablo, Technology Manager, e o Barizon, Operations Manager. E essa é a Helike, número duzentos e treze."),
    ("vinicius", "03-paradigma", "Por que substituir o paraquedas? Porque ele é o elo fraco. Sequenciador de deploy, pirotecnia, linha que enrola. Cada item dessa lista é um ponto único de falha. A gente já perdeu payload por menos. A samara não tem nada disso. É cem por cento passiva: a energia da queda vira giro estável. Sem atuador, sem pirotecnia, sem linha. O hardware que menos pode falhar é o que não existe."),
    ("vinicius", "04-aero", "Mas a semente faz uma coisa que a aerodinâmica clássica dizia ser impossível: gera sustentação além do estol. O truque é o Leading-Edge Vortex — um vórtice que gruda na borda de ataque e eleva o coeficiente de sustentação local para dois a cinco. O desafio era enfiar isso em cinquenta milímetros. As asas da Asa três foram parametrizadas em volta dessa restrição: beta de cinco graus, duzentos gramas."),
    ("vinicius", "05a-validacao", "Teoria bonita sem chão é só bonita. Então fomos para o chão: queda de vinte metros, três ciclos de teste. Resultado: doze por cento mais área deram oitenta e um vírgula seis por cento mais conicidade. O modelo previu, o experimento confirmou."),
    ("barizon", "05b-validacao", "E esses testes são da minha rotina de operações. Medir conicidade, ajustar geometria, soltar de novo. Ciclo curto, erro rápido."),
    ("vinicius", "06-autorotacao", "Com o modelo validado, rodamos a simulação completa: Runge-Kutta de quinta ordem. O sistema se estabiliza sozinho em cerca de dez segundos, depois da dispensa a novecentos e trinta e oito metros. E a partir daí é regime: treze vírgula três três metros por segundo de descida, conicidade de oito vírgula seis graus, quatrocentos e setenta e sete rotações por minuto. Soltou, girou, estabilizou — sem ninguém tocando em nada."),
    ("vinicius", "07a-montecarlo", "A pergunta que toda banca faz: e a tolerância de fabricação? Rodamos cem iterações de Monte Carlo variando massa, passo beta, arrasto parasita e fator de forma. Deu treze vírgula três dois, mais ou menos zero vírgula três um metros por segundo, variação abaixo de dois vírgula cinco por cento. A velocidade terminal fica invariante até com mais ou menos vinte por cento no arrasto."),
    ("barizon", "07b-montecarlo", "Traduzindo para a bancada: as imperfeições do PETG impresso em três D não derrubam a previsibilidade. A gente viu isso na impressora."),
    ("vinicius", "08a-trajetoria", "Agora o sistema completo: a descida do SRAB acoplada ao perfil de subida real do Dédalo onze, com vento GFS via RocketPy. Descida rápida, janela de deriva menor."),
    ("barizon", "08b-trajetoria", "E é aqui que a operação agradece. O CEP de recolhimento encola: menos área para procurar, menos tempo de payload exposto ao vento. É a diferença entre procurar um satélite e ir buscá-lo."),
    ("pablo", "09a-hardware", "E a eletrônica, que é a minha frente: MCU, IMU, sensor ambiental, GPS e LoRa em cinquenta gramas dentro do um P. O núcleo é um ESP três dois, C três, com escalonamento cooperativo. Barramentos segregados: I dois C para os sensores a vinte hertz, SPI com chip selects dedicados para LoRa e micro SD, UART exclusiva para o GPS."),
    ("vinicius", "09b-firmware", "E o firmware que roda nisso passou pela minha mão: loop determinístico de cinquenta milissegundos, telemetria por LoRa, gravação dupla em SD e LittleFS. Segurança física: kill switches no eixo Z e pino RBF. A Helike só liga quando a gente decide que ela liga."),
    ("barizon", "10-sistemas", "E para nada disso quebrar em campo, o software foi desenhado esperando o pior. A metodologia tem três filtros: compliance com os manuais da LASC; design defensivo via FMECA, com rejeição de NaN em nível de hardware e armazenamento duplo; e viabilidade temporal: um loop de cinquenta milissegundos em vez de máquinas de estado complexas. A regra da equipe é simples: se pode dar errado, já está tratado."),
    ("pablo", "11-gpsdenied", "E se o GPS morrer no momento crítico? A missão não morre com ele. A missão secundária é localização sem GPS: trilateração de RSSI via LoRa com três beacons terrestres independentes. O satélite não precisa saber onde está — os beacons sabem onde ele está."),
    ("barizon", "12a-benchmark", "Este slide resume a missão. Comparação honesta: paraquedas circular de duzentos milímetros contra o SRAB de duas asas, ambos a duzentos gramas, do apogeu do Dédalo, novecentos e trinta e oito metros. Deu sessenta e nove vírgula nove segundos contra cento e dez. E a deriva horizontal: trezentos e trinta e nove metros contra quinhentos e trinta e quatro."),
    ("vinicius", "12b-benchmark", "Trinta e seis por cento menos tempo, trinta e seis por cento menos deriva, e cem por cento dos modos de falha de deploy ativo eliminados. O paraquedas é mais simples de explicar. O SRAB é mais simples de confiar."),
    ("barizon", "13-criterios", "E o lançamento não é praça de prova aberta: tem critério. Velocidade de impacto dentro de mais ou menos cinco por cento da previsão. Tempo de descida dentro de mais ou menos três por cento. Telemetria a vinte hertz sem perder amostra. Se o voo real fechar com a simulação, o modelo está pronto para escalar."),
    ("vinicius", "14-fechamento", "Para fechar, voltando à semente do começo: ela virou um sistema que cai mais rápido, mais perto e sem pirotecnia. A simulação rodou no RocketPy com as nossas próprias equações, as referências estão aqui. E o QR Code leva para a página da missão, com a contagem regressiva para o lançamento. A natureza levou milhões de anos para aperfeiçoar a queda. A gente só precisou de um ano. Obrigado!"),
]

async def synth_all():
    ok = True
    for spk, label, text in SCRIPT:
        cfg = SPEAKERS[spk]
        dst = os.path.join(TMP, f"{label}.mp3")
        if os.path.exists(dst):
            continue
        try:
            await edge_tts.Communicate(text, cfg["voice"], rate=cfg["rate"], pitch=cfg["pitch"]).save(dst)
            print(f"OK  {label} [{spk}]")
        except Exception as e:
            ok = False
            print(f"FAIL {label} [{spk}]: {e}")
    return ok

def concat(files, dst):
    lst = os.path.join(OUT, "list.txt")
    with open(lst, "w") as f:
        for p in files:
            f.write(f"file '{p}'\n")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c:a", "libmp3lame", "-q:a", "2", dst], check=True, capture_output=True)
    os.remove(lst)

def main():
    if not asyncio.run(synth_all()):
        sys.exit(1)
    # full presentation, in script order
    full = [os.path.join(TMP, f"{lbl}.mp3") for _, lbl, _ in SCRIPT]
    concat(full, os.path.join(OUT, "helike-apresentacao-completa.mp3"))
    # one file per speaker, in order
    for spk in SPEAKERS:
        segs = [os.path.join(TMP, f"{lbl}.mp3") for s, lbl, _ in SCRIPT if s == spk]
        concat(segs, os.path.join(OUT, f"helike-{spk}.mp3"))
    print("DONE")

if __name__ == "__main__":
    main()
