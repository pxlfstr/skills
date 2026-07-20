# TouchDesigner — Control Integration Patterns

How to get MIDI, OSC and HTTP into and out of a TouchDesigner network without building something that rots.

Operator parameter names and defaults drift between builds — everything tagged `[Official]` below was read from docs.derivative.ca; verify against the build in use.

---

## 1. The operators, and which to reach for

### MIDI

| Operator | Use for |
|---|---|
| **MIDI In CHOP** | Continuous values as channels — the working input for a mapped surface |
| **MIDI In DAT** | Raw message inspection — the ground-truth capture tool |
| **MIDI In Map CHOP** | Mapper-based indirection (see below) |
| **MIDI Out CHOP** | Feedback — motors, LED rings, button LEDs |
| **MIDI Event DAT** | Event-driven handling in Python |

### OSC

TouchDesigner exposes OSC through four operators: **OSC In/Out CHOP** for channels, and **OSC In/Out DAT** for messages interpreted in Python. All use UDP. `[Official]` — [OSC, TouchDesigner Documentation](https://derivative.ca/UserGuide/OSC)

**Choose by shape of data, not by habit:**
- Continuous streams of numbers → CHOP
- Sparse, addressed, string-carrying, or needing dispatch logic → DAT

OSC In CHOP is connectionless and accepts messages from any number of sources on one port simultaneously. `[Official]` — [OSC In CHOP](https://docs.derivative.ca/OSC_In_CHOP)

### HTTP

**Web Client DAT** for outbound requests (including digest auth); **Web Server DAT** for inbound. Both are the right choice when the far end is a REST API and you want to *see* failures — unlike OSC, an HTTP call has a status code.

---

## 2. MIDI In CHOP vs. MIDI In Map CHOP

**Tier: Shipped.**

Map CHOP adds an indirection layer — the device mapper assigns slider/button identities (`s1`, `b1`…) which you then map again to meaning.

**Use MIDI In CHOP directly when the hardware assignments are already deliberate.** If you have already done the abstraction work on the device — assigning meaningful CC and note numbers in the manufacturer's editor — the mapper gives you a second mapping table to maintain and keep in sync with the first. Two tables that must agree is a bug generator.

Map CHOP earns its place when the hardware is *not* under your control: a rented surface, a device you can't reprogram, or a design that must accept several different controllers interchangeably.

---

## 3. The capture-first workflow

**Tier: Shipped.** This is the pattern; follow it in order.

1. **Register the device** — Dialogs → MIDI Device Mapper.
2. **Capture ground truth.** MIDI In DAT with **Bytes Column enabled**. Touch every control on the surface once. Record actual message type, channel, index and value for each.
3. **Build a table DAT** with columns `name`, `msgtype`, `number`, `control`, `group`. Seed it from the device's printed map if you have one, then **correct it against the live capture**. The capture wins every disagreement.
4. **Rename CHOP off the MIDI In CHOP**, driven by that table, to produce semantically named channels — `layer1_opacity`, not `ch1c10`.
5. Everything downstream references names. The mapping table is the only place a number appears.

The payoff: when a control moves or the surface is replaced, you edit one table. Nothing downstream changes.

**⚠️ MIDI In DAT reports 1-based indices (1–128).** Raw CC *n* appears as index *n+1*. TouchDesigner exposes this as a **One Based Index** parameter, defaulting to 0-based on the MIDI Out CHOP. `[Official]` — [MIDI Out CHOP](https://docs.derivative.ca/MIDI_Out_CHOP). Confirm which base each operator in your chain is using before you trust any number.

---

## 4. MIDI Out CHOP — channel naming is the API

Feedback is sent by **naming channels**, not by calling a function. The name encodes the message:

| Pattern | Meaning |
|---|---|
| `n65` | Note 65; channel value is sent as velocity |
| `c7` | Controller 7 |
| `ch1n45` | Note 45 on MIDI channel 1 |
| `pc` | Program change |
| `pw` | Pitch wheel |

A note event with no trailing number takes the note number *from the channel value*. Events without a number are sent to the whole channel. Use a **Rename CHOP** ahead of MIDI Out to produce these names from your semantic ones — the same table that drove input can drive output.

An event is sent whenever a channel changes value during the time slice. `[Official]` — [MIDI Out CHOP](https://docs.derivative.ca/MIDI_Out_CHOP)

**Consequence for feedback design:** because sends are change-driven, echo suppression is partly free — a value that doesn't change doesn't transmit. But a value driven *from* incoming MIDI will change and will echo. Break that loop explicitly.

For sending arbitrary events outside the channel-naming scheme, use the `midioutCHOP` Python class through an existing MIDI Out CHOP. `[Official]` — [midioutCHOP Class](https://derivative.ca/UserGuide/MidioutCHOP_Class)

---

## 5. The 14-bit parameter

MIDI In CHOP has a **Controller Format** parameter: 7-bit or 14-bit. In 14-bit mode it pairs controllers per the spec — MSB in range 0–31, LSB in 32–63, LSB index = MSB + 32. `[Official]` — [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP)

Set it to match the device. Mismatched, a 14-bit device read as 7-bit produces a control that works plus a phantom control that jitters violently — and the phantom is the LSB stream, which is a useful diagnostic signature.

---

## 6. The .toe restore trap

**MIDI input values are saved into the `.toe` file and restored on load.** The physical controls will be wherever the operator left them, which is not where the file thinks they are — so values jump on the first move after a reload. Derivative documents this as unavoidable. `[Official]` — [MIDI In CHOP](https://docs.derivative.ca/MIDI_In_CHOP)

**Mitigations:**
- **Motorized surface:** send a full state refresh to the surface on file open. Motors move to match; the discrepancy disappears before anyone touches anything.
- **Non-motorized:** apply a takeover strategy (see `midi-for-show-control.md` §4), or explicitly re-initialize the affected channels on start rather than trusting restored values.
- **Never let a restored value drive anything on the first frame** without deciding which side is authoritative.

---

## 7. Table-driven mapping — the general pattern

**Tier: Shipped.**

Every control-surface build in this domain converges on the same shape:

```
input operator  →  raw channels
                        ↓
              mapping table (DAT)
                        ↓
              Rename / dispatch
                        ↓
              semantic channels  →  the rest of the network
```

Design rules that make it hold up:

- **The table is edited by hand, not regenerated.** It is the human-readable contract. Scripts that rewrite it destroy the annotations that make it comprehensible six months later.
- **One row per control**, with a function-kind column — rate, integrate, pick, step, toggle — so the handler dispatches on kind rather than on a chain of special cases.
- **Numbers appear only in the table.** If a CC number is written anywhere else in the network, that is a bug waiting for the day the surface changes.
- **Names are stable, assignments are not.** Downstream references names; when hardware changes, only the table moves.

---

## 8. Script CHOP for devices TouchDesigner doesn't expose well

**Tier: Shipped.**

Where a built-in operator has a limitation you can't work around — focus-gating on input devices being the classic case — a **Script CHOP** reading the device directly through a Python library gives you full control of when and how it is polled, at the cost of owning the polling loop yourself.

Applies to game controllers, serial devices, and anything with a Python binding but no native operator. Keep the read cheap: a Script CHOP runs every cook, and blocking in it stalls the whole network.

---

## 9. Throttling outbound requests

**Tier: Shipped.**

When TouchDesigner drives a device over HTTP or serial, per-frame sends will outrun the device and the lag compounds. The working structure:

- **Minimum interval between sends**, enforced on the send side.
- **A priority chain** — when several updates are pending at the interval boundary, send the highest-priority one and **drop** the rest. Do not queue.
- **A skip-gate for offline devices.** A blocking or slow call to an unreachable device stalls the cook. Detect offline and skip rather than retry inline.

Continuous values are safe to drop; the next one supersedes them. Discrete commands are not — those need their own path.

---

## Open items

- Whether Map CHOP's indirection cost is worth it for multi-surface interchangeable setups — designed, not tested.
- Behavior of the `.toe` value restore when the surface is motorized and the refresh races file-open — order of operations untested.
- Practical Script CHOP polling cost at high cook rates — not measured.
