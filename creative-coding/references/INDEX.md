# creative-coding — Reference Library Index

Manifest of stored pattern documents. Read this first when the skill is active.

**Sibling skill:** `digital-video` holds vendor and protocol facts. This library holds code and working patterns, and cites *into* that one rather than duplicating it. If you are looking for a port number, a CC map, or a device spec, you are in the wrong library.

Maintenance is **additive and never lossy** — merge rather than replace, promote confidence tiers rather than overwriting them, keep Abandoned patterns, remove only what is shown to be *wrong*. See `STORAGE.md`.

**Confidence tiers used throughout:** Shipped (ran in a real show) · Bench-verified (tested on hardware) · Designed (reasoned, not run) · Abandoned (tried and rejected, kept deliberately).

---

## Documents

### `multi-layer-controller-led-feedback.md`
**Added:** 2026-08-01

**Covers:** Three related patterns from a control-surface + media-server integration project. (1) The TX/RX asymmetry pattern — control surfaces that expose more layers on transmit (channel-discriminated) than they can represent on receive (single LED per button, channel-agnostic), and the gate/cache/replay fix that lives upstream in software rather than in the MIDI map. (2) Splitting protocol legs by requirement instead of brokering everything through one hub — translate only where the destination can't receive the source's native protocol, and let destinations with their own multi-device feedback logic own that logic rather than re-deriving it in a broker. (3) A scoping rule for media-server control when two overlapping protocols are both available (REST/WebSocket vs. OSC): default to the structured/discoverable interface, use the second protocol only for the specific parameters the first doesn't expose, and confirm the actual gap by live diff rather than doc comparison.

**Use for:** any control-surface integration where software-side layers/banks sit on top of a receiver that doesn't natively support them; deciding whether a project needs a central broker or can split legs by protocol requirement; scoping which control protocol owns which parameters when a target app exposes more than one.

**Confidence:** Designed throughout. The TX/RX asymmetry itself is Bench-verified against one manufacturer's official documentation (not named here — generic pattern only). Nothing in this document has been built or run against real hardware/software yet.

**Open items:** whether "currently active layer" is inferable without an explicit resync mechanism on cold start; whether a native-protocol-direct leg still needs an intermediary for fan-out even without translation; a fully automated live diff between a structured API spec and a fixed-address protocol (still untried — the one worked case was resolved by reading specs, not by querying running software).

**Updated 2026-08-01:** protocol-scoping section revised after the gap was established for one real case. Adds the generalisation that the gap between a structured API and a fixed-address protocol is usually *semantics and addressing modes, not reach*, plus two sourcing lessons: a vendor's wrapper-integration limitations page can be better boundary documentation than their API reference, and those two sources can contradict each other. Vendor specifics deliberately not restated — they live in `digital-video/references/resolume-control-interfaces.md`.

---


**Added:** 2026-07-19
**Covers:** The MIDI 1.0 message model and why message type must match control type (Notes for buttons, CC for continuous); 7-bit resolution limits and the three ways around them; the 14-bit MSB/LSB pairing rule; absolute vs. relative encoders and why relative encodings must be determined empirically; feedback, state ownership, momentary-vs-toggle, echo suppression and motor re-seating; pickup/takeover strategies for non-motorized surfaces; banking and channel-as-index; the 0-based/1-based index trap and the capture-first rule; note-name convention ambiguity; MIDI clock and why it is the wrong video sync source.

**Use for:** designing any control-surface integration; deciding how to map a physical control; debugging feedback loops, stepping, or off-by-one index problems.

**Confidence:** Spec-level material is stable and safe from knowledge; the 14-bit pairing rule is `[Official]` from Derivative's documentation. Patterns are tiered in place — channel-as-index is **Shipped**, encoder and feedback behavior **Bench-verified**, takeover strategies **Designed**.

**Open items:** per-device relative-encoder encodings (empirical, always); whether echo suppression is better at the sender or via a comparison cache under many-control load.

