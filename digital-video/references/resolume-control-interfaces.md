# Resolume — Control Interfaces (OSC, REST, MIDI)

Vendor facts for controlling Resolume Arena/Avenue from outside. Integration *patterns* live in `creative-coding/references/resolume-companion-glue.md`; this file holds only what the vendor documents.

**Scope note:** Resolume 7.x. Version-specific behavior drifts — confirm against the running build.

---

## Default ports

| Interface | Default port | Source |
|---|---|---|
| OSC input | 7000 | [companion-module-resolume-arena](https://github.com/bitfocus/companion-module-resolume-arena) `[Official]` (module README) |
| REST API / web server | 8080 | [Resolume Support — REST API](https://www.resolume.com/support/en/restapi) `[Official]` |
| OSC output → Companion listener | 7001 | [companion-module-resolume-arena](https://github.com/bitfocus/companion-module-resolume-arena) `[Official]` |

All are user-configurable. **Verified.**

---

## OSC

**Addresses are discovered, not looked up.** Resolume declines to publish a full address list because the address space depends on how the composition is built — layer count, clip count, effects loaded. The documented method is to enter OSC shortcut mode (**Shortcuts → Edit OSC**) and click the control; the Shortcuts panel shows its address, click-to-copy. `[Official]` — [Resolume Support — OSC](https://resolume.com/support/en/osc)

**Absolute vs. relative addresses.** A given control is often reachable two ways: an absolute address naming the layer explicitly, and a relative address that acts on whichever layer is *currently selected*. The relative form lets one address drive the same effect across many layers, at the cost of depending on selection state. Sending to a relative address when the target effect isn't present on the selected layer is safe — it simply does nothing. `[Official]`

**Type tags.** Selecting a UI item also displays its Type Tag — what value types the address accepts and what they do. `[Official]`

**Input addresses are fixed.** They cannot be remapped. Custom OSC *presets* affect output, not input. `[Forum]` — [OSC Arena 7.13.1](https://resolume.com/forum/viewtopic.php?t=22904), Resolume forum

**Listening interface.** Resolume displays one adapter's IP as information only; OSC actually listens on all adapters, and sending follows the system routing table. A displayed APIPA address is cosmetic, not a fault. `[Forum]` — [strange OSC IP Address??](https://resolume.com/forum/viewtopic.php?t=20559)

### Connect vs. connected

- `connect` is the clip **trigger action** — a mouse click. `1` = press, `0` = release.
- `connected` is the clip slot **state**.

Reported behavior: when switching decks with a clip connected, `0` is emitted for the outgoing deck's clip — the release of the previous deck's clips. `[Forum]` — same thread, includes a Resolume developer in the discussion. Treat as a strong lead, not a spec.

---

## REST API / web server

Enabled per-application: **Arena/Avenue/Wire tab → Preferences → Web Server**. The panel shows the machine IP, an enable toggle, Listen Port and Listen Address. `[Official]`

**The reference documentation is served by the running instance.** With the web server live, the API reference page can send commands directly to it — the docs double as a test client, and they describe *your* version rather than a generic one. This is the authoritative way to get the current command list. `[Official]`

Two constraints worth knowing:
- The web root may not contain a folder named `API`.
- A path ending in `/` is served `index.html` from that folder.

---

## OSC vs. REST — which carries what

Neither interface is a superset of the other. From the Companion module's own documentation `[Official]`:

| | OSC | REST |
|---|---|---|
| Transport actions (play, pause, trigger) | Yes | — |
| Feedback / state query | Only via OSC Output → listener | Yes |
| Companion module falls back to | — | OSC, when REST port is blank |
| Connection detectable? | **No** — connectionless UDP, always reports OK | Yes, errors on misconfiguration |

Some functions exist only on OSC, some only on REST. A control system usually needs both enabled.

**OSC feedback path:** Preferences → OSC → enable **OSC Output**, set destination IP and port to the receiver. Without this, nothing flows back and every downstream surface is open-loop.

---

## MIDI

Resolume maps MIDI by learn rather than by fixed address. Both **MIDI Input and Output** must be enabled in Preferences for a feedback-capable surface (motorized faders, LED rings, button LEDs) to stay synchronized with software state.

Device-specific mapping notes for the Behringer X-Touch Compact are in `behringer-x-touch-compact.md` §6.

---

## Resolume Wire

Wire (the node-based patching environment for building effects/mixers/generators) supports both MIDI and OSC. OSC input is enabled at **Preferences → OSC → OSC Input**, which displays the listening IP and incoming port. `[Official]` — [TouchOSC manual — Setup: Resolume Wire](https://hexler.net/touchosc/manual/setup-resolume-wire)

---

## Open items

- Full default OSC namespace under 7.20+ (`/composition/...`) read from an official source rather than a third-party doc set.
- Whether `connect` deck-switch `0` emission is documented behavior or an acknowledged bug.
- REST endpoint list for the specific version in use — pull from the local web server's reference page.
