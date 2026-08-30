# AJA Mini-Converters — HA5 / Hi5 HDMI ↔ SDI

## Provenance

- **Verified [Official]** for every format and I/O figure below. Sources read 2026-08-30:
  - *HA5-4K HDMI to SDI Mini-Converter Installation and Operation Guide*, v1.7r2, published
    2019-12-03 — **read end to end**, including the Appendix A tech specs and the block diagram
  - **HA5-Plus product page tech specs**, aja.com, read in full (video formats, digital input,
    digital output, audio, size, weight, power, environment)
  - Hi5-Plus and HA5-12G product-page copy, read for feature and rate statements only
- **What was NOT read:** the HA5-Plus and Hi5-Plus user guides as PDFs (only the product-page tech
  specs), and the whole Hi5-4K-Plus / Hi5-12G / fiber line beyond model identification.
- **Nothing bench-tested.** No AJA converter has been measured in this library's history.
- **Open contradictions:** none between sources. The significant finding is an **absence** — §3.

---

## 1. Model families, and the trap in them

| Model | Direction | SDI tier | Status |
|---|---|---|---|
| **HA5** | HDMI → SDI | **SD / HD-SDI only — not 3G** | Discontinued, replaced by HA5-Plus |
| **HA5-Plus** | HDMI → SDI | **3G / HD / SD**, 1× output | Current |
| **HA5-4K** | HDMI 2.0 → SDI | 4× 3G-SDI, up to 4K/UHD 60 | Current |
| **HA5-12G** | HDMI 2.0 → 12G-SDI | 12G single link, 2 outputs | Current |
| **Hi5** | SDI → HDMI | SD / HD-SDI only | Superseded |
| **Hi5-Plus** | SDI → HDMI | **3G / HD / SD** | Current |

⚠️ **The plain HA5 and Hi5 cannot carry 1080p59.94.** That is a 3G format and those units are
HD-SDI. Anyone reaching for "HA5 and Hi5" for a 1080p60 round trip needs the **Plus** versions.
This is the easiest mistake in the family and the model names do not warn you.

---

## 2. HA5-Plus and Hi5-Plus — the 1080p59.94 round trip

**HA5-Plus** (HDMI in, 3G-SDI out):

- HDMI Type A, **HDMI v1.4**; YCbCr 4:2:2 / 4:4:4 / 4:2:0; 8 or 10-bit
- Input formats include **1920×1080p at 23.98 / 24 / 25 / 29.97 / 30 / 50 / 59.94 / 60**
- Output: **1× 3 Gb SDI (Level A or B Dual Link)** carrying 1080p at the same rate list;
  also a 1.5 Gb mode (1080p low rates, 1080i, 720p) and 270 Mb SD
- Equalized HDMI input rated to **30 m on 24-gauge cable**; PLL clock filtering on the SDI output
- 8 channels of HDMI embedded audio to SDI, or 2 channels from RCA analog
- **HDCP content not supported** — SDI outputs are unencrypted by definition
- ⚠️ **"Simple Frame Rate Conversion (FRC) from fractional to integer rates" is a listed feature.**
  At 59.94 in and 59.94 out it should be off. **If it is on, the box is doing rate conversion**,
  which is where real delay would come from. Check it in Mini-Config before trusting or measuring
  anything.

**Hi5-Plus** (3G/HD/SD-SDI in, HDMI out):

- 30-bit Deep Colour RGB output to a compatible monitor
- 16 channels of embedded SDI audio in, 8 to HDMI out, plus 2-channel RCA analog out
- **Audio delay, 0 to 7 frames, user-set in Mini-Config** — a lip-sync tool, *not* a statement
  about video delay
- PsF → progressive conversion (1080PsF in, 1080p out), since HDMI monitors do not take PsF
- 3G-B dual-stream handling: `1 x HD DS1` or `1 x HD DS2` to pick a single stream

**The round trip is valid.** 1080p59.94 goes HDMI → 3G-SDI → HDMI with no format change.

---

## 3. Latency — AJA publishes no figure. This is the finding.

**Searched and read for it on 2026-08-30; it does not exist in any AJA source consulted.**

- The **HA5-4K manual's Appendix A** covers video formats, digital input, digital output, audio,
  user interface, size, weight, power and environment. **No processing-delay figure appears
  anywhere in the document**, which was read end to end.
- The **HA5-Plus product-page tech specs** were read in full — same categories, same absence.
- The **Hi5-Plus** page names only the **audio** delay, 0–7 frames, user-set. That is a sync
  control, not a video latency spec, and quoting it as one would be wrong.

**Do not fill this gap.** No number for HA5/Hi5 video latency should enter this library, a client
quote, or a show plan until one is measured.

**Two pieces of evidence that bear on it, both short of an answer:**

1. ⚠️ **The HA5-4K block diagram shows "Frame Buffer and Video Processing" in the video path**
   (AJA's own figure, manual p.5). A frame buffer is not a line-based passthrough. **The diagram
   does not say how deep it runs**, and the HA5-Plus has no published block diagram in anything
   read, so this cannot be carried across to it.
2. **Reasoning only, not a measurement:** neither Plus box scales, neither is a frame
   synchronizer, and both are one-format-in-one-format-out. That is consistent with sub-frame
   delay per box. Tier: **Reasoned only.** It contradicts nothing, proves nothing, and must not be
   quoted.

### 3.1 The test that would settle it

Not performed — no hardware was available this session.

1. Confirm FRC is **off** on the HA5-Plus in Mini-Config (§2).
2. Split one 1080p59.94 source two ways.
3. Leg A direct to a display; leg B through HA5-Plus → Hi5-Plus into a display of the same model.
4. Film both screens together at 240 fps and count the frame offset.
5. Halve it for a rough per-box figure, or keep the pair figure — the pair is what a signal chain
   actually costs.

Result goes in §3 as **Bench-verified**, and the absence above stays recorded alongside it.

---

## 4. Open items

1. **Video latency, both directions.** The whole of §3.
2. **Whether the HA5-Plus shares the HA5-4K's frame-buffer architecture.** No block diagram for
   the Plus exists in anything read.
3. **What FRC actually does to latency when engaged** — AJA describes the feature and gives no
   delay figure for it either.
4. **The HA5-Plus and Hi5-Plus user guides as PDFs.** Only the product-page tech specs were read;
   a full manual might carry a block diagram or a delay note the page omits.