---

### `osc-for-show-control.md`
**Added:** 2026-07-19
**Covers:** OSC message structure and how it compares to MIDI; the unspecified transport and what UDP costs you — drops, reordering, no connection — and the four design rules that follow (send state not events; idempotent triggers; heartbeat repeats; never accumulate on the receive side); address-space design when you own both ends and discovery when you don't; absolute vs. relative addressing; type tags as the first thing to check when a message does nothing; bundles and uneven time-tag support; the bidirectional two-port gotcha and listening-interface confusion; choosing between OSC, MIDI and REST; the throttle-plus-priority-chain rate limiting pattern.

**Use for:** building anything that talks OSC; deciding whether OSC is even the right protocol for a given link; debugging messages that appear to send but do nothing.

**Confidence:** Protocol structure is stable. UDP transport in TouchDesigner and the connectionless-status point are `[Official]`. Rate limiting is **Shipped**; address design is **Designed / Bench-verified**.

**Open items:** bundle time-tag support per receiver; practical minimum throttle interval (measure per device, no general figure).

---

### `touchdesigner-integration.md`
**Added:** 2026-07-19
**Covers:** Which MIDI, OSC and HTTP operators to reach for and why; MIDI In CHOP vs. MIDI In Map CHOP and when the mapper's indirection is worth it; the **capture-first workflow** (register → MIDI In DAT with Bytes Column → hand-corrected table DAT → Rename CHOP → semantic names); MIDI Out CHOP channel naming as the feedback API; the Controller Format 14-bit parameter and its diagnostic signature when mismatched; the `.toe` value-restore trap and its mitigations; the general table-driven mapping pattern and the rules that keep it maintainable; Script CHOP for devices without good native operators; outbound throttling with a priority chain and offline skip-gate.

**Use for:** any TouchDesigner control-integration build or debug; structuring a mapping so hardware changes cost one table edit.

**Confidence:** Operator behavior tagged `[Official]` is read from docs.derivative.ca and should be re-verified against the build in use. The capture-first workflow, table-driven pattern, Script CHOP approach and throttling are **Shipped**.

**Open items:** Map CHOP's value for interchangeable multi-surface setups; `.toe` restore vs. motorized refresh race; Script CHOP polling cost at high cook rates.

---

### `resolume-companion-glue.md`
**Added:** 2026-07-19
**Covers:** Choosing among Resolume's OSC/REST/MIDI interfaces by what feedback you need rather than by what control you want; discovering the OSC address space instead of hardcoding from tutorials, and the coupling that creates between a control system and composition layout; feedback as opt-in and invisible when absent; mapping a two-layer surface onto Resolume as control banks; where Bitfocus Companion earns its place and how its OSC/REST split behaves; a separation-of-concerns architecture with one state owner and independently survivable nodes.

**Use for:** wiring Resolume into a larger control system; deciding whether a job belongs in Companion or TouchDesigner; debugging a control path that works while feedback silently doesn't.

**Confidence:** Patterns are **Shipped** or **Bench-verified** and tiered in place. Underlying vendor facts are cited across to `digital-video/references/resolume-control-interfaces.md` and not restated.

**Open items:** whether the layer Speed-fader feedback gap persists in current 7.x; whether REST polling can fill OSC feedback gaps without costing frames; Companion behavior with a reachable REST endpoint and a wrong OSC port.

---

### `touchdesigner-arena-sequencer.md`
**Added:** 2026-07-19
**Covers:** A column sequencer for Resolume Arena 7 built in TouchDesigner with a browser/phone UI. The three-tier split and why the browser is deliberately dumb (TD owns clock, playhead, triggers, persistence and WebSocket broadcast; clients render and send commands, holding no authority — so multiple phones stay in sync for free with no client-side merge). TD component list: Web Server DAT with **both HTTP and WebSocket enabled**, frame-driven Execute DAT clock rather than a Timer CHOP, module Text DAT called via `mod()`. Startup ordering, and phone onboarding by printing a QR of the LAN URL to the console. **Column identity keyed off `resId` rather than index**, and the default-column-name trap that forces it. Two approaches to distinguishing our own triggers from a human's — a `selected` WebSocket message plus self-trigger timestamp, and the composition-poll-and-diff fallback that proved itself. Bugs and dead ends, including a never-root-caused WebSocket drop. A debugging technique: introspect live module state from the console rather than instrumenting and reloading.

