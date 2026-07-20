# Storage Protocol — `references/`

How to add or update a document in this library.

## Adding a new document

1. **Name it functionally**, lowercase, hyphenated, by device/protocol/topic —
   e.g. `behringer-xtouch-compact-resolume.md`, `orei-uhd88-exb230r.md`,
   `st2110-bandwidth-tables.md`. Not by date or session.
2. **Mark every fact's tier** inline using the skill's verification tiers:
   **Verified** (manufacturer datasheet/manual, standards doc, device docs, or
   a measurement), **Lead** (forum/Reddit/community/blog — a pointer, not a
   fact), **Memory** (Claude's recall — fine for stable fundamentals, never for
   current specs, ports, firmware, pricing, or protocol revisions).
3. **Cite descriptor-style**, not APA/MLA: the title of the article, thread,
   manual, or PDF (hyperlinked if online), tagged `[Official]` or `[Forum]`.
   No years. In tables, add a **Source** column. In prose, name the source
   inline with its tag.
4. **No false, placeholder, or estimated numbers.** Every numeric claim must
   come from a source actually read that session. If a figure isn't in hand,
   state what was checked and what's missing — never substitute a plausible
   value or round a remembered figure into a fake-precise one.
5. **Close with a verification-status table** and an explicit
   *"Not yet verified — open items"* list, so the next session knows exactly
   where the soft spots are.
6. **Update `INDEX.md`** — add a row (document, what it covers, tier summary,
   date stored), and add any newly-identified gaps to the wanted-documents
   list.

## Updating an existing document

**Additive and never lossy.**

- **Merge, don't replace.** Fold new material into the existing structure.
- **Keep correct detail that a newer or narrower source simply omits.**
  Absence from the latest source is not evidence of error.
- **Only remove something demonstrated to be wrong** — and when removing,
  note what was corrected and on what authority.
- **Promote tiers explicitly.** When a Lead is confirmed against a datasheet,
  manual, standards doc, or measurement, upgrade it to Verified and record
  which source did the confirming. Don't silently re-tag.
- Update the verification-status table and the open-items list to match.
- Update the document's row in `INDEX.md`.

## Curation

The user curates this library. **Never store automatically** — offer, and
store when they say yes.
