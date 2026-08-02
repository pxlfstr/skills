# skills

Canonical source for Obie's Claude skills: **`analog-video`**, **`digital-video`**, and **`creative-coding`**.

This repository is the durable copy. The versions installed in Claude are *derived* from it.

---

## Why this exists

Claude unpacks an installed skill into a throwaway container at `/mnt/skills/user/<name>/`. Anything Claude writes there is **discarded when the session ends**. There is exactly one write path back to the stored skill: the upload form in Settings → Capabilities → Skills.

This was not understood for several weeks, and work was lost as a result. Documented instances:

- **2026-06-30** — a session on the Microtime T-120 TBC produced three reference documents (`time-base-correctors.md`, `microtime-t-120-panel.md`, `tbc-comparison-chart-1988.md`) plus an `INDEX.md` update. None survived. The 1988 Broadcast Engineering comparison chart had been transcribed from user photographs; that transcription is gone.
- **2026-06-20** — a ModularGrid-verified correction to the rack inventory (19 modules / 172 HP, superseding 18 / 184) never reached `my-rack.md`.
- **2026-06-04** — corrections to `my-rack.md` and `third-party-video.md` were attempted in a session where the skill folder was mounted read-only.

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
creative-coding/
  SKILL.md
  references/
    INDEX.md
    STORAGE.md
    protocols/        <- vendor and protocol facts
    patterns/         <- structures Obie developed
```

Each top-level folder is a complete skill, packageable as-is.

`creative-coding` splits its library in two. A document lives in exactly one folder and **never mixes the two kinds inside one file** — so misfiling is visible in a directory listing rather than needing to be caught by reading.

---

## How the three relate

| Skill | Holds |
|---|---|
| `analog-video` | Analog video art and engineering — synthesis, CRT, broadcast signal structure, circuits |
| `digital-video` | The **video signal and video devices** — transport, bandwidth, sync, codecs, colour, LED processors, projection optics, switcher behaviour |
| `creative-coding` | **Control protocols and the code that drives them** — TouchDesigner operators and Python, Resolume APIs, MIDI, DMX/Art-Net/sACN, show-control patterns |

### The dividing line — revised 2026-08-01

The old rule was "facts in `digital-video`, patterns in `creative-coding`." It failed in a specific way: because a TouchDesigner operator parameter is a *fact*, the entire operator reference, every MIDI map and the whole Resolume control API drifted into a skill about video signal. The split is now **by domain**, and the test is one question:

> **Would this still be true if TouchDesigner, Resolume and every control surface disappeared?**

Yes → `digital-video`. No → `creative-coding`. DMX, Art-Net and sACN are `creative-coding` entire, packet level included.

The full test with worked borderline cases is in each `SKILL.md`. Consequence worth understanding here: `creative-coding` now holds facts *and* patterns, so `protocols/` and `patterns/` do the separating that the skill boundary used to. Cross-reference by filename rather than duplicating, so there is exactly one place a spec can be wrong.

---

## Working protocol

**At the start of a session** Claude clones this repo to `/tmp/skills-repo`, reads the relevant `references/INDEX.md`, and reports the last commit date. Once per session, not once per task. Re-pull when Obie says he has committed. The exact procedure is the Order of operations at the top of each `SKILL.md`; it is not restated here.

The repo is public specifically so this needs no credentials.

**When new reference material is produced**, Claude writes the file and hands it over as a download. Obie commits and pushes. Claude does not have push access and should never claim a document is "stored" on the basis of having written it into the container.

**When the installed skill drifts too far from the repo**, re-package the relevant folder and upload it. This is now a *freshness* step, not a *safety* step — skipping it means Claude works from a stale library and can detect that, rather than losing work.

---

## What does not belong here

This repository is public. Skill material goes in; project material does not. Keep out:

- Rate card, invoicing terms, client names, contract details
- Venue drawings, show files, production documents, `.toe` files
- Rig inventories, camera IPs, network topology
- Credentials, tokens, or anything implying them
- Project-specific code as built
- Anything personal

Device configuration for commercially available gear is **not** a rig inventory and may be committed — `creative-coding/references/protocols/xtouch-compact-midi-map.md` is a decoded MIDI map for a controller anyone can buy, and is public by explicit decision. The line is whether the document identifies a deployment, a client or a venue.

Reference-grade technical material and generically written patterns only. The authoring discipline is to write a pattern generically **from the start** rather than writing it deployment-specific and sanitizing later — if a pattern cannot be stated without the rig it ran on, it is not ready to be committed.

---

## Where the rules live

**This file does not restate the operating rules, so they cannot drift.**

Claude loads `SKILL.md` into context automatically. It does **not** load this README — it is read only if a session clones the repo and opens it. So every rule that has to fire without being sought lives in `SKILL.md`, in full, in each skill that needs it. That triplication is deliberate: a session may load only one skill, and a rule it cannot see is a rule that does not exist.

| Rule | Where |
|---|---|
| Order of operations — clone once, then look up on every prompt; never ask permission to check | `*/SKILL.md`, first section |
| Rule 1 — `protocols/` and `patterns/` are separate folders | `creative-coding/SKILL.md` |
| Rule 2 — every reference document opens with `## Provenance` | all `SKILL.md` |
| Rule 3 — claim vocabulary is load-bearing | all `SKILL.md` |
| Rule 4 — instructions written in the order they are performed | `creative-coding`, `digital-video` |
| Rule 5 — no named member from memory; the lookup leaves a source block | all `SKILL.md` |
| Rule 6 — a retraction names the cause, not the state | all `SKILL.md` |

Verification tiers, citation style and the additive-maintenance rule are also defined there, and per-document tier schemes are defined in each skill's `references/INDEX.md`.

**The mechanical provenance check**, for running against the repo directly:

```bash
# scoped: the rule applies to digital-video and creative-coding only
for f in $(find digital-video/references creative-coding/references -name '*.md' \
           ! -name INDEX.md ! -name STORAGE.md ! -name README.md); do
  grep -q "^## Provenance" "$f" || echo "MISSING PROVENANCE: $f"
done
```
