# Pixel Clock & Link Bandwidth — Working Method

**Purpose:** decide whether an arbitrary raster fits down HDMI, DisplayPort or SDI *before* building it, and know which number to quote when it doesn't.

**Confidence tiers, applied strictly:**

- **Computed** — arithmetic performed this session from the stated timing model. Reproducible from the formulas below. Not a manufacturer figure.
- **Verified** — interface ceilings taken from a source read this session. Where the source is a device manual it is named.
- **Unverified** — flagged in place. Nothing in this document is filled from memory.

The distinction matters because the *active* pixel rate and the *link* rate differ by the blanking overhead, and vendors quote whichever flatters them.

---

## 1. The three rates, kept separate

| Rate | What it is | Formula |
|---|---|---|
| Active information rate | Payload only, ignoring blanking | `H_active × V_active × rate × bpc × 3` |
| Pixel clock | Rate the link actually clocks at, blanking included | `H_total × V_total × rate` |
| Link/wire rate | Pixel clock after the interface's line-coding overhead | interface-specific, below |

Quoting the first when the question is "will it fit" understates the requirement, typically by 5–20% depending on blanking. Always compute the pixel clock.

---

## 2. CVT-RB v1 timing model

This is the model to use when the raster is one *you* are defining — which is the case for any custom format on a scaler. The Analog Way VIO 4K's custom-format engine builds on **CVT 1.1** and DMT 1.0 (see `analog-way-vio-4k.md` §8), so CVT-RB is the right assumption there.

Constants:

- `RB_H_BLANK = 160` pixels (fixed)
- `RB_MIN_V_BLANK = 460` µs
- Pixel clock quantised **down** to the nearest 0.25 MHz

Procedure:

```
h_period_est = (1e6 / refresh_rate - 460) / V_active     # µs per line
vbi_lines    = floor(460 / h_period_est) + 1
V_total      = V_active + vbi_lines
H_total      = H_active + 160
pixel_clock  = H_total × V_total × refresh_rate          # then floor to 0.25 MHz
```

