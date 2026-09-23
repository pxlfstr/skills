# VJX16-4 Snapshot Manager bank (.vsbk) -> SysEx recall messages + readable summary
#
# Format and message layout: creative-coding/references/protocols/vixid-vjx16-4-midi.md
#   §3  recall message layout (218 bytes: F0 00 20 6C 00 00 <211 bytes> F7)
#   §4  .vsbk bank file format (<Data> = 5 x 128 CC values as hex)
#   §1  CC names and value bins (User Guide v5.8.3 pp. 67-70)
#
# Status: Designed. Output checked against 48 VIXID example snapshots and their descriptions;
# NOT sent to a mixer.
# UNVERIFIED: the <SendEnv> text format - banks that carry it are packed with all flags on.
# Note: VIXID's software takes the keyer "picker on" bit from the mixer's live state; offline,
# this script uses the value stored in the snapshot.
#
# Usage (Windows):  py vsbk_to_syx.py <out_folder> <bank.vsbk> [more.vsbk ...]
# Writes one .syx per snapshot (a folder per bank) and snapshots_decoded.csv.

import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HEADER = [0xF0, 0x00, 0x20, 0x6C, 0x00]
MSG_LEN = 218

BLEND = ["Normal", "Additive", "Average", "Darken", "Lighten", "Stamp", "Diff", "Subtract",
         "Negation", "Xor", "Red", "Green", "Blue", "Blue", "Blue", "Blue"]
FX = ["MirrorL", "MirrorR", "MirrorU", "MirrorD", "FlipH", "FlipV", "Rot180", "Blow", "Scroll",
      "ScrollWrap", "ScrollX", "ScrollY", "ScrollXWrap", "ScrollYWrap", "Mosaic", "Mosaic"]
KEYER = ["Color", "Chroma", "Luma", "RMask", "GMask", "BMask", "BMask", "BMask"]
MOTION = ["Freeze", "Slowmo", "Strobe", "Bloc"]
OUTCFG = ["Master1", "Master2", "Preview", "AutoPreview"]
PREVIEW = ["PreFx", "PostFx", "Keyer", "OutBlend"]


def parse_data(hexstr):
    hexstr = hexstr.strip()
    if len(hexstr) != 1280:
        raise ValueError("Data field is %d chars, expected 1280" % len(hexstr))
    v = [int(hexstr[i:i + 2], 16) for i in range(0, 1280, 2)]
    return [v[ch * 128:(ch + 1) * 128] for ch in range(5)]


def pack(ar, flags=None, tracks=(True, True, True, True)):
    f = dict.fromkeys(["inputs", "layer", "blend", "opacity", "solomute", "negbw", "bkgalpha",
                       "gain", "keyer", "fx", "motion", "crop", "rgb", "bcs", "outputs"], True)
    if flags:
        f.update(flags)
    m = [0] * MSG_LEN
    m[0:5] = HEADER
    m[5] = 0x00
    # bytes 6-9
    b = 0
    for bit, k in ((64, "inputs"), (32, "layer"), (16, "blend"), (8, "opacity"),
                   (4, "solomute"), (2, "negbw"), (1, "bkgalpha")):
        if f[k]:
            b |= bit
    m[6] = b
    b = 0
    for bit, k in ((64, "gain"), (32, "keyer"), (16, "fx"), (8, "motion"),
                   (4, "crop"), (2, "rgb"), (1, "bcs")):
        if f[k]:
            b |= bit
    m[7] = b
    m[8] = (64 if f["outputs"] else 0) | (ar[2][64] >> 5) << 4 | (ar[1][64] >> 5) << 2 | (ar[0][64] >> 5)
    b = 0
    for bit, on in ((32, tracks[3]), (16, tracks[2]), (8, tracks[1]), (4, tracks[0])):
        if not on:
            b |= bit
    m[9] = b | (ar[3][64] >> 5)
    # bytes 10-12
    M = ar[4]
    m[10] = (M[0] >> 6) << 6 | (M[1] >> 5) << 4 | (M[2] >> 3)
    m[11] = (M[3] >> 5) << 4 | (M[4] >> 3)
    m[12] = (M[5] >> 5) << 4 | (M[6] >> 3)
    # bytes 13-216
    for t in range(4):
        a = ar[t]
        o = 13 + t * 51
        blk = [
            (a[65] >> 6) << 4 | (a[66] >> 6) << 3 | (a[67] >> 6) << 2 | (a[68] >> 6) << 1 | (a[69] >> 6),
            (a[72] >> 3) << 2 | (a[73] >> 5),
            a[70], a[71],
            a[75], a[76], a[77], a[78], a[79], a[80],
            a[81], a[82], a[83],
            (a[90] >> 6) << 1 | (a[91] >> 6),
            a[0], a[32], a[1], a[33], a[2], a[34], a[3], a[35],
            (a[112] >> 6) << 4 | (a[113] >> 3),
            a[4], a[36], a[5], a[37],
            a[6], a[7], a[8], a[9],
            a[114], a[115], a[117], a[118],
            (a[102] >> 6) << 3 | (a[103] >> 4),
            (a[104] >> 5) << 4 | (a[105] >> 6) << 3 | (a[106] >> 6) << 2 | (a[110] >> 6) << 1 | (a[111] >> 6),
            a[14], a[46], a[15], a[47], a[16], a[48],
            a[10], a[42], a[11], a[43],
            (a[84] >> 6) << 2 | (a[85] >> 5),
            a[86], a[87],
            (a[88] >> 4) << 3 | (a[89] >> 4),
        ]
        assert len(blk) == 51
        m[o:o + 51] = blk
    m[217] = 0xF7
    bad = [i for i, x in enumerate(m[1:-1], 1) if x > 0x7F]
    if bad:
        raise ValueError("data bytes over 7 bits at %s" % bad)
    return bytes(m)


