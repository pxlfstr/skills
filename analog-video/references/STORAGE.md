# Storing a New Document

Follow this when the user agrees to save a document to the skill's reference library. The user curates this library — **never store automatically**; offer, and store when they say yes.

## Adding a new document

1. **Name it functionally**, lowercase-with-hyphens, by module/device/topic (e.g., `lzx-memory-palace-spec.pdf`, `syntonie-quad-frequency-doubler.md`, not `doc1.pdf`). Keep the original filename if it's already descriptive. Not by date or session.

2. **Open with a `## Provenance` block** (`RULES.md` Rule 2), heading exact, above the first content heading: sourcing tier(s) by section, each web source's own last-edited date, what was NOT read, and open contradictions left in place. No short-document waiver.

3. **Mark every fact's tier** inline using the skill's verification tiers (see `GUIDE.md`, *Sourcing, vetting & citing data*): **Verified** (datasheet, schematic, manufacturer doc/manual, the module's designer, or a measurement), **Lead** (forum/Reddit/community — a pointer, not a fact), **Memory** (Claude's recall — fine for stable fundamentals, never for module specs, pinouts or current products).

4. **Cite descriptor-style**, not APA/MLA: the title of the article, thread, manual, or PDF (hyperlinked if online), tagged `[Official]` or `[Forum]`. No years. In tables, add a **Source** column. In prose, name the source inline with its tag.

5. **No false, placeholder, or estimated numbers.** Every numeric claim must come from a source actually read that session. If a figure isn't in hand, state what was checked and what's missing — never substitute a plausible value or round a remembered figure into a fake-precise one.

6. **Close with a verification-status table** and an explicit *"Not yet verified — open items"* list, so the next session knows exactly where the soft spots are.

7. **Update `INDEX.md`** — add a row to the Documents table (document, what it covers and when to use it, tier summary, date stored), update the document count at the top, and add any newly identified gaps to *Gaps / wanted documents*.

8. **Deliver, don't claim.** Hand the file over as a download for the user to commit, and say what it will be used for next time. It is not stored until committed — see *Persistence* below.

## Updating an existing document (additive, never lossy)

When refreshing a doc with new/verified data, **be additive — never drop correct detail.** The user's standing rule: keep as much correct data as possible. So:

- **Merge, don't replace.** If a newer source is more authoritative on some fields (e.g. verified HP/MSRP/tags from a manufacturer page) but terser on others (e.g. functional/patching detail), keep the verified fields *and* retain the richer detail from the older source.
- **Keep correct data that a narrower source omits.** A module that's real and confirmed (e.g. from the maker's own site or the user's rack) stays even if a specific catalog page doesn't list it — flag its provenance so the source labelling stays honest. Absence from the latest source is not evidence of error.
- **Only remove something demonstrated to be wrong** — and when removing, note what was corrected and on what authority.
- **Promote tiers explicitly.** When a Lead is confirmed against a datasheet, schematic, manufacturer doc or measurement, upgrade it to Verified and record which source did the confirming. Don't silently re-tag.
- Update the Provenance block, the verification-status table and the open-items list to match.
- Update the document's row in `INDEX.md`.

## What's worth storing

Reusable, reference-grade material: schematics, manuals, spec sheets, build/mod notes, calibration data, curated reading lists, artist/technique references the user wants to keep.

## What's not worth storing

One-off questions, transient context, or anything the user is only asking about once. When unsure, ask the user — they curate the library, not Claude.

## Note on file types

The library can hold PDFs, images (schematics, scans), text/markdown, and similar. For large PDFs, consider also noting the key facts directly in the `INDEX.md` row so quick answers don't require re-reading the whole file.

## Persistence — read this before saying anything is "stored"

Writing a file into `references/` inside a session **does not persist**. The container is discarded at session end. The canonical library lives at https://github.com/pxlfstr/skills

Therefore:

1. Say up front, *before* doing storage work, that the file will need to be committed.
2. Never describe a document as "stored" or "saved to the skill" on the basis of having written it to disk.
3. Always deliver the file as a download via `present_files` so it can be committed.
4. At session start, report the clone's latest commit date (per RULES.md). The installed `SKILL.md` is only a pointer to the repo, so there is no installed library to compare against.
