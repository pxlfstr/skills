# creative-coding — Reference Library Index

Manifest of stored code notes and working patterns. Read this first when the skill is active.

**This skill is private.** It must never be committed to `https://github.com/pxlfstr/skills`.
See `STORAGE.md`.

**Everything here is ours, not documented behavior.** Every pattern carries a confidence tier —
Shipped / Bench-verified / Designed / Abandoned. An unmarked pattern is Designed. Vendor and
protocol facts are *not* stored here; they live in `digital-video` and are cited across.

Maintenance is **additive and never lossy** — merge rather than replace, keep abandoned approaches
with their reasons, never silently promote a tier.

---

## Documents

### `touchdesigner-arena-sequencer.md`
**Added:** 2026-07-19
**Project:** Arena Sequencer — column sequencer for Resolume Arena 7, TD + browser UI. Started 2026-05-01.
**Covers:** Three-tier architecture (TD owns clock/state/triggers, browser is dumb, Resolume receives only); Web Server DAT + Execute DAT frame-driven clock; `arena-state.json` persistence; QR onboarding via `qrcode` in TD's Python; **`resId` column identity and the default-`Column N` name trap**; external trigger detection two ways (`selected` + 1.5 s self-trigger window; 1 s composition poll + state diff); console introspection as the debugging method.
**Highest tier present:** Bench-verified. Nothing confirmed show-run.
**Abandoned/unresolved:** WebSocket dropping immediately after subscribe — never root-caused; `Origin` header fix did not work.
**Depends on `digital-video` for:** Resolume REST/WebSocket API behavior — endpoints, `by-id` addressing, structural-change push semantics, webserver port and enablement. **This reference does not exist in the public repo yet** and should be written there.
**Provenance caveat:** reconstructed from session records, not from source. Original file set (`arena_sequencer.py`, `arena_web_callbacks.py`, `index.html`, `readme.txt`) not in hand.

---

## Queue — patterns identified, not yet written up

Material from past sessions that belongs here but hasn't been captured. Ordered roughly by value.

| Project | What it covers | Notes |
|---|---|---|
| TouchDesigner PTZ control surface | Joystick CHOP focus-gating problem and the XInput-in-Script-CHOP workaround; GameSir G7 Pro specifics; table-driven mapping architecture (function-kinds, per-camera state, AF/AI coupling, wrap-select, camera registry); expression-pedal speed scaling; 40 ms throttle; digest-auth AW sender | Existed as a written doc, lost with the container. Highest-value recovery. |
| Multi-controller integration | Division of labor between Companion, RP-150, TD and PTZ Control Center to avoid command collisions; Companion→OSC→TD relay for cross-controller preset awareness | Existed as a written doc, lost. **Split needed** — the connectionless-vs-notification/5-slot distinction is a vendor fact and belongs in `digital-video`; only the division-of-labor architecture belongs here. |
| X-Touch Compact → TouchDesigner | `LayerA.bin` binary preset decode (91 records, 7 blocks) and the decoded CSV; MIDI In CHOP over MIDI In Map CHOP rationale; Table DAT + Rename CHOP naming pattern; capture-ground-truth-via-MIDI-In-DAT workflow | The 1-based index offset is a TD fact → `digital-video`. The decode and the workflow are ours. Block 7 unidentified. |
| Companion + Resolume layer count | `generic-websocket` build; `length(jsonparse(...))` extraction; `layers.length` shortcut untested; abandoned `getVariable()` / `clip_name_l{}_c{}` approach | Includes an upstream bug to file against `bitfocus/companion-module-resolume-arena`. Strip rig detail before filing. |
| Standalone tools | BNC router crosspoint HTML panel — Preview/Program/Take state model, conflict detection, drag-to-reorder; intended OSC bridge to an Evertz Quartz 3232N | Older; confirm still relevant before writing up. |

## Queue — belongs in `digital-video`, surfaced from coding sessions

Not for this skill. Listed so the split doesn't get lost.

- Resolume REST/WebSocket API reference (endpoints, `by-id` addressing, structural-change push, OSC's inability to query structure).
- Panasonic AW protocol / UE150 / RP150 device documentation.
- TouchDesigner MIDI In DAT 1-based index behavior.
- Companion Panasonic module landscape (which module to use, subscription slot limits).
