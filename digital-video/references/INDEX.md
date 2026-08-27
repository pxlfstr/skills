# Reference Library — Index

Manifest of stored reference documents for the `digital-video` skill.
Read this first in every session to know what is available.

Maintenance is **additive and non-lossy** — see `STORAGE.md`.

**Eight documents stored.**

⚠️ **Boundary revision, 2026-08-01.** Four documents moved to
`creative-coding/references/` when the skill boundary was redrawn from
"facts here, code there" to "video signal and devices here, control protocols
and software there":

| Moved document | Now at |
|---|---|
| `touchdesigner-resolume-operators.md` | `creative-coding/references/` |
| `resolume-control-interfaces.md` | `creative-coding/references/` |
| `behringer-x-touch-compact.md` | `creative-coding/references/` |
| `behringer-xtouch-compact-resolume.md` | `creative-coding/references/` |

**Nothing was deleted** — this is a move, and the receiving index lists all four.
Do not recreate them here. See `SKILL.md` for the boundary test.

A prior index revision listed only one document; six others were present but
unlisted, and therefore invisible to any session that trusted this file.
Restored 2026-07-23. `atem-supersource.md` added 2026-07-28.

---

## Documents

| Document | Covers | Tier summary | Stored |
|---|---|---|---|
| `analog-way-vio-4k.md` | Analog Way VIO 4K converter/scaler. The output-as-group-of-plugs model and why output count ≠ connector count; SDI "Level A & B" as an ST 425 mapping scheme, not two ports; native I/O ceilings (DP and HDMI both cap at 4K@30; native SDI **in** is 3G-only while **out** is 6G); all five option cards; per-plug format tables for native and expansion outputs; what 6G-SDI adds over 3G and what it does not; the screen/AOI canvas model, screen sizing, AOI windowing, pitch compensation; the input "view" (pan/zoom/mask/alpha/crop) and its menu location; the compositing stack (background colour → one live input → foreground Quick Frame); custom formats (CVT 1.1 / DMT 1.0, 64 slots, Check validator error strings, computer-formats-only so no SDI path); framelock/genlock references and the 23.97–120 Hz rate restriction; input numbering 1–7 + OPT 1/2 | **Verified [Official]** throughout §1–§9 — *VIO 4K User Manual / Programmer's Guide*, user-supplied PDF read in full. No remembered or estimated figures. §10 lists six unresolved items, incl. a self-contradiction in the source's own input count | 2026-07-19, rev. 2026-07-23 |
| `atem-supersource.md` | Blackmagic ATEM SuperSource: per-model SuperSource counts; the four-box model and box source options; the complete ATEM Software Control palette inventory (Presets/Art/Copy) and the Advanced Panel menu-page equivalents; every numeric value readable from the manual screenshots and a switcher's own saved state (quad preset **X -8.00 / Y 4.80 / Size 0.50**, border defaults 0.40 on all six widths, hue 0° / sat 0% / lum 100%, art clip 50% / gain 70%); a **derived** 32 × 18 unit space with the px-per-unit table and conversion formulas for HD/UHD/DCI, including the quad preset's 0.30-unit top and bottom overflow; the complete SDK interface and method inventory; **the two distinct border models** (`SuperSourceBorder`, bevelled and SuperSource-wide, vs `SuperSourceBoxBorder`, flat and per-box) and the `SupportsBorder` capability query; the SDK/palette/XML naming drift table; the `<SuperSources>` saved-state schema with its encoding traps (0–1 vs 0–100 scales for border saturation and luma, per-box border elements under a single palette control) | §1–§3, §5–§6 **Verified [Official]** — *ATEM Constellation Switchers Manual* pp. 68–70 and *Blackmagic Switchers SDK* §6 read directly, plus a switcher's own state export; border and art values corroborated across two independent sources. §4 unit space and all pixel conversion is **Derived** — arithmetic from one verified preset, internally consistent, never checked against a switcher. Preset 1–3 shapes are **Lead** (low-resolution thumbnail). **§5.3 records a verified negative: the SDK declares every SuperSource parameter as a bare double with no units, minima, maxima or defaults, and the manual gives no end-stops either** | 2026-07-28 |
| `christie-spyder-x20.md` | Christie / Vista Systems Spyder X20 — **scoped to X20 only; the 200/300 series it replaced has been removed from this document.** **End of production 2024-01-02, supported to 2027-01-02.** Model numbering and the two named X20 chassis (1608, 0808); the VI as the central capacity budget — **20 million pixels at every frame rate on X20**, frame rate does not trade against VI size — plus the tallest-height × summed-widths budgeting rule and the 2400 px VI height ceiling with its 1860 px still/shape restriction on layers 3, 6, 11, 14; layers as 1:1 with input cards and fixed hardware Z-order; X20 connectors by input parity (odd = analog/**composite/S-Video (confirmed standard, brochure)**/3G-SDI BNC, even = DVI-I/stereo sync) and DVI-I + SDI on every output, **with composite/S-Video confirmed absent on outputs (brochure)**; **per-output-channel exclusivity, corrected 2026-08-27: DVI digital and SDI cannot run simultaneously (verified on hardware), and DVI digital and analog cannot either — they are alternate uses of the same DVI-I connector's pin sets, not simultaneous paths; whether SDI + analog runs together is ⚠️ unverified — the manual names it as an example but no X20-specific source or observation confirms it**; dual-link rules — capable layers 1/4/7/9/12/15, the adjacent layer consumed, the preceding analog input disabled, three pairs on 0808 and six on 1608, odd outputs only; HDCP 1.4 as a licensed system-wide repeater mode that kills every analog and SDI **output** and forces single link, with the 127-device / 7-level tree and the DDC-reliability failure modes; serial vs discreet vs seamless expansion, restricted and unrestricted layers, cumulative licensing across a chain; physical, power and the 13–15 s forced-off data-loss warning; Vista Advanced install, the hard-coded `C:\SPYDER` path, broadcast-network practice and the adapter-metric fix; key modes, KeyFrame relative coordinate space, borders, shadows, clones, EDID and License managers; SourceMaster machine control; the X20-only Still Server and its OpMon capture path; output Normal/OpMon/Scaled modes, rotation, blending; the 4.x software line and the 4.1.0 upgrade procedure; the manufacturer spec table | **Verified [Official]** throughout — *Spyder X20 User Manual* 020-000916-01 Rev. 1 (04-2016), user-supplied PDF read end to end. X20 input counts **Derived** from the dual-link layer table; **output counts Inferred from the model name only and must not be quoted**. VI budgeting formula **Derived** from the manual's own worked example and checks exactly. **Revised three times on 2026-08-10, and again 2026-08-27.** Now built on seven sources: the manual, **all nine 4.x release notes read in full (4.0.0 through 4.1.0, no gaps)**, the **SSO manual**, Christie's **product page spec table**, the **product brochure**, and **two Christie chassis photographs**. Six open items closed — **output count Verified at 8**, latency **under 1.5 interlaced frames**, output sync **free-run or vertically referenced to NTSC/PAL black burst**, **output DVI pixel clock 265 MHz against 330 MHz on inputs**, **SDI Level B on inputs added in 4.0.4**, a **genlock BNC confirmed on the output board**, **USB confirmed as a real expansion path** (4.0.7 added USB redundancy for expanded systems), and the **front panel confirmed as where the running software version and IP are read**. **§12 is the whole 4.x software history** — release timeline, signal and hardware changes, the HDCP fix trail, a dozen stereo bug fixes, the router-protocol inventory and the upgrade procedure. §13 is the spec table with **three unresolved manual-vs-spec-page conflicts** (power, weight, output clock) kept side by side. **§8 now carries the observed rear- and front-panel layouts** — including that the **odd/even dual-link split is silkscreened on the outputs** (`Dual DVI-I` vs `DVI-I`), so it is readable at the back of a rack. **§11.2 documents `SourceMon`, the X20's built-in input multiviewer** — confirmed as an output mode from a running 4.1.0 client and described in no Christie document at all. §14 lists twenty open items (the 200/300 dual-table contradiction closed 2026-08-27 when that series left the document; the composite/S-Video output question, briefly open the same day after user pushback, was resolved and closed within hours once the user supplied the product brochure — see below; one item remains from that day's work: whether SDI + analog actually run simultaneously on X20), headed by **an undocumented `Colocate` command on the simulator's screen right-click menu** — reported from a live client, present in no Christie document anywhere, with a one-minute `RPD` test written out to settle it — then **three conflicting power figures: 1000 W manual, 900 W product page, and 12.0 A on the chassis nameplate** — plus **two power supply modules that no Christie document describes as redundant**. Christie never revised the manual for the 4.x line, so §9–§11 stay 3.x-era-unless-§12-says-otherwise. ⚠️ **This manual's "SSO halves VI capacity" line is contradicted by the SSO manual** — see the stereoscopic document before sizing any stereo job. **200/300-series content (2 RU/4-I/O and 3 RU/8-I/O chassis families, sample model numbers, the 200C/300C composite option, and the duplicate 200/300 VI table) removed 2026-08-27 at user request — the X20 fact that depended on knowing 200/300 existed (the 4.0.1 fix for 200/300 steppings bleeding into X20) was kept and reworded to stand alone. The other X20 fact this removal had depended on — that composite doesn't exist on X20 because Comp/S-Vid is a 200/300-only option card — was disputed by the user the same day, briefly marked unresolved, then settled hours later by the user-supplied product brochure: composite/S-Video is confirmed standard on X20 inputs (half the connectors on both chassis) and confirmed absent from the X20 output signal list** | 2026-08-10, rev. 2026-08-27 |
| `christie-spyder-x20-stereoscopic.md` | The Christie Spyder X20 stereoscopic (SSO) option. The three modes — **active** (one connection, interleaved eyes, separate sync, rate doubled), **passive** (two connections, sync-locked, standard rates) and **Mirage HD / SSO2** (projector does the frame doubling); the VESA miniDIN-3 sync pinout; the **two-canvas VI model at 20 M pixels per eye** and the two places it contradicts the main manual; active input ceilings by rate (DVI 317 MHz, analog 165 MHz, **nothing above 2048 × 1200 regardless of refresh**) and the DVI-I-only rule for active sources; passive inputs at 2048 × 1200 @ 60 including HD-SDI; the full active-output resolution table by odd/even connector, where **120 Hz active works on odd digital outputs only**; the **output-7 rule** — one shared 3-pin DIN per output board, its rate locked to output 7, split downstream, and feed the IR emitter from the display not the X20; passive outputs on any connector at 2048 × 1200 @ 60 using two output modules; the configuration path end to end, including **stereo modes being global**, **autosync silently reverting stereo mode to Off**, `StereoInvertEyes`, and the four output Mode values the control protocol does not document; SSO licensing | **Verified [Official]** throughout — *Spyder X20 User Manual (stereoscopic)* 020-000875-01 Rev. 1 (04-2016), user-supplied PDF read end to end. **Two contradictions with the main manual recorded and deliberately unresolved** — VI capacity under stereo (20 M per eye vs "halved") and which layers a stereo source may use. The back-panel connector list including **genlock** is read from a figure, marked in place. §10 lists ten open items. ⚠️ **Parallel stereo is explicitly out of scope of the source**, and nothing here has been tested on hardware | 2026-08-10 |
| `christie-spyder-open-questions.md` | **A test plan, not a reference** — every Spyder question that is undocumented, self-contradicted between Christie's own documents, or reasoning never checked against hardware. Six **contradictions** including the stereo VI capacity gap (10 M vs 40 M, a factor of four in system sizing) and three conflicting power figures (1000 W / 900 W / 12.0 A nameplate); twelve **undocumented features** including `Colocate` on the simulator's right-click menu, the `SourceMon` multiviewer, `SourceConfig`, the `Op Mon Input` capture path, the Single/Dual/Mixer device types, the `Morph` checkbox, `SpyderRouter`, genlock behaviour and "USB expansion"; the **protocol unknowns** — arguments for all eight 4.x commands, the undocumented 1400-byte response ceiling and its unstated response code, and the five-to-eight output modes of which `OCM` documents three; **signal-path questions** — crosspoint blocking, connector-switch behaviour, which BNC carries composite, SD-SDI output reliability, NTSC active raster, audio pass-through; **hardware** — the 0808→1608 card add and its firmware-vintage risk, live PSU swap, post-2027 parts. Ends with a **corrections log** of five wrong assertions and why each happened, and a **test plan ordered by value per minute** | ⚠️ **Nothing in this file is Verified — that is the point.** Each item is tiered **Contradiction**, **Undocumented** or **Theory**. **No Spyder hardware was available**: not one command sent, not one menu opened, every test proposed and none performed. Compiled 2026-08-12 from the four Christie documents, product page and brochure, two chassis photographs, three client screenshots and June 2009 trade press | 2026-08-12 |
| `film-projection-geometry-and-light.md` | Film gate dimensions (IMAX 15/70, 70mm 5-perf, 35mm scope and flat); camera-side lens coverage as a constraint on usable aspect ratio; projection lens focal-length families (Isco UltraStar HD, Schneider Super-Cinelux / Cinelux-Première) and derived throw ratios; SMPTE 196M / SMPTE 431-1 screen luminance targets and the Harkness lumens-vs-screen-width table; flux density at the film plane and the thermal ceiling on gate illumination; cross-gauge magnification asymmetry running 35mm and 70mm to one screen width. **Filed here rather than `analog-video` deliberately** — the subject is photochemical but the reasoning is the throw-ratio / foot-lambert / magnification math shared with digital projector specification | Mostly **Lead**. No standards document was purchased or read; ISO 2467:2004, SMPTE 196M and SMPTE PH22.106 were identified but not obtained. The Harkness/ICTA deck is the strongest source present. §5 (thermal ceiling) is mechanism-only with **no sourced number**, flagged in place. §7 exhibition context is explicitly perishable | 2026-07-18 |
| `panasonic-ptz-sources.md` | Panasonic PTZ source registry for the festival rig — AW-UE150 / AW-HE145 / AW-RP150. Confirmed URLs for interface specifications, operating manuals, spec pages and FAQs, plus the facts actually read: the two-command-set structure (pan/tilt head vs camera control), STX/ETX framing, HTTP-over-TCP and RS-422 control paths, the **40 ms inter-command gap** that is the documented origin of the TD control surface's throttle, the update-notification mechanism, RP150 camera-count ceilings, and Ver 2.00 ROP/switcher linkage menu paths | **Source registry, not a full extraction.** URLs **Verified [Official]**, confirmed 2026-07-19. Only the facts under "Facts read this session" are Verified; the PDFs were not read end to end. Anything else must be pulled from the linked document — explicitly not answerable from memory | 2026-07-19 |
| `pixel-clock-and-link-bandwidth.md` | Method for deciding whether an arbitrary raster fits down HDMI, DisplayPort or SDI. Separation of active information rate, pixel clock and link/wire rate; the CVT-RB v1 timing procedure (160 px H blanking, 460 µs minimum V blanking, 0.25 MHz clock quantisation); HDMI character rate vs wire rate and why character rate is the binding constraint; DP 1.2 HBR2 payload after 8b/10b; SDI tier table; worked example at 5120×2880@30 across 8/10/12-bit; comparison table of common rasters with DP 1.2 utilisation; reproducible Python | **Computed** for all clocks and bandwidths — arithmetic performed in session from the stated CVT-RB model, reproducible from the included code. Explicitly **not** manufacturer figures. Interface ceilings marked **Unverified** in place: consistent with the VIO manual's card descriptions (18 Gbps HDMI 2.0, 21.6 Gbps DP 1.2) but no HDMI Forum or VESA document was read. The 600 MHz HDMI 2.0 character-rate limit must not be quoted to a client until sourced | 2026-07-19, rev. 2026-07-23 |

---

## Cross-references

- `analog-way-vio-4k.md` ↔ `pixel-clock-and-link-bandwidth.md` — the VIO's open question about rasters wider than 4096 is answered on the clock-budget side in the bandwidth doc.
- `behringer-x-touch-compact.md` ↔ `behringer-xtouch-compact-resolume.md` — device facts and factory maps in the first, Resolume-specific application and failure modes in the second.
- `resolume-control-interfaces.md` → `behringer-x-touch-compact.md` §6 for device-specific MIDI mapping notes.
- `touchdesigner-resolume-operators.md` ↔ `resolume-control-interfaces.md` — the same protocols from both ends: what Resolume exposes, and which TD operator speaks it. Read together when designing a control hub.
- `touchdesigner-resolume-operators.md` → `creative-coding/references/touchdesigner-integration.md` for Web Client DAT, OSC and MIDI operator detail, and to `behringer-xtouch-compact-resolume.md` for the bench-confirmed MIDI In DAT callback and index offset. **Note:** that creative-coding file currently holds an operator-selection table that is arguably a vendor fact belonging here — flagged, not moved.
- `panasonic-ptz-sources.md` is depended on by `creative-coding/references/` for AW protocol facts. **Protocol facts live here, code lives there — do not duplicate.**
- `christie-spyder-open-questions.md` is the **inverse index of the other three Spyder documents** — they state what is known, it collects what is not. **Read it before quoting a Spyder figure to a client**, since several headline numbers (stereo VI capacity, power draw, output pixel clock) are contradicted between Christie's own sources. Answers found on hardware get promoted into the reference documents and struck from there.
- `christie-spyder-x20.md` ↔ `christie-spyder-x20-stereoscopic.md` — two different Christie manuals with the same cover title. Device, VI and connector facts in the first; everything that changes under stereo in the second. **They contradict each other on stereo VI capacity and on which layers a stereo source may use** — both records are kept, neither is resolved. The genlock connector is confirmed only in the stereoscopic document's figure.
- `christie-spyder-x20-stereoscopic.md` → `creative-coding/references/protocols/christie-spyder-external-control.md` §5e — the stereo output modes (`PassiveLeft`, `PassiveRight`, `ActiveStereo`, `Source`) exist in the Vista Advanced dropdown and **have no documented `OCM` equivalent.** Read together before promising a client stereo control from an external system.
- `christie-spyder-x20.md` §12 ↔ `christie-spyder-external-control.md` §8 — the same release notes read from two sides: signal and hardware changes there, command-set changes here. **Neither restates the other.**
- `christie-spyder-x20.md` ↔ `creative-coding/references/protocols/christie-spyder-external-control.md` — same manual, split by the 2026-08-01 boundary. Device, VI capacity, HDCP and connector facts here; the ASCII command set, UDP framing, register model and layer-alignment IDs there. **Several ranges in the protocol document (border −255–255, zoom 0.0–20.0, crop 0.0–1.0, shadow 0–255) are the only stated end-stops for those controls anywhere in the manual** — the feature chapters give none.
- `atem-supersource.md` is depended on by `creative-coding/references/atem-supersource-simulator.md` for the unit space, parameter names and XML schema. Same split: the numbers live here, the tool and the method live there.

---

## Gaps / wanted documents

Material that would strengthen the library if the user has it:

- ~~X-Touch Compact Quick Start Guide, per-control MIDI maps~~ — **supplied
  2026-07-20**, folded in; TX maps, RX/LED map, and CC127 mode toggle now
  Verified.
- ~~REST endpoint list for the version in use~~ — **OpenAPI spec supplied 2026-08-01**,
  all 295 operations folded into `resolume-control-interfaces.md` Appendix A. Still worth
  re-confirming against the local web server's reference page, since the supplied spec
  carries no product version.
- Pro DJ Link and StageLinQ sync pages — listed in the protocol inventory but not read.
- Resolume Advanced Output / slices / screens — confirmed unreachable from every protocol,
  but no reference document exists for the feature itself.
- **HDMI 2.0 and DisplayPort 1.2 specifications**, read directly — would promote
  the interface ceilings in `pixel-clock-and-link-bandwidth.md` from Unverified
  to Verified, and settle the 600 MHz character-rate limit.
- **VESA DisplayPort 1.4 / DSC material** — needed before the bandwidth doc can
  cover HBR3 or compressed links at all.
- Resolume version-specific release notes touching MIDI feedback behaviour —
  specifically whether shortcut Range/Invert affects the *output* value, which
  determines if the Editor-renumber LED workaround is viable without a
  translator.
- X-Touch Editor documentation — whether fader-touch CC output can be disabled
  outright, and where the global MIDI channel is set.
- Panasonic AW protocol command tables, read end to end — the registry names
  what is missing (`#O0`/`#O1`, `#RER`, `#INS`, `q[nn]` queries, `man_session`,
  the 5-terminal notification limit) but the PDFs have not been extracted.
- ISO 2467:2004, SMPTE 196M — would promote the film-projection gate and
  luminance rows from Lead to Verified.
- ~~Spyder Advanced 4.1.0 documentation~~ — **supplied 2026-08-10**, folded in. 4.1.0 is final.
- ~~Spyder X20 datasheet~~ — **product page spec table read 2026-08-10**, folded in as §13.
- ~~Release notes for 4.0.0–4.0.6~~ — **fetched and read in full 2026-08-10**; they are cumulative,
  so four documents covered eight releases.
- ~~Spyder X20 SSO manual, 020-000875-01~~ — **supplied and read 2026-08-10**, now its own document.
- ~~Spyder X20 v4.0.7 release notes, 020-000917-01~~ — **supplied and read 2026-08-10.** The 4.x
  history is complete.
- **Argument documentation for the eight commands 4.x added** — `AIR`, `RRD`, `RIF`, `RSCC`,
  `RSEC`, `RSCD`, `ASC`, `OCC`. The release notes name them and give no arguments at all. **Either a
  Christie 4.x protocol addendum, or a session with the UDP Console Simulator in Vista Advanced,
  would settle the highest-value gap in the protocol document.**
- **The 4.x response code for messages past the 1400-byte ceiling** — its value and how the
  retrieval option is requested. Until it is known, the response-code table is incomplete.
- **Spyder X20 operator's manual** (front-panel operation) — **now the largest single gap.** The
  panel's layout is photographed and its labels transcribed (`Home` / `Config` / `Health` / `T/L` /
  `B/R` / `Auto` / `Undo-Cancel` / `Save-Ok`, plus `CKey` / `FKey` / `Lock` soft keys), but
  **nothing about what any of it does** is documented anywhere in the library.
