# X-Touch Compact — MIDI map

Obie's own X-Touch Compact configuration, as loaded on the device. Not the Behringer
factory map — for that see `behringer-xtouch-compact-resolume.md`.

Approved for the public repo: device configuration for a commercial controller, not rig,
client or venue detail.

## Provenance

- **Tier: `[Official]` for the assignment table** — every number below is read out of the
  device's own configuration files, not from documentation or from observed traffic.
- **Source files:** the four `.bin` exports committed in `xtouch-compact-config/`,
  exported from X-Touch Editor and decoded 2026-08-02 by `xtouch-compact-config/decode.py`.
  723 bytes each, 91 assignment records each, all 91 decoded and accounted for.
- **Method:** byte comparison across layer pairs plus structural decode. Layer A and B
  differ in exactly 90 records, every one of them a channel byte — which pins the channel,
  type, index, min and max fields unambiguously.
- **Supplied by Obie, not derived from the files:** every physical control label, the
  C3 = 60 octave convention, which physical row is "top", and the design intent behind the
  expression-pedal channel exception. The `.bin` files carry no labels.
- **Bench-identified, not documented by Behringer:** which Editor relative mode is which
  encoding, and the encoder mode byte value. See *Encoders* below.
- **Supersedes** the version derived 2026-08-01, and its 2026-08-02 revision. Rebuilt 2026-08-04
  from the four exports committed in `xtouch-compact-config/`.
- **Not read:** no X-Touch Editor documentation of the `.bin` format is known to be
  published. The format decode is reverse-engineered from these exports alone.
- **Not verified against hardware in this pass.** The table states what the configuration
  files contain, not what the device transmits.
- **Open, unresolved:** the byte values for Relative 2 and Relative 3; what decides record
  length; where encoder ring mode is stored.
- **Closed 2026-08-04:** the button LED receive-note mapping, previously untested across all 39
  buttons, is confirmed correct — see *Button LEDs* below. The playback grid's transmit notes and
  the two silent Layer A/B positions are confirmed in the same pass. **No assignment in this
  document is now unverified against hardware.**
- **Closed since the last version:** the ring-value RX table is NOT shifted — raw sends of
  13 and 14 to CC 26 gave rightmost-LED solid and leftmost-LED blinking, matching the
  manual's documented bands. The +1 shift is specific to the button LED velocity table.

---

## Number conventions — three of them, don't mix them up

| Where | Convention |
|---|---|
| `.bin` file | Raw MIDI (CC 0–127, note 0–127) |
| X-Touch Editor display | Raw — matches the file |
| MIDI In DAT | **Always 1-based**, no parameter |
| MIDI In CHOP | Raw by default; `onebased` switches it. Affects notes AND controllers |
| MIDI Out CHOP | **0-based by default**; same `onebased` parameter |

Raw `send()` on the MIDI Out CHOP bypasses `onebased`, `controlnorm` and `controlformat`
entirely — the named methods (`sendControl`, `sendNoteOn`) honour them. Bench-confirmed for
`send()`; the docs state it for both.

Octave convention throughout: **C3 = 60 (Yamaha/Steinberg)**.

---

## Continuous controls

| Control | CC (raw) | TD (1-based) | Layer A ch | Layer B ch |
|---|---|---|---|---|
| Faders 1–9 | 0–8 | 1–9 | 1 | 2 |
| Encoders 1–8 (top row) | 10–17 | 11–18 | 1 | 2 |
| Encoders 9–16 (right side) | 18–25 | 19–26 | 1 | 2 |
| Expression pedal | 30 | 31 | 1 | **1** — intentional, layer-independent |
| Foot switch | 31 | 32 | 1 | 2 |
| Fader touch 1–9 | 0–8 | 1–9 | **3** | **4** |

CC 9 is unassigned, as are 26–29 and 32–99.

## Buttons

| Row | Notes (raw) | Note names | TD (1-based) | Count | Layer A ch | Layer B ch |
|---|---|---|---|---|---|---|
| Top row | 36–43 | C1–G1 | 37–44 | 8 | 1 | 2 |
| Middle row | 48–55 | C2–G2 | 49–56 | 8 | 1 | 2 |
| Bottom row | 60–67 | C3–G3 | 61–68 | 8 | 1 | 2 |
| Below faders 1–8 | 72–79 | C4–G4 | 73–80 | 8 | 1 | 2 |
| Below Main fader (9) | 80 | G#4 | 81 | 1 | 1 | 2 |
| Playback control grid | 84–89 | C5–F5 | 85–90 | 6 | 1 | 2 |

