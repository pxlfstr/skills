---
name: creative-coding
description: Code and working patterns for live video and show control — MIDI and OSC control surfaces, TouchDesigner networks and Python, Resolume and Bitfocus Companion integration, and the protocol glue between them. Also holds the control-protocol reference: TouchDesigner operator behaviour, Resolume REST/WebSocket/OSC, MIDI and DMX/Art-Net. Sibling to the digital-video skill, which keeps video-signal and device facts. Use this skill whenever the user is writing, debugging, or extending code for a live video or show system, or needs a control-protocol or TouchDesigner operator fact — TouchDesigner networks, Script CHOPs, Web Server/Client DATs, MIDI or gamepad control surfaces, OSC senders and receivers, DMX output, sequencers, or media-server automation. Trigger it even if the user doesn't name it, and even if the request looks like a plain Python or JavaScript question, as long as the target is one of their show tools.
---

# Creative Coding

**This file is a stub. The rules and the library live in the repository.**

## Step 1 — clone, before answering anything

```bash
[ -d /tmp/skills-repo ] || git clone --depth 1 https://github.com/pxlfstr/skills.git /tmp/skills-repo
git -C /tmp/skills-repo log -1 --format='%h %ad %s' --date=short
```

Report the commit date in the reply.

## Step 2 — read both of these, in full, now

1. `/tmp/skills-repo/RULES.md` — operating rules for all skills
2. `/tmp/skills-repo/creative-coding/GUIDE.md` — this skill's scope, workflow and knowledge map

Then `/tmp/skills-repo/creative-coding/references/INDEX.md` before answering anything that touches the library.

**Cloning is not reading.** The clone puts files on disk and nothing in context. Steps 1 and 2 are one action, not two.

## If the clone fails

**Stop and tell the user.** Do not proceed from memory — the rules are not in this file and cannot be reconstructed. Say the clone failed, say why, and ask how to proceed.

## Re-pull

`git -C /tmp/skills-repo pull` when the user says they have committed, or when the answer turns on how current the library is.
