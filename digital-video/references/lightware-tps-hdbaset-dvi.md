# Lightware TPS / HDBaseT Extenders as a Dual-Link-DVI 4K30 Path — and What the Docs Do and Don't Prove

## Why this exists

The Evertz and scaler routes (see `evertz-dvi-3glink-converters.md`, `analog-way-vio-4k.md`) solve
"dual-link DVI 4K30 → HDMI," but the scalers are expensive and the Evertz pair caps at WQXGA. The
Lightware **TPS** HDBaseT extender family looked like a cheap, low-latency alternative: a DVI-I input,
4K30 support, 0-frame delay. This doc records exactly what the documents establish — and, as
importantly, what they do **not**, because two confident inferences about these boxes turned out wrong
during the investigation and both are flagged below so they aren't repeated.

## Provenance

- **Verified [Official]** — four Lightware documents, user-supplied, read 2026-09-03:
  - *DVI-HDCP-TPS-95 series product brief* (Rev., HDCP 2.2 variant)
  - *HDMI-TPS-95 series Quick Start Guide* (Doc. 2.5)
  - *HDMI-TPS-TX200 series User Manual* (164 pp., read via pdfplumber — §1.4–1.6, §3.2, §11 specs)
  - *TPS-TX200 series Quick Start Guide* (Doc. 2.4)
  - *Remote Power Compatibility Table*
- **Verified [Official]** — two Lightware A&E specifications, user-supplied, read 2026-09-03:
  - *SW4-TPS-TX240 Architectural and Engineering Specification* v1, 2026-08-03, 3 pp., read in full
  - *MMX4x2-HT200 Architectural and Engineering Specification* v1, 2026-08-19, 4 pp., read in full
- ⚠️ **The Remote Power Compatibility Table is named above but none of its content was ever written
  into this document.** No device list, no pairing rules, nothing. It cannot be quoted or reasoned
  from — see §8.3. Re-supply it if remote power matters to a job.
- **Nothing bench-tested.** The user owns none of these; no unit has been measured.
- **Not read:** the Lightware Device Controller (LDC) software manual, which is where the TPS Cable
  Diagnostics and the actual per-input pixel-clock readout live — that tool would answer the open
  question in §4 directly.

---

## 1. Two different generations — do not conflate them

**TPS-95 series** (`DVI-HDCP-TPS-TX95/RX95`, `HDMI-TPS-TX95/RX95`) — the older, cheaper pair:

- Product brief states **"Single-Link DVI"** explicitly, "Supports all DVI resolutions up to 1080p or
  1920×1200," data rate **3.4 Gbps per colour / 10.2 Gbps total** (the single-link TMDS ceiling)
- This one is **genuinely single-link — stated, not inferred.** It cannot accept a DVI signal above
  ~165 MHz / 1920×1200, dual-link or otherwise.
- It **does** carry 4K30, but only over its **HDMI** input (HDMI 1.4 carries 4K30 on one TMDS link at
  ~297 MHz). Feed it DVI and you are capped at 1200p.

**TPS-TX200 series** (`DVI-HDCP-TPS-TX210/TX220`, `HDMI-TPS-TX210/220/226`, `DP-TPS-TX210/220`,
`SW4-TPS-TX240(-Plus)`) — the newer, more capable transmitters:

- DVI-I input's supported resolution (spec table, §11) includes **3840×2160@30 (4:4:4)** and
  4096×2048@30 (4:4:4) — the same as its HDMI and DP inputs
- **0-frame delay, Pixel Accurate Reclocking** — a transport extender, not a scaler
- Physical input is a **"29-pole 'digital only' DVI-I Dual-Link connector"** (§3.2.2)

The 95 and the TX200 are not interchangeable for this job. The 95 is single-link and out; the TX200 is
the candidate.

---

## 2. What HDBaseT / TPS is, and why the RJ45 side is never the question

