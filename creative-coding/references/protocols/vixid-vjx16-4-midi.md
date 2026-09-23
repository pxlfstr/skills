# VIXID VJX16-4 — MIDI CC map, SysEx, Snapshot Manager, bank format

Everything needed to drive a VJX16-4 without VIXID's software: the documented CC map, the
undocumented SysEx sync and full-state recall, the Snapshot Manager's OSC/MIDI triggers, and
its `.vsbk` bank file format. Device behaviour lives in
`analog-video/references/vixid/vjx16-4.md` and is not restated here.

Decoder: `vixid-vjx16-4-snapshots/vsbk_to_syx.py` (this folder).

## Provenance

- **§1 CC map — `[Official]`:** *VJX16-4 16 Channel Video Mixer — User Guide* v5.8.3
  [Official], pp. 66–70, user-supplied PDF (created 2010-03-26). Text layer read in full;
  p. 70 also read as a page image.
- **§2–§4 SysEx, Snapshot Manager, bank format — `[Official]` source, decoded:** read
  2026-09-23 from VIXID's own *VJX16-4 Snapshot Manager* Java application (jar build
  2012-02-14), user-supplied, decompiled with CFR 0.152. Classes read: the mixer MIDI class,
  the controller MIDI class, the 5 × 128 state class, the send-flag class, the bank reader and
  writer, the OSC receiver. Class names in the jar are obfuscated, so none are cited here.
  The **licence/registration code was deliberately not read.** The supplied file was the jar
  with a 723,968-byte launcher stub in front of it.
- **§4 cross-check:** four VIXID example banks (`Outputs routing`, `PInP and Split Screens`,
  `Color Variants`, `FXs on Track1`, 48 snapshots) decoded and compared against VIXID's own
  description text in each snapshot. Results in §4.
- **User-facing behaviour — `[Official]`:** *VJX16-4 Snapshot Manager — User Manual*
  [Official], user-supplied PDF (21 pp., created 2011-12-05), read in full.
- **Not committed:** the application, the manuals, the example banks and the decompiled
  source. Vendor material; only derived facts are here.
- **Not bench-tested.** No SysEx in this document has been sent to a mixer.
- **Revised 2026-09-23, additive audit:** full initial-state table, MIDI Learn detail,
  permanent-bank MIDI reach, the MIDI map / prefs / shortcuts file formats, keyboard
  shortcuts, visualization panel, and remaining UI behaviour added.
- **Open contradictions:** the manual's channel-5 CC 5 label (resolved in §1 by the
  recall layout); two example-bank descriptions that disagree with their own data (§4).

---

## §1 — CC map (MIDI In)

- **Control Change only.** Channels 1–4 = tracks 1–4, channel 5 = master. Each channel can be
  disabled in Master → MIDI → MIDI In. [p. 66]
- Switches: 0–63 off, 64–127 on. Enumerations use equal bins; the SysEx packs them as
  `CC >> n` (§3), which matches every bin width below.

### Channels 1–4 (one per track)

