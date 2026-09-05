# Evertz 2432/2431 — Dual-Link DVI ↔ Serial, and the GLINK Transport

## Provenance

- **Verified [Official]** for every figure in §2–§5. Sources: three Evertz datasheets, user-supplied
  PDFs, read end to end 2026-09-01:
  - *2432TX-2 — Dual path dual link DVI to serial converter*, Rev. 14-2
  - *2431RX-2 — Dual Path Serial Digital to DVI converter*, Rev. 14-2
  - *2432RX2-HDMI — Dual Path Serial Digital to HDMI converter*, Rev. 18-1
- **[Official], second-hand** for §6: Evertz product/manual listing pages and reseller catalogue
  copy (Midtown Video, AV-iQ, Lubbock AV), read via search extract 2026-09-01 — not fetched in full.
- **[Official], second-hand** for §3.1–§3.3: the 2431RX-2 and 2432RX2-HDMI instruction manuals
  (signal-type menu — GSDI / GLINK / RGBR / Auto), the 2430GDAC manual, a ManualsLib Evertz index,
  and the current Evertz/AV-iQ product pages for the 2430RX-J2K-IP, 2430RX2-10G, and MMA10G-TRS4K/
  TRM4K gateway family — all read via search extract 2026-09-01, none fetched in full.
- **Verified [Official]** for §10 — *MMA10G-HUB In-Room AV Switch* datasheet, **Rev. 02, © 2017
  Evertz Microsystems**, 2 pp., user-supplied 2026-09-03, read in full. Recovered from the Internet
  Archive; the gen-1 HUB has been removed from Evertz's live site, and four searches (Evertz site
  search, the `av.evertz.com/pdf/product/` path, AV-iQ, HDBaseT.org, ManualsLib, Manualzz) found no
  live copy and **no instruction manual for any HUB generation** — Evertz publishes datasheets
  publicly and gates manuals behind support.
- **Verified [Official]** for §10.3's HUB2 column — *MMA10G-HUB2* datasheet, Rev. 06, © 2020,
  fetched in full from `av.evertz.com/pdf/product/MMA10G-HUB2.pdf` 2026-09-03.
- **Bench-observed [User]** for §10.1's connector layout — back-panel photograph of a used
  `MMA10G-HUB-4S8X4-4`, S/N 7441550001, supplied 2026-09-03 and inspected enlarged. Pin field
  counted at 3 rows × 8 columns fully populated plus 4 analog pins, i.e. a 29-pin DVI-I dual-link
  receptacle. **The connector was counted; the electronics behind it were not tested.**
- **What was NOT read in full:** the *body* of any instruction manual (only the signal-type and
  resolution passages surfaced by search); the GLINK format specification, if a public one exists.
  The 2430-series relatives and the 12G line are no longer unknowns — see §3.2–§3.3.
- **Nothing bench-tested.** No Evertz unit has been measured in this library's history, and the user
  owns none of them.
- **Open contradictions:** the 2431RX-2 datasheet's body copy repeatedly names the **2430**RX-2
  while the title block, spec table and ordering information all say **2431**RX-2. Read as
  copy-paste from the predecessor datasheet, not as two products — but Evertz has never corrected
  it, and both model numbers exist on the used market. ⚠️ Confirm the model on the chassis label,
  not the datasheet body.
- **Corrected 2026-09-03:** §8 previously listed the **Analog Way VIO 4K as taking dual-link DVI in
  at 4K30**. `analog-way-vio-4k.md` §1.4 — a primary manual extract already in this library —
  contradicts it: the VIO's native DVI-DL input caps at **2560×1600@60**. The wrong line came from
  reseller/summary copy. The **Barco ImagePRO-II** entry beside it has the same provenance and has
  **not** been checked against a Barco document; it is [Lead], not [Official]. Consequence: **this
  library currently confirms no device that accepts dual-link DVI at 4K30.**

---

## 1. Why this document exists

These units come up when someone has a **dual-link DVI source and a modern destination**. That is a
dead product category almost everywhere else — see §7 — and the Evertz pair looks like the answer.

