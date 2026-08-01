# Blackmagic ATEM — SuperSource

Parameter reference for the ATEM SuperSource compositor: what the control set is,
what the values mean, how the saved-state XML encodes them, and — importantly —
which parts of the parameter space the vendor documentation simply does not
describe.

## Provenance

**Sourcing, by section:**

| Sections | Tier | Source |
|---|---|---|
| §1–§3, §5–§6 | `[Official]` | *ATEM Constellation Switchers Manual* pp. 68–70 and *Blackmagic Switchers SDK* §6, read directly; plus a switcher's own saved-state export |
| §4 unit space and all pixel conversion | **Derived** | Arithmetic performed in session from one verified preset. Internally consistent; **never checked against a switcher** |
| Preset 1–3 shapes | `[Lead]` | Read off a low-resolution manual thumbnail |

**Not read:** no ATEM firmware release notes, no per-model verification beyond the manual's own table, no bench test of any parameter end-stop.

**Open contradictions and gaps, left in place:**
- Which switcher models expose which of the two border models is **unresolved** (§ border discussion).
- **A verified negative worth keeping:** the SDK declares every SuperSource parameter as a bare double — no units, minima, maxima or defaults — and the manual gives no end-stops either. The absence is confirmed, not an oversight in this document.

---

## Sources read this session

| Source | Tag | What was read |
|---|---|---|
| *ATEM Constellation Switchers Manual*, Blackmagic Design (user-supplied PDF, 2289 pp., document date 2026-06-16) | `[Official]` | "Using SuperSource" pp. 68–70 in full, including the two palette screenshots; the SuperSource entry in the output-source table |
| *Blackmagic Switchers SDK*, Blackmagic Design (user-supplied PDF, 795 pp., document date 2025-01-22) | `[Official]` | Section 6 — SuperSource, pp. 378–420: data types, complete interface and method inventory, method signatures |
| A saved ATEM switcher state XML, exported from the user's Constellation | `[Official]` | The `<SuperSources>` element in full |

Nothing in this document comes from memory. Where a value is arithmetic rather
than a read figure it is tagged **Derived** and the derivation is shown.

---

## 1. What SuperSource is

SuperSource arranges multiple sources on one output at the same time — the
manual's example is four presenters superimposed over a background. The whole
processor **appears on the switcher as a single video input**, so it is put to
air by selecting it on the program bus like any other source. `[Official]`

**Per-model count** `[Official]`

| Model | SuperSources |
|---|---|
| ATEM 2 M/E Constellation | 1 |
| ATEM 4 M/E Constellation | 2 |
| ATEM Constellation 8K, HD and Ultra HD modes | 2 |
| ATEM Constellation 8K, 8K mode | 1 |

**Boxes.** Four per SuperSource. The palette labels them Box 1–4; the XML
indexes them 0–3.

**Box sources.** Ordinary inputs, plus M/E 2 program or preview. On ATEM 4 M/E
and Constellation 8K in HD or Ultra HD mode, M/E 3 and M/E 4 program or preview
are also selectable. `[Official]`

**Layer order — Derived, one inference from one sentence.** The manual describes
the copy function as producing boxes that "appear directly behind the master
box," with the worked example copying Box 1 to Box 2. That implies ascending box
number runs front to back, i.e. Box 1 is the front layer and Box 4 the rear.
The manual never states the stacking order directly. Treat as strong but
unconfirmed until observed on a switcher.

---

## 2. The palette in ATEM Software Control

Three tabs: **Presets**, **Art**, **Copy**. `[Official]`, read off the p. 69–70
screenshots.

**Presets tab**
- Four preset layout thumbnails. Selecting one arranges the boxes automatically.
- **Box Control** below: a *Control* selector choosing the box, an **Enable box**
  checkbox, a **Source** dropdown, **Position** X and Y, **Size**, a **Crop**
  checkbox with Top / Bottom / Left / Right, and a reset control to the right of
  the box control that resets position, size, crop, or everything.

**Art tab**
- **Fill Source** dropdown.
- **Key Source** dropdown — greyed unless art is in the foreground.
- **Place In**: Background / Foreground radio pair.
- **Pre Multiplied Key** checkbox, **Clip**, **Gain**, **Invert key** — the whole
  group greyed while art is in the background.
- **Border** group: an enable dot, **Style** (showing *No Bevel*, greyed in the
  screenshot), a **Color** swatch, **Hue** / **Sat** / **Lum**, **Outer Width**,
  **Inner Width**.

