# My Rack — "fstrvsn" (current system)

ModularGrid: **fstrvsn** (user *pxlfstr*). **21 modules · 196 HP** (was 18 / 184 before the June 2026 Syntonie additions below). Draw before additions: +12 V ≈ 1663 mA, −12 V ≈ 1124 mA, +5 V 0 mA — **refresh from ModularGrid for exact new totals** (added draws: Sawtooth Oscillator 35/20 mA, Dual Ramp Phase Shifter 55/50 mA, Quad Frequency Doubler draw TBD). Row placement of the new modules is TBD.

> **Maintenance:** this changes over time. When the user says they've added/removed/swapped a module, update this file (and the memory note). Modules we're only *considering* go in the **Auditioning** section below — never mix not-yet-owned gear into the owned list. **Naming:** refer to Syntonie modules by full name (Quadrature Oscillator, Sawtooth Oscillator, Dual Ramp Phase Shifter, Quad Frequency Doubler, …), not the VU00x code — the user can't track the codes; keep the code only as a parenthetical.

## What this system can do
A complete, performance-oriented LZX video instrument: take an external source in, **decode → shape / oscillate → do math → colorize → key → mix → encode out**, all anchored by the Visual Cortex (which provides sync, input decode, output encode and a hard keyer). It can run as a pure synth (oscillators → colorize → out), as a processor for live video, and it reaches *outside* the screen too — an ES-9 bridges CV/audio to a computer (capture, audio-reactivity, external control) and the SY1 drives DMX stage lighting from rack voltages. Quadrature oscillation opens rotations / circular motion / rescan-style moves; the hexadirectional crossfader invites feedback and multi-source blends.

## Owned — by function

**System core / sync / I-O**
- **LZX Visual Cortex** (26 HP) — the heart: external-video input decode, master sync generation, RGB→video output encode, plus a built-in hard keyer and 2D shaping. Everything resolves through this.

**Generators — shapes, ramps, oscillation**
- **LZX Prismatic Ray** (16 HP) — video-rate oscillator: ramps, shapes, patterns; the main shape/source voice.
- **Syntonie Quadrature Oscillator** (VU006, 4 HP) — phase-shifted outputs for rotations, circular/spiral motion, and X-Y / rescan moves.
- **Syntonie Sawtooth Oscillator** (VU009, 4 HP) — 0–1 V saw/ramp with FM input + offset: a dedicated ramp source for shapes, sweeps, and rotation coordinate ramps.
- **brownshoesonly bajascillator** (8 HP) — 3-phase LFO: slow, phase-related sweeps for animating parameters.
- **LZX Staircase** (10 HP) — frequency multiplier: stacks harmonics / stepped repeats off a ramp → bars, tiling, repetition.

**Math / processing / shaping**
- **LZX Passage** (10 HP) — triple arithmetic processor: add / subtract / scale across three channels (RGB-wide mixing, offsets, sums).
- **LZX Arch** (8 HP) — nonlinear functions: bends simple inputs into new curves/shapes (waveshaping feel).
- **Foxing Hour GAMMA** (4 HP) — dual log / expo + sum: gamma-style curve shaping, contrast bending, non-linear ramp warping.
- **Syntonie Dual Ramp Phase Shifter** (VU008, 4 HP) — shifts H/V ramps for horizontal/vertical displacement; on other waveforms it waveshapes. Per-channel CV with attenuverters.
- **Syntonie Quad Frequency Doubler** (VU002, 4 HP) — four saw→triangle (mirror) stages — the exact "mirror" the shape-rotation patch needs (see `patch-techniques.md`).
- **LZX Bridge ×2** (8 HP each) — utilities: buffering, scaling, conditioning and distributing signals around the patch.