It is not, for 4K. The reason is worth writing down because the arithmetic is not obvious and the
datasheets never state it: **GLINK's dual-link mode holds 2560×1600@60 and nothing larger.**

---

## 2. The three units

| Model | Direction | Video I/O | Notes |
|---|---|---|---|
| **2432TX-2** | DVI/VGA/component → serial | 2× 28-pin DVI in; 2 SDI out (4 BNCs in dual-link mode) | **Has a genlock input.** Scales best-fit to SMPTE |
| **2431RX-2** | serial → DVI | 2× 28-pin DVI-I out | No crop/scale listed |
| **2432RX2-HDMI** | serial → HDMI | 2× HDMI female, **HDMI v1.4** | **Crop and Scale listed** |

All three: 24 bits per pixel, HDCP compliant, 12 VDC, ~27–28 W, 7.81″ × 5.63″ × 1.75″, 1 lb.
Optional hot-pluggable SFP for fiber — **two SFPs per unit when in dual-link mode**, one per link.

Evertz positions the family as the **EFX system** for video wall and command-centre projects. They
are extenders that happen to convert, not converters that happen to extend. That framing explains
most of the limits below.

---

## 3. GLINK — the proprietary transport

Every unit lists its serial standard as **SMPTE 259M / 292M / 424M *and* Evertz proprietary GLINK**
(the 2432TX-2 datasheet calls it "3GLINK"; the two RX datasheets call it "GLINK"; treat as one
thing, spelled inconsistently).

**This is the load-bearing fact for the whole family:**

- **WQXGA (2560×1600@60) rides GLINK, not SMPTE.** 2560×1600 is not a SMPTE raster and never was.
- Dual-link mode uses **two 3G paths** — 4 BNCs on coax, or 2 SFPs on fiber.
- **Coax and fiber are equivalent here.** The dual-link capability is a function of transport mode,
  not medium. A common misreading is that fiber is required for WQXGA; it is not.
- Anything between a TX and an RX must be **bit-transparent at 3G**. A GLINK stream will not survive
  a format-aware router, a Blackmagic mini converter, or anything that reclocks against SMPTE.

**Consequence:** the TX and RX are a matched pair. There is no "convert to SDI, route it normally,
convert back" path at WQXGA. At SMPTE rasters the units interoperate with ordinary SDI gear; at
WQXGA they interoperate only with each other.

### 3.1 — GLINK is the multiviewer/KVM transport, not a general one

The RX instruction manuals (2431RX-2, 2432RX2-HDMI) enumerate the input signal types, and this is
where GLINK's actual purpose shows:

- **GSDI mode** — 1.5G / 3G SDI, or 3GLINK
- **GLINK mode** — "Evertz proprietary, used with **MVP/VIP**" (their multiviewer platforms)
- **RGBR mode** — "Evertz proprietary, used with **KVM products**"
- **Auto Detect** — recommended default

So GLINK is not a generic high-res transport Evertz sells to everyone; it is the **signalling that ties
their multiviewer (MVP/VIP) and monitoring-processor world together**, with RGBR as its KVM-domain
sibling. The DVI/HDMI converters in this family exist to get those proprietary domain signals onto a
normal monitor. That framing is why the resolution ceiling is WQXGA — that is what the multiviewer
domain needed, not a target anyone chose for general 4K work.

### 3.2 — The GLINK product roster (as found)

**Confirmed GLINK-carrying units:**

| Model | Role | Video out | Notes |
|---|---|---|---|
| **2432TX-2** | transmit | (DVI **in**) → serial/GLINK | dual-link DVI/VGA/component in; genlock in |
| **2431RX-2** | receive | → DVI-I | crop/scale not listed |
| **2432RX2-HDMI** | receive | → HDMI 1.4 | **Crop and Scale listed** |
| **2430GDAC** | receive | → DVI-I + analog | for 3000PPMV/PPMG monitoring; UXGA ceiling |
| **2430GDAC-WARP** | receive | → DVI-I | adds warp / geometry correction |
| **2430GDAC-MWP** | receive | → DVI-I | MWP variant |

**Checked and *excluded* — 2430-family relatives that share the DVI/HDMI output stage but do NOT
take GLINK in:**

