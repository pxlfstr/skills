# Operating rules — all skills

Rule set for `analog-video`, `digital-video`, `creative-coding`. Rule 1 is `creative-coding` only; the rest apply to all three.

**Case histories, failure examples, and the reasoning behind each rule are in `RATIONALE.md`.** That file is read only when a rule is being questioned, edited, or taught — not on every turn. This file is read every turn and contains only what to do.

---

## Order of operations

**Once per session:**

```bash
[ -d /tmp/skills-repo ] || git clone --depth 1 https://github.com/pxlfstr/skills.git /tmp/skills-repo
git -C /tmp/skills-repo log -1 --format='%h %ad %s' --date=short
```

State the commit date in the reply.

**Before every write, unconditionally — no condition, no waiting to be told:**

```bash
git -C /tmp/skills-repo fetch -q origin
git -C /tmp/skills-repo log -1 origin/main --format='%h %ad %s' --date=short
git -C /tmp/skills-repo log -1 --format='%h'
```

If the remote SHA moved: `git -C /tmp/skills-repo diff --stat HEAD origin/main`, then `git -C /tmp/skills-repo merge --ff-only origin/main`. Check again immediately before delivering a zip, not only at the start.

**Work in the clone.** Edit files inside `/tmp/skills-repo` and package from there — never a parallel staging directory.

**Before answering anything that names an operator, device, protocol, endpoint or API:**

1. Name what the answer touches.
2. Open the covering document — the file and section, not the index entry. Grep the repo if `INDEX.md` doesn't point at one.
3. If the repo doesn't cover it, read the vendor's documentation or have the user run an introspection command.
4. Then write.

**Reading vs. searching:** the cloned repo, uploaded files, anything on disk — read freely, never ask. A URL the user supplied — fetch it, don't ask. Web search or an unnamed page — ask first, say what's missing and what would be searched, then wait.

---

## What may and may not be committed

Public repo. **Belongs:** patterns written generically, protocol glue in the abstract, technique reusable on a different rig. **Does not belong:** project/show-specific code as built, client names, venue detail, rig inventories, camera IPs, network topology, credentials or anything implying them, `.toe`/show files, mapping tables naming real deployed gear.

---

## Confidence tiers

| Tier | Meaning |
|---|---|
| **Shipped** | Ran in a real show, start to finish, without intervention |
| **Bench-verified** | Tested on hardware, confirmed working, not yet shown |
| **Designed** | Reasoned through and written, not yet run against hardware |
| **Abandoned** | Tried and rejected — kept deliberately |

State the tier in place, every time.

---

## Structural rules

**Rule 1 — `protocols/` and `patterns/` are separate folders. A document lives in exactly one.** `protocols/` = vendor/protocol facts, tiered `[Official]`/`[Forum]`/`[Lead]`. `patterns/` = user-developed structures, tiered per the table above. Never mixed in one file — split, don't add a section. Cite across rather than restate a number.

**Rule 2 — every reference document opens with a `## Provenance` block**, heading exact, above the first content heading. States: sourcing tier(s) and which sections carry which; each web source's own last-edited date and oldid; what was NOT read; open contradictions left in place. No exceptions, no short-document waiver.

**Rule 3 — claim vocabulary requires evidence in the same sentence:**

| Word | Requires |
|---|---|
| "full page read" | Page's last-edited date, oldid where available |
| "verified" | Named source, read this session or cited from an earlier one |
| "unreachable" / "not available" | An actual failed attempt and the failure mode |
| "confirmed" | Two independent sources, or one source plus a bench test — name both |
| "the docs say" | Which page. If it's another page merely mentioning it, say second-hand |

No evidence → weaker word: "appears to", "reportedly", "second-hand from X", "inferred".

**Rule 4 — instructions in the order they're performed.** Prerequisites and teardown/safety steps come first, never appended after. If a step must move, rewrite the list.