| CC | Function | Values |
|---|---|---|
| 0–3 | Crop L, R, U, D | |
| 4, 5 | Scroll X, Y | |
| 6–9 | Blow L, R, U, D | |
| 10, 11 | Keyer Tolerance, Transition | |
| 12, 13 | Keyer picker X, Y | |
| 14, 15, 16 | Keyer colour 1 (R / Y), 2 (G / Cr), 3 (B / Cb) | Firmware v2.00+; previously CC 107–109 |
| 64 | Input | 0–31 In1 · 32–63 In2 · 64–95 In3 · 96–127 In4 |
| 65 / 66 / 67 / 68 / 69 | Solo / Mute / Negative / B&W / Bkg Alpha | on/off; Bkg Alpha off = black, on = alpha |
| 70 | Opacity | |
| 71 | Gain | |
| 72 | Blend | 0 Normal · 8 Additive · 16 Average · 24 Darken · 32 Lighten · 40 Stamp · 48 Diff · 56 Subtract · 64 Negation · 72 Xor · 80 Red · 88 Green · 96–127 Blue (8-wide bins) |
| 73 | Layer | 0–31 A · 32–63 B · 64–95 C · 96–127 D |
| 75–77 | RGB gain R, G, B | |
| 78–80 | RGB offset R, G, B | |
| 81–83 | Brightness, Contrast, Saturation | |
| 84 | Motion on/off | |
| 85 | Motion type | 0–31 Freeze · 32–63 Slowmo · 64–95 Strobe · 96–127 Bloc |
| 86, 87 | Motion N ("AlphaPeriod"), P ("Period") | |
| 88, 89 | Bloc size X, Y | |
| 90 | Crop on/off | |
| 91 | Crop type | 0–63 Crop · 64–127 CropCenter |
| 102 | Keyer on/off | |
| 103 | Keyer type | 0 Color · 16 Chroma · 32 Luma · 48 R Mask · 64 G Mask · 80–127 B Mask (16-wide) |
| 104 | Keyer source track | 32-wide bins, tracks 1–4 |
| 105 | Keyer source | 0–63 PreFx · 64–127 PostFx |
| 106 | Keyer Inverse | |
| 110 | Pick mode | 0–63 "Map" (manual) · 64–127 "Picker" (cursor) |
| 111 | Picker state | |
| 112 | Fx on/off | |
| 113 | Fx type | 0 MirrorL · 8 MirrorR · 16 MirrorU · 24 MirrorD · 32 FlipH · 40 FlipV · 48 Rot180 · 56 Blow · 64 Scroll · 72 ScrollWrap · 80 ScrollX · 88 ScrollY · 96 ScrollXWrap · 104 ScrollYWrap · 112–127 Mosaic (8-wide; manual prints "112-27") |
| 114, 115, 116 | Scroll Zoom X, Y, XY | |
| 117, 118, 119 | Mosaic Zoom X, Y, XY | |

**Fine-resolution partners — not in the manual.** The Snapshot Manager stores and sends
CC 32–48 as the low half of 14-bit pairs: crop 0–3 ↔ 32–35, scroll 4–5 ↔ 36–37,
tolerance/transition 10–11 ↔ 42–43, keyer colour 14–16 ↔ 46–48. [decoded, §3]

### Channel 5 (master)

| CC | Function | Values |
|---|---|---|
| 0 | Mix mode | 0–63 Compositing · 64–127 Battle 2×2 |
| 1 / 3 / 5 | Out1 / Out2 / Out3 config | 0–31 Master1 · 32–63 Master2 · 64–95 Preview · 96–127 Auto Preview |
| 2 / 4 / 6 | Out1 / Out2 / Out3 preview point | 8-wide bins: T1 PreFx 0 · PostFx 8 · Keyer 16 · OutBlend 24 · T2 32… · T3 64… · T4 96–127 |
| 7 | Wipes on/off | |
| 8 | Wipe type | Values not published ("Cf Table", no table) |
| 9 | Wipe track | 32-wide bins, tracks 1–4 |
| 10 | Wipe duration | |
| 11 | Wipe fader | |

- The manual labels CC 5 "Out2 Config". It is **Out3** — the recall message packs CC 5–6 in
  the Out3 byte (§3).
- **Not published:** CC 74, 92–101, 107–109 (old keyer colour), 120–127 on tracks; anything for
  the audio section.

### Scaling

- **RGB, BCS: panel value = 2 × CC.** VIXID's example bank descriptions give panel values
  128 / 100 / 60 where the data holds CC 64 / 50 / 30 (128/64 = 100/50 = 60/30 = 2). So
  **CC 64 = neutral**.
- ⚠️ Gain assumed the same: CC 64 = panel 128 = unity. Inferred from the pattern, not stated.
- **The Snapshot Manager's initial state table** (its model before any sync) — every
  non-zero value [decoded]:

