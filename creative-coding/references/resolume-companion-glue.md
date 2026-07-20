# Resolume & Companion — Integration Patterns

Patterns for wiring Resolume and Bitfocus Companion into a control system.

**Vendor facts — ports, address discovery, the OSC/REST capability split — are in `digital-video/references/resolume-control-interfaces.md`.** They are deliberately not repeated here.

---

## 1. Pick the interface by what you need back

Resolume's three control interfaces are not interchangeable, and the choice is usually forced by **feedback**, not by control.

| You need | Interface | Why |
|---|---|---|
| Fire a clip, run transport | OSC | Fast, fire-and-forget, always available |
| Move a parameter continuously | OSC | Float resolution, high rate |
| Read current state reliably | REST | Returns a value and errors when it can't |
| Know a command failed | REST | OSC is UDP — no acknowledgement, no connection |
| Feedback to a physical surface | MIDI out, or OSC out to a listener | Must be explicitly enabled |

**The practical answer for a real system is usually "both."** Some actions exist only on OSC, some feedback only via REST or an OSC output listener. Enabling one and assuming the other is the most common way an integration half-works.

---

## 2. Discover the address space; don't hardcode from a tutorial

**Tier: Bench-verified.**

Resolume's OSC address space depends on how the composition is built — layer count, clip count, loaded effects. There is no static list to copy, and older tutorials reference a namespace that has since changed.

Working method:
1. Enter OSC shortcut mode in Resolume and click the control you want.
2. Copy the address it shows.
3. Note the **type tag** it shows alongside — this is what the address will accept.
4. Test-send before wiring it into anything.

**Design consequence:** because addresses encode composition structure, a control system built on absolute addresses is coupled to the composition layout. Renumber the layers and the show breaks. Two mitigations:

- **Keep an indirection table** mapping semantic names to addresses, so a composition change is a table edit rather than a code edit. Same pattern as the MIDI mapping table in `touchdesigner-integration.md` §7.
- **Use relative addressing** where selection-following is genuinely wanted — but never for a cue a show depends on, because it silently depends on selection state you now have to track.

---

## 3. Feedback is opt-in, and its absence is invisible

**Tier: Shipped.**

The failure mode: control works perfectly, so the integration looks finished, and nobody notices that nothing comes back until a surface is out of sync mid-show.

Enable, explicitly:
- **MIDI Output** in Resolume preferences, for any motorized or LED surface. Without it, motors never re-seat and LEDs never reflect software state.
- **OSC Output** — destination IP and port — for any OSC listener downstream. Companion's Resolume module, for example, takes its transport variables and progress feedback from an OSC listener rather than from the control path.

**Test feedback separately from control.** They are different directions on different ports and either can be broken while the other works.

---

## 4. Layers as banks on a control surface

**Tier: Shipped.**

Mapping a two-layer control surface (an A/B preset surface, for instance) onto Resolume:

- Treat each surface layer as a **distinct control bank**, not as an extension of one flat map.
- On flip, the surface re-seats its motors and rings — which is only true if feedback is enabled and a **full state refresh** is sent on the change.
- Keep the *meaning* of a given physical control consistent across banks where possible. Fader 1 being "layer opacity" in bank A and "master speed" in bank B is legal and is a mistake you make once.

Surface-specific mapping detail for the X-Touch Compact is in `digital-video/references/behringer-x-touch-compact.md` §6.

---

## 5. Companion as the glue layer

**Tier: Bench-verified.**

Companion earns its place when you need **buttons with state** in front of several different systems at once — its value is the feedback model, not the button pushing.

Design notes:

- **Companion modules are per-vendor and open source.** Read the module's own documentation for the action and feedback set; it is the authoritative list for the version you have, and it changes.
- **Feedback frequently requires the richer interface.** Where a module supports both OSC and REST, feedbacks typically need REST while actions fall back to OSC. Configure both unless you are certain you need no feedback.
- **A module reporting OK proves nothing about a UDP link.** Connectionless transports cannot be probed. If status matters, put a REST path in the config so misconfiguration surfaces as an error rather than as silence.
- **Don't rebuild Companion inside TouchDesigner.** If the need is a button wall with state, Companion already solved it. Use TouchDesigner for the parts Companion can't do — continuous control, video, generated content — and let them talk over OSC.

---

## 6. Architecture — separate the concerns

**Tier: Shipped.**

The shape that holds up across shows:

```
physical surface  --MIDI-->  show system  --OSC-->  media application
                                   |
                                   +--REST-->  state queries / anything whose failure must be visible
                                   |
                            Companion  --OSC-->  show system
```

Principles behind it:

- **One system owns state.** Every other node displays or requests. Two systems both believing they own a parameter is the root of most sync bugs.
- **Protocol per direction, chosen on need** — a link is not obliged to use the same protocol both ways. MIDI in, OSC out is fine.
- **Each piece works alone.** The show system should run with the surface unplugged; the media application should run with the show system down. Anything that hard-fails when one node disappears will hard-fail during a show, because eventually one does.
- **The glue is a table, not a codebase.** Semantic name → address/CC/endpoint, in one editable place.

---

## 7. Known gaps

- **Layer Speed fader receives no feedback on clip change.** Observed with a motorized surface; suspected Resolume bug, unconfirmed. Practical effect: that one control drifts out of sync while everything else re-seats correctly. **Tier: Bench-verified** as an observation, **unverified** as a cause.
- **Deck-switch emits `0` for connected clips.** Understood to be the release of the outgoing deck's clips rather than a state error — reported behavior, developer participating in the discussion, but not documented as a spec. Don't build state tracking that treats it as a genuine disconnect. See `digital-video/references/resolume-control-interfaces.md`.

---

## Open items

- Whether the Speed-fader feedback gap persists in current 7.x builds.
- Whether a REST poll can fill the feedback gaps that OSC output misses, and at what rate before it costs frames.
- Companion's behavior when the REST endpoint is reachable but the OSC port is wrong — untested.
