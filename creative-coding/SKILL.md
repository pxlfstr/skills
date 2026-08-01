---
name: creative-coding
description: Code and working patterns for live video and show control — MIDI and OSC control surfaces, TouchDesigner networks and Python, Resolume and Bitfocus Companion integration, and the protocol glue between them. Also holds the control-protocol reference: TouchDesigner operator behaviour, Resolume REST/WebSocket/OSC, MIDI and DMX/Art-Net. Sibling to the digital-video skill, which keeps video-signal and device facts. Use this skill whenever the user is writing, debugging, or extending code for a live video or show system, or needs a control-protocol or TouchDesigner operator fact — TouchDesigner networks, Script CHOPs, Web Server/Client DATs, MIDI or gamepad control surfaces, OSC senders and receivers, DMX output, sequencers, or media-server automation. Trigger it even if the user doesn't name it, and even if the request looks like a plain Python or JavaScript question, as long as the target is one of their show tools.
---

# Creative Coding

Code, control protocols, and working patterns for live video and show control. Sibling skill to `digital-video`.

## The dividing line — revised 2026-08-01

**The split is by domain, not by fact-versus-pattern.** The old rule sent every protocol fact to `digital-video`, which pushed TouchDesigner operator reference, MIDI maps and the Resolume control API into a skill about video signal. That drift is what this revision corrects.

**The test — one question:**

> Would this still be true if TouchDesigner, Resolume and every control surface disappeared?

| Answer | Skill | Because |
|---|---|---|
| **Yes** — it's about the video signal or a video device's own behaviour | `digital-video` | SDI/HDMI/NDI/ST 2110, pixel clocks and link bandwidth, genlock, codecs, colour, LED processors, projector optics, switcher and scaler behaviour |
| **No** — it's a control protocol, a data protocol, or software integration | `creative-coding` | TouchDesigner operators and Python, Resolume REST/WebSocket/OSC, MIDI, **DMX and Art-Net in full**, timecode as *control*, Companion, control-surface maps, show-control code |

**DMX, Art-Net and sACN live entirely here** — including the packet-level and universe-counting material. They are control protocols that happen to drive lights and pixels; nothing about them is a video signal fact.

**Both facts and patterns live in this skill now.** Within it, keep them separated by the confidence tiers below — a vendor number is `[Official]`, a structure the user developed is `Bench-verified` or `Designed`. Do not blur the two just because they share a library.

**Still true: never duplicate across the boundary.** If a document belongs in `digital-video`, cite into it rather than restating it, so there is exactly one place a spec can be wrong. The traffic now runs mostly the other way — this skill is the larger library, and `digital-video` cites in for anything protocol-shaped.

### Borderline cases, decided

| Document | Skill | Reasoning |
|---|---|---|
| `atem-supersource.md` | `digital-video` | SuperSource is a video compositing feature of a switcher — device behaviour, not a control protocol. The SDK inventory rides along rather than pulling it across |
| `atem-supersource-simulator.md` | `creative-coding` | It's a tool that was built. Sits alongside the reference above, deliberately |
| `panasonic-ptz-sources.md` | `digital-video` | **The closest call.** The document is mostly a control protocol (AW command sets, the 40 ms inter-command gap), which argues for `creative-coding`; it is also a camera source registry for video hardware. Left in `digital-video` — revisit if PTZ control code grows |
| `resolume-control-interfaces.md` | `creative-coding` | All 13 protocols are control or sync, none are video signal |

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

## Two structural rules — added 2026-08-01

These exist because a behavioural rule ("be careful about sourcing") has repeatedly failed. Both of these are checkable by looking, not by trusting judgement.

### Rule 1 — `protocols/` and `patterns/` are separate folders. A document lives in exactly one.

`references/protocols/` — vendor and protocol facts. Operator parameters, MIDI maps, API endpoints, port numbers, packet structure. Sourced from documentation; tiered `[Official]` / `[Forum]` / `[Lead]`.

`references/patterns/` — structures the user developed. Tiered Shipped / Bench-verified / Designed / Abandoned.

**Never mix the two inside one file.** When a document starts accumulating the other kind, split it — do not add a section. A misfiled document is then visible in a directory listing in seconds, which is the property the old cross-skill boundary used to provide and this replaces.

