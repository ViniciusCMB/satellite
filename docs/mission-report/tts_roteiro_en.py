#!/usr/bin/env python3
"""English version: Helike presentation audio via edge-tts, one segment per line.
3 distinct en-US male voices (native edge voices, no pitch tricks needed)."""
import asyncio, os, subprocess, sys
import edge_tts

OUT = os.path.dirname(os.path.abspath(__file__))
TMP = os.path.join(OUT, "segments_en")
os.makedirs(TMP, exist_ok=True)

SPEAKERS = {
    "vinicius": "en-US-GuyNeural",
    "pablo":    "en-US-AndrewNeural",
    "barizon":  "en-US-ChristopherNeural",
}

SCRIPT = [
    ("vinicius", "02-abertura", "Good morning. Before the satellite, a question: when you drop a samara seed from your hand, it doesn't fall. It spins down, slowly, and lands upright. We spent a year asking: what if a satellite came down the same way? I'm Vinicius, Mission Leader, from Serra Rocketry, IPRJ UERJ. With me are Pablo, our Technology Manager, and Barizon, our Operations Manager. And this is Helike, number two hundred and thirteen."),
    ("vinicius", "03-paradigma", "Why replace the parachute? Because it's the weak link. Deployment sequencers, pyrotechnics, lines that tangle. Every item on that list is a single point of failure. The samara has none of that. It's fully passive: falling energy becomes stable spin. No actuators, no pyrotechnics, no lines. The hardware least likely to fail is the hardware that doesn't exist."),
    ("vinicius", "04-aero", "But the seed does something classical aerodynamics called impossible: it generates lift beyond stall. The trick is the Leading-Edge Vortex — a vortex that clings to the leading edge and pushes the local lift coefficient to two to five. The challenge was fitting that into fifty millimeters. The Asa three wings were parameterized around that constraint: five degrees of pitch, two hundred grams."),
    ("vinicius", "05a-validacao", "A pretty theory with no ground truth is just pretty. So we went to the ground: twenty-meter drops, three test cycles. Result: twelve percent more area gave eighty one point six percent more coning. The model predicted it, the experiment confirmed it."),
    ("barizon", "05b-validacao", "And those tests are part of my operations routine. Measure coning, adjust the geometry, drop again. Short cycle, fail fast."),
    ("vinicius", "06-autorotacao", "With the model validated, we ran the full simulation: fifth-order Runge-Kutta. The system stabilizes itself in about ten seconds after release from nine hundred and thirty-eight meters. Then it's all steady state: thirteen point three three meters per second descent, eight point six degrees of coning, four hundred and seventy-seven RPM. Released, spinning, stable — with nobody touching anything."),
    ("vinicius", "07a-montecarlo", "The question every panel asks: what about manufacturing tolerance? We ran one hundred Monte Carlo iterations, perturbing mass, pitch angle, parasitic drag, and form factor. We got thirteen point three two, plus or minus zero point three one meters per second, variation under two and a half percent. Terminal velocity stays invariant even with plus or minus twenty percent on the base drag coefficient."),
    ("barizon", "07b-montecarlo", "On the shop floor, that means the imperfections of three-D printed PETG don't hurt predictability. We saw it at the printer."),
    ("vinicius", "08a-trajetoria", "Now the full system: the SRAB descent coupled to the real ascent profile of Dédalo eleven, with GFS winds through RocketPy. Faster descent, narrower drift window."),
    ("barizon", "08b-trajetoria", "And this is where operations says thank you. The recovery CEP shrinks: less area to search, less time with the payload exposed to wind. It's the difference between searching for a satellite and going to pick it up."),
    ("pablo", "09a-hardware", "The electronics, which is my front: MCU, IMU, environmental sensor, GPS, and LoRa in fifty grams inside the one-P form factor. The core is an ESP thirty-two C three with cooperative scheduling. Segregated buses: I-two-C for sensors at twenty hertz, S-P-I with dedicated chip selects for LoRa and micro S-D, and a dedicated UART for the GPS."),
    ("vinicius", "09b-firmware", "And the firmware running on it went through my hands: a deterministic fifty-millisecond loop, LoRa telemetry, dual logging to SD and LittleFS. Physical safety: Z-axis kill switches and an RBF pin. Helike only powers up when we decide it powers up."),
    ("barizon", "10-sistemas", "And to keep none of this breaking in the field, the software was designed expecting the worst. The methodology has three filters: compliance with the LASC manuals; defensive design through FMECA, with hardware-level NaN rejection and dual storage; and temporal viability: a fifty-millisecond loop instead of complex state machines. The team rule is simple: if it can go wrong, it's already handled."),
    ("pablo", "11-gpsdenied", "And if GPS dies at the critical moment? The mission doesn't die with it. The secondary mission is GPS-denied localization: RSSI trilateration over LoRa with three independent ground beacons. The satellite doesn't need to know where it is — the beacons know where it is."),
    ("barizon", "12a-benchmark", "This slide is the mission in one table. An honest comparison: a two hundred millimeter circular parachute against the two-wing SRAB, both two hundred grams, from Dédalo's apogee, nine hundred and thirty-eight meters. That's sixty-nine point nine seconds versus one hundred and ten. And horizontal drift: three hundred and thirty-nine meters versus five hundred and thirty-four."),
    ("vinicius", "12b-benchmark", "Thirty-six percent less descent time, thirty-six percent less drift, and one hundred percent of active deployment failure modes eliminated. The parachute is simpler to explain. The SRAB is simpler to trust."),
    ("barizon", "13-criterios", "And the launch isn't an open proving ground: there are acceptance criteria. Impact velocity within five percent of prediction. Descent time within three percent. Telemetry at twenty hertz with zero sample loss. If the real flight closes with the simulation, the model is ready to scale."),
    ("vinicius", "14-fechamento", "To close, back to the seed from the start: it became a system that falls faster, closer, and without pyrotechnics. The simulation ran on RocketPy with our own samara dynamics equations; the references are here. And the QR code takes you to the mission page, with the countdown to launch. Nature took millions of years to perfect the fall. It took us one year. Thank you!"),
]

async def synth_all():
    ok = True
    for spk, label, text in SCRIPT:
        dst = os.path.join(TMP, f"{label}.mp3")
        if os.path.exists(dst):
            continue
        try:
            await edge_tts.Communicate(text, SPEAKERS[spk]).save(dst)
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
    full = [os.path.join(TMP, f"{lbl}.mp3") for _, lbl, _ in SCRIPT]
    concat(full, os.path.join(OUT, "helike-presentation-full-en.mp3"))
    for spk in SPEAKERS:
        segs = [os.path.join(TMP, f"{lbl}.mp3") for s, lbl, _ in SCRIPT if s == spk]
        concat(segs, os.path.join(OUT, f"helike-{spk}-en.mp3"))
    print("DONE")

if __name__ == "__main__":
    main()
