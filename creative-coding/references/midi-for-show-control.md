# MIDI for Show Control

The parts of MIDI 1.0 that matter when a control surface drives live video, and the patterns for making a surface behave.

Device-specific numbers are **not** here — see `digital-video/references/` for per-device maps (e.g. `behringer-x-touch-compact.md`).

---

## 1. The message model, and why it decides your mapping

MIDI 1.0 channel voice messages are a status byte plus one or two data bytes. Data bytes carry 7 bits — **0–127**. Sixteen channels.

| Message | Data | Models |
|---|---|---|
| Note On / Note Off | note number, velocity | A discrete event with a beginning and an end |
| Control Change (CC) | controller number, value | A position on a continuous range |
| Program Change | program number | A discrete selection |
| Pitch Bend | 14-bit value | A continuous bipolar range |

**Note On with velocity 0 is a Note Off.** Universal convention; assume any device may use it and handle both forms.

### Match the message type to the control type

This is the single decision that causes the most downstream pain when you get it wrong.

- **Buttons → Notes.** Press and release are discrete events; Notes model them natively. Feedback also rides more reliably on note echoes than on CC-as-button workarounds, because the LED state maps onto a message the device already understands as on/off.
- **Faders, encoders, pedals → CC.** Continuous ranges.

Using CC for buttons works, but you end up encoding on/off as 127/0 and then fighting every layer that reasonably expects a range.

### 7-bit resolution is coarser than it looks

128 steps across a fader throw is visible stepping on slow moves — brightness ramps and position pushes especially. Options, in order of preference:

1. **14-bit CC** where the device supports it (below).
2. **Interpolate downstream.** Smooth the incoming value over time rather than jumping to it. Costs latency; usually worth it.
3. **Relative encoders**, where resolution is a function of how long you keep turning rather than of the message width.

### 14-bit controllers — the pairing rule

Two 7-bit messages combine into one 14-bit value (0–16383):

- **MSB** must be controller **0–31**
- **LSB** must be controller **32–63**
- **LSB index = MSB index + 32**

`[Official]` — [MIDI In CHOP, TouchDesigner Documentation](https://docs.derivative.ca/MIDI_In_CHOP)

Both sides must agree. A receiver in 7-bit mode reading a 14-bit device sees the LSB stream as a separate, wildly jittering control.

---

## 2. Absolute vs. relative encoders

**Tier: Bench-verified** (behavior confirmed on hardware; exact encodings are per-device).

| | Absolute | Relative |
|---|---|---|
| Sends | Current position, 0–127 | A delta per detent |
| On software-side change | Goes out of sync until touched | Stays correct — it has no position |
| Resolution | Fixed 128 steps | Unbounded; keep turning |
| Endless knob | Wraps or clamps badly | Natural fit |

Relative encoders have **no single encoding.** Common schemes: two's-complement around 64, sign-magnitude, or 1/127 for up/down. **Determine empirically** — turn the encoder one detent each way and read the raw bytes. Do not assume from the family of device.

Relative is almost always the right choice for a surface driving software that also changes state on its own, because the encoder never holds a stale position.

---

## 3. Feedback, state ownership, and echo

The moment a surface has motors or LEDs, you have a loop, and loops need an owner.

**Rule: software owns state; the surface displays it.**

Set buttons to **momentary** rather than toggle. A toggling surface owns its own LED, which means the LED tells you what the *button* thinks, not what the *software* is doing — and the two drift the first time anything else changes that parameter.

Momentary + software-driven LED gives one source of truth:

```
press → note on → software toggles internal state
                → software sends note back with LED velocity
                → LED reflects software, always
```

### Echo suppression

If you feed software state back to the surface and the surface re-emits, you oscillate. Three defenses, use at least one:

1. **Suppress on origin** — don't echo a change back to the control that caused it.
2. **Compare before send** — only transmit when the outgoing value differs from the last one sent to that control.
3. **Touch-gate motors** — while a fader is being touched, don't drive its motor. Touch-sensitive faders exist for exactly this.

### Motor re-seating

Motors are the payoff of a feedback surface: on bank flip, layer change, or cue recall, every fader physically moves to the new state and there is no pickup problem to solve. Send a full state refresh on every context change.

---

## 4. Pickup / takeover — for surfaces without motors

**Tier: Designed.** Standard strategies, stated for completeness.

| Strategy | Behavior | Cost |
|---|---|---|
| Jump | Value snaps to fader position on first move | Visible jump — usually unacceptable live |
| Catch / pickup | Ignores input until the physical position crosses the software value | Dead zone; operator can't tell when it will engage |
| Scale / relative-from-touch | Move is applied as an offset from current value | No jump, but the fader's absolute position becomes meaningless |

With motorized faders, none of this is needed. That is the argument for them.

---

## 5. Channels and banking

Sixteen channels is a cheap dimension and it is under-used. Two ways to expand a surface:

- **Bank / layer switching** — same messages, different meaning depending on the active bank. Requires the surface to signal its bank, and requires a full state refresh on flip. Most surfaces do this natively.
- **Channel as index** — encode which target a message refers to in the MIDI channel rather than in the note number. Useful when one physical control needs to address N devices: parse the channel, use it as an index into a table.

**Tier: Shipped** for channel-as-index — used to map a foot controller's channel to a device index by parsing the channel out of the incoming message and looking it up.

---

## 6. Index base — the off-by-one that bites every time

**Different layers of the same stack disagree about whether MIDI indices start at 0 or 1.**

Raw MIDI is 0-based: CC numbers 0–127, notes 0–127. Some host software reports 1-based indices (1–128), so **raw CC *n* arrives as index *n+1*.**

TouchDesigner exposes this as an explicit **One Based Index** parameter on its MIDI operators, defaulting to 0-based. `[Official]` — [MIDI Out CHOP, TouchDesigner Documentation](https://docs.derivative.ca/MIDI_Out_CHOP)

**Pattern: never derive the number from a manual. Capture it.** Before writing any mapping table, put the device in front of a raw MIDI monitor, touch every control, and record what actually arrives — message type, channel, index, value. Build the table from the capture, and use a printed map only to cross-check it. Applies equally to a decoded preset file: a file you reverse-engineered tells you what the *file* says, not what the wire carries.

---

## 7. Note numbering vs. note names

Note number ↔ name mapping has **no single convention** — middle C at note 60 is variously C3, C4, or C5 depending on the vendor. Manufacturer maps often print both.

**Work in numbers.** Convert to names only for display, and label which convention you used.

---

## 8. Clock and timing

MIDI clock is 24 pulses per quarter note, sent as System Real-Time messages that may interleave anywhere — including inside other messages. If you parse a raw stream, handle real-time bytes out-of-band rather than assuming message boundaries.

For video work, MIDI clock is usually the wrong sync source: it carries tempo, not frames. Use timecode or a frame-accurate transport when frames matter.

---

## Open items

- Per-device relative-encoder encodings — determine empirically, per device.
- Whether echo suppression is better done at the sender or with a comparison cache, under load with many controls updating at once. Untested at scale.