- **2430RX-J2K-IP** — input is **JPEG2000 over IP**, out to DVI/HDMI/DP, ≤ WUXGA
- **2430RX2-10G** — input is **uncompressed SDI over 10GbE** (ASPEN / SMPTE 2022-6 / ST 2110), out to
  HDMI + SDI, ≤ WUXGA

These two look like family members and are easy to add to a GLINK list by mistake; their *inputs* are
IP transports, not GLINK. Kept here as explicit negatives so the roster isn't re-padded later.

⚠️ **Roster is not provably exhaustive.** Sourced from three datasheets, two RX instruction manuals,
a manuals-library index, and reseller catalogues — not Evertz's full catalogue. Treat as "all that
surfaced," not "all that exist."

### 3.3 — There is no 12G GLINK, and no DVI-DL in the 12G line

GLINK is a **3G-era transport (≈6G dual-link) with no 12G successor.** When Evertz moved to 12G/4K —
the **MMA10G-TRS4K / TRM4K** gateway family, and the current-catalogue **2430GDAC** product number —
they dropped GLINK entirely and moved to standard **12G-SDI, quad-link 2SI (SMPTE 425-5), HDMI 2.0a,
and ST 2110 / IPMX**.

**Every unit in that 12G family is HDMI-only or SDI-only on the video side. Not one has a DVI
connector of any kind.** Checked across the TRS4K-2 / -2x2 / -4x2 / -HDMI / -2D / -2UH variants and
the TRM4K-12G — all HDMI 2.0a and/or 12G-SDI, transported over 10GbE.

⚠️ **Scope correction, 2026-09-03.** That claim is true of the **12G gateway family** and must not be
read as "no DVI anywhere in MMA10G." The **first-generation `MMA10G-HUB` in-room switch has a DVI-I
input** — see §10. It is a 10GE-era product, not 12G, and its DVI-I is a low-ceiling connector
option rather than a dual-link path, so the dead end below is unaffected. But the blanket phrasing
was wrong.

**The dead end this creates inside Evertz:** the DVI-DL door (3G EFX boxes) and the 4K door (12G/IP
gateways) are in different product generations with **no GLINK-to-12G bridge between them.** A
dual-link DVI source can get *into* GLINK via the 2432TX-2, but GLINK terminates at the 3G RX units,
all WQXGA-ceiling. There is no Evertz product that lifts GLINK *up* into the 12G/4K world. Same
conclusion as every other vendor in §8: dual-link DVI at true 4K lives only in the scaler category.

---

## 4. The format tables — enumerated, not clock-bounded

**2432TX-2 supported input resolution**, quoted from the spec table:

> VESA: VGA, SVGA, XGA, WXGA, SXGA, SXGA+, UXGA, WSXGA+, WUXGA, WQXGA (dual-link).
> CEA-861B: 480p, 576p, 720p, 1080i, 1080p

**Both RX units** state the same output ceiling:

- Up to **WUXGA (1920×1200) @ 60 Hz** — single link
- Up to **WQXGA (2560×1600) @ 60 Hz** — dual link

This is an **enumerated list, not a pixel-clock limit.** No datasheet in the family states a pixel
clock or MHz figure anywhere. **3840×2160 appears in no form on any of the three.**

The distinction matters: a clock-bounded device might accept an unlisted timing that fits under its
ceiling. An enumerated device matches against a table and rejects everything else. Nothing in these
datasheets suggests the table is advisory.

⚠️ **Unverified:** whether the format table is firmware-enforced or merely the tested list. The
instruction manuals were not read and may say. Absent that, assume enforced.

---

## 5. Why 4K30 does not fit — the arithmetic

The tempting argument is that 2560×1600@60 and 3840×2160@30 are "the same signal." They are close,
but they are not equal, and the difference falls the wrong way.

**Active pixel rates:**

| Format | Calculation | Result |
|---|---|---|
| 2560×1600@60 | 2560 × 1600 × 60 | **245,760,000 px/s** |
| 3840×2160@30 | 3840 × 2160 × 30 | **248,832,000 px/s** |