HDBaseT (Lightware's "TPS") **packetises** the ingested video and sends it over CAT cable — it does not
pass DVI/HDMI TMDS pairs through to the RJ45 pins. TX and RX are a **matched pair**, so the cable link
between them is never a signal-compatibility question. Everything that matters happens at the **DVI-I
input connector**, upstream of the HDBaseT encode. RJ45 pinout compatibility is not an issue anywhere
in this chain — a distinction worth holding, because it is easy to misframe the open question as a
cable-pinout one when it is entirely a source-to-DVI-input one.

The block diagram (TX200 QSG, DVI-HDCP-TPS-TX220 port diagram) confirms the internal chain:
**DVI-D in → De-embedder → Embedder → CPU → TPS out.** Audio is de-embedded and re-embedded; video is
reclocked and packetised. No scaler stage — which is why it is 0-frame and why it cannot reshape a
signal the way a VIO can.

---

## 3. The single-link vs dual-link distinction (stated correctly, because it was muddled once)

Single-link vs dual-link is a **DVI-only** distinction. One TMDS link = 3 data pairs (R, G, B) + 1
clock pair. Dual-link DVI lights a **second** set of 3 data pairs on the extra connector pins, sharing
the one clock — doubling pixel throughput past single-link's ~165 MHz ceiling to reach 2560×1600@60.

- **HDMI** has no "links" in this sense — always one TMDS link (3 data + 1 clock); it raised the
  *clock* ceiling (165→340 MHz at 1.4) instead of adding a link. "Single-link HDMI" / "dual-link HDMI"
  are not real categories. (Type B was the only dual-link HDMI ever specified, never built — see
  `hdmi-type-b.md` if present.)
- **DisplayPort** has no links-in-the-DVI-sense either — it is packetised lanes.

So the single/dual-link question applies **only** to the DVI path — on the X20's DVI output and on the
TX200's DVI input. It does not apply to their HDMI or DP paths at all. A 297 MHz 4K30 signal on **one**
TMDS link is what HDMI 1.4 and single-link-at-297MHz both do; a dual-link source splitting pixels
across **two** link-bundles is a different waveform.

---

## 4. The open question — genuinely unresolved from these documents

**Does the TX200's DVI-I input clock a true dual-link DVI signal (two TMDS link-bundles), or only a
single-link signal up to ~297 MHz?**

What the documents establish:

- The connector is physically **dual-link** (§3.2.2) — but that is the shell. "Only digital pins are
  internally connected" contrasts **digital vs. analog** (VGA/RGBHV dropped), NOT link 1 vs. link 2.
  It does not restrict to single link.
- 4K30 4:4:4 is supported (§11) — but **4K30 fits on one 297 MHz link**, so this proves nothing either
  way about dual-link capability.
- The spec footnote reads "all standard VESA/CEA and custom resolutions **up to 300 MHz (HDMI 1.4)**."
  300 MHz is a single-link-class figure; a true dual-link ceiling (2560×1600@60 needs ~268 MHz *per
  the aggregate*, but dual-link is usually quoted as a higher combined rate) is not stated.

**The documents do NOT state that dual-link input fails, and do NOT state that it works.** It is
undetermined. Anyone continuing this should resolve it empirically, not from spec-sheet inference:

- Plug the X20's 4K30 odd-output into a TX200 DVI-I input and see if it locks.
- Better: use the **LDC software's TPS Cable Diagnostics / Frame Detector**, which reads the incoming
  signal's actual timing, pixel clock and scan mode — that reports directly whether the source is one
  link at 297 MHz or two.

### ⚠️ Two wrong inferences made during this investigation — recorded so they are not repeated

1. **"Dual-link shell, single-link electronics."** Asserted the TX200 only accepts single link, carried
   over from the 95-series brief's stated single-link limit. **The TX200 documents do not support this**
   — the 95's limit is the 95's, not the TX200's. Retracted.
2. **"'Combine Links' is the dual-link feature — smoking gun."** Found "Combine Links" in the TX200
   manual and read it as DVI link-combining. **It is not.** Per manual p.34 and p.61, **"Combine Links"
   is an Event Manager tool for combining up to four logical *conditions* into one Action** — pure
   control-logic, nothing to do with TMDS links. The p.12 footnote "only the Combine Links feature is
   available in these devices" sits under a *software feature-availability* table and means those models
   get a limited Event Manager, not the full Advanced Control Pack. Retracted.

Both errors were the same failure in opposite directions: deciding the answer, then reading a document
phrase as confirmation. The honest state is §4's first paragraph — undetermined.

---

## 5. The Long-Reach vs full-resolution trade (this part is clearly stated)

Both TPS generations have two link modes, and the resolution ceiling depends on which:

- **HDBaseT (HDBT) mode** — full bandwidth up to 297 MHz / 4K30, shorter cable. 4K30 UHD: **70 m on
  CAT7 AWG23**, less with remote power.
- **Long Reach (LR) mode** — longer cable, but **caps at 148.5 MHz (1080p / 1920×1200)**. Every
  resolution above that shows "NA" in the LR column of the distance table.

So: **full resolution at short range, or long range only at HD.** Not both. This is stated plainly in
every TPS distance table and is not in doubt.

---

## 6. Where this lands for the X20 job

- **If the X20 emits 4K30 as a single TMDS link (≤300 MHz):** the TX200 takes it, extends it 0-frame
  over HDBaseT to a DVI or HDMI receiver — a cheap, low-latency path, far under a VIO 4K. The 95-series
  would also work **if fed over HDMI**, but not over its single-link DVI input.
- **If the X20 emits true dual-link 4K30 (two link-bundles):** §4 is unresolved — the TX200 *may* clock
  it, but no document confirms it. Test before relying on it.
- **Either way, the Lightware boxes only transport** — no scaling, cropping, or format conversion. If
  the signal must be reshaped (canvas crop, format change, frame-rate conversion), the VIO 4K /
  ImagePRO-II scaler route is still the answer; the Lightware is not.

The hinge is the same one that has run through this whole investigation: **whether the X20's "dual link
to do 4K30" is genuinely two TMDS links on the output, or a single ≤300 MHz link that Vista *labels*
dual-link because the raster crosses the X20's internal 2048×1200 channel-allocation threshold.** That
is a Vista-Advanced-output / signal-analyser question on the X20 side — see
`christie-spyder-x20.md` — not something more Lightware datasheets will settle.

---

## 7. Not yet verified — open items

- **The §4 question** — dual-link vs single-link at the TX200 DVI-I input. The single most useful thing
  to resolve, and only a bench test or the LDC diagnostic will do it.
- **Whether the X20 4K30 odd-output is one TMDS link or two.** The other half of the same hinge; lives
  in `christie-spyder-x20.md`'s open items.
- **Whether an HDMI or DP feed sidesteps the whole question.** If the X20 (or an upstream box) can
  present the 4K30 as HDMI 1.4 or DP 1.2 instead of dual-link DVI, both TPS generations carry it with
  no dual-link ambiguity at all. Not investigated.
- **RX-side output format.** This doc covers the TX (input) side. Which Lightware RX terminates the
  link, and whether it outputs DVI or HDMI at the far end, was not worked through. **Partly closed
  2026-09-03** — §8 documents one receiving end in full, the `MMX4x2-HT200` matrix, which terminates
  TPS and outputs HDMI on two independent ports. Dedicated `RX` units are still undocumented here.
- **The contents of the Remote Power Compatibility Table.** Named in the Provenance block, never
  transcribed. §8.3 needs it to move the `MMX4x2-HT200` PoE question from inferred-from-absence to
  stated.

**See §8** for a fully documented TX→RX pair at 4K30 and for why a power-compatibility listing is not
a video-compatibility claim.

---

## 8. A TPS pair worked end to end — `SW4-TPS-TX240` → `MMX4x2-HT200` at 4K30

Added 2026-09-03 from both A&E specifications. This is the first **matched pair** in this document
where the receiving end is documented as well as the transmitting end, and it partly closes the
"RX-side output format" open item in §7.

### 8.1 The two devices

| | `SW4-TPS-TX240` | `MMX4x2-HT200` |
|---|---|---|
| Role | 4-input transmitter/switcher, TPS out + mirrored local HDMI out | 4×2 matrix, **TPS in** + 3× HDMI in, 2× independent HDMI out |
| Inputs | DP 1.2a, HDMI (DVI 1.0 / HDMI 1.4), DVI-D on a 29-pole DVI-I | 1× TPS (RJ45), 3× HDMI |
| Max at 4:4:4, 8-bit | 4096×2048@30, **3840×2160@30** | same, stated identically for HDMI **and** the TPS input |
| At 60 Hz | 4096×2048 / 3840×2160 **4:2:0 only** | same |
| 12 bits/colour | 1920×1080@60 only | 1920×1080@60 only |
| HDCP | 1.4 | 1.4 |
| Delay | 0 frame, Pixel Accurate Reclocking | 0 frame, Pixel Accurate Reclocking |

**Verdict: compatible at 3840×2160@30 4:4:4 8-bit.** Both ends state that raster explicitly on the
TPS path, HDCP tiers match, and neither box scales — so the link either carries the source format or
fails to lock; there is no silent down-conversion stage to hide a mismatch.

The 300 MHz footnote in the TX200 spec table (§4) accommodates it with margin: CTA-861 4K30 totals
4400 × 2250 × 30 = **297.000 MHz**, computed, against a stated 300 MHz ceiling.

### 8.2 The mode caveat carries over unchanged

§5 applies to this pair as to every other: **HDBaseT mode only.** Long Reach caps at 148.5 MHz and
will not pass 4K30 at any distance. Neither A&E sheet mentions link modes at all — that fact lives in
the TX200 manual's distance table, not in the A&E specs, which is a reason not to spec a run from an
A&E sheet alone.

### 8.3 Power is a separate axis from video — and a power table proves nothing about format

**The `SW4-TPS-TX240`'s TPS port is a PoE *sink*, not a source.** Its spec states remote powering
over the TPS output per IEEE 802.3af, taken either from a `TPS-PI-1P1` injector or from "a
PoE-compatible TPS input port of the matrix or input board." Its Ethernet port carries no PoE at all.
If both remote and local power are present, **the remote source wins** — stated.

**The `MMX4x2-HT200` does not appear to source it.** Its powering section names only the external 12 V
2 A adaptor and a 3.6 W / 9.6 W consumption range; **PoE is absent from the document entirely**, and a
9.6 W ceiling leaves no headroom for a 15.4 W 802.3af port. ⚠️ Inferred from absence and from the
budget, not stated — the *Remote Power Compatibility Table* is the document that would settle it, and
its contents are not recorded here (see Provenance). Until it is re-read: **power the TX240 from its
own 12 V adaptor.** Both units ship with one, so on this pair the question is moot.

⚠️ **A remote-power compatibility table is a power-pairing table, not a video-format table.** Two
devices co-listed there are stated to be safe to power one from the other — nothing more. Video
ceilings are set per family and are not uniform across TPS: the TPS-95 generation tops out at
1920×1200 over its DVI input (§1) while the TX200 generation reaches 4K30, and both generations sit
on the same TPS/HDBaseT transport. **Never read "listed together for power" as "interoperable at
4K30."** Check each end's own resolution table, every time.

### 8.4 What this pair still does not establish

- **Nothing about dual-link DVI.** §4 remains undetermined. The TX240 carries 4K30 from any of its
  three inputs; that a *single-link-class* 4K30 rides the chain was never in doubt, and this pair
  says nothing about a true two-link-bundle source such as the X20's odd output.
- **No latency figure.** "0 frame" is stated on both, per stage. No end-to-end measurement exists.
- **No cable spec in either A&E sheet.** The 70 m / CAT7 AWG23 figure for 4K30 UHD comes from the
  TX200 distance table (§5), not from these documents.
