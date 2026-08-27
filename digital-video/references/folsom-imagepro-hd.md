## Provenance

**Verified [Official]** — *ImagePRO – Multi Format Image Processor Manual*, Folsom Research (a Barco company), document # 26-0302000-00 Revision E, 121 pages, user-supplied PDF. Read in full: overview/features (all three variants), rear-panel connectors and pinouts for all three variants, video input/output connection detail, DVI-I pinout, genlock submenu in full, output formats submenu, technical specification appendix. **Not read:** the remote command reference (manual pages 64–94, serial/Ethernet command list) — this is control-protocol material and, per this repo's boundary rule, belongs in `creative-coding/references/` if extracted, not here. Not extracted into this document; flagged as present in the source if a future session needs it. No open contradictions found in what was read.

**Second source, folded in additively:** *ImagePRO product datasheet*, doc 31-0302000-00, Barco Events USA, dated February 2005, user-supplied PDF, read in full (6 pp.). A shorter marketing/spec document covering all three variants side-by-side — not ImagePro-HD-exclusive despite being supplied while discussing the -HD unit. Facts below are tagged by what this document itself scopes them to (line-wide vs. variant-specific), not by which unit the user happened to be discussing. This source contains **no new pixel-clock, MHz, or delay-in-fields figures** — both open items below (progressive-source delay, DVI-I pixel clock) remain open after this source.

**⚠️ Correction recorded in place, not silently fixed:** an earlier pass through this same manual (same session) initially described ImagePro as configurable "as ADC or DAC" — a single-direction role you set the box to. That's wrong. Rear panel and spec-table evidence (§2, §5) show ImagePro-HD is **simultaneously bidirectional** on every port — analog, SDI, and DVI-I input all present alongside analog, SDI, and DVI-D output on the same chassis, all the time. It isn't switched between modes.

**⚠️ Second correction recorded in place:** a resolution comparison between the DVI-I input's UXGA (1600×1200) and 1080p (1920×1080) entries was initially asserted in the wrong direction without computing pixel counts. 1920×1080 = 2,073,600 px; 1600×1200 = 1,920,000 px — 1080p is larger. Per Rule 3a (added to `RULES.md` this session), no such comparison is made anywhere in this document without the multiplication shown.

---

## 1. What it is

Folsom's description, direct from the manual: "a high performance digital video scaler, scan converter, standards converter, switcher and transcoder in one." Three variants, ascending capability:

| Variant | Adds over base ImagePRO |
|---|---|
| **ImagePRO** | Base: 3 universal analog inputs, 4 analog/composite/S-video outputs |
| **ImagePRO-SDI** | +1 SD-SDI input, +1 SD-SDI output. Motion-adaptive de-interlacing extended to HDTV inputs. Lower video delay than base. Logo capture/recall, dissolve to/from logo. Field-upgradable to -HD |
| **ImagePRO-HD** | +SD/HD-SDI in and out (not 3G — see §2 and open items). +DVI-I input (analog or digital, with loop-through). +DVI-D output |

**No 3G-SDI, no HDMI connector, no dual-link DVI stated anywhere in this manual, on any variant.** This is a real ceiling worth checking against source formats before patching — see §7.

**The underlying scaler is branded "Athena™"** — Folsom's proprietary processing engine, named in the datasheet but not mentioned anywhere in the full manual. Datasheet describes it as "designed from the ground up to provide the highest possible image quality while minimizing processing delays," supporting 1:1 video sampling at 10 bits/color — line-wide, not stated as HD-specific.

**Output port counts, stated as flat totals (datasheet, line-wide table):** (4) outputs on base ImagePRO, (5) on ImagePRO-SDI, **(6) on ImagePRO-HD.** Input counts: (3) on base, (4) with SDI or on -HD. These are simple totals corroborating, not contradicting, the per-connector breakdown in §2 below — the manual describes connectors by type/location, the datasheet gives the same information as flat counts.

## 2. Rear-panel I/O, by variant

**ImagePRO (base) and ImagePRO-SDI** — Universal Inputs 1 & 2 on HD-15 (RGBHV/RGBS/RGsB/component/S-video/composite), Universal Input 3 on BNC, all three with buffered loop-through. Outputs: 5-wire BNC + HD-15 (same RGB/YPbPr signal on both simultaneously), S-video 4-pin mini-DIN, composite BNC. SDI variant adds one SD-SDI BNC in, one out.