4K30 is **higher by 3,072,000 px/s — about 1.25%.**

**Against the transport, at the datasheets' stated 24 bits per pixel:**

| | Payload | vs 2× 3G-SDI (5.940 Gbps) |
|---|---|---|
| WQXGA @ 60 | 245,760,000 × 24 = **5.898 Gbps** | fits, ~0.7% margin |
| 4K30 @ 24-bit | 248,832,000 × 24 = **5.972 Gbps** | **over by ~0.5%** |

**Tier: reasoned arithmetic from datasheet figures, not a stated Evertz limit.** Real payload
accounting depends on GLINK's mapping and how it handles blanking, neither of which is published.
But the shape of the result explains the format table: Evertz stopped at WQXGA because that is
approximately what two 3G links hold at 24 bits, and 4K30 lands just past it.

**With realistic blanking it is worse.** A Spyder X20 4K output factory format observed in the field
runs HTotal 4000 × VTotal 2191 @ 29.97 (see `christie-spyder-x20.md` §5.1) — 4000 × 2191 × 29.97 ≈
**262,700,000 px/s including blanking**, ≈ 6.30 Gbps at 24-bit. Comfortably over 2× 3G.

---

## 6. The HDMI 1.4 near-miss

The 2432RX2-HDMI is the most interesting unit in the family for anyone chasing 4K30, and the most
frustrating.

- Its **HDMI output is version 1.4**, which carries 3840×2160@30 natively
- Its stated video resolution nonetheless stops at **WQXGA @ 60 dual link**
- 2560×1600@60 needs roughly 268 MHz of pixel clock; HDMI 1.4's ceiling is about 340 MHz

So the output transmitter is already capable of the target format and is being fed by an input path
that cannot deliver it. **The wall is upstream of the HDMI connector, in GLINK and the format
table — not in the output silicon.**

⚠️ The 2432RX2-HDMI datasheet describes converting "to single link or dual link HDMI." **There is no
dual-link HDMI.** This is copy-paste from the DVI-output variant; the dual-link refers to the SDI
input side and the original DVI source. Do not repeat the phrasing.

---

## 7. Where these units *do* earn their place

Not the 4K job. But two real uses came out of the same reading:

**7.1 — Genlocked scan conversion from legacy sources.** The 2432TX-2 takes DVI, VGA *or* component
in, embeds a stereo audio pair per input, and has a **genlock input** — with configurable best-fit
scaling to SMPTE 259M/292M/424M. For a rig whose rule is that scaling and scan conversion happen only
on gear with reference inputs, this qualifies, and it is cheap used.

**7.2 — Crop and scale on a 3G-SDI feed.** The 2432RX2-HDMI lists **Crop and Scale** functionality,
which neither the TX nor the DVI-output RX does. For pulling an area of interest out of a 16:9 SDI
feed, this is a small, inexpensive box that does the crop half. It outputs HDMI, so a downstream
stage is still needed to reach anything else.

---

## 8. The wider category — what else was checked

Recorded so the search is not repeated. All checked 2026-09-01 by web search; **[Official]** where a
vendor page or datasheet was read, **[Lead]** where only reseller copy was seen.

**Genuine dual-link-DVI-input converters found, with their ceilings:**

| Device | Out | Ceiling | Tier |
|---|---|---|---|
| Gefen GTV-DVIDL-2-MDP | Mini DisplayPort | 2560×1600 | [Official] — manual Rev A6 read in full |
| Gefen EXT-DVIDL-2-HDMIR | HDMI | 1920×1200 | [Lead] |
| Comprehensive CCN-DH101 | HDMI | 1080p, discontinued | [Lead] |
| Evertz 2432TX-2 + RX | DVI or HDMI | 2560×1600 | [Official] — §4 above |

**The pattern: 2560×1600 is the ceiling of every cheap dual-link-input device found.** None reaches
4K30.

**Devices that do take dual-link DVI in at 4K30** — ⚠️ **this list is now down to one candidate, and
that one is unconfirmed.**