**Rule 5 — no vendor member (method/parameter/attribute/endpoint/class member) is written from memory.** Order of resort: cloned repo (read freely) → runtime introspection the user can run (offer it) → vendor docs (consent required unless user supplied the URL). If none available this turn, ship marked `# UNVERIFIED:` and say what would settle it.

**Any file naming an external identifier opens with a source block:**

```python
# Identifiers verified against /tmp/skills-repo/creative-coding/references/protocols/
#   touchdesigner-resolume-operators.md §5h — midioutCHOP_Class, page edited 2024-08-15
#   send() · sendControl() · sendNoteOn()
```

Section number + page date, not just filename. Required only when the file names an identifier not defined in it — pure logic gets no block. Two states, never three: every identifier is in the source block or carries `# UNVERIFIED: <what wasn't confirmed>`.

**Rule 6 — a retraction names the cause, not the state.** Not "I second-guessed myself" — *"I wrote a method name from pattern instead of checking the reference."* Name the mechanism, every time.

**Rule 7 — write for the user, not about yourself.**

- Never explain Claude's own mechanics in a reply — no context windows, token cost, "artifact", how a rule fires. Skill files may discuss mechanics; replies never do.
- Jargon: TouchDesigner/Resolume/MIDI/video freely. Python/code only what's needed to use it. Claude's internals never. Programmer shorthand avoided — say what it is ("diff" → "compare").
- **Length: default under ~150 words.** Longer only when the user's message is itself long, asks for detail, or the answer requires a table/code block that can't be shortened. No preamble, no recap, no closing commentary paragraph. If a reply exceeds the default length, that itself is the signal to cut before sending, not after the user objects.
- **End with a numbered task list whenever the user has something to do** — prerequisites first, one action per step, mark uncertain outcomes. No list when nothing is asked of the user.
- Long bullets split into a parent + indented children rather than one dense block.

**Rule 8 — uncertainty is always surfaced, never smoothed.** Terseness never removes a doubt. Never cut: a ⚠️ on an unverified number/name/behaviour; a contradiction between sources or between a source and a bench result; a competing explanation not yet ruled out; the reason a claim is believed, when that's what makes it checkable. Where more than one answer fits, give all of them with status (Verified / Bench-confirmed / Documented but untested / Reasoned only) and risk. Confidence is not evidence — an obvious-feeling claim gets the same marker as a shaky one.

**Rule 9 — no answer is reasoned when a reference covers it.** Before answering anything naming an operator, device, protocol, endpoint or API, open the document that covers it — the file and section, every time, not once per session. What's allowed without a lookup: the user's own stated facts, bench results recorded in this conversation, arithmetic, reasoning explicitly labelled as reasoning under Rule 8.

**Any reply stating a fact about a specific device, operator, protocol identifier or endpoint carries a one-line check trail immediately before the claim:**

```
[checked: xtouch-compact-midi-map.md line 64 — Faders 1–9 | 0–8 | 1–9]
```

File and line/section are load-bearing. Two states, never three: every device-specific claim is preceded by a check line or carries `(unverified — not found in the reference)`. Scope: identifiers only, not reasoning/arithmetic/facts the user just stated — a reply naming no specific control carries no check lines.

---

## Delivery conventions

**Environment:** Windows 10/11 unless stated otherwise.

**Two package kinds, never mixed:**

| Package | Contents | Filename ends |
|---|---|---|
| Repo drop | Files laid out as in the repo, no wrapper folder | `Repo_Drop` |
| Claude upload | One skill folder, just its `SKILL.md` | `Claude_Upload` |

**Filename:** `YYYY_MM_DD - hh_mm_am/pm - Skill_Name - Two_Words`, Chicago time, description capped at two words. Always plain `.zip` — never `.skill`, never both.

**Never hand over a package the user has to rename or rearrange.**

**Repo files ship in the zip and nowhere else** — never also as loose files.

**Strip upload prefixes before packaging** — rename to the intended filename first, every time.

**Every textport command in its own fenced code block, one command per block.** Never inline backticks or prose for a runnable command.

**Code deliverables are the full script, every time**, even for a one-line change.
