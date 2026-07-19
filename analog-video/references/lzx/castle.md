# LZX Castle Series (DIY, binary/logic, all 4 HP)

Source: LZX community "All About Castle (DIY) Series" + linked concept/manual threads. Castle is its own series (**not** Orion/Gen3/P) — open-source DIY, all 4 HP, and acceptable under the owner's preference.

## Concept: 3-bit binary video

Castle is a system of **binary** modules. Binary = discrete ON/OFF (1/0, high/low); in Castle the low→high transition threshold is **0.5 V**. All module inputs are **comparators**, so any input does a 1-bit analog→digital conversion. Castle works in **3-bit data streams** (3 bits in parallel, like RGB) → 8 possible values. Send 3-bit binary into RGB and you get NTSC-style color bars. Patching a triangle into the ADC yields a step-pyramid (posterize) waveform.

## Modules

| Module | Rev | HP | Depth | +12V | −12V | Function |
|---|---|---|---|---|---|---|
| 000 ADC | D | 4 | 56 mm | 21 mA | 28 mA | Analog → 3-bit data stream (posterize/digitize) |
| 001 DAC | D | 4 | 41 mm | 3 mA | 4 mA | Dual: two 3-bit streams → two analog approximations |
| 010 Clock VCO | E | 4 | 51 mm | 9 mA | 7 mA | Square-wave VCO, linear CV response |
| 011 Shift Register | D | 4 | 51 mm | 21 mA | 43 mA | 4-position memory |
| 100 Multi Gate | D | 4 | 57 mm | 28 mA | 40 mA | 2 inputs → XNOR, XOR, NOR, OR, NAND, AND outputs |
| 101 Quad Gate | D | 4 | 51 mm | 31 mA | 55 mA | Single quad logic chip combined 4 ways |
| 110 Counter | D | 4 | 51 mm | 39 mA | 39 mA | 4-bit clock counter/divider |
| 111 D Flip Flops | D | 4 | 51 mm | TBD | TBD | Three D-type flip-flops sharing common Clock & Reset |

## Build note

On the **000 ADC Rev D**, the silkscreen **polarity marking for C18 is reversed** (C18 is an output filter cap on the regulator). Corrected in **Rev E**. Modules often still work either way, but orient per the schematic, not the Rev-D silkscreen.

## Typical patches

- **Posterize:** luma video → ADC → DAC; pull DAC data outs to set the number of slices.
- **Digital sample & hold / pixelate:** hold the 3-bit value at the DAC data inputs on a clock edge (clock from Castle 010 or sync) → quantized/pixelated output.
- Counters + flip-flops can build semi-random sequencers (Turing-machine-style).