**Copy tab** — copy the selected box's settings to another box, or to all. The
copy takes the master's source as well as its geometry.

**Border availability.** Borders are disabled while art is in the foreground,
because nothing would be visible behind the art. ATEM Constellation 8K presents
SuperSource without borders in 8K mode. `[Official]`

**ATEM Advanced Panel equivalents** `[Official]`
- A dedicated **SuperSource** button, then the system-control arrow buttons to
  page through settings.
- Menu page 2: preset knob, then the soft **apply preset** button.
- Menu page 3: size and position on the soft knobs — but the joystick is faster.
  Push for X and Y together; twist clockwise to grow the box, anticlockwise to
  shrink it.
- Menu page 5: fill source knob, plus foreground/background soft buttons. The
  following page carries **pre multi key on**.
- Final page: copy-from and copy-to knobs, including copy-to-all.

---

## 3. Values actually read

Every figure below was read directly off a manual screenshot or out of the saved
XML. **Verified [Official].**

| Parameter | Value | Where |
|---|---|---|
| Quad preset, Box 1 — Position X | `-8.00` | Manual p. 69 palette screenshot |
| Quad preset, Box 1 — Position Y | `4.80` | Manual p. 69 palette screenshot |
| Quad preset, Box 1 — Size | `0.50` | Manual p. 69 palette screenshot |
| Crop Top / Bottom / Left / Right at reset | `0.00` | Manual p. 69; XML |
| Border Hue | `0.0°` | Manual p. 70; XML `hue="0"` |
| Border Saturation | `0.0%` | Manual p. 70; XML `saturation="0"` |
| Border Luminance | `100.0%` | Manual p. 70; XML `luma="1"` |
| Border Outer Width | `0.40` | Manual p. 70; XML `widthOutH`, `widthOutV` |
| Border Inner Width | `0.40` | Manual p. 70; XML `widthInL/R/T/B` |
| Art Clip | `50.0%` | Manual p. 70; XML `artClip="50"` |
| Art Gain | `70.0%` | Manual p. 70; XML `artGain="70"` |

Note the border figures agree across two independent sources — a manual
screenshot and a switcher's own saved state — which is as good as this library
gets without a measurement.

**Preset geometry.** Only the quad preset yields numbers, and only for Box 1.
The other three thumbnails carry no values. From the thumbnails the four presets
appear to be: a large box with a picture-in-picture; a large box with two stacked
beside it; two side by side; and the 2×2 quad. **Shapes are Lead-grade reading of
a low-resolution figure; no coordinates exist for presets 1–3.**

---

## 4. Unit space and pixel conversion — Derived

**Neither document states the coordinate space.** This section is arithmetic on
top of the one verified triple in §3. It is internally consistent and it predicts
the quad layout correctly, but it has not been checked against a switcher.

**Derivation.** A box at Size `0.50` is half the raster. Placed on the left half,
its centre sits a quarter of the raster width left of frame centre. That
position is `-8.00`, so a quarter of the raster width = 8 units, and the full
raster is **32 units wide**. At 16:9 the height is **18 units**.

Scale is therefore `W/32` horizontally and `H/18` vertically:

| Output raster | px / unit H | px / unit V |
|---|---|---|
| 1280 × 720 | 40 | 40 |
| 1920 × 1080 | 60 | 60 |
| 3840 × 2160 | 120 | 120 |
| 7680 × 4320 | 240 | 240 |
| 2048 × 1080 (DCI 2K) | 64 | 60 |
| 4096 × 2160 (DCI 4K) | 128 | 120 |

Square units only at 16:9. The 60 px/unit figure at 1080p is exact on both axes,
which is a reasonable circumstantial argument that 32 × 18 is the intended space
rather than a coincidence of this one preset.

**Conversions**, with `k` = px per unit, `y` positive upward:

```
box width  px = W × size
box height px = H × size
centre X   px = W/2 + x·k
centre Y   px = H/2 − y·k
top-left X px = W/2 + x·k − (W × size)/2
top-left Y px = H/2 − y·k − (H × size)/2
```

**Control resolution.** At 1080p one 0.01 step = 0.6 px, so not every settable
value lands on a whole pixel. Multiples of 1/60 ≈ 0.0167 do: 0.05 = 3 px,
0.10 = 6 px, 1.00 = 60 px. The 0.40 default border width = 24 px at 1080p.

