# Christie Spyder X20 — stereoscopic (SSO) option

The 3D option: modes, the two-canvas VI model, connector rules, and the resolution ceilings that
are far lower than the 2D ones. Base device facts are in `christie-spyder-x20.md`; the control
protocol is in `creative-coding/references/protocols/christie-spyder-external-control.md`.

**Filed separately from the main X20 document because it is a separate manual with a separate
document number**, and because almost every 2D limit changes under stereo. Reading the main
document's numbers and assuming they hold in stereo is the mistake this file exists to prevent.

## Provenance

**One source, read in full.**

- *Spyder X20 User Manual* (stereoscopic), Christie document **020-000875-01 Rev. 1 (04-2016)**,
  copyright 2015 `[Official]` — supplied by the user as a PDF, read end to end. 25 pages of
  content. **A different document from the main X20 manual (020-000916-01)** despite the identical
  title on the cover.
- **Sourcing tier: Verified [Official]** throughout. Every resolution, pixel clock, pin and menu
  path below is transcribed. Nothing recalled.
- **Web sources:** none for this document.
- **What was NOT read:** parallel stereo configurations are **explicitly out of scope of the
  source** — it says to contact Christie support. No wire test, no bench check, no stereo system
  operated. The manual's figures were read only as far as text extraction and captions allow;
  Figure 10's back-panel photograph is the basis for one connector observation, flagged in §6.
- **Version:** 04-2016, same vintage as the main manual, so also **pre-4.x**. Release notes
  4.0.0–4.0.6 (see `christie-spyder-x20.md` §12) contain a dozen stereo-specific bug fixes; none
  contradicts anything here, but several describe stereo misbehaviour that this manual does not
  mention.
- **Open contradictions with the main manual:** two, both material, both recorded in §2 rather
  than resolved.

---

## 1. The three modes

| Mode | Signal | Rate behaviour |
|---|---|---|
| **Active** | **One** video connection interleaving left- and right-eye frames alternately, plus a **separate sync signal** identifying which eye is which | Two frames make one stereo frame, so effective rate is **half** the signal's refresh. To recover full rate the signal is **doubled — 60 Hz becomes 120 Hz** |
| **Passive** | **Two** physical connections, one per eye, with **sync timings locked together** | Each connection runs a **standard rate — 50 Hz PAL or 60 Hz NTSC**. No doubling |
| **Mirage HD (SSO2)** | Active stereo content, but the **Christie Mirage HD projector does the frame doubling internally** | Source and Spyder run at **normal refresh**; the projector prevents visible flicker. Exists to dodge the bandwidth cost of true active stereo |

**The stereo sync connector is a VESA miniDIN-3:**

| Pin | Function |
|---|---|
| 1 | +5 V DC, **secured with 750 mA** |
| 2 | Ground |
| 3 | Stereo sync |

⚠️ **Terminology trap.** Parts of Vista Advanced call Mirage HD stereo **"interleaved"**. True
interleaved stereo is a **200/300-series-only mode and does not apply to X20**. On X20,
interleaved and half-frame-rate modes are configured as **Active**. The word appears in three
different dropdowns meaning different things — see §7.

---

## 2. Two canvases — and the VI arithmetic that contradicts the main manual

The X20 composites onto an internal canvas, then splits it into outputs. **In stereo, a second
canvas is used**: one holds all left-eye content, the other all right-eye.

**The load-bearing number:** the manual states that the system uses **two separate VI sections,
each with a maximum capacity of 20 million pixels**, for left/primary and right/alternate eye.
It then says explicitly: whether the VI runs 2D or stereo, **the maximum VI size remains 20 million
pixels**, which means a stereo configuration **may internally be processed at up to 40 million
pixels** — 20 M per eye.

⚠️ **This flatly contradicts the main manual (020-000916-01),** which states in its VI section:
*"When using the Stereoscopic Option VI capacity is halved."* Both documents are Rev. 1 (04-2016).
Neither is marked as superseding the other.

**Reading offered, not resolved:** the main manual's line sits in a general VI section written
around the 200/300 series, where halving may well be accurate; the SSO manual's statement is
X20-specific, more detailed, and internally consistent with its own worked example. **The SSO
manual is the better source for X20.** But this has not been measured, and a job sized on 40 M
per frame should be checked against hardware before anyone commits to it.

⚠️ **Second contradiction — frame rate.** The main manual says *"Spyders using the SSO option must
always use the higher frame rate of NTSC."* The SSO manual is more precise and different:

- **Active stereo** — the **VI rate is half the output rate.** 120 Hz active outputs → VI at NTSC
  59.94 Hz.
