# digital-video — Reference Library Index

Manifest of stored reference documents. Read this first when the skill is active.

Maintenance is **additive and never lossy** — merge rather than replace, keep correct detail a newer source happens to omit, remove only what is shown to be *wrong*. (Per SKILL.md; `STORAGE.md` was not present in the library when this index was created.)

---

## Documents

### `film-projection-geometry-and-light.md`
**Added:** 2026-07-18
**Covers:** Film gate dimensions (IMAX 15/70, 70mm 5-perf, 35mm scope and flat); camera-side lens coverage as a constraint on usable aspect ratio; projection lens focal-length families (Isco UltraStar HD, Schneider Super-Cinelux/Cinelux-Première) and derived throw ratios; SMPTE 196M / SMPTE 431-1 screen luminance targets and the Harkness lumens-vs-screen-width table; flux density at the film plane and the thermal ceiling on gate illumination; cross-gauge magnification asymmetry when running 35mm and 70mm to one screen width.

**Why filed here rather than `analog-video`:** the subject is photochemical but the reasoning is throw-ratio, foot-lambert and magnification math shared with digital projector specification. Filed where the working use is.

**Confidence:** Mostly **Lead** tier. No standards document was purchased or read. The Harkness/ICTA deck is the strongest source in the file. Section 5 (thermal ceiling) is mechanism-only with **no sourced number** — flagged in place.

**Open items:** ISO 2467:2004 (5-perf apertures); Kodak print-stock thermal limits; IMAX GT projector lens options; SMPTE 196M read directly.

---

### `analog-way-vio-4k.md`
**Added:** 2026-07-19
**Covers:** Analog Way VIO 4K multi-format converter/scaler. Chassis and option-slot layout; the output-as-group-of-plugs model and why output count ≠ connector count; SDI Level A/B as a mapping scheme rather than two ports; native input/output ceilings (DP and HDMI both cap at 4K@30); all five expansion cards with connectivity and format ceilings; per-plug output format tables for native and expansion outputs; what 6G-SDI adds over 3G and what it does not; the screen/AOI canvas model, screen sizing modes, AOI windowing and pitch compensation; the input "view" (pan/zoom/mask/crop) and where it lives in the menu tree; custom formats (CVT 1.1 / DMT 1.0, 64 slots, Check validator and its error strings, computer-formats-only so no SDI path); framelock/genlock references and the 23.97–120 Hz rate-mode restriction.

**Source:** VIO 4K User Manual / Programmer's Guide `[Official]`, user-supplied PDF, read in full.

**Confidence:** **Verified** tier throughout — every figure and quoted behaviour read from the manual this session. No remembered or estimated numbers.

**Open items (§10 of the doc, all bench tests):** whether the input view can differ per screen when multiple screens exist (highest value — determines whether independently-scaled crops are possible or only AOI windows onto one canvas); whether one card runs input and output simultaneously; the manual's own input-count discrepancy (§1.3 says 9, §7.1 says 8, framelock list enumerates 7 native); Quad-Link 3G behaviour at non-2160p rasters; per-plug sub-30Hz rate options; whether custom formats gate H active above 4096.

**Noted defect in source:** the 6G/12G-SDI rows tag ST2036 as "2K" and ST2048 as "4K", which appears transposed against SMPTE ST 2036-1 (UHDTV) and ST 2048-1 (DCI). Flagged in place.

### `pixel-clock-and-link-bandwidth.md`
**Added:** 2026-07-19
**Covers:** Method for deciding whether an arbitrary raster fits down HDMI, DisplayPort or SDI. Separation of active information rate, pixel clock and link/wire rate; the CVT-RB v1 timing procedure (160px H blanking, 460µs minimum V blanking, 0.25 MHz clock quantisation); HDMI character rate vs wire rate and why character rate is the binding constraint; DP 1.2 HBR2 payload after 8b/10b; SDI tier table; worked example at 5120×2880@30 across 8/10/12-bit; comparison table of common rasters with DP 1.2 utilisation; reproducible Python.

**Confidence:** **Computed** tier for all clocks and bandwidths — arithmetic performed this session from the stated CVT-RB model, reproducible from the included code. Not manufacturer figures. Interface ceilings are marked `[Unverified]` in place: they are consistent with the VIO manual's card descriptions (18 Gbps HDMI 2.0, 21.6 Gbps DP 1.2) but no HDMI Forum or VESA specification was read. The 600 MHz HDMI 2.0 character-rate limit specifically needs a primary source before being quoted to a client.

**Cross-reference:** companion to `analog-way-vio-4k.md` — the custom-format question there (rasters wider than 4096) is answered on the clock side here.

**Open items:** obtain HDMI 2.0 and DisplayPort 1.2 specifications directly to promote the interface ceilings from Unverified to Verified; add DP 1.4 HBR3 and DSC once a source is read; add 4:2:2 and 4:2:0 rows to the comparison tables.
