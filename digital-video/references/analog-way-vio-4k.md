# Analog Way VIO 4K — Multi-Format Converter/Scaler

**Source:** *VIO 4K User Manual / Programmer's Guide* (Analog Way) `[Official]` — user-supplied PDF, read in full 2026-07-19. All section numbers below refer to that document.

**Confidence:** Everything in sections 1–9 is **Verified** tier — read directly from the manual this session. Section 10 lists what the manual does *not* settle. No figure here is remembered or estimated.

---

## 1. What it is, functionally

A single-source multi-format converter/scaler with a **canvas-and-window** multi-output architecture. It is *not* a switcher: it processes **one input at a time**. Fully loaded it drives three outputs, but those are three independently-framed renderings of the **same source** — the manual states plainly that even when equipped with expansion interfaces the device cannot output three different sources (§15.2).

The correct mental model is: one source → one screen (canvas) → up to three output windows onto that canvas, each with its own raster, active area, rotation and pixel pitch.

---

## 2. Chassis and slots

- 2 slots for **video** option cards
- 1 slot for **audio** option card
- Five option cards exist; a maximum of three can be installed at once (one audio + two video) (§15)
- 6.2 kg / 13.66 lbs (§1.2)

---

## 3. The output model — output ≠ connector

**§6.1: "An output is a group of plugs that deliver the same video content under various signal types."**

This is the single most load-bearing fact about the device and the most common source of confusion.

- The native unit ships with **1 standard output carrying 6 output plugs** (§1.5)
- Each installed video card adds **one further output resource** (§15.3) — again a group of plugs, not a single jack
- Ceiling is therefore **3 independent rasters**, on a chassis with a dozen-plus output connectors

Consequence: multiple connectors on one output give you **redundancy, confidence feeds and parallel distribution legs** at zero cost to the output count — but never a second picture.

### "SDI (6G Level A & B)" is one connector

The native output's SDI spec reads *SDI (6G Level A & B)*. Level A and Level B are SMPTE ST 425 **mapping schemes**, not two ports. Per §7.5.2 the settings are:

| Setting | Manual's description | Transport |
|---|---|---|
| Level A | 1 channel + 1 complete image | `Transport in 1 x 3G Level A coax` |
| Level B | 1 image in 2 parts (= 2 signals) | `Transport in 1 x 3G Level B coax` |

Both are single-coax. There is **one SDI BNC** on the native output.

### Per-plug status

A plug on an active output can still be dark. §6.3 enumerates plug status values including:

- `ACTIVE`
- `ACTIVE (WARNING EDID INVALID)`
- `NOT AVAILABLE` — plug not available for this output
- `DISABLED FOR HDCP REASON`
- `FORMAT NOT SUPPORTED` — plug disabled because the format isn't supported on it
- `NO DISPLAY DETECTED`
- `CONNECTION FAILED`

Check the status page rather than assuming every connector on an output is hot for a given raster.

---

## 4. Native I/O

### Inputs (§1.4) — 7 inputs + 1 audio line in

