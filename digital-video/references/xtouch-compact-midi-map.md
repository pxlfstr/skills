# X-Touch Compact — MIDI map

**Rig-specific. Does NOT go in the public `pxlfstr/skills` repo.**

Derived 2026-08-01 from `LayerA.bin` / `LayerB.bin` exported from X-Touch Editor.
Physical control labels supplied by Obie. 91 assignments per layer, all accounted for.

Octave convention: **C3 = 60 (Yamaha/Steinberg)**.

---

## Number conventions — three of them, don't mix them up

| Where | Convention |
|---|---|
| `.bin` file | Raw MIDI (CC 0–127, note 0–127) |
| X-Touch Editor display | Raw — matches the file |
| MIDI In DAT | **Always 1-based**, no parameter. Documented by Derivative |
| MIDI In CHOP | Raw by default; `1 Based Index` (`onebased`) switches it. **Affects notes AND controllers** |
| MIDI Out CHOP | **0-based by default**; same `onebased` parameter available |

The "TD (1-based)" column below is what you'll see in the DAT, and in the CHOP if `onebased` is on.

---

## Continuous controls

| Control | CC (raw) | TD (1-based) | Layer A ch | Layer B ch |
|---|---|---|---|---|
| Faders 1–9 | 0–8 | 1–9 | 1 | 2 |
| Encoders 1–8 (top row) | 10–17 | 11–18 | 1 | 2 |
| Encoders 9–16 (right side) | 18–25 | 19–26 | 1 | 2 |
| Expression pedal | 30 | 31 | 1 | **1** — intentional, layer-independent |
| Foot switch | 31 | 32 | 1 | 2 |

## Buttons

| Row | Notes (raw) | Note names | TD (1-based) | Count | Layer B ch |
|---|---|---|---|---|---|
| Top row | 36–43 | C1–G1 | 37–44 | 8 | 2 |
| Middle row | 48–55 | C2–G2 | 49–56 | 8 | 2 |
| Bottom row | 60–67 | C3–G3 | 61–68 | 8 | 2 |
| Below faders 1–8 | 72–79 | C4–G4 | 73–80 | 8 | 2 |
| Below Main fader (9) | 80 | G#4 | 81 | 1 | 2 |
| Playback control grid | 84–89 | C5–F5 | 85–90 | 6 | 2 |
| Encoder push 1–8 | 96–103 | C6–G6 | 97–104 | 8 | 2 |
| Encoder push 9–16 | 108–115 | C7–G7 | 109–116 | 8 | 2 |

Every button block runs **C through G** except two: the below-faders row is nine wide
(C4–G#4) because of the Main fader button, and the playback grid is six (C4–F5).

## Fader touch

| Control | CC (raw) | TD (1-based) | Layers |
|---|---|---|---|
| Fader touch 1–9 | 101–109 | 102–110 | Identical in both files |

⚠️ **Partly inferred.** These nine records are byte-identical across layers and carry `0x12`
in the field every other record uses for MIDI channel. The count matches the nine faders and
the CC range matches what we have recorded for fader touch — but our bench note records
101–109 as *observed*, which would mean raw 100–108, one lower than stored here.
**Unresolved off-by-one. Confirm against a DAT capture before building on it.**

---

## One control stays on channel 1 in Layer B

**CC 30 — expression pedal.** Intentional, layer-independent by design. Everything else on
Layer B transmits on channel 2.

*(Note 80 / G#4, the button below the Main fader, was also on channel 1 in the dump analysed
here. That was an oversight in the Editor config and Obie corrected it to channel 2 on
2026-08-01. **The `.bin` files this table was derived from predate that fix** — re-export the
layers if you need dumps that match the device.)*

**Consequence for TouchDesigner:** with `Channel Prefix` blank on the MIDI In CHOP, input
from multiple MIDI channels **merges into one set of CHOP channels**. The expression pedal
would then land silently in the Layer A stream. Set `prefix` to `ch` before adding Layer B.

---

## All values full-range

Every one of the 91 assignments is min `0` / max `127`. No scaling configured in the Editor —
do any normalizing in TouchDesigner.

---

## Provenance

- **Verified from the byte comparison:** channel, message type (CC vs Note), index, min, max.
  The two files differ in exactly one way — the channel byte — which makes those fields
  unambiguous.
- **Supplied by Obie:** every physical control label, the C3=60 convention, expression pedal
  intent, the Main fader button identification, and the G#4 channel fix.
- **Inferred:** the fader touch group (see caveat above).
- **Unexplained:** the `0x12` byte on the touch records, and the trailing bytes on every
  record. The `.bin` format is undocumented and reverse-engineered.
