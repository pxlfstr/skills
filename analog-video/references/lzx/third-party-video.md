# Third-Party Video Modules (non-LZX makers)

Coverage of the makers the owner asked about. Sourced from maker sites, ModularGrid, and retailers; depth varies and sparse entries are flagged. **Format matters a lot here**, so each maker is tagged:

- **LZX-format** — runs on the LZX 1 V video standard, integrates directly with an LZX rig.
- **Audio-rate CV** — Eurorack module but expects ±5 V (not 1 V); interfaces with audio modular, needs scaling for LZX.
- **Standalone / composite** — processes or generates composite (RCA) video, often outside Eurorack voltage norms.
- **Audio maker** — listed for completeness; no dedicated video module found.

Quick read on owner fit: the **LZX-format DIY** makers (Foxing Hour, Syntonie, Reverse Landfill) are the most relevant to an LZX system and many are 4–8 HP; the standalone instruments (Gieskes, Sleepy Circuits, Special Stage Systems, Razmasynth) are video sources/displays rather than rack utilities.

---

## Dave Jones Design (jonesvideo.com / djdesign.com) — *legend, standalone composite + ±5V CV*
Dave Jones is a foundational figure in video synthesis (Sandin Image Processor lineage).

| Module | HP | Function |
|---|---|---|
| **MVIP / MVIP Mk 2** | 14 | Mini Video Image Processor. **Verified from jonesvideo.com.** Standalone composite processor: 1 composite in, 1 composite out, auto-detects NTSC/PAL. Five CV inputs accept **±5 V** (audio-world, NOT LZX 1 V). CVs control brightness, color hues, **bit-swapping** of the digitized video, and processing-function/mode selection. Single-source only — does **not** combine multiple video signals. Self-contained: needs no other video modules to work. Mk 2 = 51 mm deep, 200 mA +12 / 75 mA −12 (original = 65 mm, 140/140 mA). $595. Manual: jonesvideo.com/products/MVIP_instructions_booklet.pdf |
| **O'Tool Plus** | 8 | Oscilloscope + visual audio toolkit: 1/2-channel + 3D scope, X/Y, level/VU/peak meter, voltmeter, frequency meter, tuner, spectrum analyzer, spectrogram, BPM. 3 user presets, firmware-upgradable, RCA. Power 80 mA/22 mA (or 12 mA +12 / 70 mA +5 / 22 mA −12), 40 mm deep |

**Owner fit (MVIP):** a self-contained composite effect box (bitswap / brightness / hue glitching). Sits at the output stage (after the Visual Cortex encodes to composite) or processes an external composite source. Its ±5 V CV means drive it from audio-world modulators, not directly from LZX 1 V signals. A sidecar, not an integrated 1 V rack citizen.

## Erogenous Tones (erogenoustones.com) — *digital video generator + modulation* ⚠️ low priority
Mostly an audio maker; one **video** module plus modulation/utility usable in a video rig.

| Module | HP | Function |
|---|---|---|
| **Structure** | 38 | Node-based **digital video synth** (OpenGL / GLSL shaders). Input switchable composite *or* **LZX 1 V RGB** (scalable 1–5 V); mixes incoming video with generators/effects/audio. Front-panel **joystick** for modulation + automation looping; 3 button-triggerable gate ins; **USB MIDI** host; SD-card presets/custom shaders; NTSC/PAL out. A bring-your-own-shaders module that bridges to LZX |
| **RADAR** / **BLIP** | 28 / 8 | 8-channel AD/AR LFO envelope generator (+ expander) — modulation source |
| **LEVIT8** / **VC8** | 10 / 18 | 8× attenuator/gain/invert/offset/mixer; octal linear VCA — utilities (audio-rate; scale for LZX) |

## Foxing Hour (foxinghour.com) — *LZX-format, 3U DIY + assembled*
Source: **ModularGrid manufacturer page (vendors/view/978), fetched directly.** LZX 1 V format, mostly small-HP and inexpensive. Owner owns **GAMMA**.

