# Storing a New Document

Follow this when the user agrees to save a document to the skill's reference library.

## Steps

1. **Copy the file into `references/`.** Keep the original filename if it's descriptive; otherwise rename it to something searchable (e.g., `lzx-memory-palace-spec.pdf`, not `doc1.pdf`). Use lowercase-with-hyphens.

2. **Add an entry to `INDEX.md`** under "Stored documents," using the format shown in the comment there. Capture:
   - **Topic** — what the document actually covers, specifically.
   - **Type** — spec sheet / manual / schematic / build notes / reading list / article / etc.
   - **Use for** — the kinds of questions this doc should be consulted for. This is what future sessions match against.
   - **Added** — today's date.

3. **Confirm to the user** what was stored and how it'll be used next time.

## Updating an existing document (additive, never lossy)

When refreshing a doc with new/verified data, **be additive — never drop correct detail.** The user's standing rule: keep as much correct data as possible. So:

- **Merge, don't replace.** If a newer source is more authoritative on some fields (e.g. verified HP/MSRP/tags from a manufacturer page) but terser on others (e.g. functional/patching detail), keep the verified fields *and* retain the richer detail from the older source.
- **Keep correct data that a narrower source omits.** A module that's real and confirmed (e.g. from the maker's own site or the user's rack) stays even if a specific catalog page doesn't list it — flag its provenance so the source labelling stays honest.
- Only remove something if it's been shown to be **wrong**, not merely absent from the latest source.

## What's worth storing

Reusable, reference-grade material: schematics, manuals, spec sheets, build/mod notes, calibration data, curated reading lists, artist/technique references the user wants to keep.

## What's not worth storing

One-off questions, transient context, or anything the user is only asking about once. When unsure, ask the user — they curate the library, not Claude.

## Note on file types

The library can hold PDFs, images (schematics, scans), text/markdown, and similar. For large PDFs, consider also noting the key facts directly in the `INDEX.md` entry so quick answers don't require re-reading the whole file.

## Persistence — read this before saying anything is "stored"

Writing a file into `references/` inside a session **does not persist**. The container is discarded at session end. The canonical library lives at https://github.com/pxlfstr/skills

Therefore:

1. Say up front, *before* doing storage work, that the file will need to be committed.
2. Never describe a document as "stored" or "saved to the skill" on the basis of having written it to disk.
3. Always deliver the file as a download via `present_files` so it can be committed.
4. At session start, compare installed-skill file timestamps against the repo's latest commit and flag any gap.
