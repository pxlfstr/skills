# Reference Library Index

This file is the manifest of documents stored in this skill. Read it at the start of every session so you know what reference material is available before answering.

Each entry records: the filename, what it covers, and why it was stored (so future sessions know when to reach for it).

---

---

## Lost documents — need re-derivation

Produced in session on **2026-06-30** and written into the container, but never committed or packaged. Not recoverable from this repository. Listed so their absence is visible rather than silent.

### time-base-correctors.md — LOST
- **Topic:** TBC fundamentals — two-clock architecture, windowed line correction vs. full-frame store, genlock behaviour
- **Status:** could be reconstructed from conversation record, but would be a summary of a summary. Re-derive from sources.

### microtime-t-120-panel.md — LOST
- **Topic:** Microtime T-120 front-panel control map; windowed line TBC, 35-line correction window, V-lock genlock, no frame store/freeze
- **Status:** was derived from user-supplied photographs. **Re-upload the photos and redo properly.** Do not reconstruct.

### tbc-comparison-chart-1988.md — LOST
- **Topic:** Broadcast Engineering 1988 TBC comparison chart, transcribed from user photograph
- **Status:** transcription had low-confidence tick columns flagged at the time. **Re-upload the photo and redo properly.** Do not reconstruct.

---

## Known stale entries

- **`my-rack.md`** — the entry below records 18 modules / 184 HP. The authoritative ModularGrid data sheet (2026-06-20) gives **19 modules / 172 HP**, two rows, all-video; power +12V 1270 mA, -12V 1098 mA. The June 20 correction never reached the file. Verify and update `my-rack.md` itself, then amend this entry.

---

## Stored documents

### patch-techniques.md — credibility-weighted patch knowledge
- **Topic:** community techniques distilled from LZX forum threads — 2D shape **rotation/spinning** (ramp rotate → saw→triangle mirror → mix → key; the rotation-matrix math), **center of rotation**, **animating/modulating colour** (RGB cycling vs Mapper/UV; colorspace facts), and the **Gainbrain manual/CV range fix**
- **Use for:** how to actually patch rotation, colour animation, hue-without-luma; sourced with credibility flags (Lars Larsen / module designers = authoritative; aesthetics & unbuilt modules = opinion). Several techniques map onto the owner's rack.
- **Added:** 2026-06-03

### learning-resources.md — fundamentals & community (scanlines.xyz)
- **Topic:** how-to-learn layer — Rob Schafer's Circuit Lessons video course (clamp → comparator/op-amp → blank → output chain; Two-Comparator Effect & Luminance/Chroma Inverter projects) and the scanlines **science** category (Vector Synthesis, HSLuv color, tracers/feedback math, CCTV/IR, geometry/timing)
- **Use for:** learning the craft, video-circuit fundamentals, color/perception science, vector/oscilloscope work, and pointers to deeper reading. Community build threads also document maker modules not on ModularGrid.
- **Added:** 2026-06-03

### my-rack.md — the user's actual rack ("fstrvsn")
- **Topic:** the user's current Eurorack video system — 18 modules / 184 HP, LZX-centric, anchored by Visual Cortex; modules grouped by function, plus a spec table and an Auditioning (not-owned) section
- **Use for:** any question about *their* setup, signal flow through gear they own, what to patch, or what to add. **Keep it current:** update when the user says they've added/removed/swapped a module; keep not-yet-owned modules in the Auditioning section, never in the owned list.
- **Added:** 2026-06-03

### lzx/ — LZX Industries reference pack
- **Topic:** LZX video synthesizer product line — module specs, signal standard, per-module circuit/interface detail, functional/substitution map, glossary
- **Type:** distilled from official LZX GitHub docs (`lzxtm` Technical Manual + `lzxdocs`, `lzxmodular`, `lzxcadet`)
- **Use for:** any LZX module question — what a module does, exact specs (HP/power/sync), how its controls and jacks behave, signal levels and patching, and which modules can play similar roles. **Start at `lzx/README.md`** for the map of the pack. `functional-map.md` includes the **owner's module preference filter** (strongest preference: Expedition). `expedition/` holds the Expedition manuals; `visionary.md` and `castle.md` cover those non-Orion series; `keying-dictionary.md` disambiguates keying across all series; `vhs.md` + `brownshoesonly.md` cover that maker's two brands; `third-party-video.md` covers 18 other video makers (LZX-compatible and standalone) with format tags; `open-source-repos.md` catalogs those makers' GitHub repos and the circuit building-blocks their BOMs reveal. `cadet.md` + `cadet-circuits.md` cover the Cadet series and the canonical LZX circuit building blocks (useful for explaining any module's analog stages).
- **Currency note:** reflects the product line as of ingest (lzxtm updated within days). Not authoritative for price/stock. Full manual + Cadet schematics remain at github.com/lzxindustries for on-demand deep dives.
- **Added:** 2026-06-02

<!--
Entry format — keep it scannable:

### filename.pdf
- **Topic:** LZX Memory Palace module — full spec and patch points
- **Type:** manufacturer spec sheet
- **Use for:** exact module specs, signal ranges, jack functions
- **Added:** 2026-06-02
-->