| Where | CC = value |
|---|---|
| Every track | 4, 5 = 64 (scroll centre) · 6, 7 = 28 · 8, 9 = 22 (blow) · 10 = 17 (tol) · 11 = 1 (tran) · 12, 13 = 63 (picker) · 70 = 127 (opacity) · 71 = 64 (gain) · 75–83 = 64 (RGB, BCS) · 85 = 32 (Slowmo) · 86 = 5 · 87 = 25 · 88, 89 = 48 · 110 = 64 (Picker mode) · 113 = 64 (Scroll) · 114, 115 = 2 · 117, 118 = 14 |
| Every track, low halves | 38, 39 = 38 · 40, 41 = 16 · 42 = 25 · 43 = 55 · 44 = 75 · 45 = 92 |
| Per track | 73 (layer) and 104 (keyer source) = 0 / 32 / 64 / 96 for tracks 1–4 |
| Channel 5 | 1 = 0 (Out1 Master1) · 2 = 8 · 3 = 64 (Out2 Preview) · 4 = 8 (T1 PostFx) · 5 = 96 (Out3 Auto Preview) · 6 = 40 (T2 PostFx) |

  ⚠️ The low halves at 38–45 imply 14-bit pairs for blow and picker too, which the recall
  message doesn't carry. Whether this table mirrors the mixer's factory state is unknown.

### MIDI Out

- **Out** mode: panel moves only. **Thru** mode: MIDI In copy only. Never both. [p. 66]
- The Snapshot Manager requires **Out** mode.

## §2 — SysEx

Manufacturer ID bytes `00 20 6C`. Two messages are sent by the Snapshot Manager; none are
documented by VIXID.

| Message | Bytes | Length |
|---|---|---|
| Sync request | `F0 00 20 6C 00 01 F7` | 7 |
| Full-state recall | `F0 00 20 6C 00 00` + 211 data bytes + `F7` | 218 |

**Sync = state readback.** ⚠️ Inferred from the software's handling:

- After sending the sync request the software records **every CC arriving on channels 1–5**
  into its model of the mixer state.
- It declares sync good if **channel 4 CC 64** (track 4 input) arrives within **1.5 s**;
  otherwise it shows an error asking for mixer firmware **v2.11**.
- So the mixer appears to answer the request by transmitting its whole state as CCs, and a
  third-party tool can read the deck's current state this way.
- Between recalls the software keeps its model current from the ordinary panel-move CCs.

## §3 — Recall message layout

Byte index from `F0` = 0. Byte 4 = `00`, meaning unknown. Byte 5 = command (`00` recall,
`01` sync).

### Bytes 6–9 — apply flags and inputs

| Byte | Bit(s) | Meaning |
|---|---|---|
| 6 | 6 | Inputs |
| | 5 | Layer arrangement |
| | 4 | Blend modes |
| | 3 | Opacities |
| | 2 | Solos and mutes |
| | 1 | Negative and B&W |
| | 0 | Bkg Alpha |
| 7 | 6 | Gains |
| | 5 | Keyers |
| | 4 | Fx |
| | 3 | Motion |
| | 2 | Crops |
| | 1 | RGB balance |
| | 0 | BCS |
| 8 | 6 | Outputs |
| | 5–4 / 3–2 / 1–0 | Input, track 3 / 2 / 1 (CC 64 >> 5) |
| 9 | 5 / 4 / 3 / 2 | Track 4 / 3 / 2 / 1 **excluded** (1 = leave that track alone) |
| | 1–0 | Input, track 4 |

- The software always packs every value; the flags appear to tell the mixer what to apply.
  ⚠️ Inferred.

### Bytes 10–12 — outputs (channel 5)

| Byte | Bits |
|---|---|
| 10 | 6 Mix mode (CC 0 >> 6) · 5–4 Out1 config (CC 1 >> 5) · 3–0 Out1 preview point (CC 2 >> 3) |
| 11 | 5–4 Out2 config (CC 3) · 3–0 Out2 preview point (CC 4) |
| 12 | 5–4 Out3 config (CC 5) · 3–0 Out3 preview point (CC 6) |

### Bytes 13–216 — four 51-byte track blocks

Track *n* (0-based) starts at 13 + 51 × *n*. 13 + 4 × 51 = 217 = position of `F7`.

