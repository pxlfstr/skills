# X-Touch Compact — MIDI map

The user's own X-Touch Compact configuration, as loaded on the device. Not the Behringer
factory map — for that see `behringer-xtouch-compact-resolume.md`.

Approved for the public repo: this is device configuration for a commercial controller, not
rig, client or venue detail.

## Provenance

- **Tier: `[Official]` for the assignment table** — every number below is read out of the
  device's own configuration files, not from documentation or from observation of traffic.
- **Source files:** `Touchdesigner-X_Touch-LayerA.bin` and `Touchdesigner-X_Touch-LayerB.bin`,
  exported from X-Touch Editor and supplied 2026-08-01. 723 bytes each, 91 assignment records
  each, all 91 decoded and accounted for in both files.
- **Method:** byte comparison of the two files plus structural decode. The two layers differ in
  exactly 81 bytes, every one of them a channel byte changing 0→1 — which pins the channel,
  type, index, min and max fields unambiguously. Record boundaries were derived from those
  81 offsets plus the 10 records that are identical across layers.
- **Supplied by Obie, not derived from the files:** every physical control label, the C3 = 60
  octave convention, and the design intent behind the expression-pedal channel exception.
  The `.bin` files carry no labels.
- **Supersedes** the version derived 2026-08-01 from the earlier pair of exports. One record
  changed — see *What changed* at the end.
- **Not read:** no X-Touch Editor documentation of the `.bin` format was consulted; none is
  known to be published. The format decode below is reverse-engineered from these two files
  alone and has not been tested against a file with different min/max values, a different
  device, or a differently-sized assignment set.
- **Not verified against hardware in this pass.** The table states what the configuration
  files contain. It does not confirm what the device transmits — for that, bench captures are
  recorded in the working notes, and one known discrepancy is parked below.
- **Open, unresolved:** fader touch numbering (parked, see below); the meaning of the `0x12`
  byte and of the trailing bytes on every record.

---

## Number conventions — three of them, don't mix them up

| Where | Convention |
|---|---|
| `.bin` file | Raw MIDI (CC 0–127, note 0–127) |
| X-Touch Editor display | Raw — matches the file |
| MIDI In DAT | **Always 1-based**, no parameter. Documented by Derivative |
| MIDI In CHOP | Raw by default; `1 Based Index` (`onebased`) switches it. **Affects notes AND controllers** |
| MIDI Out CHOP | **0-based by default**; same `onebased` parameter available |

The "TD (1-based)" column below is what you'll see in the DAT, and in the CHOP if `onebased`
is on.

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

CC 9 is unassigned. So is everything from 26–29 and 32 upward, apart from the parked fader
touch block.

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

Every button block runs **C through G** except two: the below-faders row is nine wide
(C4–G#4) because of the Main fader button, and the playback grid is six (C5–F5).

Blocks are spaced with gaps — 44–47, 56–59, 68–71, 81–83, 90–95, 104–107 carry nothing. The
gaps are what keep every block starting on a C.

## Fader touch — parked, not in use

Nine records exist in both files, CC 101–109 raw, byte-identical across layers. They carry
`0x12` in the field every other record uses for MIDI channel, so they are not channel-assigned
the way the rest of the map is.

**Deliberately unused.** Obie is ignoring fader touch until there is a reason to use it. Kept
here only so the record count reconciles at 91 and so the open question isn't silently lost:

⚠️ There is an unresolved off-by-one. The files store 101–109 raw, which would appear as
102–110 in a MIDI In DAT. A bench note records touch arriving as 101–109 *as displayed*,
which implies raw 100–108. One DAT capture of a single fader touch settles it. Do not build
on either number until then.

---

## Layer B is channel 2, with exactly one exception

Every assignment transmits on **channel 1 in Layer A and channel 2 in Layer B**, at the same
control number. One record breaks that, on purpose:

**CC 30 — expression pedal. Channel 1 in both layers.** Verified: it is the only
channel-1 record in the Layer B file.

The point is layer detection. The hardware Layer A/B buttons transmit nothing, so the host
cannot see a layer change on the surface. Channel now identifies the bank on every message,
and the pedal stays reachable regardless of bank.

**Consequence for TouchDesigner:** with `Channel Prefix` blank on the MIDI In CHOP, input from
multiple MIDI channels **merges into one set of CHOP channels**. The expression pedal would
then land silently in the Layer A stream. Set `prefix` to `ch` before adding Layer B.

## All values full-range

All 91 assignments in both files are min `0` / max `127`. No scaling configured in the Editor —
do any normalizing in TouchDesigner.

---

## `.bin` file format — reverse-engineered

Undocumented. Decoded from these two files only; treat as provisional.

**Header:** 5 bytes, `20 15 01 04 03`. **Identical in both files** — the layer is not identified
in the header, only by filename. Don't rely on file content to tell you which layer you have.

**Records:** 91, immediately following the header, each

```
[0] channel   0 = ch1, 1 = ch2   (0x12 on the nine fader-touch records — meaning unknown)
[1] type      0 = CC, 1 = Note
[2] index     raw MIDI CC or note number
[3] min       0 in every record here
[4] max       127 in every record here
[5..] trailing zeros
```

Record length is **7 bytes for the nine faders and for the expression pedal, 8 bytes for the
other 81.** What determines the length is not known; the extra byte is zero in every case
observed. A parser should not assume a fixed stride.

**Record order** in the file is not the physical layout order: faders, encoders 1–8, encoder
push 1–8, encoders 9–16, encoder push 9–16, then the button rows bottom-numbered-first, then
expression pedal, foot switch, fader touch.

---

## What changed from the previous version of this document

One record. **Note 80 (G#4, the button below the Main fader) now transmits on channel 2 in
Layer B.** It was on channel 1 in the earlier export — an oversight in the Editor config that
Obie corrected on 2026-08-01. These files postdate the fix, so the caveat that used to sit here
is resolved and has been removed.

The other 90 records are unchanged.