**Use for:** any sequencer, playhead or browser-UI-over-TouchDesigner build; deciding where authority lives in a multi-client control system; the `resId` identity pattern, which generalises past this project.

**Confidence:** Tiered in place — architecture and column identity **Bench-verified** (ran end to end on the rig; no record of a show), the console-introspection habit **Shipped**, the poll-removal refactor **Designed**, the WebSocket drop **Abandoned / never root-caused**.

**⚠️ Provenance caveat, stated in the document itself:** reconstructed from session records, **not** from the source files. `arena_sequencer.py`, `arena_web_callbacks.py`, `index.html` and `readme.txt` are not in hand. Code fragments are *descriptions of what the code did*, not verified transcriptions. If the originals exist locally they supersede this document entirely.

**Open items:** the 1.5 s self-trigger window never re-tested off the original network; the 1 s composition poll superseded in principle but the refactor untried; the WebSocket drop unexplained; original source files to be recovered from local storage if they exist.

---

### `atem-supersource-simulator.md`
**Added:** 2026-07-28
**Covers:** A single-file HTML tool that reproduces the ATEM SuperSource palette and renders the composite, for building a layout and reading its numbers off before load-in. Architecture: one flat state object, render-on-change rather than a frame loop (which is what makes per-pixel keying affordable), a `syncers` array so direct manipulation and numeric fields never disagree, `bindSlider` pairing a range and a text input over one state property, and a canvas at output resolution so the PNG export is a real frame. The **border ring drawn as one path with a reverse-wound inner rectangle** to punch the hole under the nonzero fill rule, with the image clipped to the interior. Foreground keying via offscreen `getImageData` / alpha write / `putImageData`. **The assumption-surface pattern** — every unverifiable constant collected into one named block (`RANGES`, `keyAlpha()`) with its provenance stated inline, so correcting the tool later is one edit rather than an archaeology exercise. Pixel readout for arbitrary output rasters. ATEM XML import and `<SuperSources>` export.

**Use for:** planning a SuperSource layout, or converting between ATEM's unit values and pixels. More generally: **the canvas-verification method** — driving a page in headless Chrome via Playwright, calling the tool's own top-level functions through `page.evaluate()`, and sampling `getImageData` in *unit* coordinates rather than pixels so assertions stay readable. Reach for this whenever visual output has to be checked programmatically.

**Confidence:** Tiered in place. Position, size, border rendering, XML round-trip and the pixel readout are **Bench-verified** (probed numerically in headless Chrome, and matching the one preset Blackmagic published). The **crop model, the clip/gain key curve and every control range are Designed** — invented, plausible, untested. The tool has **never been compared against a real switcher's output**, which is the single test that would move most of it.

**Open items:** the side-by-side switcher comparison; the crop-model test; the key curve; the invented `RANGES`; presets 1–3 traced from a thumbnail rather than measured; stills only, no video or NDI; one SuperSource; the bevelled border model not implemented.

**Depends on `digital-video` for:** `atem-supersource.md` — the unit space, parameter names, the two border models, and the saved-state XML schema. No vendor number is restated in this document.

**A lesson worth keeping, recorded in the document:** three separate "bugs" during verification were all bad test isolation — sampling outside the canvas, sampling a point covered by an adjacent box's border, and testing a border while art was in foreground where it is correctly suppressed. Before probing a canvas: disable everything else, move the object under test off the raster edge, and write down the expected value *before* sampling.

