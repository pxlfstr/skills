# LZX Visionary Series (Legacy, the original 2010-era line)

Source: LZX community "All About Visionary Series (Legacy)". Visionary is LZX's first Eurorack line — not Orion/Gen3/P, acceptable under the owner's preference. Sync-based modules need the Visionary Video Sync Generator and a 14-pin sync distribution cable.

## Design philosophy

- All signals are **1 V, DC-coupled** regardless of type or frequency; any output can patch to any input.
- Wide bandwidth to video rates throughout; signal/processing modules are format-independent.
- Video paths are triple-colorspace (RGB/YUV) or monochrome; sync/subcarrier insertion and DC restoration happen only at the dedicated input/output modules.
- Designed for functional density and full patchability over instant gratification.

## System backbone (required pair)

| Module | HP | Power | Role |
|---|---|---|---|
| **Video Sync Generator** | 6 | 60 mA | Master NTSC/PAL sync; external sync-lock (PLL, defeats Macrovision); sync-distribution bus access; 75% color-bar (0.75 V) outputs; DC-restored Y output from external video. Field/Line/Odd/Even 1 V outputs |
| **Color Video Encoder (CVE)** | 10 | 100 mA | RGB → valid composite + S-video out; per-channel bias + attenuverter (invert adds +1 V bias to stay in 0–1 V); R normalled to G/B; NTSC/PAL via jumper; 2× composite + 1× S-video outs |

## External video input

| Module | HP | Sync? | Role |
|---|---|---|---|
| **Color Time Base Corrector (CTBC)** | 4 | yes | Core external input: S-video/composite in → decoded Y/R/G/B out; one per simultaneous source |
| **Triple Video Interface (TVI)** | 6 | yes | Wideband external input: DC-restore, sync-clip, scale; 3 composite sync outs for genlocking external gear; includes YUV→RGB converter. No TBC/frame-sync/color-decode (use CTBC for those) |
| **Voltage Interface I (VI1)** | 12 | no | 5-ch precision conditioner: external 10 V / line audio → 1 V, gain+bias with clip LEDs |
| **Voltage Bridge** | 6 | no | 8-ch scaler: 4× attenuate 5 V→1 V, 4× boost 1 V→5 V (any signal type) |

## Generators

| Module | HP | Role |
|---|---|---|
| **Video Waveform Generator (VWG)** | 16 | Wide-range video VCO, 6 ranges (30 s–2 MHz), hard-sync to sync bus; 5 outs (tri/saw/square/pulse/shaped-sine); PWM + sine-shaper waveshapers with CV; precision video op-amps. (Ancestor of Prismatic Ray) |
| **Video Ramps** | 4 | Dual sync-locked ramps (V-rate + H-rate); saw/inv-saw/tri/inv-tri each; for wipes/shapes and X/Y scope sweeps |

## Processing / mixing / math

| Module | HP | Role |
|---|---|---|
| **Triple Video Processor (TVP)** | 10 | 3-ch gain+bias with secondary summing input; bias before scale/invert → adjustable inversion crossover for bipolar mixing. 40 MHz bw |
| **Video Blending Matrix (VBM)** | 22 | 3× 5-input DC mixers; per-input level/invert (add/subtract/inverted-add) or 1 V bias; Sum and **Absolute** outputs (abs enables freq-multiply, solarization, color-difference); column normalling for matrix mixing |
| **Colorspace Mapper** | 10 | HSY (hue/sat/brightness) → YUV → RGB conversion with VCAs, polar-to-cartesian waveshapers; hue-to-UV waveshaper spans 720° (2 rotations). B&W into Hue → hue-rotation/thermal effects |
| **Triple Video Multimode Filter (TVMF)** | 18 | VC filtering, edge/outline extraction, softening/blur. High-pass out is bipolar (rising=+, falling=−); OLN outputs are rectified edge variants (half-wave rising / full-wave / half-wave falling via 3-pos switch) |

## Keying / faders / switching

| Module | HP | Power | Role |
|---|---|---|---|
| **Triple Video Fader & Key Generator (TVF&KG)** | 16 | 135 mA | 3× VC crossfaders + 3× comparators (key gens). Fader modes: FADE (CV+bias drives fader), KEY (key-gen drives fader), AND (logical AND of all 3 keys). Faders 2&3 can follow fader 1 as master. **MK2 (50 units) added a soft keyer.** |
| **8 Stage Video Quantizer & Sequencer** | 18 | — | Amplitude classification + sequential multiplexing: 8 high-speed switches (one active), each with input/output/bias + global sum in/out; quantizer splits Classify input into 8 bands (0–7) with VC upper/lower thresholds; sequential clock 0–7; active switch = (quantizer + sequencer) mod 8 |

### TVF&KG patch cookbook (summary)
Single-threshold comparator; Multiplier/VCA (B input + FADE); Automated crossfade (A&B + FADE, bias = mix); Luma key (take fader out in KEY mode); RGB fader (all 3 ch, 2&3 → follow ch1); Window comparator (cascade 2 ch, opposite key inversions); Chroma key (RGB fade + ch1 AND mode); 3-band amplitude classifier (all KEY, ch1&2 −Key, ch3 +Key, cascade keys); Cascaded crossfaders (out 1&2 → in of 3); Max/Min selector (A=sig1, B+CV=sig2, +logic=Min, −logic=Max); VC panner (1 in → 2 outs via 2 ch).

## Logic (high-speed, 0.5 V comparator inputs — accept any signal, not just logic)

| Module | HP | Role |
|---|---|---|
| **Video Divisions** | 6 | H/V bar generation + signal division; EXT/FRM/X/Y modes × SQ±/DV± count modes (ring sequence or binary /2…/256) |
| **Video Flip Flops** | 6 | 4× single-bit memory: per column a toggle FF (toggle/set/reset) + a data FF (transfers data on clock); for shape processing & quantization |
| **Video Logic** | 6 | 2× boolean blocks (3-in → AND/OR/XOR) + 2 inverters → NAND/NOR/XNOR by patching |

## Audio

| Module | HP | Role |
|---|---|---|
| **Audio Frequency Decoder** | 8 | 8-ch audio envelope follower (internal mic or external in); 8 bandpass → envelope+LP → 8 CV outs for audiovisualization. (Ancestor of Sensory Translator) |

## Display

| Module | HP | Role |
|---|---|---|
| **XY Display Driver** | 4 | Interface to oscilloscopes / XY displays (special order, sync required) |

## Note on encoders/decoders (owner-relevant)
Visionary covers both ends any-generation-friendly: **CVE** (encoder out), **CTBC** and **TVI** (decoders/input). These satisfy the "encoders/decoders, any generation" preference and are small-ish (4–10 HP).
