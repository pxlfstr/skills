# digital-video — Reference Library Index

Manifest of stored reference documents. Read this first when the skill is active.

Maintenance is **additive and never lossy** — merge rather than replace, keep correct detail a newer source happens to omit, remove only what is shown to be *wrong*. (Per SKILL.md; `STORAGE.md` was not present in the library when this index was created.)

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
