# brownshoesonly (predecessor brand to VH.S)

Sources: **ModularGrid manufacturer page (vendors/view/161), fetched directly.** Earlier versions of this doc were assembled from sparse third-party listings; this version is the verified full catalog. The original site (brownshoesonly.com) is defunct.

## The key relationship: same maker as VH.S

**brownshoesonly and VH.S (Video Headroom Systems) are the same person.** brownshoesonly is the **earlier brand** (active ~2016–2019, Gen1-era LZX, often Euro 16-pin power); **VH.S is the continuation** with LZX **Gen3 power packs** and updated/expanded designs. Many VH.S modules are **successors** of brownshoesonly designs:

| brownshoesonly | → VH.S successor |
|---|---|
| **Video Grip (2018)** — 14 HP joystick | **VH.S VIDEO GRIP** (Gen3 update, joystick upgrade) |
| **SCANNER / scanner** | **VH.S SCANNERS** (dual 3:1) / **RGBSCAN** (triple, RGB cycling) |
| **bajascillator** (3-phase LFO) | **VH.S BAJA** (6-phase oscillator) |
| **Crossfade** (3-ch xfade/VCA) | **VH.S CROSSFADE** (3-ch xfade + luma out) |
| **5:1** voltage scaler | (voltage-conversion utility role) |
| mixers | **VH.S SUBMIX, RGBMIX, F4DER, 3VCA** |

Both brands are LZX-format third-party (**1 V standard**) — outside the owner's prefer-against list (that list is about LZX's own generations, not third-party makers).

## Full catalog (verified, ModularGrid)

| Module | HP | MSRP | Function | Tags |
|---|---|---|---|---|
| **QVAM** | 8 | $160 | Quad Video Attenuator Mixer | Attenuator / Mixer / Video |
| **TVVCA** | 10 | $215 | Triple Video VCA *(discontinued)* | VCA / Video |
| **Triple Summing Amp** | 6 | $120 | Sums one signal into 3 separate channels simultaneously | Video |
| **SCANNER** | 4 | $180 | 4-input video-rate interpolating scanner | Video |
| **Scanner (black panel)** | 4 | $180 | Same as SCANNER, black faceplate (cosmetic only) | Utility / Video / Panning / VCA |
| **scanner** (lowercase) | 4 | $200 | 4-input video-rate interpolating scanner — separate/revised entry | Panning / VCA / Video |
| **Triple Video LFO** | 8 | $150 | 3 discrete, skew LFOs | LFO / Video |
| **hexadirectional crossfader** | 18 | $400 | Complex crossfader (VBMv2 expander) | Expander / Mixer / VCA / Video |
| **Video Grip (2018)** | 14 | $400 | Joystick module (controller/expression) | Controller / Expression |
| **5:1** | 6 | $100 | Audio→video voltage converter (8× 5 V→1 V scalers) | Attenuator / Utility / Video |
| **5:1** (2nd entry) | 6 | $100 | Voltage converter | Attenuator / Utility / Video |
| **video soup** | 8 | $230 | Voltage-controlled video-rate mixer | Mixer / VCA / Video |
| **video mix** | 8 | $160 | 4-input video-rate mixer/attenuator | Mixer / Video / Attenuator |
| **Crossfade** | 8 | $200 | Three-channel crossfader / VCA | Video |

### Scanner variants — clarification
The catalog lists three scanner entries. **Faceplate (black vs standard) is purely cosmetic.** "SCANNER" ($180) and "Scanner (black panel)" ($180) are the same module, different panel. The lowercase "scanner" ($200) is a separate/revised entry at a higher price; all three carry the identical description "4 input video rate interpolating scanner." ⚠️ The functional difference between the $180 and $200 versions is not stated in the catalog — only price and category tags differ.

## Owner relevance notes
- These are **support/utility modules for an LZX core** — they process, mix, scale, and modulate within an LZX system; they don't generate or encode video on their own.
- For *adding* capability rather than duplicating owned gear (owner has SUBMIX, hexadirectional crossfader, Gainbrain): **video soup** (adds CV control over mixing) and **Triple Summing Amp** (signal distribution into 3 channels) are the least redundant. QVAM / video mix / Crossfade overlap the owner's existing mix/crossfade modules.

## Functional detail (patching-oriented)
Verified catalog above is from the ModularGrid manufacturer page; the notes below add the fuller "what you can do with it" layer (retained from earlier maker/forum sources). Additive only.

- **Triple Video LFO** — 3 discrete LFOs, dual-range switch + skew control, outputs ramp / triangle / sawtooth. Ranges cover slow fade/strobe and a wider fade/audio range. Built to drive faders/keyers (e.g. the Visionary TVF&KG) and to FM video oscillators.
- **hexadirectional crossfader** (owned) — VBMv2 expander: 4 signal inputs (center) + **6 CV inputs, one per fade direction**, with all video-rate crossfades available simultaneously; the 4 inputs chain from VBMv2 1a–1d and the 6 fade outs chain onward. Built for feedback loops / "knot-theory" multi-source blends.
- **5:1** — audio→video voltage converter: **8× 5 V→1 V scalers**, bringing standard Eurorack modulators (LFOs, envelopes) into the LZX 1 V range. Same role as the Visionary Voltage Bridge / Voltage Interface I.
- **video soup** — voltage-controlled, video-rate mixer (adds CV control over mixing — the least redundant vs the owner's existing mixers).
- **Triple Summing Amp** — sums one signal into 3 separate channels simultaneously (signal distribution).
- **Video Grip (2018)** — 14 HP joystick (controller/expression); the **ancestor of the VH.S VIDEO GRIP**.

### bajascillator — owned, but not on the current MG catalog table
The owner's rack includes a **brownshoesonly bajascillator** (8 HP, **3-phase LFO** — phase-related slow sweeps for animating parameters). It's the ancestor of the VH.S **BAJA** (6-phase). It appears in the successor map above but **not** in the verified ModularGrid catalog table (likely an older/discontinued entry no longer on the manufacturer page). Kept here because it's correct, owned data — see `references/my-rack.md`.
