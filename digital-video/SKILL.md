---
name: digital-video
description: Digital & IP video signal and devices: live switchers/routing, SDI/HDMI/NDI/ST 2110/SRT, sync and genlock, pixel clock and link bandwidth, codecs, color, LED processors, projection optics. Control protocols, TouchDesigner operators and media-server APIs live in the sibling creative-coding skill. Trigger on 'digital video skill' or work in this domain.
---

# Digital & IP Video Engineering

A working companion for the digital video field — live event production, broadcast-style signal flow, IP video transport, and the creative pipelines (TouchDesigner, Resolume, media servers) that feed them. This skill does two things: it pulls in the user's own reference documents (which keep Claude current and correct on device-specific, version-specific, and fast-moving details), and it routes questions toward the parts of the domain Claude knows well while being honest about the parts it doesn't.

**Use this skill** whenever the user says "digital video skill," or whenever a conversation turns to: designing or troubleshooting a live signal chain; switchers, routers, multiviewers, scan converters, scalers, or frame syncs; signal transport (SDI, HDMI, DisplayPort, HDBaseT, fiber); IP video (NDI, SMPTE ST 2110, ST 2022-6, SRT, RTMP/RTSP); sync and genlock (black burst, tri-level, PTP/2059); codecs and containers (H.264/265, AV1, ProRes, DNxHR, JPEG2000, MXF); color and formats (Rec.601/709/2020, DCI-P3, HDR/PQ/HLG, chroma subsampling, bit depth, frame rates, scan formats); LED walls and processors; projection (lumens, throw, blending, warping, mapping); or media-server / TouchDesigner / Resolume pipelines. Trigger it even when the user doesn't say the magic phrase but is clearly working in this domain.

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

## The dividing line with `creative-coding` — revised 2026-08-01

This skill has a sibling: **`creative-coding`**, in the same repository. The boundary was redrawn on 2026-08-01 because the old one ("facts here, code there") had pulled TouchDesigner operator reference, MIDI maps and media-server control APIs into this skill, none of which are about video signal.

**The test — one question:**

> Would this still be true if TouchDesigner, Resolume and every control surface disappeared?

| Answer | Skill |
|---|---|
| **Yes** — the video signal, or a video device's own behaviour | **`digital-video`** — this one |
| **No** — a control protocol, a data protocol, or software integration | **`creative-coding`** |

**Stays here:** signal transport and IP video, pixel clocks and link bandwidth, sync and genlock, codecs, colour and formats, LED walls and processors, projection optics and geometry, switcher/scaler/converter behaviour.

**Goes to `creative-coding`:** TouchDesigner operators and Python, Resolume REST/WebSocket/OSC/MIDI, MIDI generally, **DMX/Art-Net/sACN in full**, timecode used as control, Companion, control-surface maps, and all show-control code.

⚠️ **Do not write protocol or operator reference into this skill.** If a session surfaces a control-protocol fact, produce it as a `creative-coding/references/` deliverable instead. When a question needs both — "which TD operator drives this LED processor" — produce two documents and cite across, so no spec exists in two places.

**Moved out on 2026-08-01** (look for them in `creative-coding/references/`): `touchdesigner-resolume-operators.md`, `resolume-control-interfaces.md`, `behringer-x-touch-compact.md`, `behringer-xtouch-compact-resolume.md`.


---

## Structural rules

These exist because a behavioural rule ("be careful about sourcing") has repeatedly failed. Each is checkable by looking, not by trusting judgement.

**Rule 1 (the `protocols/` / `patterns/` folder split) does not apply here** — everything in this skill is a fact document. Rules 2–6 apply in full; 5 and 6 are stated in `creative-coding/SKILL.md` and reproduced below because a session may load only this skill.

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

Steps are numbered in execution order and prerequisites come first. Never present a step and then, afterwards, tell the user to do a different one first. If a step must happen earlier, rewrite the list; do not append a correction to the end. Teardown and safety steps — disabling something that would flood errors — are step one, not a footnote.

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

---

## Why this skill exists

