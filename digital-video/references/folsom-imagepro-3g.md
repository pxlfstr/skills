## Provenance

**Verified [Official]** — *ImagePRO-3G product datasheet*, Barco, "Last updated: 09 Jul 2024," user-supplied PDF, read in full (3 pp.). This is a short marketing/spec datasheet, not a full operator's manual — same tier as the ImagePRO-HD datasheet already in this library (`folsom-imagepro-hd.md`), not the same tier as that document's primary source (the 121-page full manual). **No full ImagePRO-3G manual has been supplied or read.** Barco's own datasheet states the product is **end-of-life** (superseded by "ImagePRO-II," per the datasheet's own text) — this is a discontinued product being documented for reference against existing/used hardware, not a currently-sold item.

**⚠️ Port-count note, corrected in place.** An earlier pass through this datasheet misread the spec table's output connector list — treating each signal-type mention ("RGB or component... on five BNC," "composite video on BNC," etc.) as a separate output, arriving at 6 and flagging a false contradiction with the datasheet's own prose ("four video outputs"). **The correct count, per the user:** inputs = 3 universal (HD-15, 5×BNC, DVI-I) + 1 SDI = **4**, matching the table's stated "Number of inputs: 4" directly. Outputs = 2 universal output paths (HD-15; the 5-BNC bank, one flexible group carrying RGB/component/composite depending on selection, not five separate outputs) + 1 SDI + 1 S-video = **4**. The datasheet's own "Number of outputs: 6" line in the spec table does not match this count either — that line is now the open discrepancy, not the prose. Prose and physical-connector-group counting agree at 4/4; the table's own summary line ("6") is the outlier.

---

## 1. What it is

Barco's description, direct from the datasheet: "a high-performance video scaler, scan converter, switcher and transcoder all rolled into one." Same Athena-scaler lineage as ImagePRO/-SDI/-HD (see `folsom-imagepro-hd.md`) — this datasheet doesn't name "Athena" explicitly in what was extracted, but does state the feature set matches (motion-adaptive + field-to-frame de-interlacing, 3:2/2:2 pulldown detection, 10-bit processing) point-for-point with the HD-generation datasheet's Athena-branded description.

**Positioned as the generation above ImagePRO-HD** — adds 3G-SDI (HD tops out at SD/HD-SDI only, per `folsom-imagepro-hd.md` §1) and WUXGA support, on the same fundamental chassis concept.

## 2. Video input