| Module | HP | MSRP | Function |
|---|---|---|---|
| **GAMMA** | 4 | $26 | Dual Log, Expo & Sum — gamma-style curve shaping *(owner owns)* |
| **SHUTTER** | 8 | $32 | Triple 2-to-1 video multiplexer / luma switcher; daisy-chainable |
| **VEIL** | 4 | $28 | Priority-layering video module w/ variable opacity (series/parallel for more layers) |
| **FELT** | 4 | — | Voltage-controlled state-variable video filter (HP + LP outs) — fine edge extraction / variable smearing |
| **DAISY** | 12 | $37 | Chainable matrix mixer |
| **ACCESS** | 8 | $25 | Triple attenuvert + bias (CV/processing utility) |
| **Dual A+B−C** | 4 | $22 | Dual A+B−C math |
| **RECT** | 4 | $22 | Dual rectifier & frequency doubler |
| **LUMA** | 4 | $22 | RGB → Y grayscale converter |
| **NVRT** | 4 | $16 | Quad video inverter |
| **IRIS** | 4 | — | Fixed DC voltage offset |
| **MULTA** | 4 | $16 | Dual 1-to-3 video-rate buffered multiple |
| **MULTB (8HP)** | 8 | $19 | Quad 1-to-3 distro amp (YRGB) |
| **MULTB (6HP)** | 6 | $110 | Quad 1-to-3 distro amp (YRGB) |
| **PASS4 YRGB Passive Switch** | 6 | — | Quad 2:1 or 1:2 passive switch |
| **SW6 Expander** | 4 | $10 | Six-switch expander |

Build guides, BOMs and schematics are open-source at **github.com/foxinghour/foxdocs** (see `open-source-repos.md`).

## Gieskes (gieskes.nl) — *standalone, Eurorack/LZX-compatible w/ step-up*
| Module | Function |
|---|---|
| **3TrinsRGB+1c** | Standalone analog A/V synth: 3 internal oscillators tied to R/G/B, each switchable horizontal/vertical with variable sync; composite video in; per-channel CV; brightness, color-inversion, scrolling; pin-header patchbay; audio synth too. Effects: pattern synthesis, colorization, solarization, audiovis, scrolling, keying. Eurorack/LZX-compatible but LZX 1 V signals need a voltage bridge to drive it dramatically |
| **Oscillatoscope** (1d/2b/2e) | Oscilloscope / scope-art module |

## Melted Electronics — *standalone + Eurorack, glitch*
| Module | Function |
|---|---|
| **Video Breaker** | Analog glitch processor for VGA / LZX / composite / component. VGA mode glitches HD up to 2048×1536 with stable sync (straight to projector, no TBC). Per-channel bypass + CV, Brightness and Effect-Strength knobs, 3 grain settings |
| **Glitch Boy** | NES-based 8-bit glitch video synth + chiptune instrument (standalone & Eurorack, same PCB). Composite NTSC/PAL. Glitch A = CPU (sprite/sound corruption), Glitch B = PPU (background/sprite corruption); CV-A/CV-B inputs; MIDI; open-source firmware |

## Lone Vidiot (Dan Bucciano) — *LZX-format, handmade*
| Module | Function |
|---|---|
| **Solachromatron** | 1 V LZX-compatible analog **colorizer + solarizer**: independently applies **solarization across R/G/B**, each modulated by its own CV input, with a built-in **LFO** for self-modulation. Handmade in small numbers with custom faceplates (expect cosmetic imperfections) |

## Luix — *LZX accessory (expander)*
| Module | HP | Function |
|---|---|---|
| **Visual Cortex Pre-Encoder RGB Expander** (v1.1) | 4 | Taps the LZX **Visual Cortex**'s **RGB + Luma *before* the encoder**, so the VC can feed other 1 V modules (e.g. Memory Palace, Chromagnon) without converting its composite/encoded output back to the 1 V standard. *Relevant to the owner — they run a Visual Cortex (see `references/my-rack.md`).* |

## Malekko Heavy Industry — *modulation, video-optimized (1 V)*
| Module | HP | Function |
|---|---|---|
| **AD/LFO-V** | 12 | 6-channel envelope / LFO generator, **1 V-scaled outputs**, matte panel — co-developed with LZX as a modulation source for the **Visual Cortex**. Per-channel Attack/Decay + loop (LFO mode), Gate I/O on every channel, two SUM outs (banks of 3), and a **/10** button per bank to stretch timing ×10. The video-domain answer to "I need lots of envelopes/LFOs." |

