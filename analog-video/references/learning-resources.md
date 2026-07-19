# Learning & Community Resources

Curated from **scanlines.xyz** — the central community forum for DIY video synthesis and visual music. Two of its categories are reference-grade for the *fundamentals* (how video circuits work, and the science behind the image), beyond any single maker. Use these when a question is about learning the craft, circuit fundamentals, color/perception science, or sourcing deeper reading.

## scanlines.xyz at a glance
A Discourse forum with maker categories (Visible Signals, Reverse Landfill, and others) plus general analog-video discussion, build threads, and theory. Maker build threads often hold functional detail and BOMs not on ModularGrid (e.g. the Reverse Landfill category documents SNOW/JOG/XFADE/EDGE/Sharp builds — folded into `lzx/third-party-video.md`).

## Circuit Lessons (Rob Schafer / "schaferob") — video course
`https://scanlines.xyz/c/circuit-lessons/14` · main thread `/t/circuit-lessons/78`

A beginner-friendly video series on building analog-video circuits from scratch on a breadboard, taught through two complete projects: a **Two-Comparator Effect** and a **Luminance/Chroma Inverter**. Lesson arc:

1. **Comparators** — threshold/keying building block (signal vs reference → hard switch).
2. **Clamping** — DC-restoring the video signal to a known black level (essential before processing).
3. **Sync** — separating/handling the sync portion of composite video.
4. **Power in to the breadboard** — getting clean rails to a prototype.
5. **Op-amps** — the core gain/buffer/processing stage for video.
6. **Blanking** — suppressing signal during retrace so processed video stays legal/clean.
7. **Circuit output section** — driving a proper 1 V / 75 Ω-friendly output.
8. **Wrap-up** — integrating the sections into a working module.
9. **Ohm's Law** — the underlying V/I/R relationship.
10. **Power supplies** — regulated supplies for video circuits.

Plus extras: video-clamp demo, breadboard input section, adjusting horizontal blanking, completed luminance inverter. Companion threads: **"Phase shift the colour burst!"**, **"Whiteboard schoolhouse companion circuits"** (cyberboy666), and **"Rob Schafer's 2.1 color 5 V colorizer"** (open-source colorizer design). *(Content is on video/YouTube; this is the map + project list, not a transcript.)*

Why it matters here: this is the clearest function-first walkthrough of the canonical video-signal chain — **clamp → process (comparator/op-amp) → blank → output** — which is exactly how the LZX-style modules in this skill are organized internally.

## Science category — theory & deeper reading
`https://scanlines.xyz/c/science/7`

Reference threads worth knowing (mix of original writeups and curated outside material):

- **Vector Synthesis (Derek Holzer)** — foundational text/toolkit for **oscilloscope / X-Y vector imaging** (drawing with audio-rate signals on a scope rather than raster scanning). Directly relevant to quadrature-driven X-Y work (e.g. the owner's Syntonie VU006).
- **HSLuv — a human-friendly alternative to HSL** — perceptually-uniform color model; useful when reasoning about hue/saturation/lightness in a way that matches how the eye sees, vs naive HSL.
- **Pixel count related to geometric forms** — relating raster resolution/timing to on-screen geometry (how counts/timing map to shapes).
- **CCTV cameras and infrared (IR) for video art** — using surveillance cameras and IR sources as expressive live inputs.
- **Modeling tracers** — the math/behavior behind feedback "tracer"/trail effects.
- **Video art as scientific experiment / illustration** — using the video instrument as a visualization tool.
- Outside material the community curates: *Secret Life of Chaos* (2009 chaos-theory documentary), *Introduction to Holography* (1972), Wolfram's computational-physics ideas — context/inspiration rather than build info.

Why it matters here: this is the **color-theory, perception, geometry, and feedback-math** layer that supports the skill's domain (color theory, CRT/scanning, vector/oscilloscope work, liquid-light/feedback aesthetics).
