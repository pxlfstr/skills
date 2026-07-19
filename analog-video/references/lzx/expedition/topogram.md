# Topogram (Expedition series)

Source: LZX community Legacy Docs ("All About Topogram"). This is the only documentation LZX published for Topogram.

**Function:** Sequential **soft key generator / multiband keyer-colorizer.** Slices a single luma video or pattern input into discrete value bands for colorization and control. Edge transitions have voltage-controlled gain (hard edges ↔ smooth gradients); the upper and lower thresholds of the keying range are each separately voltage-controllable. Fully active, all-analog signal path; CV attenuverters have a center deadband. Bandwidth handles up to 1080i while staying sharp.

**Outputs:** six non-overlapping band regions (for 6-band colorizer patterns) plus eight more outputs that group/span multiple ranges. A Thru output can be fed back into the gain/upper/lower inputs.

**Specifications:** Expedition · 16 HP · depth 32 mm · +12 V 200 mA / −12 V 200 mA.

**Patch ideas (from LZX/community):** route all outputs into 2× SMX3 and sum for a full colorizer; drive the 6 outs into Visual Cortex's six inputs with an additive blend; feed it a slow LFO (0–1 V) to turn it into a complex multi-output LFO/sub-event generator; cross-patch with Mapper (Y→source, U/V→upper/lower) or Polar Fringe key outs for wild colorization.
