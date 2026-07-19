# LZX Cadet Series (DIY, 4 HP)

Source: `github.com/lzxindustries/lzxcadet` (open-source hardware) + the Cadet I Owner's Manual (the only prose OM committed to that repo). Schematics live there as DipTrace files and PCB-layout PDFs; BOMs as CSV; front panels as image/CAD art.

**Why this series matters for the owner's preference:** Cadet is its *own* series — **not** Gen3, P, or Orion — so it sits outside the "prefer-against" list. Every Cadet is **4 HP** (inside the 4–8 HP sweet spot), single-function, and control-minimal (mostly jacks + at most a switch/trimmer, rarely a knob). The line also includes a sync generator, an **encoder** (C2), and a **decoder/input** (C3), which independently satisfy the "encoders/decoders, any generation" rule.

**Design philosophy (from the manual):** each Cadet does one job, built with through-hole parts, schematics under Creative Commons. LZX's framing: if their other lines are recipes, the Cadets are the ingredients — meant to be recombined and rebuilt. The series traces its lineage to Dan Sandin's Image Processor (1970s), one of the early open-source video instruments, adapted to modern parts by Lars Larsen and Ed Leckie; LZX began selling Eurorack video modules in 2010.

---

## The ten modules (all 4 HP, ±12 V via Euro 16-pin)

| # | Module | Function | Notable I/O |
|---|---|---|---|
| C1 | Sync Generator | Master NTSC/PAL timing for the system | see full breakdown below |
| C2 | RGB Encoder | Encodes R/G/B patch signals to standard video out | takes sync from C1's distribution header |
| C3 | Video Input | Brings an external video source into the 1 V standard (a **decoder/front-end**) | pairs with C1's buffered Video/Sync pass-through |
| C4 | Dual Ramp Generator | Two H/V ramp sources (the spatial backbone for shapes) | sync-locked via header |
| C5 | Scaler | Scales/attenuates a signal (gain) | no sync |
| C6 | Fader | Two-signal crossfade/blend | no sync |
| C7 | Processor | Voltage processor — attenuate/invert/offset | no sync |
| C8 | Hard Key Generator | Comparator → hard-edged key/stencil | no sync |
| C9 | VC Oscillator | Voltage-controlled oscillator for patterns | sync-lockable via header |
| C10 | Multiplier | Multiplies/modulates two signals | no sync |

Sync handling: C1, C2, C3, C4, C9 interact with the **14-pin video sync distribution header** (chained via LZX's VSDC bus cable, up to 5 modules per cable). The rest don't need sync.

---

## C1 — Cadet I Sync Generator (full detail, from the OM)

Generates master timing in NTSC/480i or PAL/576i, distributes it to other modules, and can genlock the whole system to an external source.

**Front-panel controls & connections:**

| # | Control / Jack | Behavior |
|---|---|---|
| 1 | **H Sync Pulse Out** | Positive 0–1 V pulse at the start of each scanline. 15,734 Hz NTSC / 15,625 Hz PAL. Syncs oscillators running above line rate |
| 2 | **V Sync Pulse Out** | Positive 0–1 V pulse at the start of each field. 59.97 Hz NTSC / 50 Hz PAL |
| 3 | **Frame Clock Out** | Positive 0–1 V pulse, high at each frame start and through odd fields. Drives frame-rate sequencing / strobes |
| 4 | **Video Format Select switch** | NTSC (480i) ↔ PAL (576i). Must be set *before* power-up |
| 5 | **Video/Sync In** | External video in, to genlock C1's timing to that source |
| 6 | **Video/Sync Out** | Buffered pass-through of the input — e.g. on to C3 Video Input |
| rear | **14-pin sync distribution header** | Sends composite sync, V-sync, H-sync, odd/even field, composite blanking to other modules (0–5 V). Also buffers H/V sync to the Eurorack CV/Gate bus |

**Specs:** 4 HP · depth 57.15 mm · +12 V 30 mA / −12 V 10 mA · 3.5 mm outputs 499 Ω series, inputs 100 kΩ · RCA 75 Ω · 3.5 mm levels 0–1 V DC, header 0–5 V DC, RCA 2 Vpp.

Note the layout pattern that recurs across Cadets: a few labeled jacks, a setup switch, no performance knobs — exactly the jack/switch character the owner favors.

---

## What's *not* in the repo

- **Owner's manuals for C2–C10** aren't committed to `lzxcadet` (only C1's). Their schematics, PCB PDFs, BOMs, and panel art *are* there, so jack/control layout can be read off the panel art or schematic if needed — but there's no prose walkthrough like C1's. The C2–C10 functions above are from the module names + the C1 manual's cross-references + the specs table, not from per-module manuals.
- If exact C2–C10 control detail is needed, options: read the panel art/schematic in the repo, or fetch the historical owner's manuals from the LZX site on demand.
