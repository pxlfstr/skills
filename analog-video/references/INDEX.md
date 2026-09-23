# Reference Library — Index

Manifest of stored reference documents for the `analog-video` skill. Read it at the start of every session so you know what reference material is available before answering.

Maintenance is **additive and non-lossy** — see `STORAGE.md`.

**Four entries stored: three single documents plus the `lzx/` pack (62 files).** Update this count whenever a row is added or removed — a count that drifts from the table hides missing documents.

⚠️ **No document in this library has a `## Provenance` block yet** (required by `RULES.md` Rule 2). The tier summaries below are taken from each document's earlier index entry, not from a provenance block. Treat them as provisional until each document is brought up to standard.

⚠️ **Restructured 2026-09-23** to match the `digital-video` index (count line, tier column, cross-references, wanted list). Nothing was removed: every earlier entry's text is carried into the table, and the three LOST documents moved to *Gaps / wanted documents*.

---

## Documents

| Document | Covers | Tier summary | Stored |
|---|---|---|---|
| `lzx/` — LZX Industries reference pack | LZX video synthesizer product line — module specs, signal standard, per-module circuit/interface detail, functional/substitution map, glossary. Use for any LZX module question — what a module does, exact specs (HP/power/sync), how its controls and jacks behave, signal levels and patching, and which modules can play similar roles. **Start at `lzx/README.md`** for the map of the pack. `functional-map.md` includes the **owner's module preference filter** (revised: all generations judged on merit; Expedition is a soft tiebreaker only). `modules/` holds per-module docs for the 25 active Gen3 + P-series modules. `expedition/` holds the Expedition manuals; `visionary.md` and `castle.md` cover those non-Orion series; `keying-dictionary.md` disambiguates keying across all series; `vhs.md` + `brownshoesonly.md` cover that maker's two brands; `third-party-video.md` covers 26 other video makers (LZX-compatible and standalone) with format tags; `open-source-repos.md` catalogs those makers' GitHub repos and the circuit building-blocks their BOMs reveal. `cadet.md` + `cadet-circuits.md` cover the Cadet series and the canonical LZX circuit building blocks (useful for explaining any module's analog stages) | **[Official]** — distilled from official LZX GitHub docs (`lzxtm` Technical Manual + `lzxdocs`, `lzxmodular`, `lzxcadet`). Reflects the product line as of ingest (`lzxtm` updated within days). Not authoritative for price/stock. Full manual + Cadet schematics remain at github.com/lzxindustries for on-demand deep dives. Third-party maker files are not LZX-sourced — tier per file, unrecorded. No provenance blocks | 2026-06-02 |
| `patch-techniques.md` | Credibility-weighted patch knowledge distilled from LZX forum threads — 2D shape **rotation/spinning** (ramp rotate → saw→triangle mirror → mix → key; the rotation-matrix math), **center of rotation**, **animating/modulating colour** (RGB cycling vs Mapper/UV; colorspace facts), and the **Gainbrain manual/CV range fix**. Use for how to actually patch rotation, colour animation, hue-without-luma. Several techniques map onto the owner's rack | **Mixed** — **[Forum]** threads, with credibility flags in place: Lars Larsen / module designers = authoritative; aesthetics and unbuilt modules = opinion. No provenance block | 2026-06-03 |
| `learning-resources.md` | How-to-learn layer — Rob Schafer's Circuit Lessons video course (clamp → comparator/op-amp → blank → output chain; Two-Comparator Effect & Luminance/Chroma Inverter projects) and the scanlines **science** category (Vector Synthesis, HSLuv color, tracers/feedback math, CCTV/IR, geometry/timing). Use for learning the craft, video-circuit fundamentals, color/perception science, vector/oscilloscope work, and pointers to deeper reading. Community build threads also document maker modules not on ModularGrid | ⚠️ **Not recorded** — course and community material; no tiers marked. No provenance block | 2026-06-03 |
| `my-rack.md` | The user's current Eurorack video system ("fstrvsn") — 19 modules / 172 HP in two rows (per ModularGrid data sheet 2026-06-20), LZX-centric, anchored by Visual Cortex; modules grouped by function, a spec table, a separate-rack section (ES-9, SY1), and an Auditioning (not-owned) section. Use for any question about *their* setup, signal flow through gear they own, what to patch, or what to add. **Keep it current:** update when the user says they've added/removed/swapped a module; keep not-yet-owned modules in the Auditioning section, never in the owned list | **User-stated** + ModularGrid data sheet (2026-06-20) for layout, totals and power. Per-module draw/depth figures in the spec table carry no per-row source. The Vessel layout section is **Designed**, work in progress. No provenance block | 2026-06-03, rev. 2026-09-23 |

---

## Cross-references

- `my-rack.md` → `patch-techniques.md` — the Gainbrain R4 → 10 K range fix and the shape-rotation patch the Syntonie modules support.
- `lzx/third-party-video.md` → `patch-techniques.md` — the same Gainbrain fix, from the maker catalog side.
- `learning-resources.md` → `lzx/third-party-video.md` — scanlines maker categories and build threads cover makers catalogued there.
- `lzx/brownshoesonly.md` ↔ `my-rack.md` — the owned bajascillator and its VH.S successor (BAJA).
- `lzx/functional-map.md` owner preference filter ↔ `my-rack.md` — what's owned vs. what to recommend next.

---

## Gaps / wanted documents

Material that would strengthen the library if the user has it.

**Lost documents — need re-derivation.** Produced in session on **2026-06-30** and written into the container, but never committed or packaged. Not recoverable from this repository. Listed so their absence is visible rather than silent.

- **`time-base-correctors.md` — LOST.** TBC fundamentals — two-clock architecture, windowed line correction vs. full-frame store, genlock behaviour. Could be reconstructed from conversation record, but would be a summary of a summary. **Re-derive from sources.**
- **`microtime-t-120-panel.md` — LOST.** Microtime T-120 front-panel control map; windowed line TBC, 35-line correction window, V-lock genlock, no frame store/freeze. Was derived from user-supplied photographs. **Re-upload the photos and redo properly. Do not reconstruct.**
- **`tbc-comparison-chart-1988.md` — LOST.** Broadcast Engineering 1988 TBC comparison chart, transcribed from user photograph. Transcription had low-confidence tick columns flagged at the time. **Re-upload the photo and redo properly. Do not reconstruct.**

**Other gaps:**

- **Syntonie Quad Frequency Doubler (VU002)** depth and power draw — blank in the `my-rack.md` spec table. Maker page or ModularGrid entry would fill it.
- **Provenance for every existing document** (Rule 2) — needs each source's own last-edited date, so the LZX GitHub pages and forum threads have to be re-read.

<!--
Row format — keep the Covers column scannable, and put sourcing in Tier summary:

| `filename.md` | What it covers and when to reach for it | Verified [Official] / [Forum] / Memory, by section; what was NOT read | YYYY-MM-DD |
-->