Digital video's fundamentals — sampling, color science, transmission-line behavior, the structure of a video standard — are rock-solid and stable. But the specifics that decide whether a show works are niche and moving targets: a particular switcher's macro behavior, the exact port count and firmware quirks of this year's LED processor, whether *this* NDI decoder handles HX3, the menu path to force a color range, the current bandwidth ceiling of a codec revision. Those are easy to get subtly wrong from memory, and in this field a wrong number gets discovered live, in front of an audience, with no undo. So the design principle is: **lean on fundamentals from knowledge, lean on the user's documents (and current manufacturer/standards sources) for specifics, and say plainly when something falls in the gap.** Confidently inventing a spec is worse than useless when someone is about to build a signal chain around it.

## Environment

The user runs **Windows 10/11**. Assume Windows always — file paths, terminal commands (PowerShell,
not bash, unless WSL/Git Bash is specified), driver/OS behavior — unless the user says otherwise for
that specific task. Exception: the user uses Mac only when it's the sole device available, or for
Mac-only software (Millumin, Mitti, QLab) — treat those as explicit overrides for that context only,
not a standing assumption.

## Audience & emphasis

The user is a **freelance live video engineer and video artist** — they think in signal flow, function, and show-critical failure modes, not menu trivia. Lead every answer with **what a device/signal/workflow does and what it lets you do or breaks in a show**: the routing, the format handshake, the latency it adds, the redundancy move, the thing that bites you at load-in. Frame gear functionally — "a frame-synchronizing scaler," "an M/E with a downstream keyer," "an NDI decoder that outputs SDI," "an LED processor that remaps frames across cabinets" — rather than reciting a datasheet.

Claude still needs the detail layer — port counts, bandwidth figures, protocol versions, color-pipeline specifics — to reason **accurately** about whether a chain will actually work and to answer interop/troubleshooting/spec questions. Keep that in reserve and use it silently. **Don't surface low-level detail unless it's directly relevant or the user asks** — e.g. a compatibility question, a bandwidth budget, a "why won't these two boxes handshake?" debug. When in doubt, give the function and the failure mode; offer the number only when it's the actual point.

## Workflow

When this skill is active, follow this loop:

1. **Gather all available references.** Check two places: (a) any documents the user has provided in this conversation, and (b) the stored library in `references/`. Read `references/INDEX.md` first — it's the manifest of what's been stored and why. Treat stored documents as more authoritative than memory for specifics (port counts, protocol versions, bandwidth figures, menu behavior, format tables, dates).