**Keying / mixing / crossfade / VCA**
- **LZX Doorway** (10 HP) — linear (soft) keyer: variable-opacity mixes and soft mattes.
- **VH.S SUBMIX** (8 HP) — **2×2 quadrant mixer**. In: Top-Left/Top-Right/Bottom-Left/Bottom-Right. Out: **Top (TL+TR), Bottom (BL+BR), Left (TL+BL), Right (TR+BR), +, −, fold**. Edge outs = two independent 2-input sums, so it can be the **rotation-matrix summer** (4 products → corners → X=Top, Y=Bottom) *or* a **4-corner compositor / 2D positioner** — one role at a time.
- **brownshoesonly hexadirectional crossfader** (18 HP) — complex multi-direction crossfader: multi-source blends, feedback loops, "knot-theory" mixing.
- **Visible Signals Gainbrain** (4 HP) — video VCA / crossfader / analog multiplier: amplitude control, multiply two signals, automated fades. *If the manual/CV range feels cramped, apply the designer-endorsed **R4 → 10 K** mod (and R7 → 20 K for a positive-only sweep) — see `references/patch-techniques.md`; it's what makes Gainbrain a clean multiplier.*

**Color**
- **LZX Mapper** (10 HP) — polar-to-cartesian colorizer: hue rotation, colorspace remap, radial/thermal colorizing.
- **LZX Matte** (8 HP) — static voltage generator / color picker: solid color fields, key fills, fixed offsets. *(The one Gen3 module you keep — fits the "owned/likes Matte" note.)*

**Interface / capture / lighting**
- **Expert Sleepers ES-9** (16 HP) — USB audio interface: CV ↔ computer and audio I/O — capture, external control, and an audio-reactivity bridge.
- **Soundmachines SY1 Synesthesia** (8 HP) — DMX light controller: drive stage lighting straight from rack CV, syncing lights to the patch.

> **New (June 2026): a dedicated shape/rotation toolkit.** Sawtooth Oscillator (ramp source) → Dual Ramp Phase Shifter (phase-shift H/V for displacement) → a summer → **Quad Frequency Doubler** (saw→triangle mirror) is the classic Syntonie path to symmetrical shapes (e.g. a diamond). This gives the rack a dedicated hardware route for the shape-generation/rotation technique in `patch-techniques.md` — previously the saw→triangle mirror had to come from Staircase/Arch. Combine with the Quadrature Oscillator (rotation angle) for spinning shapes.

## Owned — spec table (for rack planning)

| Module | Maker | Row | HP | Depth | +12V | −12V |
|---|---|---|---|---|---|---|
| Bridge | LZX | 1 | 8 | 32 mm | 30 | 30 |
| Bridge | LZX | 1 | 8 | 32 mm | 30 | 30 |
| Gainbrain | Visible Signals | 1 | 4 | 43 mm | 40 | 40 |
| Quadrature Oscillator (VU006) | Syntonie | 1 | 4 | 50 mm | 30 | 29 |
| Passage | LZX | 1 | 10 | 32 mm | 40 | 40 |
| SUBMIX | VH.S | 1 | 8 | 30 mm | 120 | 0 |
| bajascillator | brownshoesonly | 1 | 8 | 25 mm | 35 | 51 |
| hexadirectional crossfader | brownshoesonly | 1 | 18 | 36 mm | 120 | 120 |
| Mapper | LZX | 1 | 10 | 45 mm | 100 | 100 |
| Visual Cortex | LZX | 1 | 26 | 45 mm | 180 | 220 |
| Arch | LZX | 2 | 8 | 32 mm | 65 | 65 |
| GAMMA | Foxing Hour | 2 | 4 | 50 mm | 32 | 26 |
| Prismatic Ray | LZX | 2 | 16 | 32 mm | 120 | 90 |
| Doorway | LZX | 2 | 10 | 32 mm | 80 | 80 |
| Staircase | LZX | 2 | 10 | 32 mm | 70 | 70 |
| Matte | LZX | 2 | 8 | 32 mm | 50 | 0 |
| ES-9 | Expert Sleepers | 2 | 16 | 50 mm | 451 | 133 |
| SY1 Synesthesia | Soundmachines | 2 | 8 | 30 mm | 70 | 0 |
| Sawtooth Oscillator (VU009) | Syntonie | new | 4 | 55 mm | 35 | 20 |
| Dual Ramp Phase Shifter (VU008) | Syntonie | new | 4 | 65 mm | 55 | 50 |
| Quad Frequency Doubler (VU002) | Syntonie | new | 4 | — | — | — |