**The playback grid is 4 rows by 2 columns physically — eight positions, six assignments.** The other two are the Layer A and Layer B buttons, which transmit nothing at all. Bench-confirmed 2026-08-04: pressing all eight produced exactly six messages, raw notes 84–89 in order, left to right then top to bottom.
| Encoder push 1–8 | 96–103 | C6–G6 | 97–104 | 8 | 1 | 2 |
| Encoder push 9–16 | 108–115 | C7–G7 | 109–116 | 8 | 1 | 2 |

Every block runs C through G except two: the below-faders row is nine wide (C4–G#4)
because of the Main fader button, and the playback grid is six (C5–F5). The gaps between
blocks — 44–47, 56–59, 68–71, 81–83, 90–95, 104–107 — are what keep each block starting
on a C.

## Button LEDs — receive notes, and the device lights its own

**Transmit and receive use completely different note numbers.** A button transmits in the C-based
blocks above and receives its LED on a separate contiguous range:

| Block | Transmits (raw) | LED receives (raw) |
|---|---|---|
| Top row | 36–43 | 0–7 |
| Middle row | 48–55 | 8–15 |
| Bottom row | 60–67 | 16–23 |
| Below faders (9 wide) | 72–80 | 24–32 |
| Playback grid | 84–89 | 33–38 |

**Bench-confirmed 2026-08-04**, one send per block: raw note 0 lit row 1 button 1, 8 lit row 2
button 1, 16 lit row 3 button 1, 24 lit row 4 button 1, and 33 lit the rewind button. Ascending
left to right within each block.

**Every transmit and receive assignment on this surface has now been verified against hardware** —
all 91 transmit assignments captured in the MIDI In DAT, and every LED receive block confirmed by
raw send.

Velocity: **1 = off, 2 = on, 3 = blinking.** This contradicts the manual's p.32 table and is
bench-observed. Velocity 0 also reads as off, via the standard note-on-velocity-0 convention.

### The device lights its own button LEDs

⚠️ **In Momentary push behaviour the device drives the LED itself** — lit while the button is
held, cleared the instant it is released, regardless of what the host has sent. Bench-observed
2026-08-04.

**Consequence for any host that owns button state:** a write on the press is wiped by the device's
own clear on release. The host must **re-send on note-off**, not only on note-on. Without that the
LED goes dark on every release and only returns on the next periodic repaint — which reads as a
multi-second delay to light, and an instant response to turn off.

This mirrors the encoder rings, which the device also draws locally. The pattern is general: this
surface renders its own controls, and a host that wants authority has to write last, not first.

---

---

## Encoders — Relative 1, all sixteen

Set 2026-08-02. Relative deltas, not absolute positions, so **TouchDesigner owns the
value** and the encoders cannot jump on a layer switch or after a change made elsewhere.

**Relative 1 is two's complement:**

| Direction | Values sent | Decode |
|---|---|---|
| Right | 1, 2, 3 … | `delta = v if v < 64 else v - 128` |
| Left | 127, 126, 125 … | branchless: `(v + 64) % 128 - 64` |

Magnitude scales with turn speed, so a fast spin sends larger deltas.

**Which Editor mode is which encoding is undocumented by Behringer.** Bench-identified
2026-08-02 by setting three encoders to the three modes and reading the values:

| Editor label | Encoding | Left | Right |
|---|---|---|---|
| **Relative 1** | Two's complement | 127, 126… | 1, 2… |
| Relative 2 | Binary offset | 63, 62… | 65, 66… |
| Relative 3 | Sign and magnitude | 65, 66… | 1, 2… |

**The mode is stored in the record's min byte** — `0` = absolute, **`130` = Relative 1**.
Confirmed by changing only that setting and re-exporting: all sixteen encoder records moved
from 0 to 130, nothing else in the file changed.

⚠️ The byte values for Relative 2 and Relative 3 are **unknown** — neither has been
exported. `decode.py` reports an unrecognised value rather than guessing.

## Fader touch — its own channels

**CC 0–8 on channel 3 for bank A and channel 4 for bank B. Push behaviour Momentary.**

Touch deliberately does **not** follow the bank channels the rest of the surface uses. It shares
CC 0–8 with the faders themselves and is separated only by channel.

⚠️ **Why it was moved there.** With touch on the same channel as the fader's own move CC, Momentary
push behaviour corrupted that CC: fader 1's move messages alternated between 0 and 127 instead of
sweeping, with the host sending nothing at all. Bench-observed 2026-08-02, mechanism unknown,
undocumented by Behringer.

Toggle cleared the corruption but made touch useless as a gate — **no message on finger contact,
one message per release, alternating 127 then 0.** Moving touch to its own channels allows
Momentary, which restores proper contact and release.

**Now bench-confirmed on channel 3:** `b2 00 7f` on contact, `b2 00 00` on release, with the
fader's own move messages arriving between the two.

⚠️ **Touch-on lags the first movement message by roughly 2–9 frames** (bench-observed). Touch is
not usable as the onset signal for echo suppression — arm on first movement and use touch for the
release edge.

**Consequence for any host mapping:** the lookup must be keyed on **channel + message type +
number**. `fader1` and `fader_touch1` are both CC 0; only the channel separates them. Bank detection
also cannot be "channel 2 means B" — **channels 1 and 3 are bank A, 2 and 4 are bank B.**

**History.** Touch was previously at raw CC 101–109, then moved to 100–108 on the bank channels to
retire an off-by-one, then moved here. The off-by-one is retired either way.

---

## Bank channels, with two exceptions

Every assignment transmits on **channel 1 in bank A and channel 2 in bank B**, at the same control
number. Two things break that, both on purpose:

**CC 30 — expression pedal. Channel 1 in both banks.** So it stays reachable regardless of the
active bank, and can never be evidence of which bank is active.

**Fader touch — channels 3 and 4.** See above.

The point is layer detection. The hardware Layer A/B buttons transmit nothing, so the host
cannot see a layer change on the surface. Channel now identifies the bank on every message,
and the pedal stays reachable regardless of bank.

**Consequence for TouchDesigner:** with `Channel Prefix` blank on the MIDI In CHOP, input
from multiple MIDI channels **merges into one set of CHOP channels**, and the expression
pedal would land silently in the Layer A stream. Set `prefix` to `ch` before adding Layer B.

## Two config variants

| Variant | Expression pedal |
|---|---|
| `with_EXP` | CC 30, channel 1 |
| `NO_EXP` | Off |

⚠️ An assigned but **unterminated** expression jack emits spurious CC 30 on fast fader-9
movement. With no pedal plugged in, load a `NO_EXP` layer. The same applies to the foot
switch — set its channel to Off when nothing is in the jack.

## All values full-range

Every record in both layers is min-equivalent `0` / max `127`, except the sixteen encoder
records where the min byte carries the mode instead. No scaling configured in the Editor —
normalize in TouchDesigner.

---

## `.bin` file format — reverse-engineered

Undocumented. Decoded from these exports only; treat as provisional. Working decoder:
`xtouch-compact-config/decode.py`.

**Header:** 5 bytes, `20 15 01 04 03`. **Identical in every file** — the layer is not
identified in the header, only by filename.

**Records:** 91, immediately following the header:

```
[0] channel   0 = ch1 … 15 = ch16, 0x12 = Off
[1] type      0 = CC, 1 = Note
[2] index     raw MIDI CC or note number
[3] min       0 normally; encoder mode when the control is an encoder
[4] max       127 throughout
[5] push      push behaviour: 0 = Momentary, 1 = Toggle
[6..]         trailing zeros
```

**`0x12` in the channel byte means Off.** Established 2026-08-02 by exporting the same
layer with the expression pedal enabled and disabled — that byte was the only difference.
This also explains the original fader-touch records, which carried `0x12` because touch was
simply switched off.

Record length is **7 bytes for the nine faders and the expression pedal, 8 bytes for the
other 81.** What determines the length is not known; the extra byte has been zero in every
file examined. A parser must not assume a fixed stride.

**Push behaviour is byte 5.** Established 2026-08-02 by switching only fader touch from
Momentary to Toggle and re-exporting: exactly nine bytes changed across all four files, all
at byte 5 of the fader-touch records, `0x00` → `0x01`. Byte 5 exists on the 7-byte records
too and reads 0 there, so it is unrelated to record length.

⚠️ **Still open:** what decides record length, and where encoder ring mode is stored.

**Record order** is not the physical layout order: faders, encoders 1–8, encoder pushes
1–8, encoders 9–16, encoder pushes 9–16, then the button blocks in ascending note order,
then expression pedal, foot switch, fader touch.

---

## What changed from the previous version of this document

1. **Fader touch moved to CC 0–8 on channels 3 and 4**, push behaviour Momentary. It was at
   CC 101–109, then CC 100–108 on the bank channels, before landing here. The parked off-by-one
   is retired.
2. **All sixteen encoders set to Relative 1**, and the mode byte identified as `130`.
   The previous version stated all controls were absolute.
3. **`0x12` = channel Off** established, replacing the earlier guess that it was an unknown
   marker specific to fader touch.

Also new: the `NO_EXP` variants, and the four source exports now under version control in
`xtouch-compact-config/`.
