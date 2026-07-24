# Reference Library — Index

Manifest of stored reference documents for the `digital-video` skill.
Read this first in every session to know what is available.

Maintenance is **additive and non-lossy** — see `STORAGE.md`.

**Seven documents stored.** A prior index revision listed only one; the other
six were present in `references/` but unlisted, and therefore invisible to any
session that trusted this file. Restored 2026-07-23 from the documents
themselves and from `archive/INDEX.md`. Nothing was removed.

---

## Documents

| Document | Covers | Tier summary | Stored |
|---|---|---|---|
| `analog-way-vio-4k.md` | Analog Way VIO 4K converter/scaler. The output-as-group-of-plugs model and why output count ≠ connector count; SDI "Level A & B" as an ST 425 mapping scheme, not two ports; native I/O ceilings (DP and HDMI both cap at 4K@30; native SDI **in** is 3G-only while **out** is 6G); all five option cards; per-plug format tables for native and expansion outputs; what 6G-SDI adds over 3G and what it does not; the screen/AOI canvas model, screen sizing, AOI windowing, pitch compensation; the input "view" (pan/zoom/mask/alpha/crop) and its menu location; the compositing stack (background colour → one live input → foreground Quick Frame); custom formats (CVT 1.1 / DMT 1.0, 64 slots, Check validator error strings, computer-formats-only so no SDI path); framelock/genlock references and the 23.97–120 Hz rate restriction; input numbering 1–7 + OPT 1/2 | **Verified [Official]** throughout §1–§9 — *VIO 4K User Manual / Programmer's Guide*, user-supplied PDF read in full. No remembered or estimated figures. §10 lists six unresolved items, incl. a self-contradiction in the source's own input count | 2026-07-19, rev. 2026-07-23 |
| `behringer-x-touch-compact.md` | Behringer X-Touch Compact device facts: hardware table (encoders, buttons, faders, foot jacks, USB hub, power, dimensions), USB vs stand-alone routing behaviour, MC/Standard mode switching, status LEDs, complete factory MIDI maps for Layer A and Layer B, the receive-side (feedback) map, and a reverse-engineered decode of the Layer A `.bin` preset format | §1–§5 **Verified [Official]** — *X-Touch Compact Quick Start Guide, V 6.0* (Music Tribe) read directly. §7 `.bin` decode is **Lead** — reverse-engineered from a 723-byte export, no format spec | 2026-07-20 |
| `behringer-xtouch-compact-resolume.md` | X-Touch Compact as a Resolume (Avenue/Arena) control surface: Standard vs MC mode selection and why Standard is required, X-Touch Editor settings, full TX Note/CC maps for layers A/B, the RX/LED feedback map and why button LEDs ignore a naive note echo (§4a), Resolume MIDI In/Out config, Layer A/B banking, CC127 on-the-fly mode toggle | Mode procedure, TX maps, RX/LED map + velocity gate, and Resolume MIDI docs **Verified [Official]** (manual read first-hand). Fader-touch CC collision and the Layer Speed feedback gap remain **Leads [Forum]**. Contains an explicit correction notice for a prior over-stated claim about note echo lighting LEDs | 2026-07-18, rev. 2026-07-20 |
| `film-projection-geometry-and-light.md` | Film gate dimensions (IMAX 15/70, 70mm 5-perf, 35mm scope and flat); camera-side lens coverage as a constraint on usable aspect ratio; projection lens focal-length families (Isco UltraStar HD, Schneider Super-Cinelux / Cinelux-Première) and derived throw ratios; SMPTE 196M / SMPTE 431-1 screen luminance targets and the Harkness lumens-vs-screen-width table; flux density at the film plane and the thermal ceiling on gate illumination; cross-gauge magnification asymmetry running 35mm and 70mm to one screen width. **Filed here rather than `analog-video` deliberately** — the subject is photochemical but the reasoning is the throw-ratio / foot-lambert / magnification math shared with digital projector specification | Mostly **Lead**. No standards document was purchased or read; ISO 2467:2004, SMPTE 196M and SMPTE PH22.106 were identified but not obtained. The Harkness/ICTA deck is the strongest source present. §5 (thermal ceiling) is mechanism-only with **no sourced number**, flagged in place. §7 exhibition context is explicitly perishable | 2026-07-18 |
| `panasonic-ptz-sources.md` | Panasonic PTZ source registry for the festival rig — AW-UE150 / AW-HE145 / AW-RP150. Confirmed URLs for interface specifications, operating manuals, spec pages and FAQs, plus the facts actually read: the two-command-set structure (pan/tilt head vs camera control), STX/ETX framing, HTTP-over-TCP and RS-422 control paths, the **40 ms inter-command gap** that is the documented origin of the TD control surface's throttle, the update-notification mechanism, RP150 camera-count ceilings, and Ver 2.00 ROP/switcher linkage menu paths | **Source registry, not a full extraction.** URLs **Verified [Official]**, confirmed 2026-07-19. Only the facts under "Facts read this session" are Verified; the PDFs were not read end to end. Anything else must be pulled from the linked document — explicitly not answerable from memory | 2026-07-19 |
| `pixel-clock-and-link-bandwidth.md` | Method for deciding whether an arbitrary raster fits down HDMI, DisplayPort or SDI. Separation of active information rate, pixel clock and link/wire rate; the CVT-RB v1 timing procedure (160 px H blanking, 460 µs minimum V blanking, 0.25 MHz clock quantisation); HDMI character rate vs wire rate and why character rate is the binding constraint; DP 1.2 HBR2 payload after 8b/10b; SDI tier table; worked example at 5120×2880@30 across 8/10/12-bit; comparison table of common rasters with DP 1.2 utilisation; reproducible Python | **Computed** for all clocks and bandwidths — arithmetic performed in session from the stated CVT-RB model, reproducible from the included code. Explicitly **not** manufacturer figures. Interface ceilings marked **Unverified** in place: consistent with the VIO manual's card descriptions (18 Gbps HDMI 2.0, 21.6 Gbps DP 1.2) but no HDMI Forum or VESA document was read. The 600 MHz HDMI 2.0 character-rate limit must not be quoted to a client until sourced | 2026-07-19, rev. 2026-07-23 |
| `resolume-control-interfaces.md` | Vendor-documented control surfaces for Resolume Arena/Avenue/Wire: default ports (OSC 7000 in, 7001 out to Companion, REST 8080), the discover-don't-look-up OSC address method and Type Tags, absolute vs relative addressing, the `connect` (trigger) vs `connected` (state) distinction, REST web-server enablement and the self-hosted API reference, MIDI learn-by-mapping and the Input+Output requirement for feedback surfaces, Wire OSC setup. **Integration patterns deliberately excluded** — those live in `creative-coding/references/resolume-companion-glue.md` | Ports, OSC method, REST behaviour and Wire setup **Verified [Official]** (Resolume Support, Bitfocus module README, TouchOSC manual). Fixed-input-address claim, listening-interface behaviour and the deck-switch `0` emission are **Leads [Forum]** from the Resolume forum — the last includes a Resolume developer in-thread but is still not a spec. Scoped to Resolume 7.x; version drift expected | not dated in-document |

