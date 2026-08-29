## Provenance

**Verified [Official]** — *ATEM Constellation Switchers Manual*, Blackmagic Design, user-supplied PDF, 2289 pp. total (English section: pp. 3–177; document covers ATEM 1/2/4 M/E Constellation HD and 4K, Constellation 8K, and 4 M/E Constellation 4K Plus in one manual), document dated June 2026. English section read in full for the specific question this document answers (input format handling); not read cover-to-cover for every feature. Supplemented by one Blackmagic official press release (a different ATEM model, cited for corroboration — tagged separately) and one forum report (tagged as such, not Verified).

This is a **separate document from `atem-supersource.md`**, which is scoped specifically to SuperSource compositing parameters and doesn't cover general input handling. Same manual, different section, different question — kept separate rather than merged, per the one-file-per-subject principle.

---

## 1. Per-input format conversion — the core finding

**[Verified — manual, "Plugging in Sources," p. 10]:**

> "Plug SDI cameras and other sources into the SDI inputs. These SDI connections feature **format conversion and frame synchronizers** so all sources will conform to the video format set on your switcher."

This is the only place in the English section where this behavior is described, and it is not elaborated further anywhere else in the ~175 pages read — no separate section breaks "format conversion" and "frame synchronizer" into distinct, individually-scoped capabilities.

**Practical meaning:** sources do not need to match each other, or match the switcher's configured operating standard, before being plugged in. Each SDI input carries its own conversion/sync stage that normalizes the incoming signal to whatever standard is set switcher-wide. This directly contradicts an unsourced, general-knowledge answer given earlier in this same session (that ATEM switchers typically require matched input timing with no per-input conversion) — that earlier answer is superseded by this manual and should not be trusted going forward.

## 2. The switcher-wide operating standard

**[Verified — manual, "Setting the Switcher Video Standard," p. 23]:**

One operating standard is set for the whole switcher — not per-input. Full supported list:

| Category | Rates | Model scope |
|---|---|---|
| HD | 720p50/59.94/60; 1080p23.98/24/25/29.97/30/50/59.94/60; 1080i50/59.94/60 | All Constellation models |
| Ultra HD | 2160p23.98/24/25/29.97/30/50/59.94/60 | 4K and 8K models only |
| 8K | 4320p23.98/24/25/29.97/30/50/59.94/60 | 8K models only |

Manual's own guidance: check camera format first, then set the switcher to match — this is a workflow recommendation to minimize conversion load, not a hard requirement, since §1 already establishes every input converts independently regardless.

**Model note, directly relevant to the user's original question:** the manual documents this as shared behavior across "ATEM Constellation switchers" generally and the standards table explicitly groups HD/4K/8K models together — nothing in this section singles out 1 M/E Constellation 4K as different from the rest of the family. Reasonable to treat as applying across the whole Constellation 4K line, though the manual doesn't state a specific per-model exhaustive confirmation.

**Changing the standard erases the media pool** — stated directly, worth flagging as an operational consequence, not just a spec detail.

## 3. ⚠️ Open question: does "format conversion" include resolution, or only timing/frame rate?

**This is not resolved by the manual — recorded honestly as unresolved, not picked one way.**

The manual's own wording ("format conversion and frame synchronizers") does not distinguish these as separate cases with different rules. Two pieces of evidence point in different directions:

- **Toward "resolution included, not just timing"** — [Verified — Blackmagic Design official press release, businesswire.com, ATEM Television Studio 4K8 launch, a *different* ATEM model, not Constellation]: *"Each SDI input has a dedicated standards converter so any 720 HD, 1080 HD or 2160 Ultra HD input source will be converted to the standard of the switcher."* This explicitly names resolution tiers (720/1080/2160) as part of what gets converted, on record from Blackmagic itself — for a different product, but the same manufacturer describing the same general architecture pattern (per-input dedicated converter).
- **Toward "16:9 and timings only, not full resolution"** — **[User-reported, forum-sourced, not independently verified]**: the user reports a Reddit thread (r/VIDEOENGINEERING, "Upconvert from 1080p to 4K on the ATEM") states the per-input conversion handles matching aspect ratio (16:9) and timing/frame-rate, narrower than full resolution conversion. **This document could not independently verify the thread's content** — direct fetch of reddit.com is blocked, and search did not surface the thread's actual text. The claim is recorded as the user's account of what they read, not as independently confirmed.

**These two pieces of evidence are in tension and this document does not resolve them.** The 4K8 press release is stronger-sourced (official, direct Blackmagic language) but describes a different model. The forum report is weaker-sourced (unverified secondhand account) but specifically about upconversion behavior, which is the exact question at hand. Do not treat either side as settled without a Constellation-specific manual statement or a direct bench test.

---

## Verification status

| Claim | Status |
|---|---|
| Every SDI input has its own format conversion + frame synchronizer | **Verified [Official]** — Constellation manual, direct quote |
| One operating standard set switcher-wide, full HD/UHD/8K rate list | **Verified [Official]** — Constellation manual, direct quote |
| Behavior applies across the Constellation 4K line generally, not just 1 M/E | **Reasoned, not explicitly per-model-confirmed** — manual's language and standards table treat the family together |
| Per-input conversion includes full resolution conversion (not just timing) | **Contested — see §3.** Corroborated for a different ATEM model (official source); narrowed to timing+aspect-ratio by an unverified forum report specific to this question |
| Changing switcher standard erases media pool | **Verified [Official]** — stated directly |

## Not yet verified — open items

- **§3 is the primary open item.** Would need either a direct statement in the Constellation manual (not found in what was read) or a bench test — feed a genuinely different-resolution source (e.g. 720p into a 1080p-configured switcher) and observe whether it's scaled or rejected/black.
- Whether the per-input converter's behavior differs at all between Constellation HD, 4K, and 8K model tiers — not addressed anywhere in what was read.
- The original Reddit thread's actual content — not independently readable this session; if accessible another way (screenshot, copied text), worth confirming directly rather than relying on secondhand summary.

## Cross-references

- `atem-supersource.md` — same manual, different section (SuperSource compositing, not general input handling). Both documents share the same underlying source PDF.
