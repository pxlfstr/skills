## Provenance

**Web-sourced, mixed tiers** — no manual read in full this session. Built from Blackmagic's own product/tech-spec pages, Blackmagic support-staff forum posts (named individually below, since a support rep's direct statement is stronger evidence than a dealer listing), and independent user forum reports. Every claim below is tagged by which of these it rests on. No device in this document has been bench-tested by the user as of this writing — everything is Verified-by-source-quality, not Verified-by-hands-on-confirmation.

---

## 1. Product line, at a glance

| Line | Monitoring | Notes |
|---|---|---|
| **Videohub** (plain, current-gen, e.g. "Videohub 12G") | **Yes** — built-in LCD, live video preview, spin-knob browsing | Marketed as "zero latency." 10x10 up to 80x80 sizes found |
| **Smart Videohub** (6G-era naming) | **Yes** — same LCD/monitoring feature, explicitly the line's namesake ("Smart" = monitoring + spin-knob control) | 12x12, 20x20, 40x40 |
| **Smart Videohub CleanSwitch** | Yes, same as above | The one line with per-input frame synchronizers — see §3 |
| **Videohub Mini** (4x2/6x2/8x4) | **Not confirmed present** — every spec listing checked lists control features but never states an LCD/monitoring line item, unlike every full-size listing, which states it every time | Compact/affordable tier; absence is consistent enough across sources to treat as likely, not just unconfirmed |

**Correction worth recording:** built-in source monitoring is not a "Smart" vs "regular" distinction — it is present on both plain Videohub 12G and Smart Videohub lines. The actual dividing line is full-size vs. Mini.

## 2. Genlock / reference input — what it actually does

**[Verified — Blackmagic support rep "Gary," Blackmagic Forum, direct and unambiguous]:**

> "The Reference input on **all** VideoHubs (one exception) controls when the switch happens vertically between inputs. **It does not genlock any video.** The one exception is the Videohub CleanSwitch, where there are frame synchronizers on every input for this purpose."

This is the single most authoritative statement found on this topic — a named Blackmagic support rep, stated plainly, no hedging.

**What this means for a standard (non-CleanSwitch) Videohub or Smart Videohub:**
- The video signal itself is **not touched, delayed, or resynced** by the reference input. Pass-through is reclock-only (bit-level correction), described by Blackmagic support rep **Kaspar Ko** as producing "negligible latency in the magnitude of lines" — not frames, not meaningfully measurable in any practical sense.
- Reference only affects **when a crosspoint switch executes** — with reference connected and sources genlocked/matched, a switch is timed to land in the vertical blanking interval, producing a clean cut. Per Ko: "The only time you would see any latency from the Videohub is when you are switching inputs/outputs" — and even that isn't added *delay*, it's the switch executing at a chosen moment rather than instantly.
- **Without matched timing/reference, a switch can produce a visible glitch** at the switch instant — described independently by a separate forum user: properly-referenced routers of this era "worked correctly and would switch instantly in the vertical interleave timing resulting in a fast and glitchless switch."

**Net: a standard Videohub/Smart Videohub adds no meaningful latency to the signal path at any time, referenced or not.** Its only cost is a possible momentary glitch at switch time if sources aren't timing-matched — which proper genlocking exists specifically to prevent.

## 3. CleanSwitch — the one exception

**[Verified — multiple independent forum sources, consistent figures]:**

CleanSwitch models add **per-input frame synchronizers**, specifically to eliminate the switch-instant glitch a standard Videohub can produce. This is a deliberate tradeoff:

- **Adds a genuine, sustained 1-frame delay** — stated explicitly: "1 frame delay (in a 60Hz environment that is 16ms — 50Hz it's 20ms) because of the frame buffer inside the cleanswitch." This delay applies continuously, not just at switch moments — every signal passing through a CleanSwitch unit carries this buffer, all the time.
- Sync is **stripped on input and reinserted on output** of the frame buffer — a fundamentally different signal-path architecture from a standard Videohub's simple reclock-and-pass-through.

**⚠️ One credible, unresolved first-hand report worth flagging** — Blackmagic Forum user **Daniel Wittenaar** (experienced facility operator) reported that his 12x12 CleanSwitch appeared to **genlock its outputs to the timing of Input 1**, not to the external reference (PAL black burst) connected to the unit — "which appears to have no genlocking effect, whether or not it's plugged into the 12x12." This is a single first-hand bench report, not corroborated elsewhere in what was searched, and it is specific to CleanSwitch's frame-sync mechanism — it does not extend to the plain Videohub's much simpler (and separately, clearly documented) switch-timing-only behavior. If a CleanSwitch unit's actual reference-locking behavior matters for a project, this is worth a direct bench check rather than trusting the spec sheet.

## 4. Choosing between standard and CleanSwitch

For a latency-sensitive chain where sources are already genlocked to a common reference (the standard, correct setup) — **plain Videohub/Smart Videohub is the lower-latency choice**, with effectively zero added delay. CleanSwitch trades a guaranteed, continuous 1-frame delay for switch-glitch immunity — worth it only if mid-show switching happens often enough, or sources are timing-mismatched often enough, that glitch prevention outweighs the fixed latency cost.

---

## Verification status

| Claim | Status |
|---|---|
| Reference input only times switches, doesn't touch video timing | **Verified** — named Blackmagic support rep (Gary), direct statement |
| Standard pass-through latency is negligible (reclock only) | **Verified** — named Blackmagic support rep (Kaspar Ko) |
| CleanSwitch adds exactly 1 frame (16/20ms) of continuous delay | **Verified** — stated explicitly in forum sourcing, consistent across mentions |
| Built-in LCD monitor present on Videohub 12G and Smart Videohub lines | **Verified** — Blackmagic's own product/tech-spec pages, consistent across every model checked |
| Videohub Mini lacks the LCD monitor | **Likely, not directly confirmed** — consistent absence across multiple spec listings, but no source states this as an explicit negative |
| CleanSwitch genlocking to Input 1 rather than external reference | **Single first-hand report, unresolved** — not corroborated elsewhere, specific to one user's unit/firmware |

## Not yet verified — open items

- Whether the Wittenaar CleanSwitch reference-tracking issue is a known/widespread firmware behavior or an isolated unit problem.
- Exact behavior of a standard Videohub under genuinely mismatched input formats/rates when reference is connected — "can glitch" is established, but not how severely or for how long.
- Whether Videohub Mini has any built-in monitoring at all — worth a direct spec-sheet check if this becomes relevant to a purchase decision.
- ATEM AUX output latency — raised in conversation, answered only from general switcher-architecture reasoning (frame-store-based switchers typically don't add a second latency layer for an AUX tap vs. Program), **not sourced to any ATEM manual or Blackmagic documentation.** Worth a dedicated check if this matters for a specific show.