- **Passive and Mirage HD** — the **VI rate matches the output rate.** 50 Hz passive outputs → VI
  at PAL 50 Hz.

So "always NTSC" is wrong for passive at 50 Hz. **Setting a VI rate other than the one the mode
requires "may cause erratic operation of both the inputs and outputs of the system"** — the
manual's own words, and it does not say what erratic looks like.

**Output rate is then forced, not chosen:** stereoscopic output frame rates are **automatically
adjusted by the system based on the VI rate, regardless of what the user selects when defining
PixelSpaces.** Build an active stereo configuration at 50 Hz and the outputs come out at 100 Hz
whatever you asked for.

**Mixing 2D and 3D is supported and automatic.** Because the left/right areas are format
independent, **any number of active and passive stereo inputs can run simultaneously**, and **2D
content applied to a stereo PixelSpace is automatically copied into both eye areas.**

**When the VI runs out:** stereo can be combined with parallel widescreen or parallel discreet
configurations to add pixels across multiple X20 frames. **The manual declares parallel stereo
out of scope and says to contact Christie support** — so there is no documented procedure for it
anywhere in the library.

---

## 3. Active stereo inputs

**All active stereo connections, digital and analog alike, must be made on the DVI-I (even) input
connectors.** The sync signal goes to the **3-pin connection located above the DVI connector**.

**Active stereo DVI inputs — max pixel clock 317 MHz**

| Frame rate | Maximum resolution |
|---|---|
| 120 Hz | 1920 × 1200 · 1920 × 1080 · 2048 × 1080 · 1600 × 1200 |
| 100 Hz | 2048 × 1200 |
| 96 Hz | 2048 × 1200 |

⚠️ **Hard ceiling regardless of refresh: nothing above 2048 horizontal or 1200 vertical.**

**Active stereo analog inputs — max pixel clock 165 MHz**

| Frame rate | Maximum resolution |
|---|---|
| 100 Hz | 1280 × 1024 |
| 96 Hz | 1400 × 1050 |
| 60 Hz | 2048 × 1080 |

**Channel and layer cost:** **dual-link inputs take two input channels, and every stereoscopic
source uses two layers.** The manual's worked example: a **1920 × 1080 @ 120 Hz active stereo
input is 285 MHz**, and on input channel 2 it consumes **input channels 1 and 2**, then displays
on **any two adjacent layers**.

⚠️ **"Any two adjacent layers" does not match the main manual**, which lists dual-link-capable
layers as a fixed set — 1, 4, 7, 9, 12, 15. Whether stereo sources are genuinely freer than
dual-link sources, or whether one manual is loose, is unresolved. Recorded, not reconciled.

**Routing the sync:** both video and stereo sync can go through an upstream router under Spyder's
control. **The sync is commonly passed through the V-Sync channel of an analog routing switcher** —
the practical trick worth knowing, since nobody stocks a router with a stereo-sync channel.

---

## 4. Passive stereo inputs

- **Maximum 2048 × 1200 @ 60 Hz.**
- Signal may be **DVI, analog or HD-SDI**, provided the resolution is valid for that connector.
- Requires **two separate input modules**. Not required but conventional: put the right eye on the
  DVI input adjacent to the left.
- Can connect directly or through an upstream router.

Note the asymmetry with active: passive accepts **HD-SDI**, active does not — active is DVI-I only.

---

## 5. Active stereo outputs

**Odd output connectors (1, 3, 5 …) carry dual-link bandwidth; even connectors (2, 4, 6 …) carry
single-link only.** This is the same odd/even split as 2D, stated here with the numbers attached.

**Maximum supported output resolutions**

| | Odd — analog | Odd — digital | Even — analog | Even — digital |
|---|---|---|---|---|
| **Max pixel clock** | **165 MHz** | **317 MHz** | **165 MHz** | **165 MHz** |
| 120 Hz | N/A | 1920 × 1200 · 2048 × 1080 | N/A | N/A |
| 100 Hz | 1280 × 1024 | 2048 × 1200 | 1280 × 1024 | 1280 × 1024 |
| 96 Hz | 1400 × 1050 | 2048 × 1200 | 1400 × 1050 | 1400 × 1050 |
| 60 Hz | 1920 × 1200 · 2048 × 1080 | 2048 × 1200 | 1920 × 1200 · 2048 × 1080 | 1920 × 1200 · 2048 × 1080 |

*(The source prints "1400 x 050" in the even-analog 96 Hz cell — an obvious typo for 1400 × 1050,
corrected here and flagged.)*

**The practical consequence: 120 Hz active stereo works on odd digital outputs only.** Every other
column is N/A at 120 Hz. On an 8-output frame that is four usable active-stereo outputs, and they
are outputs 1, 3, 5 and 7.

