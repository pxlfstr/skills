# Laptop GPU → display-output routing

Which GPU actually drives a given laptop port, how to tell, and the
diagnostic traps on the way. Written for show laptops feeding processors,
switchers and LED walls, where "no signal" at load-in has to be resolved in
minutes.

## Provenance

**Compiled 2026-09-17 from a single troubleshooting session. This is a thin
document and should be read as such.** No manufacturer PDF was read end to
end; no controlled bench test was run.

| Section | Tier |
|---|---|
| §1 mirroring finding | **Bench-verified**, user-reported — observed on the user's own machine, resolved by the user |
| §2 spec-sheet method | **Derived** — arithmetic performed in this session from §3's figures |
| §3 P16 Gen 1 figures | **Verified [Official]**, ⚠️ **snippet-tier** — Lenovo PSREF, read as a search extract, not as the PSREF PDF |
| §4 graphics-mode switching | **[Lead]** — third-party spec aggregator and Claude recall; no Lenovo document read |
| §5 Control Panel absent | **[Lead] / Memory** — Claude recall plus one third-party repair blog; see the warning in that section |
| §6 corrections log | Session transcript |

**Sources actually read this session:**

- Lenovo PSREF, *ThinkPad P16 Gen 1* and *ThinkPad P16 Gen 2* specification
  pages — **search extracts only.** Page dates visible in the extracts:
  P16 Gen 1 "July 20 2023", P16 Gen 2 "December 22 2025". No oldid available.
- `thinkstation-specs.com` P16 Gen 1 / Gen 2 pages — third-party aggregator,
  **[Lead]**, not Lenovo.
- `invgate.com` P16 Gen 1 entry — third-party, **[Lead]**.
- `xda-developers.com` P16 Gen 1 review — **[Forum]**, used only for rear-port
  placement.
- A third-party repair blog on a missing NVIDIA Control Panel context-menu
  entry, supplied by the user as a URL and fetched. **Its contents are no
  longer in session context and nothing in §5 is quoted from it.**

**NOT read:** the P16 Gen 1 PSREF PDF itself; any Lenovo BIOS setup guide; any
Legion PSREF entry; NVIDIA driver release notes; NVIDIA's own documentation on
Control Panel sections.

**Nothing in this document was tested on a P16.** The one bench observation
(§1) was made on a *Legion*, not the ThinkPad the spec research covers. Do not
read §1 and §3 as describing the same machine.

**Open contradiction left in place:** §4 states the ThinkPad graphics-mode
switch lives in BIOS, on the strength of a third-party page quoting a Lenovo
phrase. No Lenovo source was read. It is plausible and unconfirmed.

---

## §1 — Mirrored displays can hide the NVIDIA Control Panel Display section

**Bench-verified (user-reported), Legion laptop with an RTX 5090, 2026-09-17.**

Symptom set, all at once:

- NVIDIA Control Panel opens but shows only **3D Settings**, with
  **Adjust video image settings** as the sole entry under Video.
- No **Display** section at all — no Change resolution, no Adjust desktop
  colour settings, no Set up multiple displays, no rotation.
- A USB-C → DisplayPort feed to an external processor shows no signal.

**Cause on this machine: the display arrangement was set to mirror.** Changing
to extend restored the signal, and the USB-C → DP path then ran through the
NVIDIA GPU normally.

**Why this matters as a diagnostic:** the same symptom set is widely — and in
this session was, wrongly — read as *"the NVIDIA GPU isn't driving any
display, so the output must be wired to the iGPU."* That reading sends you
after port routing, BIOS graphics modes and driver reinstalls. **Check the
display arrangement first.** It costs seconds and it accounts for the whole
symptom set on at least one machine.

⚠️ **Scope of this finding.** One observation, one machine, one occasion. It
establishes that mirroring *can* produce this symptom set. It does **not**
establish that mirroring is the only cause, that every mirrored configuration
does this, or that it behaves the same on other GPUs, driver versions or
Windows builds. A genuinely iGPU-wired port will also show a Control Panel
with no Display section — both causes exist and this document can only
confirm the first.

---

## §2 — The spec-sheet method for inferring which GPU feeds a port

**Derived. Useful for HDMI, weak-to-useless elsewhere.**

When a laptop spec sheet lists **different maximum resolutions for the same
physical port depending on the graphics option ordered**, the higher ceiling
is the discrete GPU driving that port directly.

Worked from §3's P16 Gen 1 figures. Active pixel rates, computed this session
(width × height × refresh; **active pixels only — no blanking, so these are
not pixel clocks**):

| Raster | Active px/s | Computation |
|---|---|---|
| 3840 × 2160 @ 60 | 497,664,000 | 3840 × 2160 = 8,294,400; × 60 |
| 7680 × 4320 @ 60 | 1,990,656,000 | 7680 × 4320 = 33,177,600; × 60 |
| 3840 × 2160 @ 240 | 1,990,656,000 | 8,294,400 × 240 |
| 5120 × 3200 @ 60 | 983,040,000 | 5120 × 3200 = 16,384,000; × 60 |

**1,990,656,000 ÷ 497,664,000 = 4.00 exactly.** The NVIDIA-model HDMI ceiling
carries four times the active pixel rate of the integrated-model ceiling on
the same connector. A single display engine does not change capability based
on which GPU was fitted — so the two figures describe two different engines,
and the higher one is the dGPU.

Note also that **8K @ 60 and 4K @ 240 are the same active pixel rate**
(1,990,656,000 px/s), which is why spec sheets tend to offer them as
alternatives on one port.

**Where the method fails:**

- **USB-C and Thunderbolt.** P16 Gen 1 lists 5120 × 3200 @ 60 for both,
  with no graphics-dependent variation — so the figure reveals nothing about
  routing. It looks like a DP Alt Mode ceiling rather than a GPU ceiling.
