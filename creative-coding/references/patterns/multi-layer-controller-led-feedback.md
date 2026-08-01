# Multi-Layer Controller LED Feedback — The TX/RX Asymmetry Pattern

**Covers:** Many MIDI control surfaces expose more virtual layers/banks on transmit than they can
represent on receive. A surface with N physical buttons and 2+ selectable layers can address
2N+ distinct outgoing controls (layer discriminated by channel, or by a separate CC/Note range),
but typically has only N physical LEDs — one per button, with no per-layer memory. The receive
side is commonly **channel-agnostic ("global channel")**: an LED-driving message addresses the
lamp by Note/CC number alone, regardless of what channel it arrives on. This is not a numbering
scheme defect — it's a hardware limit. There is one lamp behind each button; no MIDI mapping
fixes an addressing gap that the receiver's firmware never implemented.

Confirmed against a specific manufacturer's official documentation for one control surface
(channel-agnostic RX table, single-LED-per-button architecture) — pattern is described generically
here since it's a common controller-design shape, not vendor-specific reasoning.

## Provenance

**Tier: Designed throughout. Nothing in this document has been built or run against hardware or software.** The single exception is the TX/RX asymmetry itself, which is **Bench-verified** against one manufacturer's official documentation — deliberately not named here, since this document is written as a generic pattern.

**Not read:** nothing was verified against running software. The protocol-scoping section was resolved by reading specifications, not by querying a live system, and says so.

**Open items, carried:**
- Whether "currently active layer" is inferable without an explicit resync mechanism on cold start.
- Whether a native-protocol-direct leg still needs an intermediary for fan-out even without translation.
- Automating the comparison between a structured API spec and a fixed-address protocol — still untried.

**A contradiction observed and kept:** a vendor's wrapper-integration limitations page contradicted their own OpenAPI spec on one object. Both sources were `[Official]`. Recorded as a sourcing lesson rather than resolved.

**Vendor specifics deliberately excluded** — they live in `protocols/resolume-control-interfaces.md`.

---

**The consequence:** if a layer switch is invisible to the host (the surface sends nothing when
the operator flips layers locally), naively relaying software-side feedback straight to the
device will show whichever layer's state was written *last*, not whichever layer is *currently
active*. Feedback silently drifts out of sync with reality on every layer flip.

**The fix has to live upstream of the device, in whatever software owns the mapping:**

1. Track current active layer independently of the device (since the device gives no signal on a
   local layer switch, this state has to be inferred or explicitly re-synced from the software side).
2. Gate incoming feedback writes: only forward LED/state updates that belong to the currently
   active layer's channel; hold or drop updates for inactive layers.
3. Cache each inactive layer's last-known feedback state rather than discarding it.
4. On every layer switch, **replay the cached state for the newly active layer** — this is the
   step that's easy to miss. Without it, LEDs show stale state from whatever layer was active
   before, until the software happens to re-send something for the new layer on its own.

**Use for:** any control-surface integration where layers/banks are software-side conveniences
built on top of a receiver that doesn't natively support them. Applies beyond MIDI — the same
shape shows up with any channel-agnostic feedback protocol layered under a channel-aware control
scheme.