**ImagePRO-HD** — Universal Input 2 on HD-15, Universal Input 3 on BNC (both with loop-through), **Universal Input 1 on DVI-I** (analog or digital, loop-through; ships with a DVI-I→HD-15 adapter for analog use). SD/HD-SDI in and out on BNC. All the base analog outputs, **plus DVI-D output** (digital only, no analog on that connector).

## 3. DVI-I input pinout (ImagePro-HD, Universal Input 1)

Standard DVI-I: 24 TMDS/DDC/hot-plug pins (digital) plus a 5-pin MicroCross analog block (Red/Green/Blue/Hsync/Ground return) on the same physical connector — meaning one port genuinely carries either an analog RGBHV signal or a digital TMDS signal, not a combined/simultaneous feed.

## 4. Sync flexibility (input and output, all variants)

Accepts and outputs sync-on-video (sync-on-green), separate composite sync, or separate H/V — all three, both directions. This matches the DVS 304's sync flexibility (see `extron-dvs304.md` §5); no sync-type mismatch risk pairing the two devices.

## 5. Genlock

| Genlock source options | Freerun · Input Video (locks to whatever's currently selected as input) · H+V Sync (external) · Csync (external) · Blk Burst (external) |
|---|---|
| **Genlock type tiers** | **V Lock** — vertical only, available for any source. **HV Lock** — horizontal+vertical, available for any source, but only if input and output V Totals match. **HVSc Lock** — full genlock (H, V, and subcarrier), only available when output format is PAL or NTSC, source must be Blk Burst or Input Video, and V totals must match |
| H Phase | ±½ H Total, relative to genlock source. N/A when genlock type is V-lock-only |
| SC Phase | −180° to +180°, relative to genlock source. Only valid when source is Blk Burst or input decoded video |

**"Input Video" as a genlock source means ImagePro can lock to its own incoming signal without a separately distributed external reference** — relevant when chaining two ImagePro units, since the second unit can lock to what the first is feeding it rather than needing house sync run to both.

**Vertical Lock has a second, explicitly stated purpose beyond artifact avoidance** (datasheet, line-wide — not flagged as HD-specific): *"Vertical locking eliminates frame rate conversion problems that would otherwise result in motion artifacts **or allows multiple units to have their outputs timed together.**"* The second clause is new relative to the manual's own genlock submenu text — direct confirmation that Vertical Lock is a deliberate mechanism for timing multiple ImagePro units to each other, not just a single-unit motion-artifact fix. Directly relevant to a two-unit round-trip chain (e.g. ATEM → ImagePro → analog → ImagePro → X20): this is the datasheet's own stated use case for that topology.

## 6. Video processing delay

[Already the highest-value fact in this document — see cross-reference to prior session content below.]

**ImagePRO-SDI and ImagePRO-HD**, MAD (motion-adaptive) de-interlacing mode:
- **2 input fields, frame-locked to source**
- **3 input fields, if output is not frame-locked to input**

**Base ImagePRO**, MAD mode: 4 fields (locked) / 5 fields (unlocked) — worse than -SDI/-HD, which use "an advance MAD processor."

**Field-to-Frame mode** (all variants with the option; trades vertical resolution for speed, converts individual fields to progressive frames rather than reconciling motion): **1 field (locked) / 2 fields (unlocked).**

⚠️ **The manual scopes all of the above to de-interlacing specifically** — no separate progressive-in/progressive-out latency figure is stated anywhere in this document. This is a real, unresolved gap, not something reasoned around.

**The manual's own stated best practice:** frame-lock output to the input source specifically to eliminate frame-rate-conversion delay — the unlocked figures above are the cost of skipping that.

## 7. Resolution range, by input/output category

**These lists are per-connector-category as labeled in the manual's own spec-table headings, not a single flattened whole-device ceiling.** Earlier reasoning in this session conflated them — correcting that here.

| Category | Range stated |
|---|---|
| Universal (analog) inputs 1–3, all variants | VGA (640×480), SVGA (800×600), XGA (1024×768), SXGA (1280×1024), UXGA (1600×1200), HDTV 480p/720p/1080p/1080i, 875 RS-343, 525 RS-170 |
| **Digital Video (DVI) Input, ImagePro-HD only** | Same list as above — VGA through UXGA, HDTV 480p/720p/1080p/1080i, 875 RS-343, 525 RS-170. **No pixel-clock (MHz) figure given. No dual-link statement anywhere in this manual for this connector** |
| SDI input | SD-SDI (all SDI-capable variants); SD/HD-SDI (−HD only). **No 3G-SDI anywhere in this manual** |
| Standard-resolution outputs | VGA/SVGA/XGA/SXGA/UXGA; plasma-specific 1280×768, 1365×768, 1365×1024; HDTV 480p/720p/1080p/1080i; 875 RS-343, 525 RS-170 |
| **Special case — Digital Cinema** | 2048×1080p @ 59.94 Hz and 2048×1080p @ 60 Hz, **output only, ImagePRO-SDI and ImagePRO-HD only** — the one entry in this whole document that sits outside the standard-format list |

No entry in any of these lists is asserted as "the highest" without a computed pixel count per Rule 3a — none has been computed in this document because no ranking claim was needed to record the lists themselves.

## 8. What this document does not cover

- **Remote command set** (manual pp. 64–94, Ethernet + RS-232 control) — read in the sense of being present in the source, not extracted here. Belongs in `creative-coding/references/` per the repo's protocol/device boundary rule if a future session needs it.
- **DVI-I input pixel clock or dual-link capability** — genuinely absent from this manual. UXGA at standard timing fits comfortably under a single-link ~165 MHz ceiling, which is suggestive but not a substitute for a stated figure.
- **Progressive-source (non-interlaced) processing delay** — not stated. All delay figures in §6 are scoped to de-interlacing.

---

## Verification status

| Claim | Status |
|---|---|
| Rear-panel I/O, all three variants | **Verified [Official]** — manual read directly, §Installation |
| DVI-I pinout | **Verified [Official]** — manual read directly |
| Genlock source/type/phase behavior | **Verified [Official]** — manual read directly, §Genlock Submenu |
| MAD/Field-to-Frame delay figures | **Verified [Official]** — manual read directly, §Video Processing Delay |
| Resolution lists by category | **Verified [Official]** — manual read directly, Appendix Technical Specifications, corrected to per-category attribution this session |
| No 3G-SDI / no HDMI / no dual-link | **Verified negative** — absent from every I/O section and the spec table; not found despite looking |
| Progressive-source delay | **Not available in either source read this session** (manual or datasheet) |
| DVI-I pixel clock / dual-link | **Not available in either source read this session** (manual or datasheet) |
| Athena scaler name, 1:1 sampling, 10-bit | **Verified [Official]** — datasheet, technology-brief section, line-wide (not flagged HD-specific in source) |
| Output port counts by variant (4/5/6) | **Verified [Official]** — datasheet spec table, corroborates §2's connector-level detail from the manual |
| Vertical Lock enabling multi-unit output timing | **Verified [Official]** — datasheet, "Genlock/Vertical Lock" section, stated line-wide |

## Not yet verified — open items

- **Progressive-source (e.g. 1080p59.94) processing delay** — the single highest-value gap. No figure in the manual or the datasheet; would need a Folsom/Barco support inquiry or a bench measurement.
- **DVI-I input pixel clock ceiling and dual-link support** — not stated in the manual or the datasheet. A different document (an install guide, if one exists) may state it; not yet supplied.
- Remote command set — present in source, not yet extracted into `creative-coding/references/`.

## Cross-references

- `extron-dvs304.md` §5 — matching sync flexibility (sync-on-green/composite/separate H-V) confirmed on both devices; no mismatch risk when pairing them.
- `christie-spyder-x20.md` §13 — X20's own de-interlacing latency ("low delay, under 1.5 interlaced frames") pairs directly with this document's §6 for round-trip latency budgeting (ATEM → ImagePro → analog → ImagePro → X20 chains). See also `christie-spyder-x20.md` §4 for the RGBHV-via-DVI-I even-input detail this document's §3 connects to on the ImagePro side.