## Martin Devices (github.com/martindevices, UK) — *LZX-format DIY, open-source*
By "phosphenes." The **Soft Key** is the practical DIY realization of the soft-key topology Lars describes in `keying-dictionary.md` (high-gain differential amp + precision black/white clipping).

| Module | HP | Function |
|---|---|---|
| **Soft Key** | 4 | High-gain voltage processor + precision 0–1 V clipper. Gain ×0–×50 (board trimpot extends to ×100): low gain = normal processor, high gain = hard clip. Threshold knob DC-offsets the input (sets the clip point); CV input = external threshold (attenuverted). 4-layer low-noise PCB. Uses: signal processing, contrast control, shape generation, and — paired with a crossfader — a **soft keyer**. 45 mA +12 V / 40 mA −12 V, 52 mm deep. Open-source BOM |

Announced/pipeline (status uncertain): a 2U video buffered mult, an individual-outputs Sandin Function Generator, a triggerable dual monostable, and a vactrol sequencer.

## mfb — *standalone scope (only video module)*
| Module | HP | Function |
|---|---|---|
| **VD-01 Videoscope** | 8 | Oscilloscope to a TV/monitor via RCA. 2 audio ins, ≤1 MHz sample, pos/neg trigger modes, 3 display modes, AC/DC input select, freeze. Low-res "Famicom" aesthetic — a fun video *source*. mfb is otherwise an audio-synth maker |