| Plug | Ceiling |
|---|---|
| DisplayPort | **4K@30Hz** |
| HDMI (rear) | **4K@30Hz** |
| SDI | 3G Level A & B |
| Universal Analog (HD-15) | — |
| DVI Dual-Link | 2560×1600@60Hz |
| Video Optical SFP cage | — |
| HDMI (front, input #7) | 2K / 1080p |
| 3.5 mm jack | stereo audio in |

**The native DisplayPort and HDMI inputs top out at 4K@30.** 4K@60 ingest requires an expansion card. This is an easy trap when speccing a 4K60 source.

### Outputs (§1.5) — 1 standard output, 6 plugs + headphone

| Plug | Ceiling |
|---|---|
| DisplayPort | 4K@30Hz |
| HDMI | 4K@30Hz |
| SDI | 6G Level A & B |
| Universal Analog (HD-15) | — |
| DVI Dual-Link | 2560×1600@60Hz |
| Video Optical SFP cage | — |

DVI, HDMI and HD-15 output plugs are also available as **video loop-through** (§1.3, §1.5).

---

## 5. Expansion cards

### Video (max 2 installed)

| Ref | Direction | Connectivity | Ceiling |
|---|---|---|---|
| `OPT-OUT-VIO4K` | **Output only** | Dual-Link DVI, DisplayPort, HDMI, Optical, component, 6G-SDI | 4K@30 4:4:4 10-bit |
| `OPT-4K60P-VIO4K` | I/O | DisplayPort 1.2, HDMI 2.0 | UHD/4K@60 4:4:4 |
| `OPT-4K60P-SDI-VIO4K` | I/O | DP 1.2, HDMI 2.0, 12G-SDI, 12G-SFP, Quad-Link 3G-SDI | UHD/4K@60 4:4:4 |

Card interface details (§15.2.2, §15.2.3):

- **HDMI 2.0** — up to 18 Gbps; UHD/4K@60 4:4:4 8-bit, or 2560×1440@60 4:4:4 10-bit, or 2560×1440@120 4:4:4 8-bit. HDCP 1.4 and 2.2. RGB444, YCbCr BT.601/709/2020.
- **DisplayPort 1.2** — up to 21.6 Gbps; UHD/4K@60 4:4:4 10-bit. HDCP 1.3. RGB444, YCbCr BT.601/709.
- **Quad 3G-SDI** — four quadrants or SMPTE 425-5; usable as input *or* output; up to 2160p60 4:2:2 10-bit. This is **one signal across four cables**, not four feeds.
- **12G-SDI and 12G-SFP** — usable as input *or* output; up to 2160p60 4:2:2 10-bit.

Direction on the SDI connectors is selectable per connector, so committing one to output removes it from the input pool.

`OPT-4K60P-VIO4K` has **no SDI at all** — DP 1.2 and HDMI 2.0 only. If a build needs three SDI feeds on copper, the third needs an external converter.

### Audio (max 1 installed) (§15.1)

| Ref | Provides |
|---|---|
| `OPT-AUDIODANTE-VIO4K` | 8 bidirectional Dante channels, full network redundancy over GigE; 44.1 / 48 / 96 kHz |
| `OPT-AUDIOXLR-VIO4K` | S/PDIF and AES3 in (4 channels / 2 stereo pairs); AES/EBU & i3D Digital Audio (XLR); Analog Stereo Balanced (XLR) |

### Card inputs

Each 4K60P card contributes one input. The framelock reference list (§6.4) enumerates `INPUT OPT 1` and `INPUT OPT 2` alongside the seven native inputs plus `INPUT GENLOCK`.

### DisplayPort standard setting (§7.5.2.9)

On expansion cards only, DP defaults to 1.2; selectable to 1.1 for compatibility with 1.1 sources. Menu: INPUTS → optional input → DisplayPort Settings → DisplayPort Standard.

---

## 6. Output format support by plug

### Native output (§6.2)

| Plug | Formats | Standards / signals |
|---|---|---|
| Universal Analog (HD-15) | SDTV, EDTV, HDTV, Computer | YCbCr BT.601 / BT.709; RGBHV, RGBs, RGsB |
| DVI-D Dual-Link | EDTV upward | YCbCr BT.601; RGB Full (0-255) / Limited (16-235) |
| HDMI 1.4a | SDTV → UHDTV/4K **up to 30Hz** | YCbCr BT.601/709; RGB Full / Limited |
| DisplayPort 1.2 | SDTV → UHDTV/4K **up to 30Hz** | YCbCr BT.601/709; RGB Full / Limited |
| 3G-SDI | SDTV, HDTV | SMPTE 259M-C; ST296 (720p); 274M (1080i/1080p); ST2048 (2K) |
| 6G-SDI | UHDTV/4K **up to 30Hz** | SMPTE ST2036; ST2048 — BT.709 **and BT.2020** 4:2:2 |
| Optical SFP (NMSA) | SDTV, HDTV, UHDTV/4K up to 30Hz | same standards as 3G/6G rows |

### Expansion outputs (§6.2.1)

| Plug | Formats | Signals |
|---|---|---|
| HDMI 2.0 | UHDTV/4K **up to 60Hz** | YCbCr BT.601/709/2020; RGB Full / Limited |
| DisplayPort 1.2 | UHDTV/4K **up to 60Hz** | YCbCr BT.601/709/2020; RGB Full / Limited |
| 12G-SDI | UHDTV/4K **up to 60Hz** | SMPTE ST2036; ST2048 — BT.709 / BT.2020 4:2:2 |
| Optical SFP (NMSA) | UHDTV/4K up to 60Hz | same |

### What 6G-SDI buys over 3G, practically

Three things and no more:

1. 3840×2160 up to 30 Hz
2. 4096×2160 (DCI) up to 30 Hz
3. BT.2020 colorimetry on the 4K entries — the 3G row lists only BT.601/709

It opens **no intermediate rasters**. SDI is standards-locked; there is no 2560×1440, no 2560×1600, no arbitrary LED-shaped raster. The jump is 2K/1080p tier → 2160-line tier, nothing between.

> ⚠️ **Manual labelling oddity.** The 6G and 12G rows tag `ST2036` as "(2K…)" and `ST2048` as "(4K…)". SMPTE ST 2036-1 is the UHDTV standard (3840×2160) and ST 2048-1 is the DCI 2K/4K standard (2048×1080 / 4096×2160), so the parentheticals appear transposed. Read the row as UHD + DCI 4K and confirm against the unit's selectable format list.

### Colour standard tip (§15.2.3)

With a 4K60P card fitted the VIO can send/receive UHDTV using **BT.2020** rather than the BT.709 used for HDTV formats. Set the internal processing colour standard deliberately to avoid pointless colour-space conversions.

---

## 7. Screens, AOI and the canvas model

### AOI is an output-side crop (§6.4.4)

> "The Area of Interest (AOI) defines the active area of your display in the output format. The AOI can be thought of as your screen: anything positioned outside the AOI will be ignored in the processing, and only the AOI content will be displayed to the spectator."

- `Fit Format Resolution` / `Fit to Output's Active Area` checkbox auto-fits AOI to the output raster; uncheck for manual control
- Manual parameters: **H Position, H Size, V Position, V Size**, all in pixels
- Enabling/disabling auto-fit does **not** erase manual AOI settings
- Web RCS has an AOI finder with draggable handles
- `AOI Raster Box` displays a dotted outline around the AOI area
- Output patterns can be set to fit the AOI

This is why an odd LED raster (say 2112×1152) is carried as an **active island inside a standard raster** (3840×2160) over SDI — SDI cannot carry a non-standard raster, but AOI lets you place and size the real active area inside a legal one.

### Screens (§9.1, §15.3)

- A screen is "the video content that will be displayed to the spectator"
- Each installed video card adds a screen; two cards ⇒ **three screens and three output resources**
- A screen is enabled as soon as it has at least one output resource assigned
- Outputs are drag-and-dropped between screens; all outputs can be assigned to one screen, disabling the others
- With an output assigned to a screen, the **Clone** checkbox displays the entire screen scaled to that output's resolution

### Screen sizing and windowing (§15.3.1)

- **Auto** — screen size computed from the max area required to display all AOIs (H and V positions of the AOIs feed the computation)
- **Custom** — screen size set manually in pixels
- In both modes, **an output's AOI can be moved anywhere inside the screen but not outside it**
- A screen pattern (crosshatch, circles, tile borders, IDs) assists multi-output positioning

**What is documented as independent per output: AOI and rotation** (§15.3). Output rotation is 90° / 180° / 270°, per output (§1.3).

### Pitch compensation (§15.3.2)

For LED walls mixing tile pitches within one screen. Reference screen pitch = 100%; other pitches expressed as a percentage of it. Manual's worked example: an 8000×2000 wall with Standard Output 4000×2000 and Option 1 Output 3000×1500 → reference pitch is the standard output, compensation ratio **133.3%** on the Option 1 output. Set via OUTPUTS → Screen Management → Output Assignment → Screen n Settings (Size Mode CUSTOM, H/V Size) → Option n Output Configuration (H/V Position, H/V Pitch Ratio).

### The "view" is a property of the input, not the screen (§7.5.4, §9.2)

> "The view of an input allows you to control how the input is displayed in the screen." Pan and zoom to size and position the input in the screen; mask to display only a section; view alpha for transparency.

- Units selectable **PERCENT** or **PIXELS** — the same units are then used for masking
- Pan H / Pan V position the input from the **centre** of the screen
- Zoom H / Zoom V resize it; `Zoom H/V` locks aspect
- Pan/Zoom Templates: `1:1`, `CENTERED`, `FULLSCREEN`, `CROPPED` — note the manual's warning that fill templates force the view to adapt to the screen and may scale or deform it
- Reset Pan/Zoom clears all
- View banks store and recall views per input

Separately, input-side **Cropping** (§7.5.3) offers Crop Top/Bottom/Left/Right plus predefined crops and a Crop Finder, with Display Aspect Ratio correction applied *after* crop. Overscan compensation crops 11% H and V on SDTV, 5% on HDTV.

> ⚠️ **Open design question — see §10.** Because the view lives under INPUTS and there is only one active input, it is not established that pan/zoom/mask can differ per screen. The documented per-output independence is AOI and rotation only.

---

## 8. Custom formats (§11)

- Custom formats are explicitly **computer formats**, layered on the CVT 1.1 and DMT 1.0 standards the VIO supports by default
- **64 bank slots**; empty slots shown black, occupied blue in the Web RCS
- Two edit modes:
  - **CVT** — set width, height, rate, and reduced-blanking flag; remaining parameters computed to CVT 1.1
  - **Full** — set H/V front porch, sync, back porch, active, and sync polarities individually
- `Load from Template` pulls parameters from a predefined output format; `Load from Custom Format Bank` from an existing custom format
- A **Check** step validates before save and returns H Total, V Total, Pixel Frequency (Hz), Line Frequency (kHz), or one of these errors:
  - `PIXEL FREQUENCY TOO HIGH`
  - `PIXEL FREQUENCY TOO LOW`
  - `LINE FREQUENCY TOO HIGH`
  - `TOTAL PIXEL PER LINE IS TOO LOW`

**Custom formats do not apply to SDI.** They are computer formats — DP / HDMI / DVI / HD-15 territory. For an odd raster over SDI, use AOI inside a legal raster instead (§7 above).

The widest raster in the documented format list is **4096** pixels. Anything wider is unverified territory — build it in CVT mode and let **Check** decide.

---

## 9. Sync, framelock, genlock

- Genlock: Analog HD Black and Black Burst, **loopthrough**; all genlock timings meet broadcast ITU/SMPTE standards (§1.3)
- Output format modes (§6.3): `INTERNAL REF.`, `AUTO EDID FORMAT`, `FRAMELOCK`, `GENLOCK`
- **All inputs can be used as framelock reference** (§6.4). Available references: `INPUT 1` DisplayPort, `INPUT 2` HDMI rear, `INPUT 3` HD-15, `INPUT 4` Optical, `INPUT 5` SDI, `INPUT 6` DVI-D, `INPUT 7` HDMI front, `INPUT OPT 1`, `INPUT OPT 2`, `INPUT GENLOCK`
- Framelock rate modes: `MODE x0.5`, `MODE x1`, `MODE x2`. **Restriction: "Input Reference Rate × Rate Factor" must be ≥ 23.97 Hz and ≤ 120 Hz**
- Framelock Tune offers Offset H (pixels, ratio of 1 line) and Offset V (lines, ratio of 1 frame) on the output signal

Because all outputs derive from one internal reference, feeds to separate downstream processors are frame-coherent with each other — but each downstream device still has to genlock to its input rather than free-run.

---

## 10. Open items — not settled by this manual

Flagged honestly rather than filled in. Each of these is a bench test.

1. **Per-screen views.** Whether the input's pan/zoom/mask can differ per screen when two or three screens exist. Determines whether the box can deliver independently-scaled crops or only AOI windows onto one shared canvas. **This is the highest-value test.**
2. **Simultaneous input and output on one card.** §1.3 claims up to 9 inputs *and* 3 outputs, and the framelock list exposes `INPUT OPT 1/2`, which implies yes. But no passage states directly that a single card runs an input and an output at the same time. On the SDI card the per-connector direction choice is the real limiter regardless.
3. **Input count discrepancy.** §1.3 says up to 9 inputs (7 native + 2). §7.1 says up to 8 (6 native + 2). The framelock list enumerates 7 native. Unresolved in the document; verify against the unit's own input list.
4. **Quad-Link 3G behaviour at non-2160p rasters.** Undocumented whether those four BNCs emit anything usable when the output raster is 1080p. Do not plan a redundancy leg around it untested.
5. **Sub-30Hz rate options per SDI plug.** The tables state only "up to 30Hz" / "up to 60Hz"; individual rates (23.976 / 24 / 25 / 29.97 / 30) are not enumerated per plug.
6. **Rasters wider than 4096.** Whether the custom-format engine gates H active independently of pixel clock. See `pixel-clock-and-link-bandwidth.md` for the clock-budget reasoning that motivates the question.

---

## 11. Design patterns worth remembering

**Three feeds, mixed transports.** DP 4K60 in on `OPT-4K60P-VIO4K` → 12G-SDI 2160p60 out of `OPT-4K60P-SDI-VIO4K` → 3G-SDI 1080p60 out of the native output. No direction conflicts, no plug contention, each feed on its own output resource. The third card slot's output is HDMI/DP only.

**Odd LED raster over SDI.** Set a legal raster (3840×2160 or 1920×1080), then AOI the real active area inside it (2112×1152, 1536×960). The downstream LED processor windows the island. Costs bandwidth, but it is the only way to get a non-standard active area down an SDI link.

**Redundancy without spending an output.** All plugs on one output carry identical content — take 12G-SDI to the wall and HDMI 2.0 to a confidence monitor or backup path from the same output resource.

**No copper SDI redundancy on the SDI card if optical is ruled out.** Without the 12G-SFP, the card's only single-cable SDI output is the 12G-SDI BNC; Quad-Link is one signal on four cables. A backup copper leg needs an external DA, or accept HDMI for the backup.

**4K60 has exactly one path.** Native output caps at 4K@30 on every plug. Any 60 Hz 2160-line output must come off a 4K60P card.

---

## 12. Input numbering and the compositing stack

Added 2026-07-23. Both were previously implicit in the section tables; stated explicitly here because they are what a patch drawing and a show-file build actually need.

### Input numbering (§6.4 framelock reference list, corroborated by the §12 audio-source list)

| # | Plug | Physical | Version / ceiling |
|---|---|---|---|
| 1 | DisplayPort | DP, rear | DP 1.2, 4K@30 |
| 2 | HDMI | HDMI Type A, rear | HDMI 1.4, 4K@30 |
| 3 | Universal Analog | HD-15, rear | — |
| 4 | Video Optical | SFP cage, rear | 3G-SDI |
| 5 | SDI | BNC, rear | **3G only** (Level A & B) |
| 6 | DVI Dual-Link | DVI-D DL, rear | 2560×1600@60 |
| 7 | HDMI | HDMI Type A, **front panel** | 2K / 1080p |
| OPT 1 | option card slot 1 | — | per card |
| OPT 2 | option card slot 2 | — | per card |

`INPUT GENLOCK` also appears in the framelock list — reference only, not a video source. Analog HD Black / Black Burst with loopthrough.

⚠️ **The menu numbering is not the order §1.4 prints the plugs in.** §1.4 lists DP, HDMI, SDI, Universal Analog, DVI, Optical, front HDMI. The numbered order is DP, HDMI, HD-15, Optical, SDI, DVI-D, front HDMI. Use the numbered order for control work and patch drawings.

⚠️ **The native SDI input is 3G; the native SDI output is 3G/6G.** The asymmetry is easy to miss — there is no 4K path into the built-in SDI at any rate. Confirmed by the §7.2 input format table, whose SDI columns are headed 3G-SDI and 3G-SDI SFP Slot with no 6G column.

### Input plug versions (§7.2 table headers)

DisplayPort 1.2 · HDMI 1.4 · 3G-SDI · 3G-SDI SFP Slot · Dual-Link DVI-D · HD-15.

Note the output side is HDMI **1.4a** (§6.2) against HDMI **1.4** on the input — as printed in the source. Whether that reflects a real difference or loose editing is not established.

The `DisplayPort Standard` setting (DEFAULT = 1.2 / 1.1 for legacy sources) is documented as **expansion interfaces only** (§7.5.2.9). The built-in DP has no such control.

### The compositing stack

Bottom to top:

1. **Screen background colour** — customizable per screen (§9.1). The front-panel `BLACK` button and the Web RCS `CLEAR` button both output it.
2. **One live input** — the single active source, carrying its full view: pan, zoom, mask, flip, **alpha/transparency** (§7.5.4, reset value 255), colour effects.
3. **Quick Frame** — a still displayed in the screen **foreground** (§8.6).

Background-plus-layer is achievable by zooming the input's view below screen size; the background colour fills the remainder, and view alpha can blend the input against it.

What is **not** available: a still or second source *behind* a live layer. §8.1 lists frame uses as capture, foreground quick-frame, transitions, and "display a background when no input source is selected (black frame)" — that last case applies only when **no** input is selected. There is no second video layer.

⚠️ **Parsing note on §8.6.** The sentence reads: *"display a frame in the screen foreground, for example to cover underneath layers in case of emergency."* "Underneath" modifies "layers" — i.e. cover the layers beneath it. The Quick Frame is **on top**. The §9.4 restatement drops "in the screen foreground" and is genuinely ambiguous in isolation; §8.6 is the governing text. The plural "layers" is Analog Way house phrasing carried from their layered products (Ascender, NeXtage) and does not indicate multiple live layers on the VIO.

### Frames (§1.6, §8.1–8.2)

- 24-bit RGB still, maximum 8192×4320
- BMP, JPEG, PNG
- Up to 50 frame memories, fully resizable; memory space for 2 uncompressed 4K frames
- Import/export via USB key (front-panel USB HOST) or Web RCS → Setup → LIBRARY
- Capture from live inputs or outputs
- `Fade Through Frame` transition uses preset frames PF1/PF2 with adjustable duration

---

## 13. Verification status

| Claim area | Tier | Source |
|---|---|---|
| Chassis, slot counts, weight (§2) | **Verified** | VIO 4K Manual §1.2, §15 `[Official]` |
| Output = group of plugs (§3) | **Verified** | Manual §6.1 `[Official]` |
| SDI Level A/B as mapping scheme (§3) | **Verified** | Manual §7.5.2 `[Official]` |
| Plug status enumeration (§3) | **Verified** | Manual §6.3 `[Official]` |
| Native input list and ceilings (§4) | **Verified** | Manual §1.4, §7.2 `[Official]` |
| Native output list and ceilings (§4) | **Verified** | Manual §1.5, §6.2 `[Official]` |
| Option card refs, connectivity, ceilings (§5) | **Verified** | Manual §15.1, §15.2.2, §15.2.3 `[Official]` |
| Per-plug output format tables (§6) | **Verified** | Manual §6.2, §6.2.1 `[Official]` |
| 6G-SDI adds UHD + DCI 4K at ≤30 Hz and BT.2020 only (§6) | **Verified** | Manual §6.2 `[Official]` |
| ST2036/ST2048 labels appear transposed (§6) | **Lead** | Reasoning against SMPTE ST 2036-1 / ST 2048-1 scope; **neither standard read** |
| AOI definition and parameters (§7) | **Verified** | Manual §6.4.4 `[Official]` |
| Screen model, sizing modes, Clone (§7) | **Verified** | Manual §9.1, §15.3, §15.3.1 `[Official]` |
| Pitch compensation incl. 133.3% worked example (§7) | **Verified** | Manual §15.3.2 `[Official]` |
| View parameters and menu location (§7) | **Verified** | Manual §7.5.4, §9.2 `[Official]` |
| Custom formats, 64 slots, Check error strings (§8) | **Verified** | Manual §11 `[Official]` |
| Custom formats do not apply to SDI (§8) | **Verified** | Manual §11.1 — defined as computer formats on CVT 1.1 / DMT 1.0 `[Official]` |
| Framelock references and rate restriction (§9) | **Verified** | Manual §6.3, §6.4 `[Official]` |
| Input numbering 1–7 (§12) | **Verified** | Manual §6.4 framelock list, corroborated §12 audio-source list `[Official]` |
| Input plug versions (§12) | **Verified** | Manual §7.2 table headers `[Official]` |
| Native SDI in = 3G, out = 3G/6G (§12) | **Verified** | Manual §7.2 vs §6.2 `[Official]` |
| Compositing stack and Quick Frame position (§12) | **Verified** | Manual §8.1, §8.6, §9.1, §9.4 `[Official]` |
| Frame specs and formats (§12) | **Verified** | Manual §1.6, §8.1, §8.2 `[Official]` |
| HDMI 1.4 in vs 1.4a out is a real difference (§12) | **Open** | As printed in the source; not established either way |
| Design patterns (§11) | **Working practice** | Derived from the Verified rows above; not doc-sourced as recommendations |

**No figure in this document is Memory tier.** Every number was read from the manual in session. Where the manual is silent, §10 says so rather than filling the gap.

### Not yet verified — open items

Restated from §10 so this table is self-contained. All are bench tests against the actual unit and firmware:

1. **Per-screen views** — whether pan/zoom/mask can differ per screen. Highest value; determines independently-scaled crops vs AOI windows on one canvas.
2. **Simultaneous input and output on one option card** — implied by the 9-in/3-out claim and the `INPUT OPT 1/2` framelock entries, never stated.
3. **Input count** — the manual contradicts itself: §1.3 says 9, §7.1 says 8, the framelock list enumerates 7 native + 2 option. §7.2's format table shows only 6 native plug columns (no front HDMI). Four figures, no reconciliation in the source.
4. **Quad-Link 3G at non-2160p rasters** — undocumented.
5. **Sub-30 Hz rate options per SDI plug** — tables state only "up to 30Hz" / "up to 60Hz".
6. **Rasters wider than 4096** — whether the custom-format engine gates H active independently of pixel clock.
7. **PNG alpha on a foreground Quick Frame** — frames are specified as 24-bit RGB, which implies no alpha channel, but the manual does not state whether an alpha channel in a PNG is honoured or discarded. Relevant to any keyed logo bug.
8. **HDCP versions on the built-in plugs** — §7.5.2.6 states DVI/HDMI/DP inputs are HDCP-compliant but gives no version. The cards specify HDCP 1.4/2.2 on HDMI 2.0 and 1.3 on DP 1.2; the native plugs have no equivalent statement.
