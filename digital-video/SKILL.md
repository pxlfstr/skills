---
name: digital-video
description: Digital & IP video signal and devices: live switchers/routing, SDI/HDMI/NDI/ST 2110/SRT, sync and genlock, pixel clock and link bandwidth, codecs, color, LED processors, projection optics. Control protocols, TouchDesigner operators and media-server APIs live in the sibling creative-coding skill. Trigger on 'digital video skill' or work in this domain.
---

# Digital & IP Video Engineering

**This file holds no rules.** It exists only to send Claude to the repository, where the rules and the library live.

⚠️ **FROZEN — do not edit.** This file is installed in Claude and cannot be updated by a commit; changing it requires the user to re-upload the skill by hand. Rules change in `RULES.md`, scope changes in `GUIDE.md`, and both come from the clone. If a session believes this file needs changing, say so and let the user decide — do not edit it silently.

## The gate — nothing happens before this

**Do not answer, reason, propose, diagnose, or write a single line of code until Steps 1 and 2 below are done.** Not a partial answer, not "while that clones, here's my thinking", not a guess offered for speed. There is no question urgent enough to skip them.

**The reason is not procedure, it is accuracy.** Claude is a language model. It produces fluent, confident, plausible-looking answers whether or not it knows the thing — invented method names, invented parameters, invented device behaviour, all in the same register as the correct material around them. Reading the reference is the only thing that separates the two. Reasoning unaided feels identical from the inside and is not a substitute.

**This applies mid-session, not just at the start.** Turn forty is where it fails: the clone happened hours ago, the conversation has momentum, the next question feels like a continuation. It is not. Every question that touches an operator, a device, a protocol or an API gets the covering document opened again.

## Step 1 — clone

```bash
[ -d /tmp/skills-repo ] || git clone --depth 1 https://github.com/pxlfstr/skills.git /tmp/skills-repo
git -C /tmp/skills-repo log -1 --format='%h %ad %s' --date=short
```

Report the commit date in the reply.

## Step 2 — read both of these, in full, before replying

1. `/tmp/skills-repo/RULES.md` — operating rules for all skills
2. `/tmp/skills-repo/digital-video/GUIDE.md` — this skill's scope, workflow and knowledge map

Then `/tmp/skills-repo/digital-video/references/INDEX.md` before answering anything that touches the library.


**Cloning is not reading.** The clone puts files on disk and nothing in context. **After cloning, Claude knows nothing it did not know before.** Steps 1 and 2 are one action, not two.

**If a question touches something the library covers, open that document too** — `INDEX.md` says which. Answering from memory when a reference exists is the failure this whole structure was built to stop.

## If the clone fails

**Stop and tell the user.** Do not proceed from memory — the rules are not in this file and cannot be reconstructed. Say the clone failed, say why, and ask how to proceed.

## Re-pull

`git -C /tmp/skills-repo pull` when the user says they have committed, or when the answer turns on how current the library is.
