# Storing Material in creative-coding

Follow this when the user agrees to save something to this skill's library.

## Before anything else — where this is allowed to go

This skill is **private**. Its canonical home is the user's private repository or a local archive — **never** `https://github.com/pxlfstr/skills`.

Before writing a storage file, confirm:

1. The destination is the private store, not the public repo.
2. The material contains no client-identifying detail the user hasn't agreed to keep.
3. Any IPs, hostnames, ports, credentials, or venue names are either intentional or stripped.

If the user asks to "commit the skills," ask which. `digital-video` and `analog-video` go public; this one does not.

## What belongs here

- Working code and scripts, in full.
- Architectural patterns we developed — how a system was structured and why.
- Debugging techniques that worked, and dead ends that didn't.
- Empirically tuned constants, with the conditions they were tuned under.
- Bug reports and upstream issues we've traced.

## What does not belong here

- **Vendor and protocol facts.** Command syntax, endpoints, port numbers, parameter paths, timing requirements, device capabilities. These go in `digital-video`, which is the single source of truth for them. Cite across; never copy.
- One-off questions and transient context.
- Anything the user is only asking about once.

When unsure, ask. The user curates the library.

## Steps

1. **Write the file into `references/`.** Lowercase-with-hyphens, descriptive
   (`touchdesigner-arena-sequencer.md`, not `notes2.md`). Group by project, not by language.

2. **Assign a confidence tier to every pattern in the file.** Per SKILL.md:
   **Shipped** / **Bench-verified** / **Designed** / **Abandoned**. Unmarked defaults to **Designed**.
   Tier goes inline next to the claim, not just in a header — a reader skimming to one section
   must be able to see the tier without scrolling back.

3. **Record what was never established.** If a workaround works and we don't know why, that
   sentence goes in the file. If a constant was tuned by feel, say so and give the conditions.
   A file that reads as more certain than the work behind it is a defect.

4. **Add an entry to `INDEX.md`** capturing: project, what's covered, highest tier present,
   what it depends on from `digital-video`, open questions, and the date added.

5. **Confirm to the user** what was written and that it needs committing to the private store.

## Updating an existing file (additive, never lossy)

- **Merge, don't replace.** Keep correct detail a newer note happens to omit.
- **Keep abandoned approaches.** The record of what failed prevents re-walking it. Never delete
  a dead end just because a working path was found — demote it to **Abandoned** with the reason.
- **Never silently promote a tier.** A pattern moves from Designed to Bench-verified to Shipped
  only on evidence the user reports. Time passing is not evidence.
- Only remove something shown to be **wrong**, not merely superseded.

## Cross-references to digital-video

When a file here depends on a device fact, link it rather than restating it:

> Camera command syntax: see `digital-video/references/panasonic-ptz-aw-protocol.md` `[Official]`.

If the referenced file doesn't exist in the public repo yet, say so in the INDEX entry under
"depends on," and treat writing it as a separate deliverable for that skill.

## Persistence — read this before saying anything is "stored"

Writing a file into `references/` inside a session **does not persist**. The container is
discarded at session end.

Therefore:

1. Say up front, *before* doing storage work, that the file will need to be committed.
2. Never describe material as "stored" or "saved to the skill" on the basis of having written it to disk.
3. Always deliver the file as a download via `present_files` so it can be committed.
4. At session start, if the user is relying on stored material, check file dates against the
   last known package/commit date and flag any gap.
