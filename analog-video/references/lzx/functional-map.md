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

**Revised:** the old rule (Expedition strongest; prefer against Gen3 and Orion unless redeemed) is **retired**. Judge every generation on merit and function.

- **Gen3 is no longer filtered.** The knob objection is resolved by swapping in Davies 1900 D-shaft knobs (recommended by Lars / LZX `[Official]`). Expedition, Syntonie and VH.S ship with Selco knobs, which are fine as-is.
- **Expedition keeps soft tiebreaker weight only** — when two options are otherwise equal, lean Expedition.
- **Back in consideration on merit:** Contour (Gen3 edge / highpass), Swatch (Gen3 knob-free colorspace).
- **P-series:** fine. **Cadet:** valued, both as 4 HP building blocks and as a circuit reference (`cadet.md`, `cadet-circuits.md`).
- **Matte:** owned and liked.
- **Also prefers:** 4–8 HP modules.
- **Dislikes FKG3** — don't recommend it as a default keyer for this owner.
- **Syntonie Cadrans:** dropped — don't resurface it.

When the favored answer lacks control detail in this pack, say so and offer to fetch it. Expedition docs are in `expedition/`; Cadet in `cadet.md` + `cadet-circuits.md`.