def summary(ar):
    rows = []
    M = ar[4]
    rows.append(("Master", "Mix mode", "Battle 2x2" if M[0] >= 64 else "Compositing"))
    for n, (c, p) in enumerate(((1, 2), (3, 4), (5, 6)), 1):
        cfg = OUTCFG[M[c] >> 5]
        pt = M[p] >> 3
        val = cfg if cfg.startswith("Master") else "%s - Track%d %s" % (cfg, pt // 4 + 1, PREVIEW[pt % 4])
        rows.append(("Master", "Out%d" % n, val))
    for t in range(4):
        a = ar[t]
        T = "Track%d" % (t + 1)
        rows.append((T, "Input", "%d (%s)" % ((a[64] >> 5) + 1, "COMP" if a[64] < 64 else "SVIDEO")))
        rows.append((T, "Layer", "ABCD"[a[73] >> 5]))
        rows.append((T, "Opacity / Gain", "%d / %d" % (a[70], a[71])))
        rows.append((T, "Blend", BLEND[a[72] >> 3]))
        st = [n for n, cc in (("Solo", 65), ("Mute", 66), ("Neg", 67), ("B&W", 68), ("BkgAlpha", 69)) if a[cc] >= 64]
        rows.append((T, "Switches", ", ".join(st) or "-"))
        rows.append((T, "RGB gain / offset", "%d %d %d / %d %d %d" % tuple(a[75:81])))
        rows.append((T, "BCS", "%d %d %d" % tuple(a[81:84])))
        if a[90] >= 64:
            rows.append((T, "Crop", "%s L%d R%d U%d D%d" % ((("CropCenter" if a[91] >= 64 else "Crop"),) + tuple(a[0:4]))))
        if a[112] >= 64:
            rows.append((T, "Fx", "%s zoom %d/%d scroll %d/%d blow %d %d %d %d mosaic %d/%d" % (
                FX[a[113] >> 3], a[114], a[115], a[4], a[5], a[6], a[7], a[8], a[9], a[117], a[118])))
        if a[84] >= 64:
            rows.append((T, "Motion", "%s N%d P%d bloc %d/%d" % (MOTION[a[85] >> 5], a[86], a[87], a[88], a[89])))
        if a[102] >= 64:
            rows.append((T, "Keyer", "%s src Track%d %s%s tol %d tran %d col %d %d %d" % (
                KEYER[a[103] >> 4], (a[104] >> 5) + 1, "PostFx" if a[105] >= 64 else "PreFx",
                " Inverse" if a[106] >= 64 else "", a[10], a[11], a[14], a[15], a[16])))
    return rows


def safe(s):
    s = re.sub(r'[\\/:*?"<>|\r\n]+', "_", s)
    s = re.sub(r"\s+", " ", s).strip().rstrip(".")
    return s or "unnamed"


def main(inputs, outdir):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    with open(outdir / "snapshots_decoded.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Bank", "Slot", "Snapshot", "Section", "Field", "Value"])
        for path in inputs:
            try:
                root = ET.parse(path).getroot()
            except ET.ParseError:
                # macOS "._" metadata files sit beside real banks and are not XML
                print("SKIPPED (not a bank file): %s" % path)
                continue
            if root.tag != "Bank":
                print("SKIPPED (not a bank file): %s" % path)
                continue
            bank = root.findtext("Header/Name") or Path(path).stem
            bdir = outdir / safe(Path(path).stem)
            bdir.mkdir(exist_ok=True)
            for i, s in enumerate(root.findall("Snapshot"), 1):
                name = s.findtext("Name") or "Snapshot %d" % i
                if s.find("SendEnv") is not None:
                    print("NOTE: %s #%d has SendEnv - flags left at all-on (format unverified)" % (bank, i))
                ar = parse_data(s.findtext("Data"))
                (bdir / ("%02d - %s.syx" % (i, safe(name)))).write_bytes(pack(ar))
                for sec, field, val in summary(ar):
                    w.writerow([bank, i, name, sec, field, val])
    print("done ->", outdir)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: py vsbk_to_syx.py <out_folder> <bank.vsbk> [more.vsbk ...]")
        sys.exit(1)
    main(sys.argv[2:], sys.argv[1])
