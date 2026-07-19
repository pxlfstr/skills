# Patch Techniques (community-sourced)

Distilled from LZX community threads. **Sourcing/credibility:** treat **Lars Larsen** (creatorlars — LZX founder) and **module designers** (e.g. VisibleSignals for Gainbrain) as authoritative on how the circuits behave and on the underlying math. Treat aesthetic preferences ("which looks better"), workflow tricks, and proposed-but-unbuilt modules as **opinion**, flagged inline. Function-first; component values appear only where a build/repair needs them.

## Rotating / spinning a 2D shape

**The core principle (Lars — authoritative).** To rotate a 2D shape you can't just rotate the finished shape; you rotate the *coordinate ramps* and rebuild the shape from them:
1. Generate H & V ramps (Visual Cortex, or a ramp generator).
2. **Rotate the ramps first** — think of it as rotating the reference frame / "the camera," not the object. Everything derived from the rotated ramps rotates identically.
3. **Mirror both ramps after rotation** — i.e. a saw→triangle (H/V mirror) conversion on each.
4. **Mix/combine** the two mirrored ramps (a crossfader works well and behaves a bit like a skew control).
5. **Key** the result (Doorway or Visual Cortex) to get a flat-shaded shape.

**What the "mirror" actually is (Lars — factual circuit behavior):** an absolute-value rectifier in a frequency-doubling configuration. The 0–1 V input is scaled to ±1 V so it slices through the center; the rectifier folds the negative half up to give 0–1 V out at *double* frequency — that's the saw→triangle conversion.

**Module realizations:**
- **Navigator + Shapechanger** = full 2D shape generation + rotation. (Navigator's own mirrors sit *before* rotation — great for feeding Shapechanger, but that's why Navigator alone can't produce a rotated shape.)
- **Navigator + Arch/Staircase** (no Shapechanger): rotate ramps in Navigator, then do saw→triangle on the outputs with **Arch** or **Staircase** (low/2× setting), then crossfade/mix, then key. Lars notes **3 of Arch's 4 functions are patched-out Shapechanger circuits**, and **Staircase is five mirror circuits in series** (so a pair can mirror H and V and keep going). *Navigator + 2× Staircase* is itself a pattern/geometry voice.
- **No Navigator at all:** you still get the (non-frame-rotated) spinning-shape look from Arch/Staircase mirroring + key. destroythings confirmed this with **1× Staircase + 1× Arch** (2× Arch is the cheaper route; 2× Staircase opens more variation).
- **Shapechanger alternative:** 2× Arch + Bridge, or 2× Staircase, gets close. *Opinion (dni_br):* Shapechanger gives more control over the shape's own geometry (scale/skew); plain Staircase mirroring mainly yields quadrilaterals, but Staircase ×2 + Bridge + Passage + Arch can do a lot.

**Explicit rotation math (jerry + rempesm patch — a standard 2D rotation matrix driven by quadrature):**
```
X = (H_ramp × sin) + (V_ramp ×  cos)
Y = (V_ramp × sin) + (H_ramp × −cos)
```
`sin`, `cos`, `−cos` are quadrature phases (0°, 90°, 270°) taken from a **quadrature oscillator** — so the rotation *angle* is just the oscillator's phase. DIY signal flow they used: scale H/V ramps to ±1 (processors) → multiply by the quadrature phases in a VCA/multiplier (**Gainbrain**) → sum the products into X and Y (**Foxing Hour ABC / Dual A+B−C**) → offset back to 0–1 (**Access**) → **rectify** ramp→triangle (needed or you won't get a closed shape) → optional **expo/log (GAMMA)** for a non-square shape → optional **Castle ADC** to split into RGB channels.

> **Owner relevance:** this is very much within reach of the fstrvsn rack. the **Quadrature Oscillator** (VU006) supplies the sin/cos rotation angle; **Gainbrain** does the multiplies; **Staircase/Arch** do the saw→triangle; **Doorway** (or Visual Cortex) keys; **GAMMA** bends the square into something richer; ramps come from **Visual Cortex**. The DIY-module gaps are the summing/offset utilities (Foxing Hour ABC/Access) and a Castle ADC. (See the Gainbrain fix below — it matters for using Gainbrain as a clean multiplier here.)

## Center of rotation (Navigator + Shapechanger)
**Lars (authoritative):** to center rotation on the shape, set **both Anchor/Position switches on Navigator to "Position,"** **HV Mirror OFF on Navigator** and **ON on Shapechanger.**
*Workflow tip (destroythings, nerdware — opinion/technique):* set a fast rotation while you dial in the center; being off-center is much easier to see when it's spinning quickly.

## Animating / modulating colour