- **A bench answer on X20 power** — whether the two supply modules are redundant, and which of
  1000 W / 900 W / 12.0 A is rated vs typical. One pulled cord settles the first.
- **Spyder X20 operator's manual** (front-panel operation) — the user manual explicitly defers to
  it and it has not been supplied.
- **Novastar H2 and VX1000 documentation** — currently no LED-processor document
  in the library at all, despite LED processing being a named pillar of the
  skill. Wanted for downstream-of-VIO signal chain work.
- Analog Way firmware release notes for the VIO 4K — would settle the input-count
  contradiction (§1.3 vs §7.1) and confirm whether one option card can run an
  input and an output simultaneously.
- **ATEM SuperSource control ranges, read off a switcher** — X, Y, Size, crop and
  border-width end-stops. Neither the manual nor the SDK states any of them, so
  the whole §4 conversion in `atem-supersource.md` rests on a single published
  preset. This is the highest-value missing measurement in the library.
- **ATEM Ethernet protocol description** for the SuperSource command family — a
  wire-level document would almost certainly settle both the unit space and the
  value ranges, since wire encodings have to be bounded.
- **ATEM Software Control / ATEM Setup documentation**, if it exists separately
  from the switcher manual — may state ranges the switcher manual omits.
- **A measured answer to what ATEM crop actually means** — whether it is in the
  same unit space and whether it scales with box size. The test is in
  `atem-supersource.md` §8 item 2 and takes under a minute on a live switcher.
