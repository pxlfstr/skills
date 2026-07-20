# Storing a New Document — creative-coding

Follow this when the user agrees to save a pattern or technique to this library.

## Screen it first — three questions

1. **Is it a fact or a pattern?** Vendor and protocol facts go to `digital-video/references/`, not here. If the document is mostly numbers from a manual, it is in the wrong skill.
2. **Is it public-safe?** This repository is world-readable. Strip or never write: client names, venue detail, rig inventories, IP addresses, network topology, credentials, show files. If the pattern cannot be stated without the rig it ran on, it is not ready.
3. **Is it reusable?** One-off debugging is not a reference document. Patterns worth keeping are ones that will be reached for again on different hardware.

## Steps

1. **Write the file into `references/`.** Lowercase-with-hyphens, descriptive: `midi-for-show-control.md`, not `notes2.md`.

2. **Tier every pattern in place** — Shipped / Bench-verified / Designed / Abandoned. Provenance travels with the pattern. Never present an empirically developed technique as a documented fact.

3. **Cite across, don't duplicate.** Where a pattern depends on a vendor fact, reference the `digital-video` document by filename rather than restating the number. One place per spec.

4. **Add an entry to `INDEX.md`** capturing:
   - **Covers** — what is actually in the file, specifically.
   - **Use for** — the kinds of questions this should be consulted for. This is what future sessions match against.
   - **Confidence** — the tier distribution, and which sections are weakest.
   - **Open items** — what is untested or unknown, stated rather than filled.
   - **Added** — today's date.

5. **Deliver it as a download and say plainly that it must be committed.** Writing into the container is not storage. Never report a document as saved on the basis of a file write.

## Updating an existing document — additive, never lossy

- **Merge, don't replace.** Keep correct detail a newer or narrower source happens to omit.
- **Promote tiers, don't overwrite them.** When a Designed pattern gets bench-tested, change the tier and note what the test showed — including anything that turned out different from the design.
- **Keep Abandoned entries.** Knowing what failed prevents re-attempting it in eighteen months.
- Remove something only when it is shown to be **wrong**, not merely absent from the latest source.

## Open items are first-class

Every document ends with what is unknown. A gap stated is worth more than a gap filled with a plausible guess — in this domain a wrong number gets discovered live, with no undo.