**A consequence worth knowing before you use the quad preset.** Y `4.80` puts
the top row's upper edge 0.30 units above the top of the raster — 18 px at 1080p,
36 px at UHD. The bottom row overhangs by the same amount. The columns meet
exactly at frame centre horizontally, but the rows leave a 0.60-unit gap
vertically — 36 px at 1080p. `4.50` would sit the rows flush and closed. Whether
the overflow is deliberate design or an artefact is **unknown**.

---

## 5. SDK interface map

Section 6 of the *Switchers SDK*, `[Official]`. Method inventory is complete as
listed in the SDK contents and interface tables.

| Interface | Scope | Purpose |
|---|---|---|
| `IBMDSwitcherInputSuperSource` | The SuperSource input | Art fill/cut, art option, pre-multiplied, clip, gain, inverse, `SupportsBorder`, iterator factory |
| `IBMDSwitcherSuperSourceBoxIterator` | — | Enumerates the boxes |
| `IBMDSwitcherSuperSourceBox` | One box | Enabled, input source, position X/Y, size, cropped flag, four crop values, `ResetCrop`, input availability mask |
| `IBMDSwitcherSuperSourceBorder` | Whole SuperSource | Bevelled border model — see below |
| `IBMDSwitcherSuperSourceBoxBorder` | One box | Flat per-box border model — see below |
| `IBMDSwitcherInputSuperSourceCallback`, `…BoxCallback`, `…BorderCallback`, `…BoxBorderCallback` | — | Change notifications |

### 5.1 There are two different border models

This is the structural fact worth carrying forward, and it is not obvious from
the palette.

| | `IBMDSwitcherSuperSourceBorder` | `IBMDSwitcherSuperSourceBoxBorder` |
|---|---|---|
| Applies to | The whole SuperSource | One box |
| Enable | `BorderEnabled` | `BorderEnabled` |
| Width, outer | `WidthOut` (single) | `WidthOutHorizontal`, `WidthOutVertical` |
| Width, inner | `WidthIn` (single) | `WidthInLeft`, `WidthInRight`, `WidthInTop`, `WidthInBottom` |
| Bevel | `Bevel`, `BevelSoftness`, `BevelPosition` | **none** |
| Softness | `SoftnessOut`, `SoftnessIn` | **none** |
| Light source | `LightSourceDirection`, `LightSourceAltitude` | **none** |
| Colour | `Hue`, `Saturation`, `Luma` | `Hue`, `Saturation`, `Luma` |

`IBMDSwitcherInputSuperSource::SupportsBorder` exists as a capability query,
so border support is not universal across the family — consistent with the
manual's note that Constellation 8K drops borders in 8K mode.

The saved XML from the Constellation uses the **per-box, flat** model: six
independent widths, no bevel or softness attributes. The palette's greyed-out
*Style: No Bevel* control is presumably the entry point to the other model on
switchers that have it. **Which switchers expose which model is unresolved.**

### 5.2 Art methods and the naming drift

The same parameter carries three different names depending on where you are
standing. Worth a table, because it bites when moving between the SDK, the
palette and a saved file.

| SDK | Palette | XML attribute |
|---|---|---|
| `InputFill` | Fill Source | `artFillInput` |
| `InputCut` | Key Source | `artKeyInput` |
| `ArtOption` | Place In | `artOption` |
| `PreMultiplied` | Pre Multiplied Key | `artPreMultiplied` |
| `Clip` | Clip | `artClip` |
| `Gain` | Gain | `artGain` |
| `Inverse` | Invert key | `artInvertKey` |

`BMDSwitcherSuperSourceArtOption` has exactly two values:
`bmdSwitcherSuperSourceArtOptionBackground` and
`…Foreground`.

### 5.3 The SDK documents no ranges

This is the most useful negative result here, so it is stated plainly rather than
left implied. Every SuperSource getter and setter in Section 6 is a bare `double`
or `boolean`. Positions, size, crop values, border widths, hue, saturation, luma,
clip and gain are all declared without units, minima, maxima, defaults, or any
statement of what the numbers mean. The manual likewise gives no end-stops.

**Anyone needing the limits has to read them off a switcher.** Do not let a
plausible-looking range enter this library from anywhere else.

---

## 6. Saved-state XML schema

From the user's exported switcher state. Structure and attribute names are
`[Official]` — this is the device's own output.