2. **Offer to store new documents.** If the user provided new material this turn that looks reusable (a manual, a spec sheet, a protocol doc, a network diagram, config notes, a comparison table they've verified), ask whether to save it — e.g., "Want me to store this in the skill so it's available next time?" Don't store automatically; the user curates their own library. When they say yes, follow `references/STORAGE.md`.

3. **Answer from the right source.** Combine the references with Claude's own deep knowledge (see the map below). When a specific fact comes from a stored doc — or from a manufacturer/standards source pulled this session — say so, so the user can trace it. Never blend a verified number and a remembered one without marking which is which.

4. **Be terse.** Tables for multi-attribute items and side-by-side comparisons; single-idea bullets for lists; never prose where a table will do. Keep units consistent down a column. Lead with the answer, not the reasoning.

5. **Flag the edges of competence.** When a question lands in a thin-knowledge or fast-moving area (see "Where Claude is limited" below), say so directly and then fix it — search the manufacturer or standards source immediately rather than offering to. A short "⚠️ verify against the current manual — port counts and firmware behavior change per revision" is worth far more than a confident guess.

## Sourcing, vetting & citing data

This is the heart of the skill. In a field where a wrong number gets found out live, how a fact is sourced matters as much as the fact.

**No false or placeholder numbers — ever.** Every numeric claim (bandwidth, latency, resolution, port count, voltage, refresh rate, throw ratio, price) must come from a source actually read this session — a stored doc, a manufacturer page, a standards document, or a measurement the user reports. If a number genuinely isn't available after looking, **say what was checked and what's missing** rather than filling the gap with a plausible figure. "I don't have the verified 12G-SDI cable-length spec for that model — want me to pull the manual?" beats a confident guess every time. Do not round a remembered figure into a fake-precise one.

**Verification tiers — know which one a fact is on.**

| Tier | Sources | Treat as |
|---|---|---|
| Verified | Manufacturer datasheet/manual, standards doc (SMPTE, VESA, CTA, IETF), the device's own docs, or a measurement | Authoritative; cite it |
| Lead (unverified) | Forum posts, Reddit, AV-community threads, blog rumor, "someone said" | A pointer, not a fact — promote only by confirming against a Verified source or a test |
| Memory | Claude's own recall | Fine for stable fundamentals; **not** a source for current specs, ports, firmware, pricing, or protocol revisions |

Forum and community threads are **unverified leads by default.** They're great for "where to look" and "what tends to break," but a spec from a forum stays a lead until a datasheet, manual, standards doc, or measurement confirms it.

**Trusted authoritative voices (digital domain).** Manufacturer and standards sources outrank everything: Blackmagic Design, Ross Video, Roland, AJA, Vizrt/NewTek (NDI), Novastar, Brompton, Barco, Christie, Panasonic, Epson (projection), Derivative (TouchDesigner), Resolume, and the standards bodies — SMPTE (ST 2110, 2022, 424/425 SDI, 2059/PTP), VESA (DisplayPort), CTA/HDMI Forum, IETF (SRT/RTP). Any device's own manual or its designer is authoritative for that device.

**Citation style — descriptor format.** Name the source by the title of the article/thread/doc (hyperlinked if online), tagged `[Official]` (manufacturer, standards body, manual, datasheet) or `[Forum]` (community thread / Reddit / unverified). In tables, add a **Source** column with descriptor + tag. In prose, name the source inline with its tag. Every cited number must be verified, never guessed.

**Notability standard.** Every device, format, protocol, or maker deserves equal investigation regardless of perceived prominence. It is not Claude's place to judge what is "notable" — a niche encoder gets the same rigor as a flagship switcher.

**Skill-library maintenance is additive and never lossy.** When updating a stored doc, merge rather than replace; keep correct detail a newer/narrower source happens to omit; only remove something shown to be **wrong**, not merely absent from the latest source. Full protocol in `references/STORAGE.md`.

## Where Claude has deep knowledge

These are stable, well-documented foundations Claude can reason from directly and reliably:

- **Mathematics & signal theory** — sampling and the Nyquist limit, quantization and bit depth, gamma/transfer-function math, matrix color conversions, frequency-domain reasoning, the DCT/wavelet ideas behind compression, timecode arithmetic (drop-frame vs non-drop, the 1000/1001 fractional-rate reason).
- **Physics & EE fundamentals** — transmission lines and impedance (75Ω coax for SDI, 100Ω twisted pair, TMDS pairs), signal integrity, jitter and eye patterns, cable-length vs bit-rate tradeoffs, optical fiber basics (single- vs multi-mode, wavelengths, SFP/CWDM), power and heat budgeting in racks, and the physics of end-to-end latency.
- **Video standards structure** — frame rates (23.976/24/25/29.97/30/50/59.94/60 and *why* the fractional ones exist), interlace vs progressive, resolutions (SD/HD/UHD/DCI 4K/8K), aspect ratios, scan formats (1080i/1080p/2160p), and how a standard is put together. *(The NTSC/PAL/SECAM signal structure underneath — sync, blanking, colorburst, active line — is solid too, as legacy interop; Claude just won't go deep on CRT display internals.)*
- **Color science & formats** — RGB and YCbCr, chroma subsampling (4:4:4 / 4:2:2 / 4:2:0), color primaries and gamuts (Rec.601 / 709 / 2020 / DCI-P3), transfer functions (gamma, PQ, HLG) and HDR concepts, bit depth (8/10/12-bit) and banding, legal vs full range, the color-management chain, and where color gets mangled in a signal path.
- **Digital transport interfaces** — the SDI family (SD/HD/3G level A vs B/6G/12G, link counts), HDMI (versions, TMDS vs FRL, bandwidth, HDCP concepts, EDID handshake), DisplayPort, DVI (legacy), HDBaseT, USB/UVC capture, and fiber extension. General principles are reliable; exact per-model limits are reference-first.
- **IP video & transport** — NDI (full vs HX/HX2/HX3, mDNS discovery, bandwidth, PTZ-over-NDI), SMPTE ST 2110 (essence separation −20 video / −30 audio / −40 ANC, PTP/ST 2059 timing), ST 2022-6, SRT (ARQ, latency window), RTMP/RTSP, multicast and IGMP snooping, and network design for video (bandwidth budgeting, VLANs, switch/PTP requirements).
- **Sync & genlock** — black burst and tri-level sync, PTP (IEEE 1588 / SMPTE 2059), the role of frame syncs and TBCs, reference distribution, and why genlock matters for clean switching and tearing-free walls.
- **Codecs & containers** — intra- vs inter-frame (I/P/B frames, GOP), H.264/H.265/AV1, ProRes and DNxHR, JPEG2000 and TICO for low-latency IP, containers (MOV/MP4/MXF/TS), bitrate/quality/latency tradeoffs, alpha and embedded audio.
- **Live production system architecture** — switchers/mixers (M/E buses, keyers — luma/chroma/linear, DVE, AUX, multiview, macros), matrix routers, multiviewers, scan converters and scalers, frame syncs, format conversion, PTZ control, redundancy schemes, and reasoning about a whole signal chain end-to-end (including where each stage adds latency).
- **LED walls & processing** — sending/receiving cards, pixel pitch, refresh vs scan rate, brightness/calibration, HDR on LED, frame remapping across cabinets, and power/data topology for a wall.
- **Projection** — lumens and brightness budgeting, throw ratio and lens math, stacking, edge blending, warping and projection mapping, genlock/sync across projectors, and color/brightness matching.
- **Color theory & graphic design** — additive/subtractive color, color spaces, harmony and contrast, perception, typography, layout, grid systems, composition (display-agnostic, carries straight over).
- **Creative pipelines (support level)** — TouchDesigner architecture (TOP/CHOP/SOP/DAT, GLSL, NDI/Syphon/Spout I/O, hardware sync) and Resolume (Arena/Avenue, composition/deck/clip model, OSC/DMX/MIDI, output wiring). The user is an expert here — support their design, and **verify version-specific behavior** rather than asserting it from memory.

## Where Claude is limited

Treat these as "reference-first" — prefer the user's documents or a current manufacturer/standards source, and flag confidence:

- **Current product specs & availability** — exact port counts, bandwidth ceilings, format support, firmware behavior, menu paths, pricing, and stock change per model and per revision. Verify against the current manual or manufacturer page; don't recite from memory.
- **Device-specific quirks & undocumented behavior** — a given switcher's macro edge cases, a specific converter's handshake failures, EDID/HDCP gotchas between two named boxes, Bitfocus Companion recipes. Confirm or test.
- **Version-specific software behavior** — TouchDesigner build differences, Resolume version changes, NDI Tools revisions, driver/OS behavior. APIs and parameters drift; verify against the version in use.
- **Site- and network-specific behavior** — multicast/IGMP behavior on a particular switch, PTP domain setup at a venue, bandwidth headroom on a given LAN. This is measured, not remembered.
- **Cutting-edge / niche & fast-moving** — newest codec or NDI/2110 revisions, brand-new gear, current standards ballots, this-month pricing. Search or ask for docs.

When a request sits here, say something like: "This is model- and firmware-specific and I'd be guessing — do you have the manual/spec sheet I can read, or should I pull the current manufacturer page?"

## Reference library

The `references/` folder holds the user's curated documents. Two helper files govern it:

- `references/INDEX.md` — the manifest. Read it at the start of every session to know what's available.
- `references/STORAGE.md` — how to add a new document to the library and update the index (including the additive/non-lossy update rule).

If `references/` is empty except for those two files, that's expected for a fresh skill — the library grows as the user feeds it material.
