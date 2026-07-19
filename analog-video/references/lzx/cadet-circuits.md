# Cadet Circuit Building Blocks (from BOMs + schematics)

Source: open-source BOMs in `lzxindustries/lzxcadet` and schematic PDFs in `lzxindustries/lzxdocs`. Because the Cadets are deliberately single-function, through-hole, CC-licensed circuits — "the ingredients, not the recipes" — their part choices reveal the **canonical building blocks LZX reuses across the whole product line.** When reasoning about how *any* LZX module's analog stages work (including modern Gen3 or legacy Expedition modules whose schematics aren't public), these are the reference circuits.

> Note: Cadet schematic PDFs are vector graphics, so only the BOM component lists extract as text. For the actual net-level schematic, point to the PDF in the `lzxcadet` / `lzxdocs` repos.

## The recurring parts and what they tell you

| Part | Role | What it implies for other LZX modules |
|---|---|---|
| **LM6172** (dual high-speed op-amp) | The video-rate signal-path workhorse — buffers, summers, gain stages | Wherever LZX moves a 0–1 V video signal, expect a fast op-amp like this; bandwidth ≥ video rate is the constraint |
| **TL072 / TL074** (JFET op-amps) | Slower control/CV paths, bias, low-speed processing | CV and "knob" voltages don't need video bandwidth, so cheaper JFET parts handle them |
| **TL431** (precision shunt reference) | Sets a stable reference voltage | This is how the **1 V standard** is anchored — the reference a module measures black/white against |
| **LM1881** (video sync separator) | Strips sync from composite video | Any module that genlocks or accepts external video uses sync separation like this (Sync Gen, Video Input, and conceptually TBC2/ESG3) |
| **AD724** (RGB→NTSC/PAL encoder) | Encodes component RGB to broadcast composite | The core of an encoder stage — informs how ESG3 / Cadet II / legacy encoders turn patch signals into "legal" video |
| **LM361** (high-speed comparator) | Thresholds a signal to a 1-bit output | This *is* a hard key generator — a comparator. Explains Keychain, Cadet VIII, FKG3's hard-key mode |
| **LT1251** (video fader / gain-controlled amp) | Voltage-controlled crossfade / multiply | The building block behind faders and four-quadrant multiply (Cadet VI, Cadet X) |
| **CD4053** (triple analog mux) | Routes/switches signals | Switching and source-select stages (Switcher, Video Input channel select) |
| **ATMEGA88 + CD74HC4046 PLL + CD74HC4538 + SN74HC14** | MCU-driven sync timing with a PLL and Schmitt logic | How master sync timing (H/V/frame) is generated and locked digitally |

## Active components per Cadet module

| Module | Function | Key active parts |
|---|---|---|
| C1 Sync Generator | master NTSC/PAL timing, genlock | ATMEGA88 (MCU), CD74HC4046 (PLL), CD74HC4538, SN74HC14, **LM1881** (sync sep), **LM6172**, L7805 (5 V reg) |
| C2 RGB Encoder | RGB → composite/component out | **AD724** (encoder), CD4053 (mux), LM6172, TL431, SN74HC14, L7805 |
| C3 Video Input | external video → 1 V standard (decode) | **LM1881** (sync sep), CD4053 (mux), LM6172, TL072, 2N3904, TL431, L7805 |
| C4 Dual Ramp Generator | H/V ramps | (ramp integrators built from op-amps + sync from header) |
| C5 Scaler | level scaling (5 V↔1 V) | TL072 |
| C6 Fader | voltage-controlled crossfade | **LT1251** (video fader), LM6172, TL072, TL431 |
| C7 Processor | attenuate / invert / offset | LM6172, TL074, TL431 |
| C8 Hard Key Generator | comparator → hard key | **LM361** (comparator), LM6172, TL072, TL431, L7805 |
| C9 VC Oscillator | video-rate VCO | (oscillator core; see Prismatic Ray for the evolved version of this design) |
| C10 Multiplier | four-quadrant multiply / AM | **LT1251**, LM6172, TL072, TL431 |

## How to use this

When asked "how does LZX do X" or "how would I build/repair a stage that does X," map X to a building block above:
- *Hard edges / keying* → LM361 comparator (Cadet VIII pattern)
- *Crossfade or VC multiply* → LT1251 (Cadet VI / X)
- *Bring external video in / genlock* → LM1881 sync separator (Cadet I / III)
- *Output to a TV/recorder* → AD724-class encoder (Cadet II)
- *Any video buffer/sum/gain* → LM6172-class fast op-amp; *CV path* → TL07x
- *The 1 V reference itself* → TL431

These are reference points, not guarantees that a given modern module uses the exact same part — but the topology and design intent carry across the line. State that distinction when it matters.
