---
name: analog-video
description: Expert companion for analog video art and engineering — broadcast television technology (NTSC/PAL/SECAM), CRT displays, video synthesizers (Rutt-Etra, LZX, Sandin, Paik-Abe), circuit bending, video art history, color theory, graphic design, liquid light shows, and the underlying physics, electrical engineering, and math (geometry, trig, calculus). Use this skill whenever the user says "analog video skill," or whenever a conversation turns to any of the above topics — designing or repairing video gear, reading schematics, understanding TV signal structure, planning a video-art or light-show piece, or interpreting documentation the user provides about analog video. The user supplies reference documents to extend and update Claude's knowledge; this skill is the protocol for using and growing that library. Trigger it even when the user doesn't say the magic phrase but is clearly working in this domain.
---

# Analog Video

**This file is a stub. The rules and the library live in the repository.**

## Step 1 — clone, before answering anything

```bash
[ -d /tmp/skills-repo ] || git clone --depth 1 https://github.com/pxlfstr/skills.git /tmp/skills-repo
git -C /tmp/skills-repo log -1 --format='%h %ad %s' --date=short
```

Report the commit date in the reply.

## Step 2 — read both of these, in full, now

1. `/tmp/skills-repo/RULES.md` — operating rules for all skills
2. `/tmp/skills-repo/analog-video/GUIDE.md` — this skill's scope, workflow and knowledge map

Then `/tmp/skills-repo/analog-video/references/INDEX.md` before answering anything that touches the library.

**Cloning is not reading.** The clone puts files on disk and nothing in context. Steps 1 and 2 are one action, not two.

## If the clone fails

**Stop and tell the user.** Do not proceed from memory — the rules are not in this file and cannot be reconstructed. Say the clone failed, say why, and ask how to proceed.

## Re-pull

`git -C /tmp/skills-repo pull` when the user says they have committed, or when the answer turns on how current the library is.
