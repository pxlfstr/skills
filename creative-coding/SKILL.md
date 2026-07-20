---
name: creative-coding
description: The user's own code for live video and show-control — TouchDesigner Python, Resolume/Companion integration, control-surface builds, OSC/WebSocket/REST glue, and the working patterns behind them. Sidecar to the digital-video skill. Use this skill whenever the user is writing, debugging, or extending code for a live video or show system — TouchDesigner networks, Script CHOPs, Web Server DATs, gamepad/MIDI control surfaces, camera control senders, sequencers, media-server automation, or anything talking to Resolume, Companion, or PTZ hardware over a protocol. Trigger it even if the user doesn't name it, and even if the request looks like a plain Python or JavaScript question, as long as the target is one of their show tools.
---

# Creative Coding

The user's own codebase for live video and show control. This is where **their** patterns live — the things we built, tested on their rig, broke, and fixed. It is a sidecar to `digital-video`, not a replacement for it.

**The dividing line, and it is the whole point of this skill existing:**

| Kind of thing | Lives in | Example |
|---|---|---|
| Vendor/protocol fact | `digital-video` | AW protocol command syntax, Resolume REST endpoints, NDI HX3 decode support, HDBaseT limits |
| Our code and our patterns | `creative-coding` | The digest-auth AW sender, the `resId` column-identity scheme, the XInput Script CHOP, the 40 ms throttle |

Facts get looked up. Patterns get remembered. **Never duplicate a vendor fact into this skill** — cite across to `digital-video` instead, so there is exactly one place a spec can be wrong.

## Privacy — read before storing anything

This skill is **not public**. It must never be committed to `https://github.com/pxlfstr/skills`, which is a public repository. It contains show-specific code, venue and rig details, IP addresses, credentials patterns, and client work.

- **Never** `git push`, PR, or copy any part of this skill into the public repo.
- **Never** paste code from this skill into a public issue, forum post, or bug report without stripping it first.
- When filing an upstream bug (e.g. against a Bitfocus module), reduce to a minimal repro that contains no rig detail.
- Storage path for this skill is the user's private repo or a local archive — see `references/STORAGE.md`.

If asked to "commit the skills," ask which one. `digital-video` and `analog-video` are public; this one is not.

## Our techniques are not facts

The user's standing objection, and the reason this skill is separated out: **do not present our working patterns as though they were documented behavior.**

Every technique in here is something we arrived at empirically on one rig, often by trial and error, sometimes without root-causing the underlying problem. That is genuinely useful — it is *not* the same epistemic object as a line in a manufacturer's manual.

So:

- Attribute patterns as **ours**: "the approach we landed on," "what worked on your rig," not "the correct way to do this" or "TouchDesigner requires."
- Say what was actually established vs. inferred. If a workaround works but we never found out why, **say we never found out why** — every time it comes up, not just the first time.
- Tuned constants (timeouts, poll intervals, throttles) are empirical for one machine on one network. Flag them as such whenever they're reused in a new context.
- If a pattern exists because a vendor bug exists, name the bug and note it may be fixed — the workaround can outlive its reason and become the new problem.
- Never launder a technique into a fact by restating it confidently in a later session. Provenance travels with the pattern.

### Confidence tiers for stored code and patterns

| Tier | Means | Treat as |
|---|---|---|
| **Shipped** | Ran in an actual show or install without failing | Trustworthy in that exact context; still ours, still not a spec |
| **Bench-verified** | Tested on the user's rig, observed working, not yet load-bearing in a show | Good; re-verify under show conditions |
| **Designed** | Written and reasoned through, never run | Untested. Say so, prominently |
| **Abandoned** | Tried, didn't work, superseded | Keep it — the record of what failed is worth as much as what worked. Note *why* if known |

Mark every stored pattern with a tier. An unmarked pattern is **Designed** until proven otherwise.

## Sourcing hardware and protocol detail

When a coding task needs a device fact — a command string, an endpoint, a parameter path, a port, a timing requirement — **do not write it from memory and do not store it here.** Pull it from `digital-video`:

```bash
git clone --depth 1 https://github.com/pxlfstr/skills.git /tmp/skills-repo
git -C /tmp/skills-repo log -1 --format='%h %ad %s' --date=short
cat /tmp/skills-repo/digital-video/references/INDEX.md
```

Then read the relevant reference file from `/tmp/skills-repo/digital-video/references/`. State the repo's last commit date so the user knows how current the library is.

If the fact isn't in `digital-video` yet:

1. Research it properly (manufacturer doc, standards doc, the device's own manual).
2. Note that it **belongs in `digital-video`**, and offer to write it there — as a separate deliverable to be committed to the public repo.
3. Use it in the code here, citing across rather than copying.

If a clone fails, say so plainly and fall back to whatever local copy exists, flagging that it may be stale. Do not fill the gap with a remembered value — the no-false-numbers rule from `digital-video` applies here in full.

## Working rules

**Full scripts, never diffs.** On any update to any script, output the complete file. Never "change just this line," never a partial patch, never an ellipsis standing in for unchanged code. This applies to every language and every project in this skill. It is the single most-repeated correction in this working relationship.

**The user is the engineer.** They decide architecture and make the calls. Flag a factual error once, with backing, then defer. Don't argue, don't pad, don't re-litigate a decision they've made.

**Debug by observing, not guessing.** The pattern that has repeatedly worked: introspect live state directly rather than adding print statements and reloading. In TouchDesigner that means reading module state from the console (`mod('/project1/thing')._some_state`). Establish what the system is actually doing before proposing a fix.

**Root-cause before workaround, but ship the workaround.** Say which one is being delivered. A workaround shipped knowingly is fine; a workaround mistaken for a fix is not.

**Be concise.** Bullets and explicit steps over prose paragraphs. Keep caveats grouped at the end rather than interleaved through the answer. The user reads these to act on them.

## Scope

Code and integration work for live video and show control:

- **TouchDesigner** — Python in Script CHOPs/DATs, Execute DAT callbacks, Web Server DAT and browser UIs, MIDI/gamepad input, table-driven architectures, state management, cook-order and timing problems.
- **Show control integration** — Bitfocus Companion (modules, custom variables, generic-websocket, triggers), OSC relays, division of labor between controllers sharing one device.
- **Media server automation** — Resolume REST/WebSocket clients, composition state tracking, cue/sequencer logic.
- **Device control senders** — HTTP/CGI, digest auth, serial, throttling and rate-limit handling for PTZ and other hardware.
- **Standalone tools** — the HTML/Python utilities built alongside shows (router crosspoint panels, patch calculators, config generators).

Out of scope, and belongs in `digital-video`: signal chain design, format and bandwidth math, device selection, projection and LED engineering, protocol specifications.

## Reference library

`references/` holds the stored patterns and code notes. Two helper files govern it:

- `references/INDEX.md` — the manifest. Read it first when this skill is active.
- `references/STORAGE.md` — how to add material, how tiers are assigned, and where this skill is allowed to be stored.

**Nothing written to `references/` persists.** The container is discarded at session end. Never describe something as "stored" or "saved to the skill" on the basis of having written it to disk. Produce the file, deliver it as a download, and say plainly that it needs to be committed to the private repo. Full rules in `references/STORAGE.md`.