## Nonlinearcircuits (NLC) — *chaos modulation (audio-rate; scale for LZX)*
Not a video maker, but its **chaos** sources are prized for organic, never-repeating video modulation (same Sloth lineage as Scopic's 1v Slowboy).

| Module | HP | Function |
|---|---|---|
| **Triple Sloths V2** | 8 | Three slow chaotic modulation generators ("Sloth" chaos) — smooth, drifting, non-periodic CV |
| **Wangernumb** | 14 | Multi-function chaos/modulation ("3 modules in one… or 4") |

## Omiindustriies (omiindustriies.com) — *digital/logic, audio-rate* ⚠️ spelling
By Naomi Mitchell (LA), a video-synthesis educator. **Note the name is "Omiindustriies"** — "Omi" + industries, two i's; the maker explicitly states it is *not* "omniindustriies." No dedicated video module, but the logic modules are usable as video-rate logic building blocks (cf. LZX Castle / Video Logic):

| Module | Function |
|---|---|
| **4013 (Dual Digital Shift Register)** | CD4013-based dual flip-flop: 1-bit memory, clocked comparator, sub-oscillator, glitch-pulse generator |

## Plankton Electronics — *audio maker*
Spain. Lineup (Spice distortion, Earwig rectifier/mixer, ENVF envelope follower, Jellyfish, Ants!) is audio. **No dedicated video module found.**

## Razmasynth (France) — *standalone displays + generators*
| Module | HP | Function |
|---|---|---|
| **Telewizor V1 / V2 / FR4** | 16 | AV display + CV-controlled video pattern generator (9+ patterns) + 1-channel oscilloscope (700 kHz–228 Hz). Arduino-based, hackable patterns. PAL/NTSC, composite out. ~191 mA |
| **Display** | 16 | AV display with buffered composite out (800×480, 25 mm deep) |
| **Vector** | 16 | Display + video generator + scope (Telewizor-series evolution) |
| **Video Slooper** | 6 | USB video sampler/looper, HDMI, freeze, fast/slow, CV trig restart; ~300 mA, 80 mm deep |
| **Video Mapler** | — | Raspberry-Pi video-mapping instrument with joystick/mouse; companion to Video Slooper |

## Reverse Landfill (reverselandfill.org) — *LZX-format DIY, by Martijn Verhallen*
Source: **github.com/MartijnVerhallen/Video-Documentation, fetched directly** (BOMs, build guides, schematics, manuals). Open-source DIY video modules, LZX 1 V format. Further per-project build threads (incl. SNOW, JOG, XFADE, EDGE, Sharp) are on the **scanlines.xyz `reverselandfill` category**.

| Module | HP | Function |
|---|---|---|
| **TFG (Triple Function Generator)** | 14 | 3 identical function-generator / colorizer-shaper channels (fast video op-amps, LM6172). Each: 10k level pot + DPDT mode switch, normalizable in/out via 3-pin header. **Channels can normal in PARALLEL** (one source → all three, ideal for RGB recoloring / applying the same shape to R,G,B) **or in SERIES** (output→next input, three shapers in a row). Build doc calls parallel routing best for video recoloring / RGB functions |
| **Video Matrix Mixer** | 14 | 4×3 matrix mixer for LZX systems (25 mm, reverse-power protection) |
| **BLUR** | 4 | Analog video lowpass filter — blur/softening trails; blur + gain + 3-range switch; video-rate DRY/WET CV; camera-feedback wash-outs |
| **CMIX** | — | 6-channel video mixer |
| **SNOW** | — | Analog video **noise** generator (open-source DIY) |
| **JOG** | — | **Precision voltage source** (stable DC / offsets) |
| **XFADE** | — | **Triple RGB crossfader** |
| **VEB** | — | **Video Experimentation Board** — DIY breadboard/prototyping platform for video circuits |
| **DBM** | — | (repo folder, BOM present) |
| **Scaler** | — | Voltage scaler — BOMs/sims for ±5V↔±1V, ±5V↔+1V, +1V↔±5V, +1V↔+5V (multiple conversion directions) |
| **3T-OUTPUT-X** | — | 3TrinsRGB output expander (connector board + manual) |
| **Triple Comparator** | — | Plug-in board for the Gieskes 3TrinsRGB (3 comparators: signal + CV + bias, ±outputs) |
| **Syncbus v4** | — | Sync bus board (schematic + build guide) |
| **Matrix Mixer** | — | (schematic v2 + build guide + BOM in repo) |
| **EDGE** | — | Feedbacked **edge / high-pass filter bank** (edge & outline extraction with feedback) |
| **Sharp** | — | **Sharpen** effect for external video input |
| **Shifty Shaper** | — | Waveshaper *(WIP, documented on scanlines)* |
| **experimental Painter** | — | Experimental "painter" video module *(WIP, documented on scanlines)* |

**Owner fit (TFG):** legit colorize/shape tool — three waveshaping channels gangable across RGB, complements owner's Arch + GAMMA. Full open-source docs available.

## Scopic Modular (scopicmodular.com) — *LZX-format utilities + cases*
Best known for low-noise eurorack **case systems** (RDB-6 6U enclosures, TDP-12 linear PSU, PBX-14 active busboard, DBS-14 DC distribution, Quick-Connect hardware: LMS-6, RDA-6, ANX-12, SNX-12, QC brackets). Only **two are video/signal modules** — the rest is power/case infrastructure:

| Module | HP | Function |
|---|---|---|
| **SCA-5** | — | 4-channel 5:1 voltage scaler: eurorack CV → LZX 1 V (bipolar preserved); normalled inputs make it a scaling buffered multiple |
| **1v Slowboy** | 4 | Chaotic bipolar modulation source (−1/+1 V, LZX-range), NLC-Sloth lineage — smooth random "orbits around two strange attractors" for organic drift/animation. To/Fro + Hence/Whence (inverted) outs; Slow (~15 s/cycle) and Slower (minute+) ranges. 21 mm deep |
| **DNX-2** | — | *Power, not video:* 15 A DC power inlet feeding the PBX-14/DBS-14 busboards (chainable; not for passive busboards) |
| **INX-1** | — | Function unconfirmed — likely power/case infrastructure given the DNX/INX naming; treat as unverified |

## Sismo (sistema modular, Colombia/Brazil) — *standalone, mostly audio*
| Module | Function |
|---|---|
| **VGA Box** | Eurorack VGA video processor: R/G/B passed through pots + push-buttons to mix color intensity and on/off each channel; buttons can be triggered/synced from a sequencer |

## Sleepy Circuits — *standalone + Eurorack, audio-rate CV*
| Module | Function |
|---|---|
| **Hypno** / **Hypno 2** | Raspberry-Pi digital video synth. Two oscillators (shape/frequency/rotation/polarization), colorizer, 5-mode feedback, fractals, modulation matrix; 7 CV (−5/+5 V, *not* LZX 1 V) + 2 triggers; MIDI/USB; composite + HDMI out; USB webcam/capture input and MP4 looping. Standalone or pops into Eurorack. **Hypno 2** adds a built-in display and resampling/audio-visualizer features |

## Soundmachines (Italy) — *no video synth*
Audio/CV/lighting maker (Modulör114, BI1 brainterface, LP1/LS1 controllers, RB1, UL1, DS1). Closest to video art is **SY1** — a CV-to-DMX interface for controlling stage lighting. **No video synthesis module.**

## Special Stage Systems — World Core — *standalone, digital videogame synth*
| Module | Function |
|---|---|
| **World Core** | Voltage-controlled **tile engine + collision/physics processor** — the centerpiece of the Ming Mecca "videogame synthesizer." Builds CV-manipulable videogame worlds: toggle gravity, scroll seasons, populate with creatures, modulate identities with random voltage; object collisions trigger events elsewhere in the modular. NTSC composite out; graphics from SD card. (Companions Control Core / Oscillographic Block exist; owner asked for World Core only) |

## Steady State Fate — *audio maker*
Audio modules only (Steady State Gate LPG, Zero Point Oscillator, VERSA, Autodub, Entity). **No video module.**

## Synthrotek (store.synthrotek.com) — *standalone composite*
| Module | Function |
|---|---|
| **VID MIX** | Eurorack "Dirty Video Mixer": crossfade/switch two composite signals via high-speed op-amps + buffered ins; one input fades in VCA-style; CV over crossfader; MIX "accent" button slams both signals together. Lo-fi VHS/synthwave effects |
| **VID PIX** | 8-bit audio-reactive video pattern generator (incoming audio drives onscreen patterns; CV over pattern mode + color palette; RCA composite out) |

## Syntonie (syntonie.fr, France) — *LZX-format DIY + standalone*
Source: **ModularGrid manufacturer page (vendors/view/882), fetched directly.** Much larger line than previously documented. LZX 1 V format. Owner owns **VU002, VU006, VU008, VU009**.

**Encoders / sync / output (relevant to "more outputs > more inputs"):**

| Module | HP | MSRP | Function |
|---|---|---|---|
| **Sortie** | 8 | $332 | Sync Generator / RGB Encoder — dedicated output path independent of the Visual Cortex |
| **VU007B** | 8 | $341 | Sync Generator / RGB Encoder |
| **VU007** | 4 | — | RGB2Component encoder (tiny) |
| **VU001C** | 8 | $163 | Triple Video Distribution Amplifier — fan one signal to many outputs |
| **VU001B** | 4 | $116 | Video Distribution Amplifier |
| **VU001** | 4 | — | Quad Distribution Amplifier for composite video |

**Inputs / decoders:**

| Module | HP | Function |
|---|---|---|
| **Entrée** | 8 | Component to RGB Decoder / Luma Processor ($280) |
| **VU003B** | 8 | Component to RGB decoder / Luma Processor ($235) |
| **VU003** | 4 | Component to 1V RGB |

**Generators / oscillators / animation:**

| Module | HP | Function |
|---|---|---|
| **VU006** | 4 | Quadrature oscillator — phase-shifted outs for rotations / circular motion / X-Y / rescan *(owner owns)* |
| **VU009** | 4 | Sawtooth (ramp) VCO — 0–1 V, FM in + offset; ramp/saw source *(owner owns)* |
| **Animate** | 8 | Quadrature LFO ($280) |
| **Animate Exp** | 8 | Waveforms expander for Animate ($128) |
| **VU008** | 4 | Dual ramp **phase shifter** — shifts H/V ramps for horizontal/vertical displacement; waveshapes other signals; CV + attenuverters *(owner owns)* |
| **Rampes** | 8 | Ramp Generator / Sync Extractor ($376) |
| **VU005** | 4 | Dual Sinewaveshaper |
| **VU002** | 4 | **Quad frequency doubler** — four saw→triangle ("mirror") stages for symmetrical shape generation (the mirror the rotation patch needs) *(owner owns)* |

**Processing / shaping / color / mix:**

| Module | HP | Function |
|---|---|---|
| **Isohélie** | 12 | Triple 3-bit Posterizer ($467) — hard posterization/quantize, distinctive stepped look |
| **Seuils** | 12 | Triple Comparator / Boolean Logic / Ramp Shifter ($400) |
| **Solaire** | 8 | Full-Wave Rectifier / 2:1 Mixer ($294) |
| **Courbes** | 8 | Triple Expo/Log Shaper ($306) |
| **Cadrans** | 12 | Triple VCA / Crossfader / Four-Quadrant Multiplier ($341) |
| **Matrice** | 16 | 1×3 Matrix Mixer / Triple VCA ($424) |
| **Combines** | 8 | Triple Analog Combiner ($270) |
| **VU010** | 4 | Triple 2:1 Mixer |
| **VU004** | 4 | Quad Inverter |
| **Détail** | 12 | Softener / Enhancer ($376) — edge softening/sharpening filter |
| **Stable** | 16 | Processing Amplifier / Glitch Stabilizer ($471) |

**Glitch (standalone-ish):**

| Module | HP | Function |
|---|---|---|
| **CBV001** | 12 | Circuit Bent Video Enhancer — composite glitch/colour/distortion (AVE MOD circuit); CV + attenuator; NTSC/PAL |
| **CBV002** | 16 | Circuit Bent Video Delay — Discret11-based; few-hundred-ns delay → horizontal displacement + hue shift ($306) |

**Owner note:** Sortie / VU007B are dedicated RGB encoders — exactly the "more outputs" axis (independent output path separate from the Visual Cortex's encoder). VU001B/C add output fan-out. Isohélie's hard posterization is a unique look nothing in the owned rack does.

## Teletect (github.com/Teletect) — *LZX-format DIY, open-source*
By **Philip Baljeu** (pbalj — author of the LZX **Castle** patching tutorials). Open-source designs on GitHub.

| Module | HP | Function |
|---|---|---|
| **VS-002 Dual Enhancer** | 4 | Dual video enhancer based on the **Archer Video Enhancer**; works with LZX video signals |
| **VS-001 (BNC Adapter)** | 4 | Passive 1/8" → BNC adapter module |

## Tsyklon Labs (tsyklon.com) — *video logic tiles* (sparse)
| Module | Function |
|---|---|
| **PLITKA** series (DIOD OR, NULL, …) | "Tile" video-logic/pattern modules (PLITKA = "tile") |
| **Video Monitor** | Prototype TFT monitor module |
| **SOYUZ MLDAOUR** | Attenuverter / offset / half- & full-wave rectifier utility (video-rate capable) |

## Visible Signals (visiblesignals.net) — *LZX-format DIY, discontinued*
Source: **ModularGrid manufacturer page (vendors/view/891), fetched directly.** DIY video-synth PCBs/panels. **No longer selling** (existing-customer support only). LZX 1 V format. Owner owns **Gainbrain**.

| Module | HP | MSRP | Function |
|---|---|---|---|
| **Gainbrain** | 4 | $20 | Video VCA / crossfader / analog multiplier *(owner owns)* — range fix: R4 → 10 K (designer-endorsed), +R7 → 20 K for positive-only manual sweep; see `patch-techniques.md` |
| **Video Mult** | 4 | $20 | Video-bandwidth dual 3-output buffered multiple |
| **Dual Distrib** | 4 | $20 | Two-channel, 3-output 75 Ω video distribution amplifier |
| **Quarterizer** | 8 | $30 | Amplitude classifier / 4-input VC switch — inspired by the Sandin IP Amplitude Classifier. Complex signal manipulator, **hard keyer with 4 independent inputs**, CV waveshaper, 4-ch sequencer, or 4-preset manual controller |
| **Wrangler** | 4 | $25 | High-bandwidth voltage processor/mixer with LED meter + second 0–1 V clipped output |
| **Xordand** | 4 | $110 | Logic-gate performance control for LZX-compatible video (AND/OR/XOR-style boolean video logic) |
| **RGB Matrix (Combo Panel)** | 16 | $60 | Expandable 3-channel (RGB) matrix mixer with A/B bus + crossfading keyer |
| **RGB Matrix Input** | 4 | $15 | Single-channel video-rate input for the RGB Matrix set |
| **RGB Matrix Direct In** | 4 | $20 | RGB full-colour 3-input module for the RGB Matrix set |

**Owner note:** **Xordand** = boolean video logic (geometric intersections / punch-outs between keys), a function the owned rack lacks. **Quarterizer** = 4-input hard keyer / amplitude classifier, a distinctive Sandin-derived tool. Both are small (4 / 8 HP) and on-brand for the owner's size preference, but the line is discontinued (used market only).