- ~~**Analog Way VIO 4K** — DVI-DL input at 4K30.~~ **Wrong, corrected 2026-09-03.** The VIO manual
  extract in this library contradicts it directly: `analog-way-vio-4k.md` §1.4 gives the native
  **DVI Dual-Link input a ceiling of 2560×1600@60**, the same as the Evertz pair. Its 4K@30 inputs
  are **DisplayPort and HDMI**, not DVI. The `OPT-OUT-VIO4K` card reaches 4K@30 on dual-link DVI but
  is **output only**. This entry was written from reseller/summary copy while the primary manual
  extract sat in the same directory saying otherwise — **read the device's own document before
  listing it here.**
- **Barco ImagePRO-II** (**not** the Jr — dual-link resolutions are unavailable on Jr) — DVI-DL
  input up to 300 MHz. ⚠️ Its 4K@30 support is on **dual-link DVI and DisplayPort only**; its HDMI
  is 1.4 at 165 MHz and its SDI is 3G. A DVI-DL → HDMI job needs a second box after it. ⚠️ **This
  entry comes from the same reseller-copy sweep that produced the wrong VIO line above and has not
  been checked against a Barco document.** Treat as [Lead], not [Official], until one is read.

**So the honest state of the survey: no device in this library is confirmed to accept dual-link DVI
at 4K30.** The claim that cheap options stop at 2560×1600 stands; the claim that expensive options
clear it does not currently rest on anything primary.

**Checked and does not do it:** Analog Way QuickVu and Pulse² (Midra platform, DVI-D single-link,
2K ceiling); Analog Way LiveCore/Ascender (has DVI-DL, but discontinued and 4K is a quad-output
combine); Lightware MX DVI-DL matrices (route dual-link to 3840×2400 but **do not transcode** to
HDMI; the newer MX2 generation dropped DVI-DL entirely); DVIGear DVI-3531a (165 MHz single-link);
Extron dual-link DVI scalers (retired line).

**The market asymmetry, worth knowing:** DisplayPort → dual-link DVI is a healthy, cheap category
(StarTech DP2DVID2, Club3D CAC-1010, Monoprice, VisionTek — ~$30–120, 2560×1600). The reverse is
nearly empty. Active converters are unidirectional, so none of those reverse. The demand existed for
driving old 30″ monitors from new GPUs, not for feeding new gear from old sources.

---

## 9. Not yet verified — open items

- **Whether the format tables in §4 are firmware-enforced or advisory.** The three instruction
  manuals were not read. This is the single question that would close the 4K30 case properly.
- **GLINK's actual payload mapping** — how it handles blanking, and whether the §5 arithmetic
  reflects what the transport really carries. No public specification was found.
- ~~Whether Evertz has a later 4K-capable member of this family.~~ **Answered 2026-09-01 (§3.3):**
  yes, the MMA10G-TRS4K/TRM4K 12G/IP gateways — but **none takes GLINK or DVI of any kind**, so they
  do not bridge a dual-link DVI source to 4K. The 2430RX2-10G and 2430RX-J2K-IP are WUXGA-ceiling IP
  receivers, not GLINK carriers. No GLINK-to-12G path exists inside Evertz.
- **The 2431 vs 2430 model-number contradiction** in the RX datasheet body copy — see Provenance.
- **Whether the 2432TX-2's genlock input works at WQXGA/GLINK rates or only at SMPTE rasters.** The
  datasheet lists genlock without qualifying it. §7.1 assumes SMPTE use, where it is unambiguous.
- **A dual-link-DVI-input converter above 2560×1600 that is not a full scaler.** Vendors checked in
  §8; tvONE and Apantac were named as candidates and **never searched**. Reddit r/VIDEOENGINEERING
  could not be reached through the available search tool — a failed attempt, not an absence of
  content there.

---

## 10. The `MMA10G-HUB` gen 1 — the DVI-I in the MMA10G line, and why it doesn't help

Added 2026-09-03 from the **first-generation MMA10G-HUB datasheet, Rev. 02, © 2017**, recovered from
the Internet Archive after it was pulled from Evertz's live site, plus a back-panel photograph of a
used unit (S/N 7441550001). §3.3's blanket "no DVI of any kind" was written before either existed.

