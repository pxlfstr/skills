# skills

Canonical source for Obie's Claude skills: **`analog-video`** and **`digital-video`**.

This repository is the durable copy. The versions installed in Claude are *derived* from it.

---

## Why this exists

Claude unpacks an installed skill into a throwaway container at `/mnt/skills/user/<name>/`. Anything Claude writes there is **discarded when the session ends**. There is exactly one write path back to the stored skill: the upload form in Settings → Capabilities → Skills.

This was not understood for several weeks, and work was lost as a result. Documented instances:

- **2026-06-30** — a session on the Microtime T-120 TBC produced three reference documents (`time-base-correctors.md`, `microtime-t-120-panel.md`, `tbc-comparison-chart-1988.md`) plus an `INDEX.md` update. None survived. The 1988 Broadcast Engineering comparison chart had been transcribed from user photographs; that transcription is gone.
- **2026-06-20** — a ModularGrid-verified correction to the rack inventory (19 modules / 172 HP, superseding 18 / 184) never reached `my-rack.md`.
- **2026-06-04** — corrections to `my-rack.md` and `third-party-video.md` were attempted in a session where the skill folder was mounted read-only.

Every file in the installed `analog-video` skill is timestamped `2026-06-12 23:17`, the moment the last package was uploaded. Nothing has been written since.

Git removes the silent-failure mode. A commit either happened or it didn't, and `git log -1` says which.

---

## Layout

```
analog-video/
  SKILL.md
  references/
    INDEX.md          <- manifest; read first
    STORAGE.md        <- protocol for adding documents
    ...
digital-video/
  SKILL.md
  references/
    INDEX.md
    STORAGE.md
    ...
```

Each top-level folder is a complete skill, packageable as-is.

---

## Working protocol

**At the start of a session**, Claude should clone this repo and read the relevant `references/INDEX.md`, then report the last commit date. If the installed skill's file timestamps predate the newest commit, the installed copy is stale and Claude must say so before answering from it.

```bash
git clone --depth 1 https://github.com/pxlfstr/skills.git
git -C skills log -1 --format='%h %ad %s' --date=short
```

The repo is public specifically so this needs no credentials.

**When new reference material is produced**, Claude writes the file and hands it over as a download. Obie commits and pushes. Claude does not have push access and should never claim a document is "stored" on the basis of having written it into the container.

**When the installed skill drifts too far from the repo**, re-package the relevant folder and upload it. This is now a *freshness* step, not a *safety* step — skipping it means Claude works from a stale library and can detect that, rather than losing work.

---

## What does not belong here

This repository is public. Keep out:

- Rate card, invoicing terms, client names, contract details
- Venue drawings, show files, production documents
- Anything personal

Reference-grade technical material only.

---

## Document conventions

Verification tiers are used throughout — **Verified** (datasheet, schematic, manufacturer documentation, or direct measurement), **Lead** (forum, wiki, secondary source), **Memory** (model knowledge, unverified). Citations use descriptor style: article or document title, hyperlinked where online, tagged `[Official]` or `[Forum]`. No years.

Standing rule: **no false, placeholder, or estimated numbers.** Every figure must come from a source actually read. Derived values are labelled as derived. Where a number is missing, the gap is stated explicitly rather than filled.

Library maintenance is **additive and never lossy** — merge rather than replace; remove only what has been shown to be wrong, not merely what a newer source omits.
