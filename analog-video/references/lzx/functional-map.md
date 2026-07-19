# LZX Functional Map & Substitution Guide

Modules grouped by the *role* they play in a patch, so you can answer "what else can do this?" and "which one should I use?" The principle that makes substitution possible: in the LZX standard, **every signal — video, ramp, CV, logic — shares one electrical standard (0–1 V unipolar / ±1 V bipolar, ~100 kΩ in, ≥5 MHz)**, so a module doesn't "know" whether it's processing a picture or a control voltage. That's why a math/utility module can stand in for a "video" module and vice-versa.

Names below are current (Gen3 + P-series) unless marked *(legacy)*. Confirm exact behavior in `modules/<name>.md` and specs in `module-specs.md`.

---

## Sources — generate signals from nothing

| Module | Generates | Notes |
|---|---|---|
| DWO3 | Oscillator: sine/square/saw/triangle, sub-Hz to 2 MHz | the pattern/animation workhorse; can lock to sync |
| DSG3 | 2D shapes via dual ramps + waveshaping/blend/logic | shapes, not raw oscillation |
| Angles | H/V ramps + 24-output fixed-ratio mixer | ramps as a backbone for shapes/gradients |
| Scrolls | Dual ramps with *motion* control | ramps that move/scroll without external animation |
| Matte | Static voltages / flat RGB fields | not time-varying; a "color source" |

**Substitution:** For **ramps**, Angles ↔ Scrolls overlap — pick Scrolls when you want built-in motion, Angles when you want the fixed-ratio mixer too. For **shapes**, DSG3 builds them from ramps any ramp source can feed. *(Legacy ramp/osc: Cadet IV Dual Ramp, Cadet IX VCO.)*

---

## Mixing & summing — combine multiple signals into one

| Module | Best for | Shape |
|---|---|---|
| SMX3 | Routing/matrixing many sources; RGB color matrixing | 9-in → 3-out, per-input gain −2…+2 |
| Sum/Dist | Summing *and* fanning out | function bank of sum + distribution amps |
| Proc | Sum with per-channel attenuate/invert/bias | triple processor + summing amp |
| PGO | Compact add/subtract of two signals | 4 HP gain + offset |
| Angles | Fixed proportional blends | 24-output fixed-ratio mixer |

**Substitution:** To **add two signals**, any of PGO, Proc, Sum/Dist, or SMX3 works — choose by channel count and whether you also need routing (SMX3), fan-out (Sum/Dist), or per-channel processing (Proc). SMX3 doubles as a color matrix because RGB mixing is just summing weighted channels.

---

## Compositing & keying — layer images with a stencil

| Module | Role | Key type |
|---|---|---|
| FKG3 | Full compositor: layer two RGB sources + key | soft / component (R, G, or B) keying, built in |
| Keychain | Generates key signals | triple *hard* key (fast comparators) |
| Stacker | Generates + prioritizes window keys | triple window key, priority layering |
| Matte | Supplies the fill color a key cuts into | static RGB |

**Substitution:** FKG3 is the all-in-one (make a key *and* composite). Keychain and Stacker are **key generators** — their output feeds a fader/compositor (e.g., FKG3 or a mixer) to actually layer. Use Keychain for hard-edged luma/level keys, Stacker for interlocking rectangular windows. Any comparator-type module can rough-in a hard key, since a hard key *is* a 1-bit comparator (see glossary).

---

## Math & level processing — reshape one signal's values

| Module | Operation |
|---|---|
| Proc | Attenuate, invert, add bias/offset (triple) |
| PGO | Gain + offset; uni↔bipolar conversion |
| Factors | Four-quadrant multiply (AM, ring-mod-like, contrast) |
| PRM | Rectify + multiply |
| Stairs | Wavefold + frequency-multiply (solarize/colorize) |
| Contour | High-pass / detail & edge extraction |

**Substitution:** For **multiplication/modulation**, Factors (4-quadrant) ↔ PRM (rectify+multiply) overlap; Factors for bipolar AM/contrast, PRM when you want rectification too. For **gain/offset**, PGO ↔ Proc overlap — PGO is compact 2-channel, Proc is triple with inversion. Uni/bipolar conversion: Proc or PGO. *(Glossary cross-refs DSG3, Contour as bipolar-accepting; Swatch as bipolar-requiring.)*

---

## Color — manipulate hue/chroma

| Module | Role |
|---|---|
| Swatch | Color-space conversion (work beyond RGB; needs bipolar) |
| Ribbons | 3-bit digitize + colorize (8 quantized bands) |
| SMX3 | RGB channel matrixing (color via summing) |
| Stairs | Colorization through wavefolding |
| Matte | Pick/define RGB colors |

