# Creative Coding — guide

Read after `RULES.md`. Scope, workflow and knowledge map for this skill.


# Creative Coding

Code, control protocols, and working patterns for live video and show control. Sibling skill to `digital-video`.

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

---

## Workflow

The Order of operations in `RULES.md` runs first, every turn. What follows applies once you are writing.

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
