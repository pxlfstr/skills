# Film Projection: Gate Geometry, Lens Selection & Light Budgeting

**Stored:** 2026-07-18
**Why it's here:** Filed under `digital-video` deliberately. The material is photochemical, but the reasoning is the same throw-ratio / foot-lambert / magnification math used to spec digital projectors — and the film cases make the *limits* of that math visible in a way digital doesn't. Useful as a reference frame for large-venue projection work.

**Verification note:** Nothing here comes from a purchased standards document. The controlling standards (ISO 2467:2004 for 65mm/5-perf, SMPTE 196M for screen luminance, SMPTE PH22.106 series for 35mm apertures) were identified but **not read**. Figures below are the best available secondary sources, tiered honestly. Anything marked *Derived* is arithmetic performed on a cited figure, not a sourced value.

---

## 1. Gate dimensions

| Format | Projected aperture (mm) | Area (mm²) | AR | Source | Tier |
|---|---|---|---|---|---|
| IMAX 15/70 | 69.6 × 48.5 | 3,376 | 1.43:1 | [IMAX film format](https://www.britannica.com/technology/IMAX-film-format), Britannica [Official-ish] | Lead |
| 70mm 5-perf (Todd-AO) | 48.56 × 22.09 | 1,073 | 2.20:1 | [70 mm film](https://en.wikipedia.org/wiki/70_mm_film), Wikipedia [Forum] | Lead |
| 35mm anamorphic (scope) | 21.29 × 17.78 | 379 | 2.39:1 (post-2× squeeze) | [Wide Screen Apertures and Aspect Ratios](https://www.widescreenmuseum.com/widescreen/apertures.htm), Widescreen Museum, citing SMPTE PH22.106-1971 [Forum] | Lead |
| 35mm flat 1.85 | 20.96 × 11.33 | 238 | 1.85:1 | [List of motion picture film formats](https://grokipedia.com/page/List_of_motion_picture_film_formats), Grokipedia [Forum] | Lead — weakest source here |

*Areas are Derived.* Inch source values: scope 0.838 × 0.700 in; flat 0.825 × 0.446 in.

**IMAX camera aperture** (larger than projected): 70.41 × 52.63 mm — [IMAX 15perf_70mm Tech Specs](https://www.cinematography.net/edited-pages/IMAX15perf_70mmTechSpecs.htm), cinematography.net [Forum] — Lead. Projection aperture is spec'd as at least 2 mm less vertically and 0.41 mm less horizontally than camera aperture ([What Is IMAX](https://nofilmschool.com/what-is-imax), NoFilmSchool [Forum]) — Lead.

**Upgrade path:** ISO 2467:2004 (*Cinematography — Image area produced by 65 mm/5 perforation motion-picture camera aperture and maximum projectable image area on 70 mm/5 perforation prints*) is the authoritative source for the 5-perf row. ~CHF 44 from ISO. Buy it before betting anything on the 48.56 × 22.09 figure.

---

## 2. Camera-side lens coverage — the constraint that moves aspect ratio

The gate is mechanical and lens choice can't change it. But a lens with insufficient image circle vignettes the corners, and cropping to a wider delivery ratio removes exactly those corners. So coverage sets which ratios a given lens can serve.

| Delivery | Frame at full gate width (mm) | Required image circle (mm) |
|---|---|---|
| IMAX 1.43:1 | 69.6 × 48.5 | 84.8 |
| IMAX 1.90:1 crop | 69.6 × 36.6 | 78.7 |

*Both Derived from the Britannica figure.* The 1.90 crop needs ~7% less diagonal.

Practical consequence: a lens that's unusable for a 1.43 presentation can be clean for the 1.90 extraction. Since IMAX-shot features are finished for both, "which lenses cover" and "which ratio am I protecting" are the same question. Coverage is the reason IMAX cinematography runs on a small pool of adapted/rehoused medium-format optics (Mamiya, Hasselblad/Zeiss lineages) — the ~85mm diagonal exceeds what most 6×7 designs were built to fill.

Separate mechanical vignetting (hard clip; doesn't improve stopped down) from natural falloff (gradient; sometimes gradeable). The first hard-limits your ratio. The second is a taste call.

---

## 3. Projection lens focal lengths & throw

Throw ratio ≈ **f ÷ gate width** at cinema magnifications (the `(1 + 1/m)` term is negligible when m ≈ 300–400).

**Isco-Optic UltraStar HD, 70mm series:** 38, 68, 74, 81, 87, 93, 99, 106, 112 mm
**Schneider Super-Cinelux:** range extended to 32.5–100 mm by ~2005
**Schneider Cinelux-Première:** aspherical elements, variable iris f/1.7–f/4.0, released 2002
Source for all three: [The Isco Story](https://deltalenses.com/the-isco-story-2/), Delta Lenses [Forum] — Lead.

Dual-format 35/70 projection lenses were a standard product category, letting one house run both gauges to one screen without re-rigging — [Film Lenses](https://www.mteworld.com/categories/film-lenses.html), Magna-Tech [Forum] — Lead.

**Throw ratios from the Isco set** (*Derived*):

| Gate | TR at f=38 | TR at f=112 |
|---|---|---|
| IMAX 15/70 (69.6 mm) | 0.55 | 1.61 |
| 70mm 5-perf (48.56 mm) | 0.78 | 2.31 |
| 35mm scope (42.58 mm effective, post-squeeze) | 0.89 | 2.63 |
| 35mm flat (20.96 mm) | 1.81 | 5.34 |

**Key structural point:** bigger gate → shorter throw ratio for the same focal length. This is why IMAX booths sit close behind the top rows.

**Real-world IMAX data point:** BFI London IMAX — 26.0 m screen width at 25.8 m throw, i.e. **TR ≈ 0.99**, back-solving to a lens near 69 mm. Source: [Physics final exam problem: IMAX projector lens focal length](http://waiferx.blogspot.com/2012/06/physics-final-exam-problem-imax.html), citing the BFI IMAX technical guide [Forum] — Lead. Treat as one data point, not the IMAX GT lens range.

**Unresolved:** no authoritative source found this session for the IMAX GT projector's actual lens options. IMAX theaters are purpose-built — screen size and booth position designed together, lens matched once at install — so it's plausible there is no catalogue to find. Needs an IMAX engineering doc to close.

**Not like digital:** no zoom, no optical lens shift. Aiming is done by tilting the whole machine and correcting keystone with a filed aperture plate and tilted gate. Booth throw is fixed by architecture, so ~9 focal lengths yields ~9 image widths — you land on the nearest and adjust side masking. That's what adjustable masking is *for*.

---

## 4. Screen luminance & the lumens budget

| Standard | Target | Source | Tier |
|---|---|---|---|
| Film projection (SMPTE 196M) | 16 fL open-gate; ~14 fL with film in gate (base density ~0.05) | [Screen Selection](https://www.slideshare.net/slideshow/screen-selectionfordigitalcinema-1/33005772), Harkness Screens / ICTA [Official] | Verified-adjacent |
| Digital cinema (SMPTE 431-1-2006) | 14 fL ±3 at centre; 75% of centre at sides, min 9 fL | Harkness/ICTA, same deck [Official] | Verified-adjacent |
| Permissible range, commercial | 12–22 fL centre, edges ≥10 fL | [Question about projector luminance](https://www.avsforum.com/threads/question-about-projector-luminance.1244514/), AVS Forum [Forum] | Lead — do not spec from this |

**Lumens required for 14 fL, gain 1.0, incident on screen** (Harkness/ICTA [Official]):

| Screen width | Scope format | Flat format |
|---|---|---|
| 12 m | 9,200 | 11,700 |
| 15 m | 14,400 | 18,300 |
| 18 m | 20,800 | 26,400 |
| 22 m | 31,000 | 39,400 |
| 30 m | 57,700 | — |

Higher-gain screens cut this substantially — the same deck gives gain 1.4 / 1.8 / 2.2 rows. Gain is the primary lever when lamp power runs out.

---

## 5. The thermal ceiling — the one thing that has no digital equivalent

Screen lumens are set by area and target luminance and are indifferent to gauge. But that flux passes through the gate, and **flux density at the film plane scales inversely with gate area.**

Relative flux density at the film plane, equal screen lumens (*Derived* from §1 areas):

| Comparison | Ratio |
|---|---|
| 70mm 5-perf vs IMAX 15/70 | 3.15× |
| 35mm scope vs 70mm 5-perf | 2.83× |
| 35mm flat vs 70mm 5-perf | 4.52× |
| 35mm scope vs IMAX 15/70 | 8.92× |

A DMD/LCoS panel is a cooled solid that tolerates high flux. A film frame is a thin strip parked in a focused beam for ~1/48 s, absorbing energy, and it will buckle then cook. This puts a hard ceiling on lumens per unit gate area that **is not solvable with a bigger lamp** — past it the only levers are screen gain or a smaller image.

This is a real reason (alongside resolution) that the largest roadshow screens were built around 70mm: a bigger gate admits more total flux before the print starts cooking.

⚠️ **Unquantified.** No sourced figure was found this session for maximum permissible flux density or gate temperature on any print stock. The mechanism is sound; the number is missing. Would need a Kodak print-stock technical bulletin or a projector manufacturer's lamphouse spec. **Do not attach a number to this until that's read.**

---

## 6. Cross-gauge magnification — the asymmetry worth knowing

Running 35mm and 70mm to the **same screen width** (routine; dual-format lenses exist for it). Magnification penalty relative to 70mm 5-perf (*Derived*):

| Format | Horizontal | Vertical |
|---|---|---|
| 35mm scope | 2.28× | 1.14× |
| 35mm flat | 2.32× | 2.32× |
| IMAX 15/70 | 0.70× | 0.70× |

**Scope degrades almost entirely horizontally.** The anamorphic frame is only 21.29 mm wide before the squeeze is undone, but uses nearly full frame height — and a 2.39:1 screen is shorter than a 2.20:1 one at equal width. Result: grain stretches into horizontal ovals, horizontal detail softens, vertical detail holds up. That's the characteristic big-scope look, and it's a consequence of the squeeze, not print quality.

Against 35mm flat the penalty is near-uniform. IMAX vs 70mm is also uniform (both spherical) and runs in IMAX's favour.

**Magnification behaves better on film than digital.** Past its pixel pitch a digital image shows structure; film shows grain, which is stochastic and reads as texture. This is why 15/70 tolerates a floor-to-ceiling screen at close viewing distance — the one place film's scaling is more forgiving than a fixed pixel grid.

---

## 7. Exhibition context (as of 2026-07, perishable)

- **The Odyssey** (Nolan, released 2026-07-17) — first feature shot **entirely** with IMAX film cameras. No footage in it was framed for a wider ratio, so every non-1.43 presentation is a crop. Prior Nolan films intercut 15/70 with 5-perf 65mm.
- Presentation hierarchy: 1.43:1 IMAX 70mm film → IMAX with Laser 1.90:1 → 5-perf 70mm 2.20:1 → everything else at 2.39:1.
- ~41 venues worldwide can present 1.43:1 IMAX 70mm. Cinemark commissioned three new IMAX 70mm film sites ahead of this release, including Seven Bridges (Woodridge, IL), adding to its existing Dallas location.
- Some IMAX with Laser sites also run 1.43:1 — check the individual screen, not the brand.
- ⚠️ **Unverified:** the claim that The Odyssey's 35mm engagements run at 2.39:1 was asserted in session without a direct source. Plausible from format convention; not confirmed.

---

## Open items

1. Buy/read ISO 2467:2004 to promote the 5-perf aperture row to Verified.
2. Find a Kodak print-stock or lamphouse source to quantify §5's thermal ceiling.
3. Find an IMAX engineering source for GT projector lens options.
4. Read SMPTE 196M directly rather than via the Harkness deck.
