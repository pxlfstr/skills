# OSC for Show Control

What OSC actually guarantees, what it doesn't, and the patterns for building on it.

Vendor-specific address spaces and ports are **not** here — see `digital-video/references/resolume-control-interfaces.md` and equivalents.

---

## 1. What OSC is

A message is an **address pattern** (`/composition/layers/1/clips/3/connect`), a **type tag string** (`,f`), and **arguments** matching the tags.

Compared to MIDI:

| | MIDI 1.0 | OSC |
|---|---|---|
| Value width | 7-bit (or 14-bit paired) | 32/64-bit float, int, string, blob |
| Namespace | Fixed: 16 channels × 128 controllers | Arbitrary hierarchical strings |
| Transport | Serial / USB, point to point | Unspecified — UDP in practice; routable |
| Discovery | None | None in the base spec |
| Delivery guarantee | Wire-level reliable | **None** over UDP |

The two live differences that shape design: **OSC gives you real resolution and a self-describing namespace; it gives you no delivery guarantee.**

---

## 2. The transport is not specified — and that is the whole problem

OSC 1.0 defines the message encoding, not the transport. In practice everything uses **UDP**, including TouchDesigner's OSC CHOPs. `[Official]` — [OSC In CHOP, TouchDesigner Documentation](https://docs.derivative.ca/OSC_In_CHOP)

Consequences you must design around:

- **Messages can be dropped**, and nothing tells you.
- **Messages can arrive out of order.**
- **There is no connection.** A receiver cannot distinguish "sender is idle" from "sender is gone." Anything reporting a connection status for a plain OSC link is inferring, not observing — Resolume-side, the Companion module explicitly always reports OK for OSC-only configuration. `[Official]` — [companion-module-resolume-arena](https://github.com/bitfocus/companion-module-resolume-arena)

### Design rules that follow

1. **Send state, not events, wherever you can.** A dropped "set opacity to 0.7" is corrected by the next one 20 ms later. A dropped "toggle" is wrong forever.
2. **Where an event is unavoidable** (trigger, go, fire), either send it more than once with idempotent semantics, or confirm it against a state query.
3. **Repeat continuous values on a heartbeat**, even when unchanged, so a receiver that missed one recovers.
4. **Never build a counter or accumulator on the receive side** from incremental OSC messages. Drop one and it drifts silently for the rest of the show.

---

## 3. Address design

**Tier: Designed / Bench-verified.**

When you own both ends, the namespace is yours to shape:

- **Hierarchical and stable** — `/rig/layer/3/opacity`, not `/opacity3`. Structure lets you use wildcards and lets a receiver route by prefix.
- **Index in the path, not the argument.** `/cam/2/pan 0.5` beats `/cam/pan 2 0.5` — the receiver can dispatch on the path without unpacking arguments.
- **One address, one meaning.** Overloading an address by argument count is legal and painful.
- **Nouns for state, verbs for actions.** `/cam/2/preset/recall` reads differently from `/cam/2/preset` and should.

When you *don't* own both ends, the address space is the vendor's and is often not published — discover it from the running application rather than looking for a list.

### Absolute vs. relative addressing

Some hosts expose both an absolute address (naming the target explicitly) and a relative one (acting on whatever is currently selected). Relative addressing lets one control drive many targets — at the cost of depending on selection state, which is itself a piece of state you now have to track. Prefer absolute for anything a show cue depends on.

---

## 4. Type tags

The type tag string declares argument types. Getting it wrong is the most common OSC bug after ports.

- `i` — int32, `f` — float32, `s` — string, `b` — blob
- `T` / `F` — true / false, sent as **type tags with no argument bytes**
- Many receivers are strict: sending `1` (int) where `1.0` (float) is expected silently does nothing

**Pattern:** when a message appears to do nothing and the address is confirmed correct, check the type before checking anything else. A receiver that shows the expected type tag in its UI is telling you what to send — use it.

---

## 5. Bundles and time tags

A bundle groups messages with a time tag for atomic or scheduled execution. Two cautions:

- **Support is uneven.** Many receivers unpack bundles and execute immediately, ignoring the time tag entirely. Verify before depending on scheduling.
- **Atomicity is a receiver behavior, not a wire guarantee.** If you need two parameters to change on the same frame, test that the receiver actually honors it.

Where bundle support is unreliable, achieve the same effect by sending a single message carrying multiple arguments, and let the receiver apply them together.

---

## 6. Ports, and the bidirectional gotcha

OSC over UDP is **one-way per port.** A bidirectional link is two independent unidirectional links, and each needs configuring separately at both ends:

```
controller  --:7000-->  application     (control)
controller  <--:7001--  application     (feedback)
```

The single most common integration failure is enabling input and assuming output. Feedback almost always requires explicitly enabling an OSC *output*, setting the destination IP, and setting the destination port — and until you do, everything downstream is open-loop and looks like it is working.

**Listening interfaces:** an application that displays "its" OSC IP is usually showing the first active adapter as information only, while actually listening on all of them. A displayed link-local (169.254.x.x) address is cosmetic and not necessarily a fault — test by sending, not by reading the label.

---

## 7. OSC vs. MIDI vs. REST — choosing

| Need | Reach for |
|---|---|
| A physical surface with knobs and motors | MIDI |
| Resolution better than 7-bit | OSC |
| Control across a network / between machines | OSC |
| Reading state back reliably, with errors when it fails | REST/HTTP |
| Fire-and-forget at high rate | OSC |
| A guarantee the command landed | Not OSC |

Real systems mix them: MIDI at the surface, OSC for machine-to-machine, REST for state queries and anything whose failure you need to *see*. Vendor capability is rarely symmetric across the three — some actions exist only on one interface, which means enabling both is normal rather than redundant.

---

## 8. Rate limiting

**Tier: Shipped.**

A continuous controller sampled at frame rate will happily emit 60 messages/sec per control, and a receiver — especially one doing HTTP or moving hardware — will fall behind and then lag by a growing margin.

The working pattern is a **throttle plus a priority chain**: enforce a minimum interval between sends, and when several updates are pending at the interval boundary, send the highest-priority one and drop the rest rather than queueing them. Dropping stale continuous values is correct — the next one supersedes it anyway. Queueing them guarantees the lag you were trying to avoid.

Choose the interval from the receiver's demonstrated capability, not from a guess. Measure where it starts falling behind and back off from there.

---

## Open items

- Whether bundle time tags are honored by the specific receivers in use — untested per application.
- Practical minimum throttle interval per receiver — measure per device, no general figure.
