# Rationale — case histories behind RULES.md

Read this only when a rule is being questioned, edited, taught to a new session, or when a failure needs diagnosing. Not read on every turn — `RULES.md` is.

Split from `RULES.md` on 2026-08-26 after repeated failures to apply Rule 7 (length) and Rule 9 (lookup-before-answer) despite both being present in the combined file every turn. The hypothesis: a 346-line file re-read every turn buries the two or three lines that actually govern behavior under narrative that doesn't need to be re-read to be followed. Untested whether the split helps — noted here rather than asserted as fixed.

---

## Why the pull-before-write rule is unconditional

An earlier version said to re-pull "when the user says they have committed" — a conditional trigger. It failed in practice: the user said "uploaded to github," the trigger wasn't noticed, three commits went unfetched. Not gated on elapsed time either — there's no clock between turns, so "pull if it's been an hour" fails silently. Gated on the event (any write) instead, because that's the only thing checkable by looking.

## Why token cost doesn't excuse skipping a pull

The cost of a tool call is what lands in context, not what lands on disk. `git clone --depth 1` ≈ 30 tokens. `git fetch` + `git log -1` ≈ 20 tokens. `git diff --stat` ≈ 50 tokens. Reading one INDEX.md ≈ 5,000 tokens. A fetch is a rounding error next to any real read — so selectivity belongs in what gets read, never in whether to pull. Edit with `str.replace`, not by reading the file first; read into context only to reason about content, never merely to change it; `grep -n`/`sed -n` over `cat` above a few KB.

## Why working in the clone matters

A parallel `drop/` directory was maintained across a multi-session build once. It happened to stay a clean superset of the repo — but nothing would have revealed it if it hadn't. Working in the clone makes drift structurally impossible: `git status` and `git diff --stat HEAD origin/main` show exactly what changed, on both sides, by looking.

## Why Rule 2's provenance block has to be mechanically checkable

The block is what caught errors that careful reading did not. Heading has to be exactly `## Provenance` so coverage can be grepped:

```bash
for f in $(find digital-video/references creative-coding/references -name '*.md' \
           ! -name INDEX.md ! -name STORAGE.md ! -name README.md); do
  grep -q "^## Provenance" "$f" || echo "MISSING PROVENANCE: $f"
done
```

All 17 reference documents across both skills carried one as of 2026-08-01; twelve were retrofitted that day from each document's own inline tier tags.

## Rule 5 — where invention actually happens

Risk peaks where confidence is highest, not where it's lowest. `sendMIDI` was invented *because* it felt certain — `sendNote`, `sendControl`, `sendMessage` are real in adjacent APIs, so the shape was overlearned and never questioned. Other high-risk moments: mid-artifact, where a lookup breaks a flowing generation; when 149 correct lines launder one invented one; under time or money pressure; late in long sessions when earlier tool results have scrolled away. Recalled and constructed feel identical from the inside — the rule doesn't ask for better judgement, it asks for a lookup and a receipt, because a rule with no artifact does not fire. Rule 2 works because `## Provenance` is greppable; a purely behavioural version of Rule 5 would be unauditable, which is why the source-block requirement exists.

## Rule 6 — two failure modes, opposite directions, one cause

| Failure | Looks like | Cost |
|---|---|---|
| Silent invention | A plausible name in the same confident register as correct code beside it | User finds it by running it |
| Noisy hedging | Flagging uncertainty on something one tool call would settle | Offloads the check onto the user, devalues the hedges that matter |

One tool call beats a hedge. If it's checkable now, check it.

## Rule 7 — why "shortest reply that answers" got replaced with a number

The prose version was read, understood, and still didn't hold — repeatedly, across a real conversation, even while other rules in the same file were being actively followed. "Shortest reply that answers" is a judgment call, the same shape as "do I need to look this up" in Rule 5 — and Rule 5 already established that judgment calls answered by the same faculty that does the inventing don't work as a check. The ~150-word default replaces judgment with a number for the same reason Rule 9 replaced "look it up" with a check-line requirement: not because the number is more correct, but because exceeding it is visible by looking, the same property every other structural rule in this file relies on.

## Rule 9 — the fader-9 failure, in full

2026-08-26. A prose reply named a specific device fact (whether the X-Touch Compact has a 9th fader, and its CC) and answered from the session's established bank/channel/CC-sharing pattern — correctly recalled from earlier bench work — instead of from `xtouch-compact-midi-map.md`, which had the actual number and had it verified against hardware. The pattern was real; the number was never checked. Asked once, wrong. Asked again, wrong again. Only corrected on a third ask, after the user pushed back twice.

The rule existed before this — "before answering anything that names an operator, device, protocol, endpoint or API, open the document that covers it" — and was insufficient on its own, for the same reason Rule 5 names: *"a rule with no artifact does not fire... neither party can tell from the output whether the lookup happened."* Rule 9 had no artifact. It was a correct instruction with nothing to check it against. The fix borrows Rule 5's shape directly: a one-line check trail (file + section/line) before any device-specific claim, so the lookup is visible by reading the reply instead of inferred from whether the answer sounds right.

**The failure has a shape**, independent of this specific instance: it happens deep in a working session, after a clone that felt like compliance, on a question that reads as a continuation of something already established. Momentum is the risk factor, not difficulty.

**Open, unresolved:** whether writing the check line first actually forces the file open, or whether the check line itself can eventually be produced from pattern once the habit sets in — the same risk Rule 5 already flags as the leading cause of invented code. Watch for this if the rule stops catching anything.
