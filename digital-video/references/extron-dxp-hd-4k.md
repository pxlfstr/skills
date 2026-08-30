# Extron DXP HD 4K Series — HDMI matrix switchers

## Provenance

- **Sourcing tier: Verified [Official] for the figures, but snippet-level, not a full read.** The
  source is Extron's own specifications PDF, *DXP 44/84/88/168/1616 HD 4K Series • Specifications*,
  document `dxp_hd_4k_ser_5377-D10.pdf`, reached via web search on 2026-08-30. **A direct fetch of
  that PDF was attempted the same session and failed** — Extron's site returned a bot-defense
  rejection (support ID logged, HTML error page in place of the document). Only the search-returned
  extract was read.
- **What was NOT read:** the full specifications PDF, any DXP HD 4K user manual, EDID Minder
  documentation, and the whole PLUS-series line beyond what is needed to keep the two apart.
- **Reseller pages** (Creation Networks, ITM Components, Ivojo) were seen and are **[Forum]-tier
  restatements of Extron marketing copy** — used only where they agree with the Extron figures,
  never as the sole source for a number.
- **Nothing here was bench-tested.** No DXP has been put in front of a signal in this library's
  history.
- **Open contradictions:** none between sources. The live risk is a **model-name collision**, §1.

---

## 1. Two different products, one name apart

**`DXP … HD 4K` and `DXP … HD 4K PLUS` are different switchers with different ceilings.** Confusing
them is the failure mode this document exists to prevent — the part numbers differ only in a
suffix (`60-1495-01` vs `60-1495-21` on the 88).

| | **DXP HD 4K** | **DXP HD 4K PLUS** |
|---|---|---|
| Max data rate | **10.2 Gbps** (3.4 Gbps per colour) | **18 Gbps** |
| Max pixel clock | **300 MHz** | Not stated in the extract read |
| Resolution range | Up to **2560×1600 @ 60**, or **4096×2160 @ 30** / **3840×2160 @ 30** | 640×480 to **4096×2160 @ 60** |
| Standards | DVI 1.0, HDMI 1.4, **HDCP 1.4**, CEA-861E | DVI 1.0, HDMI 1.4 and 2.0/2.0b, **HDCP 1.n and 2.3**, CEA-861E |
| 12-bit Deep Colour | Up to 1920×1200 / 1080p @ 60 | Up to 1080p/60; 12-bit supported per HDMI 2.0b |

**The non-PLUS is a 4K/30 box.** Its 4K support is 30 Hz only; 60 Hz stops at 2560×1600.

**Formats:** RGB and YCbCr digital video, both series.

⚠️ **DVI sources need a passive DVI-D↔HDMI cable or adapter** — Extron states this explicitly as a
note on the standards line. **This covers single-link DVI only.** Nothing in either series accepts
dual-link DVI; see §3.

---

## 2. I/O and the model-number trap

`DXP 88 HD 4K` is an **8×8** matrix — 8 female HDMI in, 8 out, HDCP compliant, with 2 audio outputs.

⚠️ **The specifications PDF's own I/O summary line reads "DXP 88 HD 4K Series … 4 × 4 matrix"**,
which contradicts the product name and every other statement about the model. Read as a **typo or
a mis-scoped line in the series table** (the same table's other rows are consistent), not as a real
4×4 variant — but recorded rather than silently corrected, since the extract read was partial.

Audio can be **de-embedded from any input** and assigned to digital or analogue stereo outputs.

**Signal conditioning:** automatic input cable equalisation and **output reclocking** — timing is
reshaped at each output, so the switcher does not pass the source's jitter downstream. It is a
matrix, **not a scaler and not a frame sync**: no format conversion, no genlock, no timing change
beyond reclocking. Extron technologies present: SpeedSwitch, EDID Minder, Key Minder.

---

## 3. Feeding a DXP HD 4K from a Christie Spyder X20

**The reason this document exists.** Worked through 2026-08-30.

**The bandwidth side is fine.** The X20's 4.1.0 4K output factory format is 3840×2160 @29.97 at a
computed **262.66 MHz** (`christie-spyder-x20.md` §5.1). Comparison, computed this session:
262.66 < 300, so the raster sits inside the non-PLUS DXP's 300 MHz pixel-clock ceiling, and
3840×2160 @30 is named explicitly in its resolution range.

**The connector side does not work.** At 262.66 MHz that X20 format is **true dual-link** — above
the 165 MHz a single TMDS link carries — and:

- **No dual-link-DVI → HDMI converter appears to exist as a shipping product.** Searched three
  ways on 2026-08-30. Everything returned was either a **passive adapter** wired to the
  single-link pins only (Monoprice's own support states their dual-link-labelled adapter carries
  single link and caps at 1920×1200), or **genuine dual-link gear that stops below 4K** (Ophit's
  DQSP dual-link fibre extender maxes at 2560×1600@60). Tier: **negative result from search, not
  from a vendor statement** — no manufacturer says such a box does not exist.
- Passive adapters do reach 4K30 from **GPUs**, because a GPU drives one TMDS link at HDMI-style
  ~297 MHz through the DVI connector. **That path does not apply to a true dual-link source**,
  where the pixels are split across two links.

**Two workable paths, in preference order:**

| | Path | Cost | Notes |
|---|---|---|---|
| **B** | **Tile the canvas across four single-link X20 outputs at 1920×1080**, passive DVI→HDMI on each, into four DXP inputs | No new hardware; 4 X20 outputs | 3840×2160 = 8,294,400 px against a 20 M VI budget, so it fits **at 60 Hz** — where the dual-link route is locked to 30. Framelock the outputs. Reassembly happens downstream, not in the DXP |
| **A** | **Datapath x4** — dual-link DVI in to 330 Mpixel/s, four single-link DVI/RGB out at 165 Mpixel/s, max 2048 px either direction | One X20 output; discontinued, used market only | Cannot emit a single 4K30 — it splits the 4K into four HD feeds, so the DXP still sees four inputs. No HDCP, which is moot: HDCP mode forces the X20 to single link anyway. Source: Datapath product/reseller pages, **[Official]/[Forum] mixed, not a manual** |

**Path B is preferred** — same end state at the matrix, no extra box, and it doubles the available
frame rate.

⚠️ **Neither path has been built.** Both are **Designed**, not bench-verified.

---

## 4. Open items

1. **The full specifications PDF has never been read** — blocked by bot defense. Vertical frequency
   range, audio detail, control interfaces, power and environmental figures are all unknown for the
   non-PLUS series.
2. **The PLUS series' maximum pixel clock** is not in anything read. 18 Gbps is stated; the clock
   figure is not.
3. **The "4 × 4 matrix" line** against the DXP 88 name (§2) — assumed a source typo, unconfirmed.
4. **EDID Minder behaviour with a Spyder as source** — whether the DXP's EDID presentation would
   even offer the X20 a 3840×2160@29.97 timing, or force a different one. Unknown, and it decides
   whether path B's outputs handshake cleanly.
5. **Whether any dual-link-DVI → HDMI converter exists at all.** Searched, not found; a negative
   result of this kind is never final.
