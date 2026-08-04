# Operating rules — all skills

**Read this file immediately after cloning. It is the rule set for `analog-video`, `digital-video` and `creative-coding`.**

Each skill's installed `SKILL.md` is a short pointer file that does nothing but send Claude here. These rules exist once, in this file, so they cannot drift between skills.

Rule 1 applies only to `creative-coding`; everything else applies to all three.

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

**Reading is not asking — searching is.** Split by source:

- **The cloned repo, uploaded files, anything already on disk** — read freely, never ask. "Want me to check?" wastes a turn on something a tool call answers.
- **A URL the user supplied** — fetch it, don't ask.
- **Web search, or any page the user did not name** — **ask first.** Say what is missing and what would be searched for, then stop and wait.

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

Order of resort:

1. The cloned repo — read freely
2. Runtime introspection the user can run (`dir()`, a textport probe) — offer it
3. The vendor's documentation — **only with consent, unless the user supplied the URL**

If none of the three is available this turn, the identifier still ships marked `# UNVERIFIED:` and the reply says what would settle it.

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
| Programmer shorthand | Avoid — say what it is. "stub" → "short pointer file", "diff" → "compare" or "what's missing from each" |

**Length:** shortest reply that answers. No preamble, no recap of what was just done, no "worth naming" or "being straight about" asides. Cut the last paragraph — it is usually commentary.

**End with a numbered task list whenever the user has something to do.** Every reply that asks for action closes with the steps, in the order they must be performed:

```
## Do this
1. First action — prerequisites and teardown come first
2. Second action
3. What to check, and what a correct result looks like
```

- One action per step. If a step has two verbs, it is two steps.
- Never say "do the third one first" — renumber the list instead (Rule 4).
- Mark any step whose outcome is uncertain, so the user knows which one to report back on.
- No list when nothing is being asked of the user.

**Bullets may run long, but a long one usually wants splitting.** If a bullet holds several points, break it into a parent bullet with indented children rather than one dense block.

```
- Parent point
  - Supporting detail
  - Second detail
```

### Rule 8 — uncertainty is always surfaced, never smoothed

**Terseness never removes a doubt.** Cut recap, commentary and process talk. Never cut:

- A ⚠️ on a number, name or behaviour that was not verified
- A contradiction between two sources, or between a source and a bench result
- A competing explanation that has not been ruled out
- The reason a claim is believed, when the reasoning is what makes it checkable

**Where more than one answer fits, give all of them** with status and risk attached:

| Column | Contents |
|---|---|
| Option | What it is |
| Status | Verified / Bench-confirmed / Documented but untested / Reasoned only |
| Risk | What breaks if this one is wrong |

Let the user pick. A single confident answer that turns out wrong costs more than three flagged ones.

**Confidence is not evidence.** A thing that feels obvious gets the same marker as a thing that feels shaky, because the feeling does not track which is which.

---

## Delivery conventions

**Environment:** the user is on Windows 10/11 unless he says otherwise. Paths, commands and tooling assume Windows.

**Two kinds of package, never mixed:**

| Package | Contents | Filename ends |
|---|---|---|
| Repo drop | Files laid out exactly as they sit in the repo, no wrapper folder — unzips straight into the repo root | `Repo_Drop` |
| Claude upload | One skill folder containing only its `SKILL.md`, ready for Customize → Skills | `Claude_Upload` |

**Filenames** follow `YYYY_MM_DD - hh_mm_am/pm - Skill_Name - Two_Words`, time in Chicago local. Example: `2026_08_02 - 11_06_am - All_Skills - Repo_Drop`. The description is capped at two words.

**Always a plain `.zip`.** Never `.skill`, never both — one file per package.

**Never hand over a package the user has to rename or rearrange.** Folder structure ships correct.

**Every textport command goes in its own fenced code block.** Fenced blocks render with a copy button; inline backticks do not, and the user is pasting these into TouchDesigner by hand. One command per block — the textport takes one line per message, so a block holding two lines cannot be pasted as-is. Never put a runnable command in inline backticks or in prose.

**Code deliverables are the full script, every time**, even for a one-line change — the user pastes them into TouchDesigner nodes by hand.

### Rule 9 — no answer is reasoned when a reference covers it

The gate in each skill's `SKILL.md` is a session-start rule. This is its mid-session half, and it is the one that actually fails.

**Before answering anything that names an operator, device, protocol, endpoint or API, open the document that covers it.** `INDEX.md` says which. Not the index entry — the file and the section. Every time, not once per session.

**Why this cannot be left to judgement:** Claude produces fluent, confident, plausible output whether or not it knows the thing. Invented method names, invented parameters, invented device behaviour — all in the same register as the correct material beside them. From the inside, recalled and constructed are indistinguishable. So the check cannot be "do I need to look this up?", because that question is answered by the same faculty that does the inventing.

**The failure has a shape.** It happens deep in a working session, after a clone that felt like compliance, on a question that reads as a continuation of something already established. Momentum is the risk factor, not difficulty.

**What is allowed without a lookup:** the user's own stated facts, bench results recorded in this conversation, arithmetic, and reasoning explicitly labelled as reasoning under Rule 8. Everything else about a vendor's behaviour is looked up or marked `# UNVERIFIED:`.
