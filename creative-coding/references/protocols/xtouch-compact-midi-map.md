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
- **Supersedes** the version derived 2026-08-01. Three things changed — see
  *What changed* at the end.
- **Not read:** no X-Touch Editor documentation of the `.bin` format is known to be
  published. The format decode is reverse-engineered from these exports alone.
- **Not verified against hardware in this pass.** The table states what the configuration
  files contain, not what the device transmits.
- **Open, unresolved:** the byte values for Relative 2 and Relative 3; what decides record
  length; where encoder ring mode is stored.
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
| Fader touch 1–9 | 100–108 | 101–109 | 1 | 2 |

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
| Encoder push 1–8 | 96–103 | C6–G6 | 97–104 | 8 | 1 | 2 |
| Encoder push 9–16 | 108–115 | C7–G7 | 109–116 | 8 | 1 | 2 |

Every block runs C through G except two: the below-faders row is nine wide (C4–G#4)
because of the Main fader button, and the playback grid is six (C5–F5). The gaps between
blocks — 44–47, 56–59, 68–71, 81–83, 90–95, 104–107 — are what keep each block starting
on a C.

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

## Fader touch

CC 100–108 raw, in use as of 2026-08-02. **Push behaviour must be Toggle, not Momentary.**

⚠️ With fader touch set to Momentary, the touch signal interferes with the fader's own
move CC: fader 1's move CC alternated between 0 and 127 instead of sweeping, with the host
sending nothing at all. Setting touch to Toggle cleared it. Bench-observed 2026-08-02,
undocumented by Behringer, mechanism unknown. Reads as **101–109 in the MIDI In DAT**, which
lines up with fader numbering.

Value 127 on touch, 0 on release. ⚠️ **Touch-on lags the first movement message by roughly
2–9 frames** (bench-observed), so touch is not usable as the onset signal for echo
suppression — latch on first movement instead and use touch only for the release edge.

This numbering was chosen deliberately to retire an earlier off-by-one: the files
previously stored 101–109 while a bench note recorded 101–109 *as displayed*, and which
convention the note used was never recorded. Moving the device to 100–108 makes both
readings agree rather than resolving which was right.

---

## Layer B is channel 2, with exactly one exception

Every assignment transmits on **channel 1 in Layer A and channel 2 in Layer B**, at the
same control number. One record breaks that, on purpose:

**CC 30 — expression pedal. Channel 1 in both layers.** Verified: it is the only channel-1
record in the Layer B file.

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

1. **Fader touch moved from CC 101–109 to CC 100–108** and is now in use, channel-assigned
   in both layers. The parked off-by-one is retired.
2. **All sixteen encoders set to Relative 1**, and the mode byte identified as `130`.
   The previous version stated all controls were absolute.
3. **`0x12` = channel Off** established, replacing the earlier guess that it was an unknown
   marker specific to fader touch.

Also new: the `NO_EXP` variants, and the four source exports now under version control in
`xtouch-compact-config/`.