- **A MUX switch changes routing at runtime.** The sheet describes one mode.
- **Some makers publish only the best-case number** for any configuration,
  which collapses the distinction the method depends on.

**For real link-budget work, not inference**, use
`pixel-clock-and-link-bandwidth.md` — it does blanking, pixel clocks and wire
rates properly. §2 here is a routing hint, not a bandwidth calculation.

---

## §3 — ThinkPad P16 Gen 1, as published

**Verified [Official], ⚠️ snippet-tier** — Lenovo PSREF, search extract only.
Page date in extract: 2023-07-20.

| Item | Published figure |
|---|---|
| Independent displays | Up to 5 (native panel + 4 external via HDMI, USB-C and Thunderbolt) |
| HDMI, integrated or Arc models | 3840 × 2160 @ 60 |
| HDMI, NVIDIA models | 7680 × 4320 @ 60 |
| USB-C | 5120 × 3200 @ 60 |
| Thunderbolt | 5120 × 3200 @ 60 |
| Chipset | Intel WM690 |

Rear ports per a third-party review (**[Forum]**, placement only): power,
2 × Thunderbolt 4, 1 × HDMI 2.1. A USB-C 3.2 Gen 2 port sits on the side,
separately from the rear Thunderbolt pair.

⚠️ **One PSREF extract carries the line "Power Delivery only supports
power-out for charging peripherals."** Which port that qualifies was not
determined, and it is not obviously consistent with the monitor-support line
naming USB-C as a display path. **Recorded unresolved.**

**Adjacent generation, for contrast** (P16 Gen 2, PSREF extract, page date
2025-12-22): HDMI 3840 × 2160 @ 60 on integrated or Arc models;
7680 × 4320 @ 60 **or** 3840 × 2160 @ 240 on NVIDIA or Arc Pro A30M models.
The same two-ceiling pattern §2 relies on.

---

## §4 — Where the graphics-mode switch lives differs by product line

**[Lead] — no Lenovo document read for either claim.**

| Line | Reported location |
|---|---|
| ThinkPad P-series | BIOS setup |
| Legion | Lenovo Vantage / Legion Space |

The ThinkPad side rests on third-party aggregator pages quoting a Lenovo
phrase — Intel UHD Graphics "Utilized via *Hybrid Mode* in BIOS" — against
both P16 Gen 1 and Gen 2. That the phrase names BIOS is real; that the menu
path is `Config → Display → Graphics Device` is **Claude recall and was
asserted in session without a source. Treat it as unverified.**

**Discrete-only mode for show machines — reasoned, not measured:**

- Removes the hybrid-graphics handoff from the display path entirely.
- Costs battery life and keeps the fans up, since the dGPU no longer idles.
- ⚠️ **No latency or frame-timing figure is claimed here.** The argument that
  it gives more predictable behaviour is mechanism-level reasoning. Nothing in
  this library measures it.

---

## §5 — NVIDIA Control Panel missing entirely

⚠️ **Weakest section in the document. Everything here is Claude recall or a
third-party repair blog, and one claim in the session was already wrong.**

Reported behaviours, all **[Lead] / Memory**:

- On current driver packages the Control Panel is distributed as a Microsoft
  Store app, so it can be absent from a machine whose driver is fine.
- The service that matters is **NVIDIA Display Container LS**
  (`NVDisplay.ContainerLocalSystem`).
- **NVIDIA LocalSystem Container** (`NvContainerLocalSystem`) ships with
  GeForce Experience / the NVIDIA App rather than the bare driver, so its
  absence from `services.msc` is not a fault. **Confirmed only in the weak
  sense that the user's machine had exactly one NVIDIA service present and
  worked** — that is one observation, not a general rule.

**Before any of this, check §1.** A Control Panel that opens but looks wrong
is a different problem from one that is not installed.

**What would settle §5:** NVIDIA's own driver documentation on which services
ship in which package, read directly. None was read.

---

## §6 — Corrections log

Recorded per `RULES.md` Rule 6 — cause, not state.

| Claim made in session | Status | Cause |
|---|---|---|
| "USB-C and Thunderbolt are almost always iGPU; HDMI is the dGPU port" | **Wrong on the user's Legion** — USB-C → DP ran through the NVIDIA GPU once mirroring was cleared | Generalised a consumer-laptop pattern into a rule and stated it without a source for either machine |
| "Control Panel showing only 3D Settings means the dGPU drives no display" | **Wrong in this case** — mirroring produced it | Reasoned from one plausible mechanism and presented the conclusion as diagnosis, with no second cause offered |
| P16 BIOS path `Config → Display → Graphics Device` | **Unverified** | Written from recall; no Lenovo source read |
| Advice framed for a Legion while the user's spec question was about a P16 | Two machines conflated for several turns | Did not ask which machine each symptom belonged to |

**The general lesson worth keeping: port-to-GPU routing varies by model and by
generation within one product line.** It is not a rule that transfers. §2's
spec-sheet method is per-model on purpose, and even it only works on HDMI.

---

## §7 — Open items

1. **Does mirroring reproduce this on other hardware?** One machine, one
   occasion. Two laptops and five minutes would make §1 a rule instead of an
   anecdote.
2. **P16 Gen 1 BIOS menu path**, read off a machine or a Lenovo setup guide.
3. **The PSREF "Power Delivery only supports power-out" line** — which port,
   and does it contradict the USB-C display path.
4. **Whether P16 Gen 1 USB-C/TB is dGPU-routed in discrete mode.** The spec
   figures cannot answer it; plugging in and looking at the Control Panel can.
5. **NVIDIA service inventory by driver package**, from NVIDIA rather than
   from recall — would replace §5 with something citable.
