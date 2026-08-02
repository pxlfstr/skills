#!/usr/bin/env python3
"""
Decode Behringer X-Touch Editor .bin layer exports.

    python decode.py LayerA-with_EXP.bin
    python decode.py *.bin --compare

Format is undocumented by Behringer. Everything below was reverse-engineered
from Obie's own exports by comparing layer pairs byte for byte; see
../xtouch-compact-midi-map.md for the provenance and the decoded map.

Header   5 bytes, always 20 15 01 04 03. Identical in every file — the layer
         is NOT identified in the header, only by filename.

Records  91, immediately after the header:

    [0] channel   0 = ch1 ... 15 = ch16, 0x12 = Off
    [1] type      0 = CC, 1 = Note
    [2] index     raw MIDI CC or note number
    [3] min       encoder mode lives here: 0 = absolute, 130 = Relative 1
                  (two's complement). Values for Relative 2 and 3 unknown.
    [4] max       127 throughout in every file seen so far
    [5..] trailing zeros

Record length is 7 bytes for the nine faders and the expression pedal,
8 bytes for the other 81. What decides the length is not known — the extra
byte has been zero in every file examined. Do not assume a fixed stride.
"""

import sys

HEADER = bytes([0x20, 0x15, 0x01, 0x04, 0x03])
CH_OFF = 0x12

# Record start offsets, derived empirically and constant across all exports.
STARTS = list(range(5, 68, 7)) + list(range(68, 636, 8)) + [636] + list(range(643, 723, 8))

# Physical control names by position. The grouping and note ranges below are
# byte-derived and verified; which physical row is "top" versus "bottom" is
# Obie's own labelling from ../xtouch-compact-midi-map.md, not readable from
# the file.
NAMES = (
    [f"fader{i}" for i in range(1, 10)]          # CC 0-8
    + [f"enc{i}" for i in range(1, 9)]           # CC 10-17
    + [f"encpush{i}" for i in range(1, 9)]       # note 96-103
    + [f"enc{i}" for i in range(9, 17)]          # CC 18-25
    + [f"encpush{i}" for i in range(9, 17)]      # note 108-115
    + [f"btn_top{i}" for i in range(1, 9)]       # note 36-43
    + [f"btn_mid{i}" for i in range(1, 9)]       # note 48-55
    + [f"btn_bot{i}" for i in range(1, 9)]       # note 60-67
    + [f"btn_fader{i}" for i in range(1, 10)]    # note 72-79 + 80 (below Main)
    + [f"btn_grid{i}" for i in range(1, 7)]      # note 84-89
    + ["exp_pedal", "footswitch"]                # CC 30, CC 31
    + [f"fader_touch{i}" for i in range(1, 10)]  # CC 100-108
)


def channel(v):
    return "Off" if v == CH_OFF else f"ch{v + 1}"


# Encoder mode is stored in the min byte. Only these two values have been seen.
# 130 was confirmed by setting all sixteen encoders to Relative 1 in the Editor
# and re-exporting — single variable, unambiguous. Relative 2 and 3 have never
# been exported, so their byte values are unknown.
ENC_MODE = {0: "absolute", 130: "relative1"}


def enc_mode(v):
    return ENC_MODE.get(v, f"unknown({v})")


def read(path):
    d = open(path, "rb").read()
    if d[:5] != HEADER:
        raise SystemExit(f"{path}: unexpected header {d[:5].hex(' ')}")
    if len(d) != 723:
        raise SystemExit(f"{path}: expected 723 bytes, got {len(d)}")
    out = []
    for n, s in enumerate(STARTS):
        out.append(
            {
                "offset": s,
                "control": NAMES[n] if n < len(NAMES) else f"record{n}",
                "channel": d[s],
                "type": "note" if d[s + 1] == 1 else "cc",
                "index": d[s + 2],
                "min": d[s + 3],
                "max": d[s + 4],
            }
        )
    return out


def dump(path):
    print(f"\n=== {path} ===")
    print(f"{'control':<16}{'type':<6}{'num':>5}{'channel':>10}{'min':>6}{'max':>6}  mode")
    for r in read(path):
        mode = enc_mode(r["min"]) if r["control"].startswith("enc") and not r[
            "control"].startswith("encpush") else ""
        print(
            f"{r['control']:<16}{r['type']:<6}{r['index']:>5}"
            f"{channel(r['channel']):>10}{r['min']:>6}{r['max']:>6}  {mode}"
        )


def compare(paths):
    """Compare every file against the first. Reports channel-only differences
    separately, because a Layer A/B pair is expected to differ that way."""
    base = read(paths[0])
    for p in paths[1:]:
        other = read(p)
        chan_only, deeper = 0, []
        for a, b in zip(base, other):
            if a == b:
                continue
            if {k: v for k, v in a.items() if k != "channel"} == {
                k: v for k, v in b.items() if k != "channel"
            }:
                chan_only += 1
            else:
                deeper.append((a, b))
        print(f"\n{paths[0]}  vs  {p}")
        print(f"  channel-only differences : {chan_only}")
        print(f"  deeper differences       : {len(deeper)}")
        for a, b in deeper:
            print(
                f"    {a['control']:<16} "
                f"{channel(a['channel'])} {a['type']}{a['index']}"
                f"   |   {channel(b['channel'])} {b['type']}{b['index']}"
            )


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        raise SystemExit(__doc__)
    if "--compare" in sys.argv:
        if len(args) < 2:
            raise SystemExit("--compare needs at least two files")
        compare(args)
    else:
        for p in args:
            dump(p)