⚠️ **Output rotation is not supported in active stereo**, with one exception: **interleaved (SSO2)
up to 1920 × 1200 @ 60 Hz.**

---

## 6. Wiring active stereo displays — the output-7 rule

**Each X20 output board has a single 3-pin DIN stereo sync connector shared by every output on
that board.** Driving multiple active stereo displays means **splitting that one signal downstream
of the frame** with an analog splitter.

⚠️ **The stereo sync refresh rate is locked to the video refresh rate of output 7 on that board.**
In a multi-board system, **the seventh output on each board controls that board's sync interval.**

This is the single most surprising fact in the document. **Output 7 must be running at the same
refresh rate as the outputs actually feeding the stereo displays**, or the sync timing will not
match the video. On a system where outputs 1 and 2 feed the projectors, output 7 still has to be
set correctly even if nothing is plugged into it.

**Feed the IR emitter from the display device, not from the X20 sync.** The manual is explicit:
this lets the stereo display **offset the sync timing to compensate for delay the display itself
adds.** Taking the emitter straight off the X20 gives up that compensation.

**Connector observation from Figure 10's back-panel photograph** — the output board carries, left
to right: **Output 7 (Dual DVI-I plus a digital BNC), Output 8 (DVI-I), the Stereo Sync 3-pin DIN,
a Control port (USB), an Op Mon Input on DVI-D, a Genlock connector, and the InfiniBand expansion
port.** ⚠️ **This is read from a figure, not from body text.**

✅ **Corroborated 2026-08-10** against a Christie product photograph of a real X20-1608 chassis —
see `christie-spyder-x20.md` §8.2. That photograph shows the same cluster right of Output 8, with
**one `Stereo Sync` 3-pin mini-DIN per output board** (confirming the shared-connector rule above)
and a **BNC labelled `Genlock`**. Two independent images, same layout. **The genlock connector is
confirmed present and is a BNC; its behaviour remains undocumented.**

The chassis photograph also confirms the odd/even output split of §5 **from the silkscreen
itself** — odd outputs are marked `Dual DVI-I`, even outputs `DVI-I`. And every **even input**
carries its own `Stereo Sync` 3-pin mini-DIN beside its `Dual DVI-I`, which is the input-side
sync connection §3 describes as "the 3-pin connection located above the DVI connector."

⚠️ **The main manual never mentions any of these connectors.** Without this document and the
chassis photograph, an engineer reading only 020-000916-01 would not know the X20 has stereo sync
or genlock connectors at all.

---

## 7. Passive stereo outputs

- **Maximum 2048 × 1200 @ 60 Hz.**
- **Any connector** may be used, provided the format is valid for it — no odd/even restriction,
  unlike active.
- **Two outputs are required**, and with universal output modules, **two separate output modules**
  must supply the two eyes.

Passive is the low-stress path: standard rates, any connector, no sync distribution, no output-7
rule. It costs twice the outputs.

---

## 8. Configuring stereo in Vista Advanced

### Building the configuration

The new-configuration GUI's frame-rate selector carries a **Mode dropdown: Normal ·
ActiveStereo · PassiveStereo · MirageHDStereo**. The mode chosen here **defines the output
configuration**; inputs are defined afterwards.

⚠️ **Stereo modes are global.** It is **not possible to create both stereo and non-stereo
PixelSpaces in one system** through the new-configuration GUI.

Set the VI rate per §2 — half the output rate for active, matching for passive and Mirage HD.

### Defining sources

The new-source property panel has a **Stereo Options** section, defaulting to **Off**. Available
selections change with the configuration mode:

| Source stereo mode | What it exposes |
|---|---|
| **Active** | A **router and input for the stereo sync signal**, routable separately from the video |
| **Passive** | A **second router input** specifying the alternate-eye video |
| **Interleaved** | **200/300 series only — not valid on X20** |

⚠️ **Auto-syncing after a stereo mode is selected reverts the stereo mode to Off.** Set the stereo
mode after the autosync, not before, or it silently disappears.

The configuration monitor **does not support stereoscopic output** — only a 2D representation of a
source appears on it.

### Input configuration, per layer

| Control | Behaviour |
|---|---|
| **Stereo Mode** | Off · Passive · Active · Interleaved. Defines the mode for the selected input |
| **Clone Offset** | ⚠️ **Previous-generation hardware only — no effect on X20** |
| **StereoInvertEyes** | In the **advanced** section of the layer properties panel only. **Swaps left and right eye on the VI.** The fix when the glasses look wrong and the cabling is right |

### Output configuration