```xml
<SuperSources>
    <SuperSource index="0" artFillInput="3010" artKeyInput="3011"
                 artOption="Background" artPreMultiplied="False"
                 artClip="50" artGain="70" artInvertKey="False">
        <Boxes>
            <Box index="0" enabled="False" inputSource="0"
                 xPosition="0" yPosition="0" size="1"
                 cropped="True" cropTop="0" cropBottom="0"
                 cropLeft="0" cropRight="0">
                <border enabled="False"
                        widthOutH="0.4" widthOutV="0.4"
                        widthInL="0.4" widthInR="0.4"
                        widthInT="0.4" widthInB="0.4"
                        hue="0" saturation="0" luma="1"/>
            </Box>
            <!-- Box index 1..3 -->
        </Boxes>
    </SuperSource>
</SuperSources>
```

**Encoding notes**

- Booleans are the strings `True` / `False`, capitalised.
- `artClip` and `artGain` are on a 0–100 scale, matching the palette's percent display.
- Border `saturation` and `luma` are on a **0–1** scale while the palette displays
  the same values as 0–100%. `luma="1"` is the 100.0% shown in the screenshot.
  The two scales do not match and the file does not say so.
- `hue` is in degrees.
- `artOption` carries the literal strings `Background` / `Foreground`.
- The border element is written **per box** even though the palette exposes a
  single border control described as applying to all boxes. A writer that only
  updates Box 0's border will produce a file the palette cannot represent.
- `cropped="True"` persists independently of the crop values, so a box can be
  flagged cropped with all four values at zero.

**Source ID scheme** observed in the same file: `0` black, `1000` colour bars,
`2001`/`2002` colour generators, `1`–`n` external inputs, `3010`/`3020` media
player fills with `3011`/`3021` their keys, `6000` SuperSource 1, `7001`/`7002`
clean feeds, `10010`/`10011` and `10020`/`10021` M/E program and preview.
Key-mask outputs occupy the `4xxx` and `5xxx` ranges.

---

## 7. Verification status

| Section | Status |
|---|---|
| §1 model counts, box count, box sources, on-air behaviour | **Verified [Official]** — manual |
| §1 layer order | **Derived** — one inference from the copy-function description |
| §2 palette and panel control inventory | **Verified [Official]** — manual text and screenshots |
| §3 numeric values | **Verified [Official]** — read off screenshots, border and art values corroborated by the switcher's own XML |
| §3 preset shapes 1–3 | **Lead** — read off a low-resolution thumbnail, no coordinates exist |
| §4 unit space and pixel conversion | **Derived** — arithmetic from one verified triple; internally consistent, never checked against a switcher |
| §5 interface and method inventory, art option enum, two border models | **Verified [Official]** — SDK |
| §5.3 absence of documented ranges | **Verified [Official]** — confirmed by reading the method definitions, not by failing to find them |
| §6 XML schema and encodings | **Verified [Official]** — device output |

---

## 8. Not yet verified — open items

1. **Slider end-stops.** X, Y, Size, crop, and border widths all have unknown
   minima and maxima. Nothing in the manual or SDK states them. Read them off a
   switcher by driving each control to its stop.
2. **Whether crop shares the 32 × 18 unit space, and whether it scales with box
   size.** Test: set a box to Size `1.00`, Crop Left `8.00`. If exactly a quarter
   of the picture disappears, crop is in frame units. Then repeat at Size `0.50`
   and see whether the same value still removes a quarter of the *source* or a
   quarter of the *screen area*.
3. **The clip/gain transfer function** for non-pre-multiplied art. The manual
   defers to its keying section; no curve is given anywhere.
4. **Which switchers expose `IBMDSwitcherSuperSourceBorder` (bevelled) versus
   `IBMDSwitcherSuperSourceBoxBorder` (flat)**, and whether the Constellation's
   greyed *Style* control ever becomes active.
5. **Layer order confirmation** — put four overlapping boxes up and look.
6. **Whether the quad preset's 0.30-unit top and bottom overflow is intentional.**
7. **Coordinates for presets 1–3.** Apply each preset on a switcher and read the
   box values back.
8. **ATEM Software Control / ATEM Setup documentation** was not supplied and may
   state ranges the switcher manual omits.

## 9. Wanted documents

- ATEM Software Control operator documentation, if it exists separately from the
  switcher manual.
- The ATEM Ethernet protocol description for the `SSBP` / `SSrc` command family —
  a protocol-level document would very likely settle both the unit space and the
  value ranges, since wire encodings have to be bounded.