**Substitution:** Several paths to "change the colors": Swatch for true color-space rotation, SMX3 for channel-mix recoloring, Ribbons for posterized/banded color, Stairs for fold-based color cycling. They produce *different looks* from the same goal — not 1:1 swaps.

---

## Routing, distribution & manual control — utilities

| Need | Options (passive → active) |
|---|---|
| Split one signal to many | MLT (passive) → Sum/Dist (buffered) → PAB (buffered + 16 ns delay steps) |
| Select among sources | Switcher (dual 4×3 mux, RGB) ; SMX3 (matrix) |
| Manual level/attenuate | P (passive pot) → Proc / PGO (active) |
| Link/normal signals | LNK (passive links) |

**Substitution:** Passive (MLT, P, LNK) costs no power and adds no buffering — fine for short chains; use buffered (Sum/Dist, PAB, Proc) when fan-out or cable length degrades the signal. PAB is the pick when you also need small delays for timing alignment.

---

## Sync, encoding & I/O — system backbone (not interchangeable)

| Module | Role |
|---|---|
| ESG3 | Encoder + sync generator + proc amp — converts patch signals to legal video out, and clocks the system |
| TBC2 | Dual video *input* / timebase corrector — brings external sources into the 1 V standard, can generate sync |
| Chromagnon | Instrument with built-in sync/encode (self-contained) |

These are infrastructure: ESG3 = "way out" (to a display/recorder), TBC2 = "way in" (external cameras/players). Both can be a sync master. They don't substitute for each other — a full system usually wants input (TBC2) *and* output/encode (ESG3), unless an instrument like Chromagnon bundles both.

---

## Quick "I want to…" index

- **Make moving patterns** → DWO3 (oscillate) or Scrolls (moving ramps) → into DSG3 for shapes
- **Layer two videos** → FKG3 (+ Keychain/Stacker for the key) → Matte for fill
- **Add/mix sources** → SMX3 (matrix) / Sum/Dist (fan-out) / PGO (compact)
- **Recolor** → Swatch / SMX3 / Ribbons / Stairs (different looks)
- **Get video in** → TBC2 · **Get video out** → ESG3
- **Modulate one signal by another** → Factors (multiply) — and remember any input can be a modulator

---

## Owner preference filter (apply when recommending modules)

The owner has a specific taste. When suggesting what to buy/patch, sort by it; don't just name the "textbook" module if it conflicts.

**Strongest preference: the Expedition series** — lead with Expedition options when one fits (see `expedition/` for per-module docs).

**P-series is acceptable** (no longer prefer-against).

**Prefer-against:** Gen3 and Orion modules — *unless* one of these redeems it:
- **(a) Unique use case** — e.g. Matte (owned, liked, as an RGB picker).
- **(b) All jacks/switches, no knobs — *Gen3 only.*** (A knob-free Orion module is not redeemed by this.)
- **(c) Encoder or decoder — any generation** is fine.

**Also prefers:** 4–8 HP modules. Owns and dislikes **FKG3** (don't recommend it as a default keyer for this owner).

**Cadet** is favored both as small 4 HP building blocks *and* as a circuit reference: its open BOMs/schematics (`cadet.md`, `cadet-circuits.md`) explain how other LZX modules work.

**What this means in practice:**

| Verdict | Modules |
|---|---|
| ⭐ Lead with | **Expedition** (Arch, Bridge, Color Chords, Curtain, Doorway, Liquid TV, Marble Index, Navigator, Polar Fringe, Prismatic Ray, Shapechanger, Staircase, Visual Cortex, War of the Ants, etc.) — favor 4–8 HP ones |
| ✅ Also good | Cadet (4 HP, incl. encoder/decoder); Castle (4 HP); P-series (any); VH.S (LZX-compatible third-party, mostly 6–12 HP — see `vhs.md`); **Matte** (owned); any encoder/decoder (ESG3, TBC2, Cadet I/II/III) |
| ⚠️ Only if Gen3 + knob-free | Gen3 jack/switch-only: **PGO**(4HP), **Swatch**(8HP), DSG3(12HP), Angles(12HP), Sum/Dist(12HP), Switcher(18HP) — check against 4–8 HP pref |
| 🚫 Deprioritize | Gen3 with knobs and no unique case: Contour, Factors, **FKG3**, Keychain, Proc, Ribbons, Scrolls, SMX3, Stacker, Stairs, DWO3. Orion generally (unless unique-use / encoder-decoder / Gen3-only knob rule doesn't apply to it) |

When the favored answer lacks control detail in this pack, say so and offer to fetch it. Expedition docs are in `expedition/`; Cadet in `cadet.md` + `cadet-circuits.md`.