### 10.1 The DVI-I is real, and it is not its own input

Every gen-1 model is specified as **"n HDMI (Type A) + 1 (either HDMI or DVI-I)"**. One input is
dual-connectored — you pick HDMI *or* DVI-I for it, not both. The back-panel photo confirms this
physically: HDMI jacks labelled 1, 2, 3, then a single bracket labelled `4` spanning both an HDMI
jack and the DVI-I.

| Model | Video inputs | Video outputs | 10GE |
|---|---|---|---|
| `MMA10G-HUB-4x2-2` | 3 HDMI + 1 (HDMI or DVI-I), 2 SDI | 2 HDMI | 2× SFP+ |
| `MMA10G-HUB-4x2A-2` | same, + 32×32 Dante | 2 HDMI | 2× SFP+ |
| `MMA10G-HUB-8x4-4` | 7 HDMI + 1 (HDMI or DVI-I), 4 SDI | 4 HDMI | 4× SFP+ |
| `MMA10G-HUB-8x4A-4` | same, + 32×32 Dante | 4 HDMI | 4× SFP+ |

**SDI inputs are not fitted by default** — they require `SFP3R-DIN2-3G` dual 3G-SDI DIN SFP
receivers, ordered separately. This decodes the field-applied label on the used unit: **`4S8X4-4`
reads as an `8x4-4` with four SDI SFPs fitted**, the `4S` being the SDI count the base ordering code
omits.

### 10.2 The ceiling kills it

**`Supported Resolutions: HDMI: up to 1920x1200p @ 60 Hz`.** That is the entire video spec line for
all four models. There is no 4K entry, no WQXGA entry, and **no separate ceiling stated for the
DVI-I** — the datasheet gives one resolution row covering the HDMI path and never qualifies the
DVI-I connector at all.

So the dual-link question is moot on this box. 1920×1200@60 CVT-RB is a 154 MHz raster that rides one
TMDS link with room to spare; nothing this switch accepts needs a second link, whatever the
receptacle's pin count suggests. ⚠️ **A fully populated 24-pin DVI-I receptacle is not evidence of
dual-link electronics** — this unit is the library's clearest demonstration of that, and the same
caution applies to the Lightware `SW4-TPS-TX240`'s 29-pole DVI-I (`lightware-tps-hdbaset-dvi.md` §4).

### 10.3 Gen 1 vs HUB2 — do not read one's spec table onto the other

| | `MMA10G-HUB` (Rev. 02, 2017) | `MMA10G-HUB2` (Rev. 06, 2020) |
|---|---|---|
| Video ceiling | **1920×1200@60, all inputs** | 3840×2160@30 on odd inputs; 1920×1200@60 on even |
| DVI | **1 shared HDMI/DVI-I input** | **none** |
| HDBaseT | none | 2 or 4 ports on the `22x11` / `44x22` models |
| SDI | 2 or 4, **SFP required** | 2 or 4, fitted |
| Control Ethernet | 2× 10/100Base-T | 1–3× 10/100/1000Base-T |
| Odd/even input split | **none — flat ceiling** | yes, odd inputs are the 4K ones |

⚠️ The odd/even 4K split is a **HUB2-only** structure. It was briefly applied to gen 1 in session
before the gen-1 datasheet was recovered, and that was wrong in an interesting way: gen 1 has no 4K
inputs at all, so there is nothing for the split to divide.

⚠️ **Open contradiction inside the gen-1 datasheet, kept not corrected:** the front-page model table
gives `MMA10G-HUB-8x4A-4` **2 SDI**, while the specifications table on page 2 gives the same model
**4 SDI**. The other three models agree across both tables. Read the spec table as authoritative on
the strength of the ordering information, but confirm SFP count on the chassis.

### 10.4 Verdict for a dual-link DVI source

**Out.** Not on connector grounds — on raster grounds. A 1920×1200 ceiling is below every candidate
raster in §8, below the Evertz GLINK pair's 2560×1600, and far below 4K30. The DVI-I on this box
exists to take a legacy laptop or lectern PC into a meeting room, which is what the whole product is
for.