| Offset | Content (CC numbers on the track's channel) |
|---|---|
| 0 | b4 Solo · b3 Mute · b2 Negative · b1 B&W · b0 Bkg Alpha (each CC >> 6) |
| 1 | b5–2 Blend (CC 72 >> 3) · b1–0 Layer (CC 73 >> 5) |
| 2, 3 | Opacity 70 · Gain 71 |
| 4–9 | RGB gain 75, 76, 77 · RGB offset 78, 79, 80 |
| 10–12 | BCS 81, 82, 83 |
| 13 | b1 Crop on (90) · b0 CropCenter (91) |
| 14–21 | Crop pairs 0/32 · 1/33 · 2/34 · 3/35 |
| 22 | b4 Fx on (112) · b3–0 Fx type (113 >> 3) |
| 23–26 | Scroll X 4/36 · Scroll Y 5/37 |
| 27–30 | Blow 6, 7, 8, 9 |
| 31–34 | Zoom X 114 · Zoom Y 115 · Mosaic X 117 · Mosaic Y 118 |
| 35 | b3 Keyer on (102) · b2–0 Keyer type (103 >> 4) |
| 36 | b5–4 Source track (104 >> 5) · b3 Pre/Post (105) · b2 Inverse (106) · b1 Pick mode (110) · b0 Picker on (111) |
| 37–42 | Keyer colour pairs 14/46 · 15/47 · 16/48 |
| 43–46 | Tolerance 10/42 · Transition 11/43 |
| 47 | b2 Motion on (84) · b1–0 Motion type (85 >> 5) |
| 48, 49 | Motion N 86 · Motion P 87 |
| 50 | b5–3 Bloc X (88 >> 4) · b2–0 Bloc Y (89 >> 4) |

**Not carried by a recall:** Zoom XY (116, 119), picker X/Y (12, 13), wipes, audio.

- The software takes the **Picker on** bit from the mixer's live state, not from the stored
  snapshot.
- With Layers on and only some tracks included, the software rebuilds a consistent A–D order
  before packing: included tracks take their stored layer and the others shift by one layer
  step (32) to make room. With exactly one track included, layer order is left as it is.

## §4 — Snapshot Manager and `.vsbk` banks

### The application

- Java application (jar build 2012-02-14). Requires an activation key issued online by
  VIXID, which is **no longer obtainable** (user-stated).
- 10 banks × 12 snapshots, plus a 4-snapshot permanent bank, and a Load/Rec toggle.
  [Snapshot Manager User Manual]
- Rec stores the software's state model — built from the sync reply and incoming CCs — not a
  fresh read from the mixer. [decoded]
- Per-snapshot send flags ("SendEnv") map one-to-one to the §3 apply flags, plus per-track
  enables.
- Snapshot Chase: auto-steps a range at an interval in seconds.
- Snapshot operations: Rec stamps the date into the description and returns to Load;
  right-click Copy / Paste / Edit / Reset (Reset clears state, description and colour);
  per-snapshot button colour; bank and snapshot names and descriptions. [manual]
- **Visualization panel** shows, for each opacity fader and gain knob, three positions: the
  physical control, the value the mixer is actually using, and the value stored in the
  snapshot under the pointer. The software updates it from incoming CC 70 and CC 71.
  [manual + decoded]
- Activation dialog shows a **Computer ID** and asks for a **License Key**; it asks to be run
  with administrator rights. [strings in the jar's message bundle]
- Operator-fader "hang up": after a recall, a physical fader is ignored until it reaches the
  recalled value. ⚠️ Stated in the Snapshot Manager manual; unknown whether the mixer does this
  itself or only under the software.

### Remote triggers

| Protocol | Format | Source |
|---|---|---|
| MIDI | Note On (velocity > 0) on a learned channel; one note per snapshot via MIDI Learn | manual + decoded |
| OSC | `/bankX/snapshotY`, one float = **1.0**; X 1–10, Y 1–12; UDP port set by user (> 1023) | manual + decoded |

- **The permanent bank is not reachable over OSC** — the receiver drops any bank above 10.
  [decoded] **It is reachable over MIDI:** learned notes map to a global snapshot index,
  banks 0–119 (bank × 12 + slot) and permanent 120–123. [decoded]
- MIDI Learn: toggle it (Ctrl+M), click a snapshot, send a Note On. One MIDI channel is used
  for all triggers. A note already in use prompts **Continue** (move it) or **Cancel**.
  The controller monitor shows only Note On, Note Off and CC. [manual]
- The trigger controller gets its own MIDI In, separate from the two mixer ports. [manual]
- The manual's example `/ bank3/snapshot10` has a stray space; the parser expects none.

### `.vsbk` bank file

XML, one bank:

```
<Bank>
  <Header><Name/><Description/></Header>
  <Snapshot> ×12
    <Name/> <Description/> <SendEnv/>? <Color><Red/><Green/><Blue/></Color>? <ModificationDate/>
    <Data/>
  </Snapshot>
</Bank>
```

- `<Data>` = **1,280 hex characters** = 5 channels × 128 CC values, 2 hex digits each, in
  order channel 1 CC 0 … channel 5 CC 127.
- No `<SendEnv>` → every flag on (the send-flag class defaults all true).
- `<SendEnv>` text format: ⚠️ not decoded; none of the four example banks carries it.
- **MIDI map file** (Save / Load MIDI Mapping):
  `<MidiMap><Header><Version>MidiMap-v1.0</Version></Header><MidiChannel/>` then one
  `<Snapshot><Nb/><Note/></Snapshot>` per assignment. [decoded; no file examined]
- **Other files it writes** [decoded, names only]: preferences `<Prefs><MIDI_IO><MIDI_In/>
  <MIDI_Out/><MIDI_Ctrl_In/></MIDI_IO><LoadProject/><History><Path0/>…<Path9/></History>`;
  shortcuts `<Shortcuts><Snapshot><Number/><KeyCode/>…</Snapshot></Shortcuts>` for the 12 load
  keys; a language file; a licence file.
- Projects wrap banks in `<Project><Version/><OSC><Enable/><IncomingPort/></OSC><Banks>…
  </Banks><PreferredBank/><MidiMap/></Project>`. ⚠️ Element names read from the writer only; no
  project file examined.

### Cross-check against VIXID's example banks

48 snapshots decoded; each compared with the description VIXID wrote into it.

| Field | Result |
|---|---|
| Fx and Motion types, B&W, Negative, blend modes, mutes, layers | All match |
| Output routing | 11 of 12 match |
| RGB / BCS scale | Matches at 2 × CC (see §1 *Scaling*) |

⚠️ **Disagreements, left in place:**
- *Outputs routing* #6: description says Out2 = Track 1; data holds Track 2 PostFx
  (channel 5 CC 4 = 40).
- *Outputs routing* #4 and #12: described as 75 % and 50 % opacity; both store about 80
  (80/127 = 63 %).

### Keyboard shortcuts

[Snapshot Manager User Manual, appendix]

| Keys | Action |
|---|---|
| Ctrl press / release | Toggle Rec / Load |
| `1`–`9`, `0`, `-`, `=` | Load snapshot 1–12 of the current bank |
| Ctrl + the same keys | Record snapshot 1–12 |
| Ctrl+Backspace | Reset snapshot |
| Arrows · Enter / Space | Choose snapshot · load it |
| Ctrl+C / Ctrl+V | Copy / paste snapshot |
| Page Up / Page Down | Previous / next bank |
| Ctrl+E · Esc | Edit / finish edit · cancel edit |
| Alt+Left / Right | Change right-panel tab |
| Ctrl+N / O / S | New / open / save project |
| Ctrl+M | Toggle MIDI Learn |
| Alt+F / C / H | File / Communication / Help menu |

## Not yet verified — open items

- **Bench test:** send the sync request and one recall to a mixer; capture the reply.
- What firmware versions answer the sync request (the software wants v2.11+).
- Byte 4 of the SysEx header.
- `<SendEnv>` text format.
- Whether "hang up" pickup happens on CC-driven changes, SysEx recalls, or neither.
- Wipe type CC values; audio-section CCs.
- Whether the initial-state table mirrors the mixer's factory defaults; the 38–45 low halves.
- MIDI map `<Note>` numbering (the learn code stores note + 1 in one place) — check against a
  saved map file.

| Section | Status |
|---|---|
| §1 CC map | `[Official]` manual; not bench-tested |
| §1 CC 32–48 pairs, Out3 correction | Decoded from vendor software |
| §1 Scaling | Computed from vendor example banks; gain ⚠️ inferred |
| §2 Messages | Decoded; sync-as-readback ⚠️ inferred |
| §3 Layout | Decoded; consistent with 48 vendor snapshots; not sent to hardware |
| §4 Triggers, file format | Manual + decoded; `<SendEnv>` and project format ⚠️ unverified |
