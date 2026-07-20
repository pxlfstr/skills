---
name: creative-coding
description: Code and working patterns for live video and show control — MIDI and OSC control surfaces, TouchDesigner networks and Python, Resolume and Bitfocus Companion integration, and the protocol glue between them. Sidecar to the digital-video skill. Use this skill whenever the user is writing, debugging, or extending code for a live video or show system — TouchDesigner networks, Script CHOPs, Web Server/Client DATs, MIDI or gamepad control surfaces, OSC senders and receivers, sequencers, or media-server automation. Trigger it even if the user doesn't name it, and even if the request looks like a plain Python or JavaScript question, as long as the target is one of their show tools.
---

# Creative Coding

Code and working patterns for live video and show control. This is a **sidecar** to `digital-video`, not a replacement for it.

## The dividing line — this is why the skill exists

| Kind of thing | Lives in | Example |
|---|---|---|
| Vendor / protocol fact | `digital-video` | Resolume's OSC port, X-Touch CC numbers, AW protocol syntax, NDI HX3 decode support |
| Code and working patterns | `creative-coding` | The table-driven MIDI rename pattern, throttle-and-priority-chain structure, how to seed state on mode exit |

Facts get looked up. Patterns get remembered. **Never duplicate a vendor fact into this skill** — cite across to `digital-video` instead, so there is exactly one place a spec can be wrong.

When a coding session surfaces something that is actually a protocol fact, it does not belong in a code comment. Write it to `digital-video/references/` as a separate deliverable.

---

## What may and may not be committed

This skill lives in the **public** repository `https://github.com/pxlfstr/skills`. Everything here is world-readable.

**Belongs here:**
- Patterns written generically — the structure, not the deployment
- Protocol glue explained in the abstract
- Technique documented so it can be reused on a different rig

**Does not belong here:**
- Project- and show-specific code as built
- Client names, venue detail, rig inventories, camera IPs, network topology
- Credentials, tokens, or anything that implies them
- `.toe` files, show files, mapping tables naming real deployed gear

The authoring discipline is to write the pattern generically **from the start**, rather than writing it deployment-specific and sanitizing later. If a pattern cannot be stated without the rig it ran on, it is not ready to be a reference document.

---

## Confidence tiers — provenance travels with every pattern

The user's own empirically developed techniques must never be presented as documented facts. Every pattern carries a tier:

| Tier | Meaning |
|---|---|
| **Shipped** | Ran in a real show, start to finish, without intervention |
| **Bench-verified** | Tested on hardware, confirmed working, not yet shown |
| **Designed** | Reasoned through and written, not yet run against hardware |
| **Abandoned** | Tried and rejected — kept because knowing what failed is worth as much as knowing what worked |

State the tier in place. A Designed pattern presented as Shipped is the failure mode this system exists to prevent.

---

## Workflow

1. **Sync the library from the canonical repo.** The `references/` folder in this container is a snapshot taken at the last skill upload and may be weeks stale. The canonical library is public and needs no credentials:

   ```bash
   git clone --depth 1 https://github.com/pxlfstr/skills.git /tmp/skills-repo
   git -C /tmp/skills-repo log -1 --format='%h %ad %s' --date=short
   ```

   Prefer `/tmp/skills-repo/creative-coding/references/` over the local copy wherever they differ, and **state the repo's last commit date** so the user knows how current the library is. Pull `/tmp/skills-repo/digital-video/references/` in the same clone — coding work almost always needs hardware facts from it.

2. **Read `references/INDEX.md`** before answering. It is the manifest.

3. **Separate fact from pattern before writing anything.** A vendor number goes to `digital-video`. A structure goes here. If a request needs both, produce both, as two deliverables.

4. **Deliver complete scripts, never partial diffs.** The user stitches code into TouchDesigner nodes by hand; "change just this line" causes errors. Every code update is the **full script**, every time, even for a one-line change. This is a standing preference, not a per-request one.

5. **Be terse.** Bullets and tables over prose. Give the code and the reason it is shaped that way; skip the walkthrough unless asked.

6. **Flag the edges honestly.** Version-specific operator behavior, undocumented device quirks, and anything derived from a single bench test get said out loud. "I'd be guessing — want me to pull the current docs?" beats a confident invention.

---

## Where Claude can reason directly

- **MIDI 1.0 message structure** — channel voice messages, Note on/off and the velocity-0 convention, CC, 7-bit vs. 14-bit controllers and the MSB/LSB pairing rule, Program Change, pitch bend, running status, System Real-Time and clock, SysEx framing. Stable spec; safe from knowledge.
- **OSC 1.0/1.1 structure** — address patterns and wildcards, type tag strings, argument encoding, bundles and time tags, the fact that the transport is unspecified (UDP in practice) and what that implies for reliability and ordering.
- **Control-surface design** — absolute vs. relative encoders, pickup/takeover strategies for non-motorized controls, feedback loops and echo suppression, state ownership between surface and software, debounce and throttling, banking.
- **Network and protocol glue** — UDP vs. TCP tradeoffs for show control, HTTP/REST and digest auth, WebSocket, polling vs. event-driven state, rate limiting and priority queues, failure behavior when a device goes offline.
- **General programming** — Python, JavaScript, GLSL, data structures, concurrency, the table-driven and state-machine patterns this domain leans on.

## Where Claude is reference-first

- **TouchDesigner operator specifics** — parameter names, defaults, and Python class members drift between builds. Verify against docs.derivative.ca for the build in use.
- **Resolume version behavior** — the OSC namespace and REST surface change across 7.x. Discover from the running instance, don't recite.
- **Bitfocus Companion modules** — action and feedback sets are per-module and per-version, maintained in the open. Read the module.
- **Any device's control protocol** — that is a `digital-video` question. Go there or go to the manual.

---

## Reference library

**Canonical source: https://github.com/pxlfstr/skills** (`creative-coding/references/`). The repo is authoritative; the copy in this container is a snapshot.

- `references/INDEX.md` — the manifest. Read first.
- `references/STORAGE.md` — how to add a document, including the additive/non-lossy rule and the public-repo screen.

**Nothing written to `references/` persists.** This container is discarded when the session ends; the only durable copy is the GitHub repository above. Never tell the user a document has been "stored" or "saved to the skill" on the basis of having written it to disk. Produce the file, deliver it as a download, and say plainly that it needs to be committed.