**Confidence:** Designed. The asymmetry itself is Bench-verified (confirmed against one
manufacturer's official manual). The gate/cache/replay fix is reasoned through, not yet built or
tested against real hardware.

**Open items:** whether the "currently active layer" state can be inferred at all without an
explicit resync mechanism, given some surfaces send zero signal on a local layer switch; how to
handle the cold-start case (software doesn't know current layer state at connection time).

---

# Protocol Selection: When One Feedback Path Isn't Enough — Splitting Legs Instead of Brokering Everything

**Covers:** A common trap when a control surface needs to drive multiple destinations (a media
server, a lighting console, a second app) is defaulting to "route everything through one central
bridge" as the only architecture. That's the right call when a destination genuinely can't be
reached without protocol translation — but it's the wrong call for any leg where the destination
already speaks a protocol the source can produce natively, or where a target application already
implements its own multi-device feedback routing.

**The decision framework that generalizes:**

- If a destination requires protocol translation the source can't produce (e.g. the controller
  only speaks MIDI, the destination only speaks OSC/Art-Net/sACN) — a broker is a hard
  requirement for that leg, not a design preference.
- If a destination can already receive the source's native protocol directly, and that
  destination already has its own internal logic for disambiguating multiple inputs/outputs
  (e.g. tracking device identity, per-shortcut output routing) — routing that leg through a
  broker anyway adds a redundant hop and forces the broker to re-derive logic the destination
  already owns.
- **Splitting legs by requirement, rather than brokering uniformly, avoids a specific failure
  mode:** if a broker sits on a leg it didn't need to, and that leg also has its own feedback
  path (state coming back from the destination to update the controller), the broker now has to
  relay that feedback too — inheriting problems (like the TX/RX asymmetry pattern above) that
  the destination's own direct feedback path wouldn't have had to deal with, because the
  destination becomes the sole writer to that state rather than sharing write responsibility
  with a broker.

**Use for:** any project routing one control surface to multiple software/hardware destinations
across different protocols. Worth explicitly asking, per destination: does this leg need
translation, or does it just need the source's native protocol handed to it directly?

**Confidence:** Designed. Reasoned through this session against one project's requirements;
not yet built or tested.

**Open items:** whether a "native protocol direct" leg still needs *some* intermediary for
things like fan-out (one control affecting multiple parameters on the same destination) even
when no translation is required.

---

# OSC vs. REST/WebSocket — Scoping Rule for Media-Server Control

**Covers:** When a target application exposes more than one control interface (e.g. both a
REST/WebSocket API and an OSC listener), a simple scoping rule avoids maintaining two redundant
mapping systems: **default to whichever interface is structured/discoverable (REST/WebSocket),
and use OSC only for the specific parameters that interface doesn't expose.** This keeps OSC's
scope narrow and intentional rather than letting two overlapping control paths both grow over time.

Some things worth checking before assuming REST covers everything:
- Whether individual deep parameters (e.g. specific effect-stack parameters on a specific
  layer/clip) are reachable via REST/WebSocket the same way they're addressable via OSC's fixed
  address-per-parameter scheme.
- Whether OSC-specific features — relative value operators (add/subtract/multiply against the
  current value server-side), or a simple "send `?`, get current value back" poll pattern — have
  a REST/WebSocket equivalent, or whether those specific capabilities are the actual reason to
  keep an OSC leg at all.

The only reliable way to establish the actual gap is to **check both interfaces against a running
instance** —
comparing the REST/WebSocket API's actual endpoint list against the OSC address space the running
composition/session exposes — rather than reading documentation for both and assuming coverage
lines up. Static docs (especially auto-rendered API references) may not reflect runtime-dependent
address spaces.

**Use for:** any media-server or show-control software offering multiple control protocols, when
deciding which protocol owns which slice of control.

**Confidence:** Designed. The scoping principle itself is straightforward; the actual gap for any
specific application/version has to be established live, not assumed from docs.

**Update — gap established for one case (2026-08-01):** for Resolume Arena/Avenue specifically, the
gap was resolved by reading the vendor's OpenAPI spec directly rather than the rendered API
reference page (which is JS-rendered and yields nothing to a plain fetch). Findings, now filed as
vendor facts in `creative-coding/references/protocols/resolume-control-interfaces.md` rather than restated here:
the structured interface reaches deep effect parameters after all, so the gap is *not* parameter
coverage; it is a small set of value-semantics and addressing features. This is worth generalising:
**the likely gap between a structured API and a fixed-address protocol is semantics and addressing
modes, not reach** — check what the structured API can't *express* before assuming it can't *reach*.

Two further generalisable notes from that case:
- The vendor's own documentation for a *third* surface (an agentic/MCP integration) published an
  explicit list of what it could not do "because it is limited to what the REST API can do" — which
  turned out to be the clearest published statement of the REST boundary anywhere in their docs.
  When a vendor ships a wrapper over their own API, its limitations page is often better boundary
  documentation than the API reference itself.
- That same exclusion list **contradicted** the OpenAPI spec on one object, which the spec exposes
  and the wrapper page says is unreachable. Neither source is automatically right; flag and test.

**Open items:** methodology for automating the comparison — walking an OpenAPI spec
programmatically against a captured address list from the other protocol — still untried; the case
above was resolved by reading the spec and the protocol docs, not by querying a running instance.
Nothing here has been confirmed against live software.
