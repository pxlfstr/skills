# vixid-vjx16-4-snapshots

`vsbk_to_syx.py` turns VJX16-4 Snapshot Manager bank files (`.vsbk`) into ready-to-send
SysEx recall messages, one `.syx` per snapshot, plus `snapshots_decoded.csv` listing each
snapshot's state in readable form.

## Provenance

- Format and message layout are documented in `../vixid-vjx16-4-midi.md` §3–§4 and not
  restated here.
- **Designed.** Checked against VIXID's four example banks (48 snapshots): output routing,
  Fx/Motion types, blend modes, mutes, layers and colour values agree with VIXID's own
  descriptions, with the two exceptions recorded in the protocol document. **Never sent to a
  mixer.**
- **Not committed:** VIXID's example banks. Vendor material.
- Python 3 standard library only.

## Use

```
py vsbk_to_syx.py out "Outputs_routing.vsbk" "Color_Variants.vsbk"
```

- Output: `out/<bank>/NN - <snapshot name>.syx` and `out/snapshots_decoded.csv`.
- macOS `._` metadata files are skipped with a message.
- Send a `.syx` with any SysEx sender; the mixer's MIDI Out must be in **Out** mode for the
  sync reply.

## Open items

- `<SendEnv>` not decoded: banks carrying it are packed with every apply flag on.
- Keyer "picker on" comes from the snapshot; VIXID's software uses the live value.