**Direct-RGB cycling (Gavin — community patch):** patch a **quadrature oscillator into the RGB source, one phase per R/G/B**; mix via Passage, a crossfade, or a matrix mixer.
- *Factual nuance (Rik_bS):* the **bajascillator's phases are 60° apart (0/60/120)**, which suits RGB nicely, whereas most Eurorack quadrature oscillators are 90° apart.
- Feedback + delay (Memory Palace / mixer) with colour sent through **wavefolders (Arch, Staircase)** → "deterministic chaotic" colour evolution.
- **Posterize** with Castle to limit to ~8 colours, then Baja→RGB through a **sample & hold (with slew)** for an 8/16-bit "colour cycling" look.

**Shifting hue without changing brightness (Lars — authoritative):** any *direct RGB* manipulation cross-modulates luma. To move hue/chroma independently, use **Mapper** (polar-to-cartesian) — or build it: a **quadrature VCO as the UV/chroma source + a static Y, through a YUV→RGB matrix** (SMX3 or any 3×3) gives continuous hue cycling. That's essentially what Mapper does internally.
- *Opinion (Lars):* neither RGB-cycling nor the Mapper/UV approach is "superior" — RGB cycling yields different palettes and the brightness shifts make the image more dynamic; it's a taste/technique choice.

**Colorspace facts (Lars — authoritative):**
- RGB = Red / Green / Blue. YUV = **Luma (Y)**, **U / Pb (Blue − Luma)**, **V / Pr (Red − Luma)**.
- RGB and Luma transforms are **1-D** (per-channel contrast/brightness). **Hue and Saturation are 2-D** transforms of the UV plane: **Hue = angle, Saturation = distance from center.** So process chroma with **2-D / quadrature** functions (polar-to-cartesian + dual VCA), not mono VCAs. Hue "doesn't exist" without Saturation — they're a pair (U and V each exist independently, which is why you patch UV, not "hue").
- A **joystick into a YUV→RGB matrix** becomes a chroma selector: distance from center = Saturation, angle = Hue, with luma left alone.
- **RGB↔YUV conversion = 2× SMX3** (or any 3×3 matrix) with the right coefficients.
- *Opinion / framing (Lars, explicitly his perspective):* RGB is closest to physics/optics and how the eye works (best for mixing two images); YUV is closest to how artists think (the color wheel, paint-mixing, value/contrast). The **"HSL Amp"** he describes (Mapper + RGB input + a rotator, in 12 HP) is a **proposed/unbuilt** concept, not a shipping product — treat as roadmap musing.

## Gainbrain (Visible Signals) — manual/CV range fix
**Issue (jerry; confirmed by several builders):** out of the box the manual knob only crossfades in a narrow band around 12 o'clock and CV has a tiny useful range — the control voltage swings ~±10 V into a fader stage that wants ~0–2.5 V.
**Fix (VisibleSignals, the module's designer — authoritative):** set **R4 = 10 K** (brings the manual range down to ~2.5 V). He'd bumped R26/R24 to 10 K in the build guide but missed R4. Other options he gave: lower **R26** (~2.4 K) to cut overall gain (manual + CV together); omit **R13** to cut just the CV-input gain; the negative manual offset is *intentional* (lets you re-center the crossfade for inputs that exceed 1 V).
**The "2-resistor mod"** (jerry — used in the rotation patch above): **R4 → 10 K and R7 → 20 K**, which removes the dead negative half of the manual sweep so it acts as a clean attenuator — important when using Gainbrain as a **multiplier** (e.g. the rotation patch).

> **Owner relevance:** you run a Gainbrain. If its manual/CV range feels cramped, this is the fix — and it's specifically what makes Gainbrain behave as a reliable multiplier in the rotation patch.

## Quadrant-orbit compositor (owner patch — SUBMIX + Hex + bajascillator)
A continuously swirling four-source spatial blend, built entirely from owned modules at the output stage.

- **SUBMIX as a 2×2 quadrant mixer:** feed four *distinct* sources into the corners (Top-Left, Top-Right, Bottom-Left, Bottom-Right). Its edge outputs — Top (TL+TR), Bottom (BL+BR), Left (TL+BL), Right (TR+BR) — go to the **four signal inputs of the hexadirectional crossfader**.
- **bajascillator's six phases** (60° apart, video-rate) → **Hex's six CV inputs** (one per fade direction). Four inputs give C(4,2)=6 pairwise crossfades, so the six phases map **one-to-one** onto the six blend directions.
- **Result:** the four edge signals blend along all six axes at once, each offset 60°, producing a smooth **rotating/swirling spatial morph**. Shines in a feedback loop ("knot theory"). It's a compositing/output move, not the geometric rotation — pairs naturally with SUBMIX-as-compositor + Hex-as-blender.

Caveats: SUBMIX edge outs are *sums* (can exceed 1 V) → attenuate into Hex; feed four **distinct** corner sources or the motion goes flat; **phase-to-direction mapping** sets the character (rotational order = clean swirl); LFO rate = slow drift, video rate = texture/interference. Confirm Hex's four inputs accept direct patches (it's nominally a VBMv2 expander).
