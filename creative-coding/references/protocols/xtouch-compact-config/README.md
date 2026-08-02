# X-Touch Compact — Editor config exports

Raw `.bin` layer exports from X-Touch Editor, kept under version control so every
save to the device leaves a traceable change.

`../xtouch-compact-midi-map.md` is the human-readable decode of these files. **The two
drift the moment a `.bin` changes without the document being regenerated** — run
`decode.py` and update the document in the same commit.

## Files

| File | Layer | Expression pedal |
|---|---|---|
| `Touchdesigner-X_Touch-LayerA-with_EXP.bin` | A — channel 1 | CC 30, channel 1 |
| `Touchdesigner-X_Touch-LayerA-NO_EXP.bin` | A — channel 1 | Off |
| `Touchdesigner-X_Touch-LayerB-with_EXP.bin` | B — channel 2 | CC 30, channel 1 |
| `Touchdesigner-X_Touch-LayerB-NO_EXP.bin` | B — channel 2 | Off |

The pedal is deliberately pinned to **channel 1 in both layers** so it stays reachable
regardless of the active bank. It is the only control that does not follow the layer's
channel.

The two `NO_EXP` variants exist because an assigned-but-unterminated expression jack
emits spurious CC 30 on fast fader-9 movement. With no pedal plugged in, load a
`NO_EXP` layer or the noise comes back.

**Filenames are the Editor's own, fixed and not timestamped.** The Editor writes straight
into this folder, so overwriting the same four names is what makes each save show up as a
change in git. Superseded exports go in `archive/` with a date prefix.

## Usage

```
python decode.py Touchdesigner-X_Touch-LayerA-with_EXP.bin
python decode.py *.bin --compare
```

`--compare` checks every file against the first and separates channel-only differences
from deeper ones. A correct Layer A/B pair differs by **90 records, channel only** — 81
controls plus the 9 fader-touch records. Anything under "deeper differences" means the
two layers have drifted apart in numbering, which is almost always a stale export.

## File format

Undocumented by Behringer. Reverse-engineered by comparing layer pairs byte for byte;
full provenance is in the map document.

**Header** — 5 bytes, `20 15 01 04 03`. Identical in every file. The layer is **not**
identified in the header, only by filename.

**Records** — 91, immediately following the header:

```
[0] channel   0 = ch1 ... 15 = ch16, 0x12 = Off
[1] type      0 = CC, 1 = Note
[2] index     raw MIDI CC or note number
[3] min       encoder mode: 0 = absolute, 130 = Relative 1 (two's complement)
[4] max       127 in every file so far
[5..]         trailing zeros
```

Record length is **7 bytes for the nine faders and the expression pedal, 8 for the other
81**. What decides the length is not established — the extra byte has been zero in every
file examined. A parser must not assume a fixed stride.

⚠️ **Open:** whether the 8-byte records use their extra byte for button push behaviour
and encoder ring mode. Plausible, since exactly those controls have such a setting and
faders do not, but every export so far has that byte at zero, so it has never been seen
to change.

## Record order

Byte-derived and verified: faders, encoders 1–8, encoder pushes 1–8, encoders 9–16,
encoder pushes 9–16, the button blocks in ascending note order, expression pedal, foot
switch, fader touch.

⚠️ Which physical row is "top" versus "bottom" is **Obie's labelling**, not readable from
the file. `decode.py` uses the names from the map document.

## Archive

`archive/` holds superseded exports, date-prefixed. Kept rather than deleted so a change
in device behaviour can be traced to the config change that caused it.
