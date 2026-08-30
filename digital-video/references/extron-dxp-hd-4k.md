# Extron DXP HD 4K Series — HDMI matrix switchers

## Provenance

- **Sourcing tier: Verified [Official] — both user guides now read directly.** Revised 2026-08-30,
  same day it was created, when the user supplied the two manuals:
  - *DXP HD 4K Series User Guide*, **68-2759-01**, 113 pp., PDF dated 2019-06-28 — the non-PLUS line
  - *DXP HD 4K PLUS 4K HDMI Switchers User Guide*, **68-2939-01 Rev. R**, 132 pp., PDF dated
    2026-05-22 — the PLUS line
  Text extracted in full from both; the EDID chapters and EDID reference tables were read
  section by section.
- **The specification figures in §1 remain snippet-tier.** Extron publishes rate and pixel-clock
  numbers on a separate specifications sheet, not in either user guide, and **a direct fetch of
  `dxp_hd_4k_ser_5377-D10.pdf` was blocked by Extron's bot defense** (support ID logged, HTML
  error page returned in place of the document). Those figures come from the search-returned
  extract of that sheet, not from a document read end to end. **Neither user guide states a
  maximum data rate, a pixel clock, or a resolution range anywhere** — checked by search across
  both extracted texts.
- **Reseller pages** (Creation Networks, ITM Components, Ivojo) were seen and are **[Forum]-tier
  restatements of Extron marketing copy** — used only where they agree with the Extron figures,
  never as the sole source for a number.
- **Nothing here was bench-tested.** No DXP has been put in front of a signal in this library's
  history. The user owns **both an 88 HD 4K and an 88 HD 4K PLUS**, so every open item below is
  answerable on hardware.
- **Open contradictions:** none between sources. The live risk is a **model-name collision**, §1.

---

## 1. Two different products, one name apart

**`DXP … HD 4K` and `DXP … HD 4K PLUS` are different switchers with different ceilings.** Confusing
them is the failure mode this document exists to prevent — the part numbers differ only in a
suffix (`60-1495-01` vs `60-1495-21` on the 88).

| | **DXP HD 4K** | **DXP HD 4K PLUS** |
|---|---|---|
| Max data rate | **10.2 Gbps** (3.4 Gbps per colour) | **18 Gbps** |
| Max pixel clock | **300 MHz** | Not stated in anything read — see §5 |
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

## 4. EDID — read from both manuals, 2026-08-30

**This is the part the user guides actually cover well**, and it is where the two models differ
most in practice.

**EDID Minder, both series.** Each source connected to an input sees the EDID of a display even
when that source is not currently selected for any display. The unit either stores the connected
display's EDID automatically (default) or takes a factory file the user picks.

### 4.1 DXP 88 HD 4K (non-PLUS) — a numbered table, front-panel-independent

68-2759-01 p.64 gives an explicit **DDC source-selection table** for the 88, addressed by the SIS
variable `X4$`:

| Slot | EDID |
|---|---|
| 1–7 | 1280×800 / 1440×900 / 1600×900 / 1680×1050 / 1920×1200 / 2560×1440 / 2560×1600, all @ 60, 2-ch audio |
| 8–12 | 720p50, **720p60 (factory default)**, 1080p50, 1080p60, **4K/UHD @ 30** — 2-ch audio |
| 13–17 | 720p50, 720p60, 1080p50, 1080p60, **4K/UHD @ 30** — S/PDIF audio |
| 18–25 | Outputs 1–8, stored from the connected display as reference |
| 26–33 | **Eight user-loaded slots** |

Commands: `EA` assign to an input, `EA…*` assign to all, `ES` save an output's EDID to a custom
slot, `EI` / `EE` import and export a `.bin` from a PC, `EE…UNAM` name a custom slot. Custom slot
names are up to 16 characters, pipe excluded. **EDID files are 128 or 256 bytes.**

**So the non-PLUS can advertise 4K/UHD @30 as a factory choice, with no import needed.**

### 4.2 DXP 88 HD 4K PLUS — a file-based model, no resolution table

68-2939-01 Rev. R pp. 3–5 describes a different scheme. There is **no numbered resolution list** in
the manual. Instead:

- Factory EDID come from the **Extron EDID Standards Folder**, created on the unit by PCS. The user
  picks a file from that folder via PCS or SIS.
- **Default file: `EXN_HDMI_1080p60_2Ch.bin`** on every input slot.
- HDMI inputs take **2-block / 256-byte** Extron EDID files; the second block carries audio, and
  the HDMI EDID support **2-channel PCM**.
- **Assigned Output EDID:** the unit auto-saves each output's sink EDID into its own memory slot,
  overwritten whenever a new display is detected, and **any of those can be assigned directly to
  any input via PCS**. On the 88 that is 8 input store slots plus 8 output slots.
- All inputs support unique EDID emulation, HDCP, and per-input HDCP-authorization enable/disable.
- SIS: `EI` / `EE` import and export EDID tables by file.

⚠️ **On the PLUS, EDID cannot be managed from the front panel at all** — PCS or SIS only. The
manual states this explicitly. Plan for a laptop at load-in.

### 4.3 What this does and does not solve

**It does not rescue a dual-link source.** EDID advertises capability; it does not raise a link
rate. The X20's own maximum DVI link speed is 165 MHz per link (`christie-spyder-x20.md` §6),
which is why its 262.66 MHz 4K format needs two links — no EDID changes that.

**It helps the tiled plan considerably.** Holding a fixed 1080p60 EDID on the four inputs means the
X20's four outputs see a stable sink and will not renegotiate or drift when outputs are repatched
or a downstream display changes. On the PLUS this is already the default file.

---

## 5. Open items

1. ~~The full specifications PDF has never been read~~ — **partly closed 2026-08-30.** Both user
   guides are now read in full. What remains missing is the **separate specifications sheet**,
   still blocked by Extron's bot defense: vertical frequency range, maximum data rate and pixel
   clock appear in **neither user guide**, so those figures stay snippet-tier.
2. **The PLUS series' maximum pixel clock** is not in anything read. 18 Gbps is stated; the clock
   figure is not.
3. **The "4 × 4 matrix" line** against the DXP 88 name (§2) — assumed a source typo, unconfirmed.
4. ~~EDID Minder behaviour with a Spyder as source~~ — **largely closed 2026-08-30**, see §4. The
   non-PLUS carries a factory 4K/UHD @30 EDID and eight user slots; the PLUS is file-based off the
   Extron EDID Standards Folder. ⚠️ **Still open in one respect:** neither manual says whether any
   available EDID describes **tri-level sync**, which is what the X20's 4K factory format sets
   (`christie-spyder-x20.md` §5.1). Untested.
5. **Whether any dual-link-DVI → HDMI converter exists at all.** Searched, not found; a negative
   result of this kind is never final.
6. **Whether the X20 reads output-side EDID at all.** The X20's EDID Manager is an *input*-side
   tool (`christie-spyder-x20.md` §10); nothing in that library says the Spyder negotiates its
   output format from a downstream sink. If it does not, the DXP's EDID work is irrelevant on that
   link — and if it does, it decides which formats appear. **No document read on either side
   settles this.**
7. **Latency through the DXP.** Neither user guide gives a figure. The switcher reclocks outputs
   and does not scale, which suggests it is negligible — ⚠️ that is reasoning, not a spec, and
   nothing was measured.