## Proposed layout — Vessel (Navigator top / Shapechanger bottom)
**WORK IN PROGRESS — not settled.**
**Vessel geometry (verified specs + user):** 208 HP = two **104 HP rows**; the case ends are **45° angled faces (left AND right)**, so the **shallow zone is only ~one Bridge module (≈8 HP) wide at each far edge** (≈32 mm at the very edge, rising to the full ≈64 mm just inboard). The **entire center of each row is full ≈64 mm depth.** The Malekko bus sits in that shallow edge zone.
**→ Rule: a shallow module at each of the 4 edge slots (far-left + far-right of both rows); everything else sits center with no depth limit.** Far-left edges = **Bridges** (32 mm; Bridge #1 mults H/V). Deep modules (oscillators 50–55, GAMMA 50, ES-9 50, Mapper/VC 45, Gainbrain 43) all live in the full-depth center. Only hard depth limit: **65 mm never fits** (over the ~64 mm max). (This is why GAMMA at 50 mm can't sit over the shallow-edge bus — it belongs in the center.)
- **Deep (center-only), by depth:** Dual Ramp Phase Shifter ~65 mm ⚠️ *(over the max — likely won't fit anywhere)*, Sawtooth Oscillator 55, Quadrature Oscillator / GAMMA / ES-9 50, Mapper / Visual Cortex 45, Gainbrain 43.
- **Shallow (edge-friendly):** Bridges 32, Prismatic Ray / Arch / Staircase / Doorway / Matte 32, SUBMIX / SY1 30, Hex 36, bajascillator 25.

⚠️ **Open conflicts to resolve:**
1. **Phase Shifter ~65 mm** exceeds the 64 mm max — verify it seats (low-profile cable?) or rehome.
2. **ES-9 (50 mm) pinned *furthest-right*** lands on the shallow ramp — its right ~3.5 HP overhangs. Fix: put **SY1 (30 mm) at the extreme right corner, ES-9 just inboard**, or confirm ES-9 clears.
3. **Visual Cortex (45 mm) top-right** should sit ~2.5 HP in from the corner, not flush at the edge.
4. **Bottom row ~124 HP > 104** with ES-9+SY1 — ~20 HP must move up; best candidates are the deep center-needing modules (Mapper, GAMMA) which can ride the top-row center and cable down.

**Power — Malekko supply (factor this in):** ±2 A per rail; the supply is **four isolated regulator pairs feeding four separate header groups** (quadrants), so noisy modules can be quarantined to keep their hash off the clean video rails.
- **Budget (owned rack):** **≈1.75 A on +12 V → ~88 % of the 2 A rail (only ~250 mA spare)**; **≈1.2 A on −12 V → ~60 %**. The **+12 V rail is the ceiling.** Biggest draws: **ES-9 = 451 mA** (a quarter of the whole +12 V budget by itself), then Visual Cortex 180, Hex / SUBMIX / Prismatic Ray 120 each, Mapper 100. Adding Cadrans or anything else eats the last of the +12 V headroom — watch it.
- **Quadrant strategy:** put the **digital/switching-noisy modules — ES-9 (USB) and SY1 (DMX) — together on their own isolated quadrant**, away from the clean analog path (oscillators, Visual Cortex, Mapper, Prismatic Ray). Their bottom-right grouping already sets this up. Balance the +12 V load across the four quadrants — ES-9's 451 mA nearly fills one on its own, so don't stack it with other heavy +12 V modules on the same regulator pair.
- Headers/board live in the shallow edge zones; keep each module within cable reach of its quadrant.


`Bridge #1 (mult H/V)` ┃ *oscillators:* `Prismatic Ray` · `Sawtooth Oscillator` · `Quadrature Oscillator` ┃ *rotation math:* `Gainbrain (multiply)` · `Passage (sum → X/Y)` ┃ *I/O (top-right):* `Visual Cortex`  *(ES-9 + SY1 moved to bottom row)*
- **Passage is the rotation summer** (SUBMIX reserved for output). **Cadrans (if acquired)** slots beside Gainbrain (both multipliers/VCAs — same control family).
- Oscillator cluster is ordered so the **Quadrature Oscillator sits rightmost — adjacent to Gainbrain**, the multiplier it feeds (sin/cos). Sawtooth's ramp also feeds the multiply stage; Prismatic Ray rides on the outer (left) side and cables down to the shape row.
- Prismatic Ray rides up here with the oscillator cluster for HP balance; its output cables down to feed the shape row.

**Bottom row — Shapechanger / shape → colour → output, left → right (≈100 HP):**
`Bridge #2 (summer)` ┃ *Syntonie shapers:* `Dual Ramp Phase Shifter` · `Quad Frequency Doubler (mirror)` ┃ *waveshapers:* `Staircase` · `Arch` ┃ *key:* `Doorway` ┃ *colour:* `Mapper` · `Matte` ┃ *mix / output:* `SUBMIX` · `hexadirectional crossfader` · `bajascillator` ┃ *I/O (far-right):* `SY1` · `ES-9`
- **Output compositor = the quadrant-orbit patch** (SUBMIX edges → Hex inputs; bajascillator 6 phases → Hex CV — see `patch-techniques.md`). bajascillator sits with the mix cluster by Hex for the short CV run, even though it's an oscillator — function wins over control-grouping there.
- **Shape-combine** (mixing mirrored ramps) falls to Bridge #2's fader or Gainbrain, since Hex is the output blender.
- Output returns up to Visual Cortex to encode (now a slightly longer hop, since SY1/ES-9 occupy the far-right corner).
- **ES-9 + SY1 = bottom-right I/O corner** (ES-9 rightmost, SY1 just left) — keeps the external connections (USB, DMX) together at the case edge.
- **GAMMA — relocating (slot TBD):** it doesn't clear the LZX/Malekko power bus in the waveshaper slot. It's 50 mm deep, so it needs a deep, bus-free position. Candidate = the freed top-row space in the deep zone by Sawtooth/Quadrature, where its log/expo/sum can still feed the shape chain (and could gamma-shape the rotation ramps) — pending confirmation of where the bus runs and whether the top row clears it.

Control-family clusters: *oscillators* (freq/shape) · *math/utility* (attenuvert/bias) · *waveshapers* (curve/fold) · *colour* (RGB/hue) · *mix/crossfade* (level/CV) · *I/O* (connectors). The one cross-flow placement is Prismatic Ray (top for HP fit) — if you have row width to spare it can drop to the bottom shape sources.



- **Syntonie Cadrans** — triple four-quadrant multiplier (3 identical channels; modes: VCA/crossfade, 4Q-bipolar, 4Q-unipolar; manual + CV amplitude). **Role it would fill:** the multiplier muscle for *full* rotation. The rotation matrix needs four 4Q multiplies (H·sin, V·cos, V·sin, H·−cos); with only one Gainbrain the rack is limited to partial rotation, but **Cadrans (×3) + Gainbrain (×1) = the 4 multiplies for true continuous rotation.** Its 4Q-UNI mode may multiply the 0–1 V ramps directly, potentially skipping the ±1 scaling step. Would sit in the top-row (Navigator/rotation) multiply stage, fed by Bridge #1's multed H/V and the Quadrature Oscillator, feeding Passage (sum). **HP + depth: to verify** (depth matters for Vessel placement). *Not owned — audition.*