| | |
|---|---|
| Number of inputs | **4** — 3 universal (HD-15, 5×BNC, DVI-I) + 1 SDI. Matches both the spec table's stated total and the datasheet's own prose once counted correctly — see Provenance note |
| Universal inputs | (3) high-bandwidth channels: RGBHV/RGBS/RGsB, component (SD or HDTV), S-video, or composite, with loop-through |
| Connectors | Input 2 on 15-pin HD (loop-through). Input 3 on five BNC (loop-through). **Input 1 on DVI-I** (analog or digital, loop-through) — same DVI-I-as-Input-1 pattern as ImagePRO-HD |
| SDI input | **(1) 3G/HD/SD-SDI on BNC** — this is the headline upgrade over ImagePRO-HD, which has no 3G-SDI at all (`folsom-imagepro-hd.md` confirms "no 3G-SDI... on any variant" for that document's scope) |
| Resolution range | VGA (640×480), SVGA (800×600), XGA (1024×768), SXGA (1280×1204 — *sic*, datasheet's own typo for 1280×1024), UXGA (1600×1200), **WUXGA (1920×1200)**, HDTV 480p/720p/1080p/1080i, 875 RS-343, 525 RS-170. **WUXGA is new relative to ImagePRO-HD's input list, which tops out at UXGA** |
| Horizontal frequency | 15 kHz–120 kHz |
| Vertical frequency | 25 Hz–120 Hz |
| Input termination | 75 Ohm |
| Input sync | Sync-on-Video, Separate C or H/V |
| **External sync (genlock) input** | **Blackburst, Computer H/V Sync, or C-sync.** Same as every other ImagePro variant checked this session — **no tri-level listed as an input reference type**, despite tri-level being supported on output (see §3) |

## 3. Video output

| | |
|---|---|
| Number of outputs | **4**, by physical output path — HD-15 + the 5-BNC bank (one flexible group, not 5 separate outputs) + SDI + S-video. **The spec table's own summary line states "6," which doesn't match this count** — see Provenance note |
| Connectors | RGB or component (SD or HDTV) on HD-15; RGB/component/composite on five BNC; composite on BNC; S-video on 4-pin mini-DIN; **3G/HD/SD-SDI on BNC**; **DVI output on DVI-D** |
| Standard-res output | NTSC, PAL |
| High-res output | VGA, SVGA, XGA, SXGA, UXGA, **WUXGA (1920×1200)**. Plasma-specific 1280×768, 1365×768, 1365×1024. HDTV 480p/720p/1080p/1080i. 875 RS-343, 525 RS-170. User-definable formats supported |
| **Sync** | RGBHV, RGBS, RGsB, TTL level, polarity selectable, HDTV. **Tri-level Sync supported.** 75 ohm output impedance |

**The tri-level-sync line is output-side only, per this table's structure** — it appears under "Video outputs → Sync," not under the input/genlock row in §2. This is consistent with the pattern already established across every ImagePro-family document this session: tri-level is something these devices can *produce* on output, not something they accept as an external genlock *reference*. Worth being precise about this distinction — it directly resolves the "does the 3G take tri-level as a reference input" question raised earlier in this conversation: **per this datasheet, no** — genlock input is Blackburst/H-V/C-sync only, same as every other variant.

## 4. What this datasheet does not cover

- No mention of MAD de-interlacing delay figures in field counts (the headline fact in `folsom-imagepro-hd.md` §6) — this datasheet doesn't restate them. Presumed similar or better given "3G" generally implies a later/more capable processing generation, but **this is not stated anywhere in this document** and should not be assumed without a source.
- No DVI-I pixel clock or dual-link statement — same gap as ImagePRO-HD.
- No genlock-type-tier detail (V Lock / HV Lock / HVSc Lock, as documented for -HD) — this datasheet only lists "Genlock, H/V lock and Vlock" as a bullet feature, no mechanics.
- No full operator's manual has been read for this specific model — everything here comes from a 3-page datasheet.

## 5. Upgrades over ImagePRO-HD, confirmed vs. assumed

Direct comparison against `folsom-imagepro-hd.md`, assuming both documents' connector/feature lists are otherwise complete — i.e. anything not called out below as different is the same across both generations.

| | ImagePRO-HD | ImagePRO-3G | Genuine change? |
|---|---|---|---|
| SDI generation | SD/HD-SDI only, no 3G-SDI | **3G/HD/SD-SDI**, both directions | **Yes — the headline upgrade** |
| Max resolution | UXGA (1600×1200) ceiling, input and standard output | **WUXGA (1920×1200)** added, both directions | **Yes** |
| S-video output | Present (inherited from base ImagePRO) | Present | **No — already existed line-wide, not a 3G addition** |
| Input 1 (DVI-I), Inputs 2–3 (HD-15, 5×BNC) | Same | Same | **No change** |
| Output connector set (HD-15, 5×BNC, composite BNC, S-video, DVI-D) | Same | Same | **No change** |
| Genlock input type | Blackburst/H-V/C-sync | Blackburst/H-V/C-sync | **No change** |
| Tri-level sync (output) | Not mentioned in HD's datasheet either way | Explicitly stated, output-only | **Possible addition, or just an HD documentation gap** — HD's datasheet doesn't state tri-level is *absent*, only that it's unmentioned. Not confirmed as a true spec difference |
| Genlock mechanics (V/HV/HVSc Lock tiers) | Fully detailed, from the full HD manual | Not detailed at all — 3G has no full manual sourced | Not a spec change — a documentation-depth gap, since HD's detail comes from a manual and 3G's source is datasheet-only |

**Net: two confirmed upgrades (3G-SDI, WUXGA), one uncertain (tri-level sync may or may not be new), nothing else changed.** The tri-level line is the one worth treating cautiously — it's the kind of spec a thin datasheet might simply omit on one generation without it being a true absence, unlike SDI generation and resolution ceiling, which are both stated unambiguously as different on both sides.

## 6. Teranex 3D comparison

Cross-manufacturer comparison against `blackmagic-teranex.md`. **Caveat worth stating first:** the Teranex document's own §5 records that the physical unit examined in that context does not match Blackmagic's documented Teranex 3D on several points (SDI generation, port count, power redundancy) — so this comparison is against the *documented* Teranex 3D, not necessarily against that specific physical unit.

| | **ImagePRO-3G** | **Teranex 3D (as documented)** |
|---|---|---|
| Max SDI | 3G/HD/SD-SDI | 3G-SDI |
| Channel handling | Not detailed in the 3G datasheet — no equivalent statement to Teranex's single/dual-link explanation found | Confirmed single-channel: A/B pair carries one signal redundantly, bandwidth-split (dual-link), or as a stereo L/R pair — never independent multi-channel |
| Analog video I/O | Yes — RGBHV/RGBS/RGsB, component (SD/HDTV), S-video, composite | Yes — component (Y/B-Y/R-Y) only. Narrower analog format support than ImagePRO-3G |
| Max resolution | WUXGA (1920×1200) | Not stated for 3D specifically in what was read |
| Genlock/reference input | Blackburst, H-V sync, or C-sync. **No tri-level accepted as input** | REF IN present; input signal type not detailed in the Teranex document |
| Tri-level sync | Output-side only, confirmed | Not confirmed either way for 3D |
| On-device scopes | Not covered by any ImagePro source — no equivalent claim found | **Confirmed absent** — Blackmagic UltraScope is external, Thunderbolt-connected, not on-device |
| Power redundancy | Not stated in the 3G datasheet | Documented 3D: redundant dual-IEC |
| Audio | Not covered in the 3G datasheet's extracted text | XLR ×2 in, ×2 out, plus dedicated XLR timecode in/out |
| Documentation depth | Datasheet only (3 pp.) — genlock mechanics, delay figures, audio I/O all absent | Full manual read — but with the unresolved real-unit mismatch noted in that document's §5 |

**The honest shape of this comparison, same as before:** ImagePRO-3G's gap is thin sourcing (a 3-page datasheet leaves audio, delay figures, and genlock mechanics all unknown). Teranex's gap is different — a thorough manual exists, but per that document's own §5, doesn't necessarily describe the specific unit in hand. Where they're genuinely comparable: both are Athena/Blackmagic-class scaler-and-converter boxes, both position SDI generation as their main tier differentiator, and both show the same tri-level-is-output-only genlock pattern (confirmed for 3G; unconfirmed but not contradicted for Teranex 3D). ImagePRO-3G has the broader analog format support (RGBHV/RGBS/RGsB vs. Teranex's component-only); Teranex 3D has the documented redundant power and dedicated timecode I/O that ImagePRO-3G's datasheet doesn't address either way.

---

## Verification status

| Claim | Status |
|---|---|
| Input/output connector types and signal support | **Verified [Official]** — datasheet spec table, read in full |
| 3G/HD/SD-SDI in and out | **Verified [Official]** — explicitly stated, both directions |
| WUXGA (1920×1200) input and output support | **Verified [Official]** |
| Tri-level sync is output-only, not a genlock input type | **Verified [Official]** — by the table's own structure (appears under output sync, absent from the input/genlock row) |
| Physical I/O count: 4 in / 4 out, by connector-group | **Verified [Official] — corrected in place.** Datasheet prose and a connector-group count agree at 4/4. The spec table's own bare summary line ("Number of outputs: 6") is now the outlier and doesn't match either count — likely counts the 5-BNC bank's signal-type options as separate outputs rather than one flexible physical group |
| Processing delay in fields (MAD mode) | **Not available in this document** |
| DVI-I pixel clock / dual-link | **Not available in this document** |
| Genlock type-tier mechanics (V/HV/HVSc Lock) | **Not available in this document** — only named as a feature, not detailed |

## Not yet verified — open items

- **The input/output count contradiction (§ Provenance) is unresolved** — would need the full ImagePRO-3G operator's manual, if one is findable for this now-discontinued product, to settle definitively.
- Processing delay figures, DVI-I pixel clock, and genlock mechanics — all absent here; would need the same kind of full manual that exists for ImagePRO-HD, not yet supplied for 3G.
- Whether "Athena" branding applies to this generation — feature set matches, but the name itself wasn't found in this specific extracted text.

## Cross-references

- `folsom-imagepro-hd.md` — same product family, one generation earlier. See §5 above for the full confirmed-vs-assumed upgrade comparison (3G-SDI and WUXGA are the two genuine changes; both are 4 in / 4 out by physical connector group, corrected in place this session).
- `blackmagic-teranex.md` — different manufacturer, same broad product category. See §6 above for the full comparison against the documented Teranex 3D, including the caveat that document's own §5 raises about the specific physical unit examined there.