Reached by clicking an output in the **System Patch** tab of Vista Advanced or Basic.

| Control | Behaviour |
|---|---|
| **Sync Type → "Stereo"** | ⚠️ **Previous-generation only — not valid on an X20.** The option is present in the dropdown and does not apply |
| **Mode → ActiveStereo** | Interleaves frames between the left- and right-eye areas of the VI to build an active stereo signal |
| **Mode → PassiveLeft / PassiveRight** | Forces the output to show one eye's content. **PassiveLeft is equivalent to Normal**, offered separately only for clarity |
| **Interleaved (SSO2)** | Output mode is set to **ActiveStereo**, but **refresh must be 59.94 Hz in the Advanced Menu, and output 7 must also be 59.94 Hz** |

The full observed Mode dropdown is **Normal · Scaled · OpMon · Source · PassiveLeft ·
PassiveRight · ActiveStereo**. ⚠️ **The external control protocol's `OCM` command documents only
Normal, OpMon and Scaled** — see the protocol document. Four of these seven modes have no
documented protocol equivalent.

---

## 9. Licensing

- SSO is a **license file from Christie**, purchased separately, and applies to **any new or
  existing X20**.
- **Without a valid stereo license, none of the stereoscopic functions work at all** — not
  degraded, absent.
- Per the main manual, **licences are cumulative across an expansion chain**: every frame needs it.
- **SSO is a licence, not a hardware change** — unlike HDCP, which needs a possible factory return.

---

## 10. Not yet verified — open items

1. **The 20 M-per-eye vs "VI capacity is halved" contradiction** (§2). Two Christie documents of
   the same vintage disagree. **Unmeasured. This is the highest-value bench test in this file** and
   it changes what a stereo system can be sized to do by a factor of four.
2. **"Any two adjacent layers" for stereo sources vs the main manual's fixed dual-link layer set**
   (§3). Unresolved.
3. **Parallel stereo configurations are out of scope of the source.** No procedure exists in this
   library. Christie support was the manual's own answer, and Christie support for X20 ends
   2027-01-02.
4. **What "erratic operation" means** when the VI rate does not match the mode (§2). Named as a
   consequence, never described.
5. **The genlock connector's behaviour** (§6). Now confirmed to exist and to be a BNC, on two
   independent images. Still no signal spec beyond the product page's "black burst", no menu path,
   no reference-loss behaviour, and no statement of how reference works across an expansion chain.
6. **Whether output 7 must be physically connected**, or merely configured to the right rate, for
   the stereo sync to be correct (§6). The manual says its *refresh rate* controls the sync
   interval, which implies configuration alone suffices — **that is inference, not a statement.**
7. **Mirage HD input-side requirements** — SSO2 is described as an output-side and projector-side
   arrangement; what the source must deliver is not stated separately from active stereo.
8. **No stereo latency figure**, and no statement of whether stereo adds a frame over 2D.
9. **Passive stereo over HD-SDI** is permitted by one sentence (§4) and never elaborated — no rate
   table, no level A/B statement, no mention of how two SDI feeds stay locked.
10. **Whether the 4.x software changed any of this.** All nine 4.x releases have now been read and
    carry roughly a dozen stereo bug fixes — alternate-eye transparency, command-key recall of the
    alternate eye, stereo sources overwriting layers, left/right correlation across reboots,
    **4.0.7's "issue with Dual link resources"** (undetailed, on the mechanism every stereo source
    depends on), and 4.1.0's analog/SDI-goes-black-next-to-a-stereo-input fix. **No stereo manual
    revision was ever issued**, so none of it is reflected in the text above. See
    `christie-spyder-x20.md` §12.4.

---

## Verification status

| Section | Tier |
|---|---|
| §1 modes and sync pinout | **Verified [Official]** |
| §2 two-canvas VI and rate rules | **Verified [Official]** for both documents' claims; **the contradiction is recorded, not resolved.** The preference for the SSO manual on X20 is **reasoning**, flagged as such |
| §3 active inputs | **Verified [Official]**; the layer-set conflict with the main manual flagged in place |
| §4 passive inputs | **Verified [Official]** |
| §5 active outputs | **Verified [Official]**; one obvious source typo corrected and flagged |
| §6 display wiring and output 7 | **Verified [Official]** from body text; the back-panel connector list is **Observed** — from this manual's Figure 10 and corroborated against a separate Christie chassis photograph, both marked in place |
| §7 passive outputs | **Verified [Official]** |
| §8 software configuration | **Verified [Official]**, 3.x-era |
| §9 licensing | **Verified [Official]** |

**Nothing in this document has been tested on hardware.** No stereo system was operated, no
resolution was confirmed, no sync was scoped.
