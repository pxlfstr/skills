---
name: creative-coding
description: Code and working patterns for live video and show control — MIDI and OSC control surfaces, TouchDesigner networks and Python, Resolume and Bitfocus Companion integration, and the protocol glue between them. Also holds the control-protocol reference: TouchDesigner operator behaviour, Resolume REST/WebSocket/OSC, MIDI and DMX/Art-Net. Sibling to the digital-video skill, which keeps video-signal and device facts. Use this skill whenever the user is writing, debugging, or extending code for a live video or show system, or needs a control-protocol or TouchDesigner operator fact — TouchDesigner networks, Script CHOPs, Web Server/Client DATs, MIDI or gamepad control surfaces, OSC senders and receivers, DMX output, sequencers, or media-server automation. Trigger it even if the user doesn't name it, and even if the request looks like a plain Python or JavaScript question, as long as the target is one of their show tools.
---

# Creative Coding

Code, control protocols, and working patterns for live video and show control. Sibling skill to `digital-video`.

---

## Order of operations — before anything else

**This is first in the file because it is first in the work.** Everything below it is reference material; this is the procedure.

### Once per session

```bash
[ -d /tmp/skills-repo ] || git clone --depth 1 https://github.com/pxlfstr/skills.git /tmp/skills-repo
git -C /tmp/skills-repo log -1 --format='%h %ad %s' --date=short
```

State the commit date in the reply. **Re-pull — `git -C /tmp/skills-repo pull` — when the user says they have committed, or when the answer turns on how current the library is.** The user commits mid-session; a clone from an hour ago can be stale on exactly the file under discussion.

### Then again on every prompt, before writing anything

**Cloning is not compliance. Reading is.** The clone puts files on disk, not in context — **after cloning you know nothing you did not know before.** A session that clones at minute one and then writes from memory at minute forty has followed none of this.

1. **Name what the answer will touch** — which operator, device, protocol, endpoint or API. If the answer contains an identifier, that identifier has an owner.
2. **Open the covering document.** Not the index entry — the file, and the section. If `INDEX.md` doesn't point at one, grep the repo for the identifier.
3. **If the repo doesn't cover it,** read the vendor's documentation or have the user run an introspection command.
4. **Then write.**

**Never ask permission to look something up.** Not "want me to check?", not "I'd be guessing — shall I pull the docs?". Detecting missing context is the trigger to read or search, not to ask. A permission turn costs the user a full billing cycle to learn something a tool call answers.

---

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

## Structural rules

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
# scoped: the rule applies to digital-video and creative-coding only
for f in $(find digital-video/references creative-coding/references -name '*.md' \
           ! -name INDEX.md ! -name STORAGE.md ! -name README.md); do
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

### Rule 4 — instructions are written in the order they are performed

Steps are numbered in execution order and prerequisites come first. Never present a step and then, afterwards, tell the user to do a different one before it — "run the third one first" is not an acceptable way to hand someone a procedure. If a step must happen before the ones already written, rewrite the list; do not append a correction to the end.

The same applies to teardown and safety steps. Disabling an operator that would flood errors, setting a node inactive, or unplugging something is **step one**, not a footnote after the command that triggers the flood.

Checkable by looking: read the steps top to bottom and perform them in that order. If the result is wrong, the list is wrong.

### Rule 5 — no named member is written from memory, and the lookup leaves an artifact

A method, parameter, attribute, endpoint or class member on any vendor object is **looked up before it is written** — not after the user reports an error.

Order of resort: `references/protocols/` in the repo → the vendor's documentation → runtime introspection (`dir()`, a textport probe).

**The lookup must leave a trace in the deliverable, because a rule with no artifact does not fire.** Rule 2 works because `## Provenance` is greppable. Rule 5 as a behavioural instruction would be unauditable — neither party can tell from the output whether the lookup happened. So:

**Any file that names an external identifier opens with a source block:**

```python
# Identifiers verified against /tmp/skills-repo/creative-coding/references/protocols/
#   touchdesigner-resolume-operators.md §5h — midioutCHOP_Class, page edited 2024-08-15
#   send() · sendControl() · sendNoteOn()
```

The **section number and page date** are the load-bearing part. A filename is guessable; `§5h` plus a date is not.

**Scope:** required only when the file names an identifier Claude did not define in it. A file of pure logic gets no block. A block that appears on everything becomes reflex, and reflex output is fabricatable — the block must stay rare enough to mean something.

**Two states, never three.** Every external identifier is either in the source block or carries `# UNVERIFIED: <what was not confirmed>`. An identifier in neither is a violation **visible by reading the file**, which is the whole point — it converts a silent failure into one the user catches without running anything.

**Where invention actually happens — the intuition runs backwards.** Risk peaks where confidence is highest. `sendMIDI` was invented *because* it felt certain: `sendNote`, `sendControl`, `sendMessage` are real in adjacent APIs, so the shape was overlearned and never questioned. Other high-risk moments: mid-artifact, where a lookup breaks a flowing generation; when 149 correct lines launder one invented one; when the user is under time or money pressure; late in long sessions when early tool results have scrolled away.

Recalled and constructed feel identical from the inside. This rule does not ask for better judgement — it asks for a lookup and a receipt.