---

## Cross-references

- `analog-way-vio-4k.md` ↔ `pixel-clock-and-link-bandwidth.md` — the VIO's open question about rasters wider than 4096 is answered on the clock-budget side in the bandwidth doc.
- `behringer-x-touch-compact.md` ↔ `behringer-xtouch-compact-resolume.md` — device facts and factory maps in the first, Resolume-specific application and failure modes in the second.
- `resolume-control-interfaces.md` → `behringer-x-touch-compact.md` §6 for device-specific MIDI mapping notes.
- `panasonic-ptz-sources.md` is depended on by `creative-coding/references/` for AW protocol facts. **Protocol facts live here, code lives there — do not duplicate.**

---

## Gaps / wanted documents

Material that would strengthen the library if the user has it:

- ~~X-Touch Compact Quick Start Guide, per-control MIDI maps~~ — **supplied
  2026-07-20**, folded in; TX maps, RX/LED map, and CC127 mode toggle now
  Verified.
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
- **Novastar H2 and VX1000 documentation** — currently no LED-processor document
  in the library at all, despite LED processing being a named pillar of the
  skill. Wanted for downstream-of-VIO signal chain work.
- Analog Way firmware release notes for the VIO 4K — would settle the input-count
  contradiction (§1.3 vs §7.1) and confirm whether one option card can run an
  input and an output simultaneously.
