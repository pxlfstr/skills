# digital-video — Reference Library Index

Manifest of stored reference documents. Read this first when the skill is active.

Maintenance is **additive and never lossy** — merge rather than replace, keep correct detail a newer source happens to omit, remove only what is shown to be *wrong*. Full protocol in `STORAGE.md`.

**Sibling skill:** `creative-coding` holds code and working patterns and cites *into* this library for vendor and protocol facts. Facts live here; patterns live there. Never duplicate a vendor fact across the two.

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
**Covers:** Analog Way VIO 4K multi-format converter/scaler. The canvas-and-window architecture and why the device is **not** a switcher — one source at a time, and three outputs means three framings of the *same* source. The load-bearing **output ≠ connector** distinction (an output is a group of plugs delivering identical content; one output resource per option card; ceiling of three independent rasters). Why "SDI (6G Level A & B)" is one BNC and not two ports. Per-plug status values and why a connector on an active output can still be dark. Native I/O tables; the five expansion cards and the max-three-installed rule; output format support per plug; AOI as an output-side crop; screens, windowing and pitch compensation; the "view" as a property of the input rather than the screen; custom formats; sync, framelock and genlock.

**Use for:** specifying or troubleshooting a VIO 4K; working out whether a proposed routing is physically possible on it; any question where someone has assumed connector count equals output count.

**Confidence:** Sections 1–9 **Verified** — read directly from the *VIO 4K User Manual / Programmer's Guide* `[Official]`, user-supplied PDF, read in full. Section numbers cited throughout. No figure remembered or estimated.

**Open items:** listed in the document's own §10.

---

### `pixel-clock-and-link-bandwidth.md`
**Added:** 2026-07-19
**Covers:** A working method for deciding whether an arbitrary raster fits down HDMI, DisplayPort or SDI *before* building it. Keeps three rates strictly separate — active information rate, pixel clock, and link/wire rate — and explains why quoting the first understates the requirement by 5–20% depending on blanking. The **CVT-RB v1 timing model** with constants and procedure (160-pixel H blank, 460 µs minimum V blank, clock quantised down to 0.25 MHz). Interface ceiling table for HDMI 2.0, DP 1.2 HBR2, and 3G/6G/12G-SDI, with the derivation showing that the **TMDS character rate, not the wire rate, is the binding HDMI 2.0 constraint**. A worked 5120×2880@30 4:4:4 example, a reference table of common rasters, reproduction instructions, and rules of thumb.

**Use for:** bandwidth budgeting; defining a custom format on a scaler; answering "will this fit down that cable" with arithmetic rather than a guess.

**Confidence:** Three-tier scheme applied strictly in place — **Computed** (arithmetic done this session, reproducible from the stated formulas, not a manufacturer figure), **Verified**, **Unverified**. Note the document flags its own HDMI 2.0 600 MHz character-rate ceiling as needing an HDMI Forum source before being quoted to a client.

**Related:** the CVT-RB assumption is chosen because the VIO 4K's custom-format engine builds on CVT 1.1 — see `analog-way-vio-4k.md` §8.

---

### `panasonic-ptz-sources.md`
**Added:** 2026-07-19
**Covers:** AW-UE150 / AW-HE145 / AW-RP150 **source registry** — verified official URLs for the interface specification, operating manuals, spec pages, Ver 2.00 guide and FAQs, plus the Panasonic manual portal. Then a separate section of facts *actually read*: the two distinct command types (pan/tilt head vs. camera control) and their STX/ETX framing; HTTP-over-TCP as host protocol with RS-422 for serial; the **40 ms inter-command gap required for pan/tilt commands**; the update-notification mechanism for multi-terminal control; RP150 capacity (200 cameras over IP, 5 over serial, mixed); Ver 2.00 additions with menu paths (ROP linkage, AV-HS6000 switcher link, TMEM bulk delete, CAMSEL OP, iris limit, preset name editing, I.ZOOM assignment); and the RP150↔UE150 setup gotcha where IP control silently fails until user registration is completed on the camera via a browser.

**Use for:** any AW-protocol or RP150 question — but **read the linked source first**. This is a registry with a partial extraction, not a full one.

**Confidence:** All URLs `[Official]` and confirmed. Facts under "Facts read this session" are **Verified**; everything else in those documents is **unextracted** and must not be answered from memory.

**Note for `creative-coding`:** the 40 ms throttle in the TouchDesigner PTZ control surface originates here — it is a documented protocol requirement, not a tuned constant.

**Open items:** listed in the document's own "Not yet extracted" section.

---

### `behringer-x-touch-compact.md`
**Added:** 2026-07-19
**Covers:** Behringer X-Touch Compact control surface — hardware spec table; USB vs. stand-alone routing behavior; MC-mode entry procedure; **complete factory MIDI maps for Preset Layer A and Layer B** (encoder turn/push, three button grids, fader move and fader touch, transport, foot jacks); MC-mode assignment; and the **receive-side map** for driving motors, encoder LED rings, button LEDs and status LEDs back from software. Plus bench-derived integration notes for Resolume and TouchDesigner, and a decode of the Layer A `.bin` preset format.

**Use for:** any question about mapping this surface into Resolume, TouchDesigner, a DAW, or custom code; working out which CC or Note a given control emits; building feedback so motors and LEDs re-seat; deciding Standard vs. MC mode.

**Confidence:** §1–§5 **Verified** from the *X-Touch Compact Quick Start Guide V 6.0* `[Official]`, read directly. §6–§7 are **Lead / bench-derived** and labelled as such in place.

**Open items:** RX button-LED numbering under Layer B (manual shows fixed notes 0–38 with no per-layer variant — untested); the `0x12` prefix block in the preset file; where per-control MIDI channel is stored; whether the Resolume Speed-fader feedback gap is a vendor bug.

---

### `resolume-control-interfaces.md`
**Added:** 2026-07-19
**Covers:** Resolume Arena/Avenue 7.x external control — default ports (OSC 7000, REST/web server 8080, OSC-out listener 7001); how OSC addresses are discovered rather than published; absolute vs. relative addressing and Type Tags; the `connect` vs. `connected` distinction; enabling and using the REST API where the running instance serves its own version-correct reference; the split of capability between OSC and REST (transport vs. feedback) and why a control system usually needs both; MIDI feedback requirements; Resolume Wire OSC input.

**Use for:** wiring anything external to Resolume — Companion, TouchDesigner, TouchOSC, a control surface, or custom code — and for working out which interface can actually carry a given action or piece of feedback.

**Confidence:** Ports and interface behavior **Verified** `[Official]` from Resolume support pages and the Bitfocus module documentation. `connect`/`connected` semantics and the deck-switch emission are **Lead** `[Forum]` (Resolume forum, developer participating) and flagged in place.

**Open items:** full `/composition/...` namespace from an official source; whether the deck-switch `0` is documented or a bug; per-version REST endpoint list (pull from the local web server reference page).
