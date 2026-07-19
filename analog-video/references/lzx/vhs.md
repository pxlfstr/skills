# VH.S (Video Headroom Systems) — current brand, successor to brownshoesonly

Source: **ModularGrid manufacturer page (vendors/view/1005), fetched directly.** VH.S is the continuation of **brownshoesonly** (same maker) with LZX **Gen3 power packs** and updated/expanded designs. LZX-format, **1 V standard** — third-party, not subject to the owner's LZX-generation preference list.

See `brownshoesonly.md` for the predecessor lineage and the successor mapping.

## Full catalog (verified, ModularGrid)

| Module | HP | MSRP | Function | Tags |
|---|---|---|---|---|
| **SUBMIX** | 8 | $179 | Mixer (with wavefold + utility out) — *owner owns this* | Mixer / Video / Waveshaper |
| **BAJA** | 6 | $169 | 6-phase oscillator (successor to brownshoesonly bajascillator) | LFO / Oscillator / Video |
| **CHANNEL** | 8 | $265 | Video crossfader / panner / mixer | Mixer / Panning / VCA / Video |
| **SCANNERS** | 8 | — | Dual 3:1 video scanner | Panning / VCA / Sequencer / Video |
| **CROSSFADE** | 8 | $200 | 3-channel crossfader with luma output | (crossfader / VCA) |
| **RGBMIX** | 12 | $399 | Voltage-controlled RGB color mixer | Mixer / VCA / Video |
| **AURAL SCAN** | 12 | $350 | 3-band envelope follower for video | Envelope Follower / Dynamics / VCA / Video |
| **3VCA** | 8 | $230 | Triple discrete video VCA | Utility / VCA / Video |
| **F4DER** | 8 | $209 | 4 utility crossfaders | Utility / VCA / Video |
| **RGBSCAN** | 12 | $400 | Triple scanner with RGB cycling | Utility / VCA / Video |

## Notes
- **CHANNEL** answers the earlier open question — it's a video crossfader/panner/mixer, 8 HP, $265 (not previously documented).
- **AURAL SCAN** is a video-domain envelope follower (audio/signal → CV for driving video params) — relevant for audio-reactive work; complements the owner's ES-9 bridge with a hardware-native path.
- **RGBMIX** is the full VC RGB color mixer; **RGBSCAN** cycles a scanner across RGB. Both are the higher-end color/mix tools in the line.
- **3VCA** = clean triple video VCA; **F4DER** = four utility crossfaders. These are the workhorse utility modules.

## Functional detail (patching-oriented)
Verified catalog above is from the ModularGrid manufacturer page; the fuller per-module functions below are retained from the maker's own product pages (videoheadroom.systems). Nothing here overrides the table — it adds the "what you can do with it" layer.

- **SUBMIX** (owned) — a **2×2 quadrant/matrix mixer**. Inputs: **Top-Left, Top-Right, Bottom-Left, Bottom-Right.** Outputs: **Top (TL+TR), Bottom (BL+BR), Left (TL+BL), Right (TR+BR), + (all four), − (inverted all), fold (wavefolded all)**. The edge outputs are **two independent 2-input sums** (Top & Bottom, or Left & Right), so SUBMIX can compute two separate weighted sums at once — e.g. load the four rotation-matrix products into the corners and read **X off Top, Y off Bottom** (a one-module rotation summer). The same quadrant structure also makes it a natural **4-corner compositor / 2D positioner**; fold adds symmetry/tiling, +/− give free inversion/subtraction. It can only be one of those at a time (single module).
- **CHANNEL** — multi-utility: signal **router**, fader, **1:3 panner**, mixer, and **soft keyer** in one. The soft-keyer mode is the notable bit — it's not just a crossfader.
- **CROSSFADE** — 3-channel crossfader with a **luma output** (take a key/matte off the blend).
- **SCANNERS** — dual **3:1** video-rate scanner with dual CV inputs (attenuation/bias). A "scanner" = a crossfader with more than two inputs, so this sequences/blends 3 sources per channel.
- **RGBSCAN** — 3-channel scanner with **cycling/rotating RGB normalization**: patch RGB into the top row and each row below shifts it one position (RGB rotations). Also three independent 3-input scanners; chainable to a 7-input "mega scan."
- **RGBMIX** — voltage-controlled RGB mixer: 3 RGB channels via manual gain *or* video-rate VCA CV. Doubles as an **RGB keyer** (drive the VCA CV from a key generator) or a preset/patch blender. Pairs with CHANNEL and BAJA.
- **3VCA** — triple independent video VCA, channels **normalled 1→3**, tuned around **black level** (vs LZX Factors, which centers on gray — so 3VCA behaves differently on bipolar signals). Pair with key gens to build keyers, or animate modulation amplitude over time.
- **F4DER** — 4 utility crossfaders, **fully normalled UL→UR→LL→LR** (community design by Ramin Rahni). Strong with key-gens for luma or RGB keying and for compositing.
- **AURAL SCAN** (MK2) — 3-band audio envelope follower for video: **onboard mic + preamp**, or 3 mono audio ins (low/mid/hi). Each band feeds a **SCANNER sub-circuit** to map low/mid/hi energy to screen regions; each envelope also hits a video-rate mixer. A hardware-native audio-reactive path (complements the ES-9 bridge).
- **BAJA** — 6-phase (also 3-phase) unipolar analog **sine** oscillator; the multiple phase-related outputs are quadrature-ish — patch them into XY inputs for circular/rotational motion.

### VIDEO GRIP — *real module, not yet on the MG manufacturer page*
Confirmed from videoheadroom.systems (shipping ~mid-2026): a **joystick controller** = preset manager + 4-quadrant video-rate mixer + quad video-rate panner. A front-panel control toggles joystick (center 0 V) vs center-mix for the SUM out. Patch BAJA's quadrature outputs into the XY inputs to auto-cycle inputs. It's the **Gen3 successor to the brownshoesonly Video Grip** (see `brownshoesonly.md`). Listed here because it's verified-correct data even though it hasn't appeared on the ModularGrid manufacturer page yet.