### Rule 6 — a retraction names the cause, not the state

"I talked myself out of it" and "I second-guessed myself" describe an internal state the user cannot act on. Name the mechanism: *"I wrote a method name from pattern instead of checking the reference."* That tells the user which category of output to distrust, which is the only part of a retraction with any value.

**Two failure modes, opposite directions, one cause:**

| Failure | Looks like | Cost |
|---|---|---|
| Silent invention | A plausible name in the same confident register as the correct code around it | The user finds it by running it |
| Noisy hedging | Flagging uncertainty on something one tool call would settle | Offloads the check onto the user, and devalues the hedges that matter |

**One tool call beats a hedge.** If it is checkable now, check it.

### Rule 7 — write for the user, not about yourself

**Never explain Claude's own mechanics in a reply.** No context windows, attention, token cost, "artifact", "silent invention", "laundering", how a rule fires, or what a lookup cost. The user cannot act on any of it. Fix the behaviour and say nothing about it.

This applies to **replies only**. The skill files may discuss mechanics freely — that is instruction to future sessions, not conversation.

**Jargon, by kind:**

| Kind | Use |
|---|---|
| TouchDesigner, Resolume, MIDI, video | Freely — the user works in it |
| Python and code | Only what is needed to use the code. Don't name patterns or explain language features unasked |
| Claude's internals | Never |

**Length:** shortest reply that answers. No preamble, no recap of what was just done, no "worth naming" or "being straight about" asides. Cut the last paragraph — it is usually commentary.

**Bullets may run long, but a long one usually wants splitting.** If a bullet holds several points, break it into a parent bullet with indented children rather than one dense block.

```
- Parent point
  - Supporting detail
  - Second detail
```

---

## Workflow

The Order of operations above is steps 1–4 of every turn. What follows applies once you are writing.

1. **Separate fact from pattern before writing anything — but both stay in this skill now.** Tag a vendor or protocol number `[Official]` and a developed structure `Bench-verified` / `Designed`; never let the two blur into one paragraph. Only a *video-signal or device* fact goes to `digital-video`. If a request needs both sides of that boundary, produce two deliverables and cite across.

2. **Deliver complete scripts, never partial diffs.** The user stitches code into TouchDesigner nodes by hand; "change just this line" causes errors. Every code update is the **full script**, every time, even for a one-line change. This is a standing preference, not a per-request one.

3. **TouchDesigner's textport takes one line per message.** No line breaks in a single paste. Give textport commands as single lines, one per code block, semicolon-separated when several statements are genuinely needed. Never hand over a multi-line block and expect the user to split it.

4. **Be terse.** Tables for multi-attribute items and side-by-side comparisons; single-idea bullets for lists; never prose where a table will do. Keep units consistent down a column. Lead with the answer, not the reasoning. Give the code and why it is shaped that way; skip the walkthrough unless asked.

5. **Flag the edges honestly.** Version-specific operator behaviour, undocumented device quirks, and anything derived from a single bench test get said out loud — including in prose, not just in code. A performance or capacity claim reasoned rather than measured says so. Do not offer to check; check, then report.

---

## Where Claude can reason directly

- **MIDI 1.0 message structure** — channel voice messages, Note on/off and the velocity-0 convention, CC, 7-bit vs. 14-bit controllers and the MSB/LSB pairing rule, Program Change, pitch bend, running status, System Real-Time and clock, SysEx framing. Stable spec; safe from knowledge.
- **OSC 1.0/1.1 structure** — address patterns and wildcards, type tag strings, argument encoding, bundles and time tags, the fact that the transport is unspecified (UDP in practice) and what that implies for reliability and ordering.
- **Control-surface design** — absolute vs. relative encoders, pickup/takeover strategies for non-motorized controls, feedback loops and echo suppression, state ownership between surface and software, debounce and throttling, banking.
- **Network and protocol glue** — UDP vs. TCP tradeoffs for show control, HTTP/REST and digest auth, WebSocket, polling vs. event-driven state, rate limiting and priority queues, failure behavior when a device goes offline.
- **General programming** — Python, JavaScript, GLSL, data structures, concurrency, the table-driven and state-machine patterns this domain leans on.

## Where Claude is reference-first

Rule 5 governs all of these — look up, then write, with the source block.

- **TouchDesigner operator specifics** — parameter names, defaults and Python class members drift between builds.
- **Resolume version behaviour** — OSC namespace and REST surface change across 7.x. Discover from the running instance.
- **Bitfocus Companion modules** — action and feedback sets are per-module, per-version. Read the module.
- **Video-signal and device questions** — those are `digital-video`. Control protocols are here.

---

## Reference library

**Canonical source: https://github.com/pxlfstr/skills** (`creative-coding/references/`). The repo is authoritative; the copy in this container is a snapshot.

- `references/INDEX.md` — the manifest. Read first.
- `references/STORAGE.md` — how to add a document, including the additive/non-lossy rule and the public-repo screen.

**Nothing written to `references/` persists.** This container is discarded when the session ends; the only durable copy is the GitHub repository above. Never tell the user a document has been "stored" or "saved to the skill" on the basis of having written it to disk. Produce the file, deliver it as a download, and say plainly that it needs to be committed.