If your source device uses different blanking (GTF, DMT, or a vendor's own), the clock moves and every margin below moves with it. Recompute rather than reusing these numbers.

---

## 3. Interface ceilings

| Interface | Ceiling | Coding | Usable payload |
|---|---|---|---|
| HDMI 2.0 | 600 MHz TMDS character rate; 18 Gbit/s wire | 8b/10b | wire × 0.8 |
| DisplayPort 1.2 (HBR2) | 4 lanes × 5.4 Gbit/s = 21.6 Gbit/s wire | 8b/10b | **17.28 Gbit/s** |
| 3G-SDI | 2.97 Gbit/s | — | 1080p60 4:2:2 10-bit |
| 6G-SDI | 5.94 Gbit/s | — | 2160p30 4:2:2 10-bit |
| 12G-SDI | 11.88 Gbit/s | — | 2160p60 4:2:2 10-bit |

HDMI derived quantities, for 4:4:4:

```
TMDS_char_rate = pixel_clock × bpc / 8
HDMI_wire_rate = TMDS_char_rate × 30      # 10 bits/char × 3 data lanes
```

The **character rate** is the binding constraint on HDMI 2.0, not the wire rate — deep colour inflates the character rate above the pixel clock, and 600 MHz is the wall.

`[Unverified]` The HDMI 2.0 and DP 1.2 ceilings above were not read from a specification document this session; they are the figures the VIO 4K manual's own card descriptions are consistent with (18 Gbps HDMI 2.0, 21.6 Gbps DP 1.2 — §15.2.2, §15.2.3 `[Official]`). Treat the 600 MHz character-rate limit specifically as needing an HDMI Forum source before it is quoted to a client.

**SDI carries only standard rasters.** No custom-format path exists on any SDI link at any rate. For a non-standard active area over SDI, place it as an AOI island inside a legal raster.

---

## 4. Worked example — 5120×2880 @ 30 Hz, 4:4:4

CVT-RB v1 gives `H_total = 5280`, `V_total = 2921`, pixel clock `462.6864 MHz → 462.50 MHz` after quantisation. **[Computed]**

Active information rate: 5120 × 2880 × 30 = **442.4 Mpixel/s**

| bpc | Active-only | Payload @ 462.50 MHz | HDMI TMDS char rate | HDMI wire rate | DP 1.2 utilisation |
|---|---|---|---|---|---|
| 8 | 10.62 Gbit/s | 11.10 Gbit/s | 462.50 MHz | 13.88 Gbit/s | 64.2% |
| 10 | 13.27 Gbit/s | 13.88 Gbit/s | 578.12 MHz | 17.34 Gbit/s | 80.3% |
| 12 | 15.93 Gbit/s | 16.65 Gbit/s | 693.75 MHz | 20.81 Gbit/s | 96.4% |

Verdicts:

- **HDMI 2.0** — 8-bit comfortable; 10-bit passes but consumes 96% of the 600 MHz character-rate budget; 12-bit **fails**, 694 MHz exceeds the ceiling outright.
- **DP 1.2** — 8-bit at 64%, 10-bit at 80%, 12-bit at 96% with no headroom for unusual blanking. DP is the better carrier here.
- **SDI** — no path at any link rate.

### The useful comparison

`3840×2160 @ 60` under the same model needs `H_total = 4000`, `V_total = 2222`, pixel clock **533.25 MHz** — *higher* than 5120×2880@30's 462.50 MHz. **[Computed]**

So a device documented to 4K@60 4:4:4 is already clocking faster than this wider raster demands. Pixel clock alone does not rule 5120×2880@30 out. What might rule it out is an independent gate on H active: the VIO's documented format list tops out at 4096 pixels wide. Build it in CVT mode and let the **Check** step answer — it returns `PIXEL FREQUENCY TOO HIGH` / `LINE FREQUENCY TOO HIGH` / `TOTAL PIXEL PER LINE IS TOO LOW` before allowing a save.

---

## 5. Reference table — common rasters, CVT-RB v1 **[Computed]**

| Raster | H_total | V_total | Pixel clock | 8bpc payload | 10bpc payload | 12bpc payload |
|---|---|---|---|---|---|---|
| 5120×2880 @30 | 5280 | 2921 | 462.50 MHz | 11.10 Gbit/s | 13.88 Gbit/s | 16.65 Gbit/s |
| 3840×2160 @60 | 4000 | 2222 | 533.25 MHz | 12.80 Gbit/s | 16.00 Gbit/s | 19.20 Gbit/s |
| 3840×2160 @30 | 4000 | 2191 | 262.75 MHz | 6.31 Gbit/s | 7.88 Gbit/s | 9.46 Gbit/s |
| 4096×2160 @30 | 4256 | 2191 | 279.50 MHz | 6.71 Gbit/s | 8.38 Gbit/s | 10.06 Gbit/s |

DP 1.2 utilisation against 17.28 Gbit/s payload:

| Raster | 8bpc | 10bpc | 12bpc |
|---|---|---|---|
| 5120×2880 @30 | 64.2% | 80.3% | 96.4% |
| 3840×2160 @60 | 74.1% | 92.6% | **111.1% — fails** |
| 3840×2160 @30 | 36.5% | 45.6% | 54.7% |
| 4096×2160 @30 | 38.8% | 48.5% | 58.2% |

Note that 4K60 4:4:4 **12-bit** does not fit DP 1.2 — consistent with the VIO manual listing DP 1.2 at UHD/4K@60 4:4:4 **10-bit**, and HDMI 2.0 at 4K@60 4:4:4 **8-bit**. The arithmetic and the manual agree, which is a decent check on the model.

---

## 6. Reproducing these numbers

```python
import math

def cvt_rb(h_active, v_active, rate):
    h_total = h_active + 160
    h_period_est = (1e6 / rate - 460) / v_active
    vbi = math.floor(460 / h_period_est) + 1
    v_total = v_active + vbi
    clk = h_total * v_total * rate
    return h_total, v_total, math.floor(clk / 250_000) * 250_000

def budget(h, v, rate, bpc):
    ht, vt, clk = cvt_rb(h, v, rate)
    payload = clk * bpc * 3 / 1e9          # Gbit/s, 4:4:4
    tmds    = clk * bpc / 8 / 1e6          # MHz, HDMI character rate
    return dict(h_total=ht, v_total=vt, clock_mhz=clk/1e6,
                payload_gbps=payload, tmds_mhz=tmds,
                hdmi_wire_gbps=tmds * 30 / 1000,
                dp12_util_pct=payload / 17.28 * 100)
```

---

## 7. Rules of thumb

- Compute the **pixel clock**, not the active rate. The gap is where surprises live.
- On HDMI, watch the **character rate**, not the wire rate — deep colour inflates it 1.25× (10-bit) or 1.5× (12-bit) above the pixel clock.
- Reduced blanking is worth roughly 15–20% of link budget over standard blanking on large rasters. If a raster is marginal, forcing RB is the first move.
- 4:2:2 halves chroma and drops the per-pixel bit count by a third versus 4:4:4 — often the difference between fitting and not, and usually invisible on an LED wall.
- A device's stated "maximum resolution" is a resolution/rate pair, not a clock budget. Two different rasters at the same clock may not both be accepted; gates on H active exist.
- When a custom format is involved, the validator is the answer. Ten minutes with the format editor beats an hour of arithmetic.

---

## 8. Verification status

| Claim area | Tier | Source |
|---|---|---|
| Three-rates distinction; active vs clock vs wire (§1) | **Method** | Definitional, not a sourced figure |
| CVT-RB v1 constants — 160 px H blank, 460 µs min V blank, 0.25 MHz quantisation (§2) | **Unverified** | CVT 1.1 standard **not read**. Model reproduces the VIO manual's stated card ceilings correctly (see cross-check below), which is corroboration, not verification |
| All pixel clocks, payloads, TMDS rates, utilisation figures (§4, §5) | **Computed** | Arithmetic in session from §2's model; reproducible from §6's code. Not manufacturer figures |
| HDMI 2.0 = 600 MHz TMDS character rate | **Unverified** | No HDMI Forum document read. **Do not quote to a client** |
| HDMI 2.0 = 18 Gbit/s wire | **Verified** | *VIO 4K User Manual* §15.2.2 `[Official]` |
| DisplayPort 1.2 = 21.6 Gbit/s wire | **Verified** | *VIO 4K User Manual* §15.2.3 `[Official]` |
| DP 1.2 = 4 lanes × 5.4 Gbit/s HBR2 | **Unverified** | No VESA document read; consistent with the 21.6 Gbit/s total above |
| 8b/10b coding on both HDMI 2.0 and DP 1.2 | **Unverified** | No specification read |
| SDI tier rates — 2.97 / 5.94 / 11.88 Gbit/s | **Unverified** | SMPTE ST 424 / 2081 / 2082 **not read**. Format ceilings per tier are corroborated by the VIO manual's plug tables `[Official]` |
| SDI carries only standard rasters | **Verified** | *VIO 4K User Manual* §11.1 — custom formats defined as computer formats `[Official]` |
| DP 1.2 caps at 4K60 4:4:4 10-bit; HDMI 2.0 at 4K60 4:4:4 8-bit | **Verified** | *VIO 4K User Manual* §15.2.2, §15.2.3 `[Official]` |

### Cross-check on the model

The computed figures independently reproduce two ceilings the VIO manual states directly: 3840×2160@60 4:4:4 **12-bit** comes out at 111.1% of DP 1.2's payload (fails), matching the manual's stated 10-bit ceiling for DP 1.2; and the same raster at 10-bit needs a 666.6 MHz HDMI character rate, exceeding 600 MHz, matching the manual's stated 8-bit ceiling for HDMI 2.0. Two independent agreements between the arithmetic and an `[Official]` source.

This raises confidence in the model. It does **not** promote the underlying constants to Verified — agreement at two points is not proof of the constants, and the CVT and interface specifications remain unread.

### Not yet verified — open items

1. **Obtain CVT 1.1 (VESA)** — would promote the reduced-blanking constants from Unverified to Verified. Everything computed here rests on them.
2. **Obtain the HDMI 2.0 specification** — needed for the 600 MHz character-rate limit, currently the single most load-bearing unsourced number in this document.
3. **Obtain VESA DisplayPort 1.2** — for lane count, HBR2 rate, and the 8b/10b overhead assumption.
4. **Obtain SMPTE ST 424 / ST 2081 / ST 2082** — for the SDI tier rates.
5. **Add DP 1.4 (HBR3) and DSC** — cannot be attempted until a VESA source is in hand; nothing about DP 1.4 should be asserted from memory.
6. **Add 4:2:2 and 4:2:0 rows** to §5's comparison tables. Straightforward arithmetic once the 4:4:4 rows are trusted, and often the difference between fitting and not.
7. **Confirm HDMI 2.1 FRL behaviour** is out of scope here — this document covers TMDS-era links only, and should say so once an FRL source exists to contrast against.