Where a pattern depends on a protocol fact, **cite the file in `protocols/` rather than restating the number.** One place per spec, exactly as before — the citation is now within this library instead of across to `digital-video`.

### Rule 2 — every reference document opens with a provenance block

Not just the ones that happen to get one. No exceptions, including short documents. The block states, at minimum:

```
## Provenance
- Sourcing tier(s) present in this document, and which sections carry which
- For each web source: the page's own last-edited date, and its oldid or revision
  identifier where the source exposes one
- What was NOT read, listed explicitly
- Open contradictions, in place — never silently resolved
```

A document without this block is not finished. The provenance block is what caught the errors that careful reading did not.

**The heading must be exactly `## Provenance`** (a suffix such as `## Provenance — ⚠️ READ THIS FIRST` is fine; a different word is not), placed **above the first content heading**. This is so coverage can be checked mechanically:

```bash
for f in $(find */references -name '*.md' ! -name INDEX.md ! -name STORAGE.md); do
  grep -q "^## Provenance" "$f" || echo "MISSING PROVENANCE: $f"
done
```

**All 17 reference documents across both skills carry one as of 2026-08-01.** Twelve were retrofitted that day from each document's own inline tier tags and source statements — the blocks summarise what the documents already recorded, and where a document never recorded what was *not* read, the block says so rather than guessing.

### Rule 3 — claim vocabulary is load-bearing

Never write any of these without the concrete evidence attached in the same sentence:

| Word | Requires |
|---|---|
| **"full page read"** | The page's last-edited date, and an oldid where available |
| **"verified"** | Named source, read directly this session or an earlier one that is cited |
| **"unreachable" / "not available"** | An actual attempt that failed, and the failure mode. A tool refusing a URL for lack of provenance is **not** unreachability — say what actually happened |
| **"confirmed"** | Two independent sources, or one source plus a bench test. Name both |
| **"the docs say"** | Which page. If the claim came from another page *mentioning* the parameter, that is second-hand — say so |

**No evidence, weaker word.** "Appears to", "reportedly", "second-hand from X", "inferred". Downgrading a claim costs nothing; an overstated one gets discovered live.

When a fact arrives from a page that merely *references* another page's parameter, it is **second-hand until the owning page is read.** Mark it and move on — do not launder it into a flat assertion.


---

## Workflow

1. **Sync the library from the canonical repo.** The `references/` folder in this container is a snapshot taken at the last skill upload and may be weeks stale. The canonical library is public and needs no credentials:

   ```bash
   git clone --depth 1 https://github.com/pxlfstr/skills.git /tmp/skills-repo
   git -C /tmp/skills-repo log -1 --format='%h %ad %s' --date=short
   ```

   Prefer `/tmp/skills-repo/creative-coding/references/` over the local copy wherever they differ, and **state the repo's last commit date** so the user knows how current the library is. Pull `/tmp/skills-repo/digital-video/references/` in the same clone — coding work still needs video-signal and device facts from it (bandwidth ceilings, LED processor behaviour, projector optics, switcher behaviour), even though the protocol reference now lives here.

2. **Read `references/INDEX.md`** before answering. It is the manifest.

3. **Separate fact from pattern before writing anything — but both stay in this skill now.** Tag a vendor or protocol number `[Official]` and a developed structure `Bench-verified` / `Designed`; never let the two blur into one paragraph. Only a *video-signal or device* fact goes to `digital-video`. If a request needs both sides of that boundary, produce two deliverables and cite across.

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
- **Video-signal and device questions** — bandwidth ceilings, genlock, codecs, colour, LED processors, projector optics. Those are `digital-video`. Control protocols are no longer in that set; they are here.

---

## Reference library

**Canonical source: https://github.com/pxlfstr/skills** (`creative-coding/references/`). The repo is authoritative; the copy in this container is a snapshot.

- `references/INDEX.md` — the manifest. Read first.
- `references/STORAGE.md` — how to add a document, including the additive/non-lossy rule and the public-repo screen.

**Nothing written to `references/` persists.** This container is discarded when the session ends; the only durable copy is the GitHub repository above. Never tell the user a document has been "stored" or "saved to the skill" on the basis of having written it to disk. Produce the file, deliver it as a download, and say plainly that it needs to be committed.
