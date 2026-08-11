# Christie / Vista Systems Spyder — X20, and the 200/300 series it replaced

Device and signal facts. The ASCII external control protocol is **not** here — it lives in
`creative-coding/references/protocols/christie-spyder-external-control.md`.

## Provenance

**Five source groups. Four read in full, one read as a rendered product page.**

1. *Spyder X20 User Manual*, Christie document **020-000916-01 Rev. 1 (04-2016)** `[Official]` —
   supplied by the user as a 180-page PDF (a manualslib.com capture of the Christie PDF, page
   furniture included). Text extracted and read end to end. **Confirmed 2026-08-10 to be the
   current and final X20 user manual**: Christie's own product page still posts this same document
   number, re-dated 2021-06-28, at
   `https://www.christiedigital.com/globalassets/020-000916-01-lit-man--usr-spyder-x20.pdf`. There
   is no later revision.
2. *Christie Spyder X20 v4.1.0 Software Release Notes*, **020-000917-08 Rev. 2 (1-2017)**
   `[Official]` — supplied by the user as a PDF, read in full. One page. **4.1.0 is the final X20
   software release**; nothing is listed after it on Christie's download page.
3. **The 4.0.x release notes, fetched from Christie 2026-08-10 and read in full** `[Official]` —
   **020-000917-02** (v4.0.0), **-04** (v4.0.3), **-06** (v4.0.5) and **-07** (v4.0.6). These are
   **cumulative**: the 4.0.6 document contains every entry back to 4.0.0, including the 4.0.1,
   4.0.2 and 4.0.4 releases and every intervening beta. ⚠️ **The 4.0.7 notes (020-000917-01) could
   not be retrieved** — the fetch was refused for lack of a search-result provenance chain, not
   because the file is missing; it is listed and linked on Christie's download page. **4.0.7's own
   delta is the one unread gap in the 4.x history.**
4. *Spyder X20 User Manual* (stereoscopic), **020-000875-01 Rev. 1 (04-2016)** `[Official]` —
   supplied by the user, read in full. **Filed as its own document**,
   `christie-spyder-x20-stereoscopic.md`, and cited from here rather than restated.
5. **Christie Spyder X20 product page** `[Official]` —
   `https://www.christiedigital.com/products/end-of-support/image-processors/christie-spyder-x20/`,
   fetched 2026-08-10. The page carries no last-edited date and no revision identifier; its
   copyright line reads 2026 and its most recent dated asset is 2025-02-03. **Christie's own site,
   so `[Official]`, but a marketing spec table rather than an engineering document** — where it
   disagrees with the manual, §13 records both rather than picking one.

- **Sourcing tier:** §1–§13 are **Verified [Official]** except where a line is marked **Derived**
  or **Inferred** in place. Each section names which source it came from. No figure in this
  document was recalled; every number appears in one of the five.
- **What was NOT read:** the manual's figures and screenshots carry values that text extraction
  does not capture — back-panel photographs (Figure 51), the front-panel status display, the patch
  utility screenshots, and the HDCP topology diagrams. Nothing in this document comes from a
  figure. The manual also defers front-panel operation to a separate "software / operator's manual
  for the X20", which was not supplied and has not been read. **Also not read:** the
  **4.0.7 release notes** (020-000917-01), and the separate X20 **operator's manual** covering
  front-panel operation.
- **Version gap, now nearly closed:** the manual **predates 4.x** — its own troubleshooting
  section names 3.5.5 as current "at the time of this writing" — and **Christie never issued a
  manual revision for the 4.x line.** §12 now carries the whole 4.x history from the release
  notes, so the delta between the manual and the final software is known **except for 4.0.7's own
  entries.** Anything in §9–§11 not contradicted by §12 remains 3.x-era-as-documented.
- ⚠️ **Release notes are one-line summaries, not documentation.** They name features and commands
  without arguments, ranges or behaviour. A command named in §12 is **confirmed to exist and
  nothing more** — never write one from the name alone.
- **Open contradictions and gaps:** conflicts between the manual and the spec page are in §13; everything still unanswered is in §14. Both left in place, not resolved.

---

## 1. Product families and model numbering

| Family | Chassis | I/O modules | Notes |
|---|---|---|---|
| Spyder 200 series | 2 RU | 4 | `[Official]` |
| Spyder 300 series | 3 RU | 8 | `[Official]` |
| Spyder X20 | modular, smallest chassis is three slots; 4 RU chassis specified | factory-populated, slots need not all be filled | second-generation line |

**200 series sample configurations** — 240 (4 in / 0 out), 204 (0 / 4), 222, 213, 231.
**300 series sample configurations** — 380 (8 / 0), 308 (0 / 8), 344, 353, 362.
Both all-input and all-output models (240, 204, 380, 308) are **available only with the control
expansion option**; fixed-control versions of those are not offered.

Reading the number: leading digit is the series, remaining digits are input count then output
count.

**X20 model names.** The manual names exactly two — **X20 1608** and **X20 0808** — and never
states their I/O counts directly.

- **Input counts are Derived, and firmly:** a layer is one physical input card, 1:1. The dual-link
  table (§5) runs to layer 8 on the 0808 and to layer 16 on the 1608. So 8 and 16 inputs.
- **Output counts are Verified** as of 2026-08-10, but from the **product page, not the manual** —
  the spec table gives **8 outputs** and describes how they trade against resolution (§13). The
  manual itself never states an X20 output count.
- The product page's own input breakdown for the **X20-0808** is **4 inputs carrying composite,
  S-Video, component analog, SDI, HD-SDI and 3G-SDI, plus 4 carrying progressive DVI and
  progressive RGBHV** — which is the odd/even connector split of §4 stated as a count, and
  independently confirms 8 inputs.

X20 chassis is populated at the factory with whatever mix of input and output channels is ordered,
and can be upgraded later by adding cards to empty slots.

**Control paths** (all series): the PC-based Spyder Control Suite (Vista Advanced / Vista Basic),
the Montage II hardware control surface, and third-party control systems such as AMX or Crestron
over the external protocol.

---

## 2. The VI, and how much of it there is

**VI (Visual Image / Virtual Image)** — the internal high-resolution canvas the whole processor
renders into. It is partitioned into **PixelSpaces**, each a clipping rectangle that defines one
screen area. Outputs are then windowed onto the VI. This is why Spyder is resolution-independent:
the audience-facing raster is a region of the VI, not the format of any one source or display.

**X20 VI capacity — 20,000,000 pixels at every listed frame rate:** NTSC, PAL, 23.98, 24, 25,
29.97, 30, 48, 50, 60. Frame rate does **not** trade against VI size on X20. That is the headline
difference from the older families.

**200/300 series VI capacity by frame rate** (system-introduction table):

| Frame rate (Hz) | Pixels available |
|---|---|
| 23.97 | 16,500,000 |
| 25 | 15,800,000 |
| 29.97 | 13,200,000 |
| 48 | 8,200,000 |
| 50 | 7,900,000 |
| 59.94 | 6,600,000 |

⚠️ **The manual contradicts itself.** Its expansion chapter gives a second, coarser table for the
same 200/300 hardware — 59.94 → 6.6 M, 29.97 → 13 M, 50 → 8 M, 25 → 16 M, 24 → 16.5 M. Both
tables are in the same document. Unresolved; use the finer table above and flag the discrepancy if
a job depends on it.

Other VI rules:

- **Physical input and output module count has no effect on VI size.** Capacity is a frame
  property, not an I/O property.
- ⚠️ **Stereoscopic (SSO): this manual says "VI capacity is halved" and that an SSO system must
  always run the higher (NTSC) frame rate. The dedicated SSO manual says something different and
  more specific — 20 M pixels per eye, up to 40 M total, and a VI rate that depends on the stereo
  mode rather than always being NTSC.** Both are Rev. 1 (04-2016). See
  `christie-spyder-x20-stereoscopic.md` §2, which records the conflict in full. **Do not size a
  stereo job from the line in this manual without reading that section.**
- **Budgeting formula.** The manual states it as "V pixels (highest) × H pixels" and gives a worked
  example: two outputs at 1400 × 1050 plus one at 1920 × 1080 plus a 640 × 480 operator monitor =
  5,788,800 of 6.6 M. **Derived** from that arithmetic: the rule is *(tallest output height) ×
  (sum of all output widths)* — 1080 × (1400 + 1400 + 1920 + 640) = 5,788,800. The example checks
  out exactly. **The operator monitor counts against the VI.**
- **X20 maximum VI height is 2400 px.** Taller needs multiple X20 frames in parallel.
- **Above 1860 px of VI height the X20 restricts which layers accept stills**, and bitmap borders
  and shapes are limited to **layers 3, 6, 11 and 14**. The manual marks this as applying to *all
  versions* — the one limit here explicitly not tied to a software release.

---

## 3. Layers, priority, backgrounds

- **Layer = one input displayed on the VI**, live video or still. **1:1 with physical input
  cards** — layer count is input count. Also called a window.
- **Priority is fixed in hardware.** Layer 1 is always below layer 2, and so on. There is no
  arbitrary Z-reorder; you get the order the hardware gives you.
- **Two background layers** exist per system, holding user stills (JPG, BMP, TIFF, PNG, GIF and
  similar), loaded per PixelSpace, drawn behind every layer.
- **In the external protocol, layer IDs start at 2** — 0 and 1 are reserved for those two
  backgrounds. `RLC` returns the logical layer count *including* them, so subtract two.
- **KeyFrame** is the term for a layer's visual attributes: size, position, border, shadow, clone,
  crop, pan/zoom, aspect-ratio offset.
- **Treatment** is a saved set of KeyFrame attributes, recallable to any layer.

---

## 4. Connectors and signal support

### X20 inputs — alternate by parity, one active connector per input

| Input | Connectors |
|---|---|
| **Odd** (1, 3, 5 …) | Analog on 3- or 4-wire BNC · Composite / S-Video (shares the BNC used for the composite analog sync signal) · SDI / HD-SDI / **3G-SDI** on a dedicated BNC |
| **Even** (2, 4, 6 …) | DVI-I (analog and digital on one connector) · Stereo sync input on 3-pin DIN |

Only one connector / signal type can be selected per input at a time.

### X20 outputs

Every output channel carries **DVI-I** and **SDI / HD-SDI / 3G-SDI**. Multiple output connectors
can be enabled at once *provided the configured output format is valid for each* — the manual's
example: SXGA 1280 × 1024 is valid on DVI and analog, invalid on SDI, composite and S-Video.

### 200/300 series — signal facts that do not carry over cleanly

- **Pixel clock ceilings: analog 165 MHz, digital 330 MHz.**
- **Only odd inputs have de-interlacers.** SDI and HD-SDI are available on odd inputs only.
- **Interlaced sources cannot be used on the DVI connector.**
- Accepted formats listed: 24p, NTSC, PAL, SECAM; analog RGB (sync-on-green, composite or separate
  sync); analog YUV; SDI; HD-SDI; DVI single-link; DVI dual-link; stereo sync.
- Output-side format list adds DVI twin link and pairs of single/dual link.
- Simultaneous output connector examples: DVI + analog for non-interlaced computer formats,
  SDI + analog at 480i/575i, HD-SDI + analog at 1080i.
- **200C / 300C option** adds composite (BNC) and S-Video (SVHS) on every input and output.

⚠️ The manual gives **no X20-specific accepted-format table and no SDI rate table** — 3G-SDI is
named on the connector list and nowhere else, with no bitrate and no cable length. **On SDI level:
the 4.0.4 release notes record "Added Spyder X20 support for SDI Level B on inputs"** (§12), which
establishes that level B input support exists and dates it, but states nothing about outputs and
gives no format table. Before 4.0.4, level B inputs were not supported.

**Genlock:** the main manual never mentions a reference input. **A genlock connector is visible on
the X20 output board** in the SSO manual's back-panel figure, alongside the stereo sync DIN, the
Op Mon input and the InfiniBand port — see `christie-spyder-x20-stereoscopic.md` §6. The product
page states the capability as **free-run or vertically referenced to NTSC/PAL black burst** (§13).
Connector confirmed to exist; **its type and behaviour are documented nowhere.**

---

## 5. Dual link on X20

- Certain X20 inputs and outputs support **2560 × 1600 @ 60 Hz, or up to 330 MHz**.
- **All X20 DVI inputs can take dual-link**, but a dual-link source **disables the preceding analog
  input connector** — it consumes that input's resources. Dual-link on input 2 kills input 1.
- **Dual-link-capable layers: 1, 4, 7, 9, 12, 15.** Each consumes the next adjacent layer as well;
  the simulator shows this as a `1/2` style label in the layer's top-left corner.

| Model | Simultaneous dual-link sources | Layer pairs |
|---|---|---|
| X20 0808 | 3 | 1/2, 4/5, 7/8 |
| X20 1608 | 6 | 1/2, 4/5, 7/8, 9/10, 12/13, 15/16 |

- **Outputs: dual-link on odd-numbered outputs** (1, 3, 5, 7).
- **HDCP mode forces every output to single link, odd outputs included** (§6).
- The product page states the same constraint from the raster side: **any resolution above
  2048 × 1200 consumes two input channels** (§13). Same mechanism, stated as a rule about the
  picture rather than about the connector.

---

## 6. HDCP — licensed option, system-wide

**X20 supports HDCP 1.4** and interoperates with 1.0 through 1.4 devices. **X20 is an HDCP
repeater**: it decrypts on the input, processes, and re-encrypts on the output.

Implementation: cipher and control logic in FPGA; **every input and every output DVI connection
has its own unique Device Key Set**, encrypted into PROMs at production. The **cipher engine runs
at 200 MHz to service the maximum DVI link speed of 165 MHz per link** — for dual-link sources,
each link authenticates and encrypts independently.

**Two modes, system-wide, mutually exclusive. There is no mixed-mode configuration.**

| Mode | Behaviour |
|---|---|
| HDCP | HDCP-enabled sources can send protected content. **All analog and SDI *outputs* shut down — DVI only.** All *inputs*, including non-HDCP interfaces, keep working normally |
| Non-HDCP | Normal operation. HDCP content will not be displayed |

Set it at **Server → Frame Configuration** in Vista Advanced; it requires a soft restart of the
frame. Once a downstream device is connected, X20 begins authentication and **only HDCP-capable
displays will function** — downstream traffic is encrypted regardless of whether the incoming
content was.

**Repeater limits: 127 downstream devices, 7 levels.** Each repeater is one level. X20 supports
the maximum of both, but the upstream transmitter may not, and X20 has no control over a
transmitter that refuses to send because the tree is too deep or too wide.

**Status in the UI:** each output's handshake result shows as an LED icon in the system patch
utility — **green = handshake complete, output transmitting encrypted video; amber/red = handshake
failed, output not transmitting**. **There is no input-side handshake status** — the manual is
explicit that none is available. License status appears in the License Administrator under Help.

**Show-floor failure modes named in the manual:**

- HDCP authentication uses the **I²C / DDC channel** in the DVI connection. Reliability depends on
  cable length and quality — a link that passes video can still fail HDCP.
- **DVI distribution amps, routers and splitters** that don't manage HDCP or pass DDC reliably will
  break the chain.
- Decrypted content may never leave the X20 unencrypted, so there is no "one clean output" escape.

**Retrofit:** adding HDCP to a fielded X20 needs hardware, firmware and licence changes together.
A licence can be bought for any fielded system, but **a factory return may be required**.

---

## 7. Expansion

Requires the Expansion Module option on every frame involved. Legacy frames use the **200X / 300X**
expansion option and an **InfiniBand cable, Vista P/N CAB-60670**.

**Licensed options are cumulative across a chain — every frame must carry the licence or the
option is disabled completely.** This is the expansion gotcha most likely to bite at load-in.

**Signal flow is one-directional.** Inputs add their pixels to the VI and pass downstream through
the frames to the outputs and out the expansion port. **Signal never flows upstream, so upstream
outputs cannot carry downstream layers.** Useful side effect: an upstream frame's outputs give a
**clean feed** without the downstream frames' keys or layers — the manual suggests it for IMAG or
downstream keying.

| Type | Purpose | VI |
|---|---|---|
| **Serial** | Increase total I/O count | One VI across the whole chain, still capped at the VI pixel limit |
| **Parallel — Discreet** | Multiple independent screens | Multiple VIs, one per Frame Group. Layers in one Frame Group **cannot** reach outputs in another |
| **Parallel — Seamless** | One continuous pixel space larger than a single VI | Pixel Renewal Groups each own a portion of the space |

**First upstream frame is Master; the rest are Slaves.** Every frame is a Master until it joins an
Expansion Group. Frames report their role on the front-panel LED (Frame 0, Slave Frame 1 …).

**Restricted vs unrestricted layers (seamless expansion only):**

- **Restricted** — the default. Placeable anywhere inside its **home Renewal Group**, but not
  outside it and **not on the overlap between groups**.
- **Unrestricted** — placeable anywhere in the PixelSpace regardless of group boundaries. Created
  by making **Master script elements** in a command key or script. **Consumes one hardware layer
  in every Renewal Group**, so it is expensive.
- Mixing is the normal answer: unrestricted only for the layers that actually cross a boundary.

**Operator monitors:** if preview is enabled, **each frame group needs an additional universal
output dedicated to the operator monitor**, and its pixels count against that group's VI.

---

## 8. Physical, power, front panel

| | X20 4 RU | Spyder 3 RU | Spyder 2 RU |
|---|---|---|---|
| W × H × D | 17.3 × 7 × 21.9 in (43.9 × 17.78 × 55.6 cm) | 17.3 × 5.3 × 22.1 in (43.9 × 13.3 × 56.1 cm) | 17.3 × 3.5 × 22.1 in (43.9 × 8.9 × 56.1 cm) |
| Weight | ~70 lb | ~33 lb | ~25 lb |
| Power | 100–240 V AC, **1000 W max**, internal auto-resetting fuse | 100–240 V AC, 375 W max, 5 A slow-blow | 100–240 V AC, 225 W max, 3 A slow-blow |

**Standby power < 20 W** on 200, 300 and X20 alike.

⚠️ **The product page disagrees with the manual on X20 power and weight** — 900 W and 9.0 A at
100 VAC against the manual's 1000 W max, and 59 lb / 70.5 lb against the manual's ~70 lb. Both
figures recorded in §13; neither has been resolved.

**Soft power scheme.** The front Standby switch starts a power-up or power-down cycle; the rear
hard switch should only be used when the unit is already in standby. On X20, **holding the front
power button for 13–15 seconds forces power off, and may cause permanent configuration data
loss**. **Never pull AC before the unit reaches standby** — the manual warns of hard drive
corruption on both families.

**X20 back panel exposes the internal PC's connections** — keyboard, mouse, HD15 monitor, USB,
mic in, speaker out. **Factory use only**, not intended for user peripherals.

**Front panel:** legacy frames have a status/error display showing version, frame, I/O
configuration and IP address. X20 has an LCD plus switch-button interface for control and status;
**its actual operation is deferred to a separate operator's manual that is not in hand.** The X20's
IP address is readable from that front-panel display.

**110 V / 220 V conversion** (legacy frames): pull the fuse holder from the AC inlet and swap
between a jumper-plus-one-fuse arrangement for 110 V and two fuses for 220 V — 2 × 3 A for 3 RU or
2 × 2 A for 2 RU at 220 V; 1 × 5 A for 3 RU or 1 × 3 A for 2 RU at 110 V. Units ship set for their
destination with a sticker over the AC inlet.

---

## 9. Vista Advanced client — install, permissions, network

- Ships as part of the **Spyder Control Suite**; updates from the Christie site.
- Requires **Microsoft .NET Framework 4 or later**, and a **Windows Experience Index of 4.0 or
  greater**.
- **The data path is hard-coded to `C:\SPYDER`.** Any machine running Advanced needs a writable
  C: drive, with **Full Control** on `C:\Spyder` and on the installation path for every user.
- **A maintenance-contract licence is required to update to software versions at or above 3.0.**

**Network practice, per the manual:**

- Put Spyder and all clients on a **closed network** — Spyder communicates with clients by
  **broadcast**, which is heavy on an already-busy network.
- Avoid multiple IP addresses on one NIC; avoid a second wired or wireless connection.
- **Complex routers and managed switches are not recommended** — misconfiguration causes
  communication drops.
- **Adapter priority fix**, for a laptop on wireless internet plus wired Spyder: in IPv4 Advanced
  settings, uncheck automatic metric and set the **wired LAN adapter metric to 2** and the
  **wireless to 3** (Windows reserves 1 for loopback). Advanced binds to the lowest-metric adapter.
  This replaces the older advice to disable the wireless adapter outright.
- **Remote Desktop into the X20**: connect to the frame's IP, log in as **username `Cricket`,
  password `Cricket`** — the manual's documented default. Treat as a documented default
  credential, not a secret.

**Simulator / DirectX history:** before Advanced 2009 version 3.5.0 the display simulator used
Managed DirectX, deprecated by Microsoft in 2009, and produced lock-ups or a blank simulator on
some PCs. **Rebuilt on WPF at 3.5.0.** Affected: Advanced 2005 all versions, and Advanced 2009
3.4.3 and lower.

---

## 10. Feature set as documented (3.x-era Advanced)

**Sources.** A source is an input configuration (connector type, format, levels) plus either a
router input or a direct-to-layer patch. Optional **Preferred Treatment** (auto-applied on
selection) and **Preferred Layer** (falls back to the first available layer if busy). Autosync
detects source type and properties.

**Key modes** (set in the input configuration property panel):

| Mode | Behaviour |
|---|---|
| **Luma key** | Clips pixels below a user-defined darkness threshold |
| **Color key** | Clips pixels within a threshold of a specified colour |
| **Linear key** | Two sources — a **cut** and a **fill**. The **luminance (green) channel of the cut** is a real-time mask over the fill. Uses **two adjacent layers, and the cut must be on the lower of the two** |

**KeyFrame geometry.** Position is **relative**, measured from the layer centre against the
containing PixelSpace: **left and top = −1.0, right and bottom = +1.0, centre = 0.0**. **Width is
in pixels; height is not settable** — it is derived from the source aspect ratio. Duration is in
**frames**, used by scripting for KeyFrame-to-KeyFrame transitions.

**Border:** RGB colour, thickness, horizontal and vertical offset (a *lighting* bevel offset, not
a position), inside softness, outside softness.

**Shadow:** horizontal and vertical offset (positionable through 360°), size, softness, and
transparency **0 = black through 255 = transparent**.

**Clone:** a free duplicate of a layer sharing every KeyFrame property **except horizontal
position**. Horizontal offset only — **a clone cannot be offset vertically**. Two modes: **Mirror**
(clone moves opposite to the original) and **Offset** (clone holds a fixed horizontal distance).
Built for widescreen repeats of one source on both sides of a screen.

Also documented: cropping on every edge, pan and zoom, aspect-ratio offset, standard and custom
shapes, per-layer test patterns, relative and absolute modes, scripts, cue triggers, function keys.

**EDID Manager** — `Server → EDID Manager`. Records EDID from a display, edits it, programs it into
a Spyder input, and verifies an input against known data. **Does not work offline; needs a live
connection to a frame.**

**License Manager** — `Help → License Manager`. Generates `License.req` from a hardware snapshot
plus contact details, for one frame or every frame on the network; the file is **emailed manually
to `techsupport-az@christiedigital.com`**. Installing a licence **restarts the frame**. Licence
files must not be renamed or have their extension changed or they become invalid.

**Licensed options named:** maintenance contract, **Stereoscopic (SSO)** (any mix of 2D and active
or passive 3D inputs on one screen, with passive or active stereo output), HDCP, expansion.

**User diagnostics / Real-Time Protection** — monitors hardware state while running and raises
alerts before failures become visible.

**Machine control and PlayItems.** Decks connect through **SourceMaster** ports — **eight
checkboxes, one per port**, on each PlayItem. Fields: preroll (frames to ramp up; the deck cues to
in-point minus preroll), rollout, in point, out point, clip name for clip-based devices, frame
rate. Multiple decks in one PlayItem get cue, stop and play simultaneously for a sync roll, but
**clock skew will drift them over a long roll — timecode chase or genlock between decks is
required**. Scripts can trigger PlayItems and PlayItems can trigger scripts by timecode; **each
script has exactly one clock source port**. Troubleshooting note: timecode not refreshing is
usually **SourceMaster's port switched to RS-232 when it must be RS-422**.

**Still Server — X20 only.** An external Windows PC connected to the X20 by **Ethernet and DVI**.
The X20 sends the image file if needed plus a display command; the PC shows it; **the X20 captures
that DVI signal into memory at the OpMon input connector** and routes it. Dramatically faster still
loading than the internal path.

| | Spec |
|---|---|
| Minimum | Pentium 4 2.5 GHz, 512 MB RAM, Windows XP SP3 |
| Recommended | 2048 MB RAM, Windows Vista or 7 (**Windows 8 and above not supported**), 1000 Mbit NIC, DVI output supporting 2048 × 1200 |

Configure at `Server → Still Server Configuration`: enable checkbox, still-server IP, and **Delay
Before Capture, default 300 ms** — the wait between "display this" and the capture. Lowering it
speeds loads; too low makes capture unreliable, and the floor varies by PC. **Do not run the still
server on the Advanced client PC.**

---

## 11. Output configuration

Three output modes:

| Mode | What it does |
|---|---|
| **Normal** | Window onto the VI at a given horizontal and vertical start position |
| **OpMon** | Operator monitor focused on a program PixelSpace (supplying a preview ID resolves to its program PixelSpace) |
| **Scaled** | Scales a whole program PixelSpace to the output |

- **Rotation in 90° increments only** (0, 90, 180, 270), and **not supported on all output module
  types**.
- **Blending is per edge, Left or Right only** — enable, blend width in pixels, mode **Bezier /
  Gamma / Velocity**, and two curve parameters in the range 0.000–1.000. No top/bottom edge blend
  is exposed in the external protocol.
- **Output configuration must be explicitly saved or it is lost on restart** (the `OCS` command;
  the software equivalent is the frame's own save).
- **DX4 quad-output modules** exist: they take a channel ID 0–3 on still load/clear, and **DX4
  outputs do not support individual freeze** — output freeze is universal-output only.
- Output format setting via the protocol supports **VESA formats only**, with an optional
  reduced-blanking flag, and snaps to the nearest supported refresh if an unsupported one is asked
  for.

---

## 12. Software — the whole 4.x line

**Sources: release notes 020-000917-02 (4.0.0), -04 (4.0.3), -06 (4.0.5), -07 (4.0.6) and -08
(4.1.0), all read in full.** The 4.0.x notes are **cumulative** — the 4.0.6 document carries every
entry back to 4.0.0 — so four documents cover eight releases. ⚠️ **4.0.7's own entries are the one
gap** (see Provenance).

**4.1.0 is the last X20 software release.** The user manual was never revised for any of the 4.x
line, which is why §9–§11 are labelled 3.x-era.

### 12.1 Release timeline

| Version | Date | Headline |
|---|---|---|
| 4.0.0 | 2012-03-08 | Repackaging of beta 0.53.3. Baseline for the 4.x line |
| 4.0.1 | 2012-11-19 | **200/300 VI height steppings were being wrongly enforced on X20** — fixed |
| 4.0.2 | 2013-06-17 | Repackaging of beta 0.55.9 |
| 4.0.3 | 2014-02-04 | SDI-and-HDCP fix; Chinese Windows scaling fix |
| 4.0.4 | 2014-05-13 | **SDI Level B on X20 inputs.** Frame naming in Connection Manager. EDID wizard first-try failure fixed |
| 4.0.5 | 2015-03-05 | **VDCP external control. SMPTE 352M insertion on 3G outputs.** True Mix. Static-IP fallback when DHCP fails |
| 4.0.6 | 2015-08-25 | HDCP enhancement; **`ASC` command gains optional ±X**; several router protocols |
| 4.0.7 | 2016-06-30 | ⚠️ **Notes not read** |
| 4.1.0 | 2017-01-05 | Backup/Recovery; two 4K output factory formats; Imagine Platinum router |

### 12.2 Signal and hardware changes

These are the entries that change what the box can do, as distinct from what the client looks like.

| Release | Change |
|---|---|
| 4.0.4 | **SDI Level B support added on X20 inputs.** Level B was not supported before this |
| 4.0.5 | **SMPTE 352M payload identifier insertion added for 3G output modes.** Downstream gear that demands a valid 352M packet on 3G will not behave correctly on older software |
| 4.0.5 | **IP address falls back to static when DHCP fails** — the frame no longer strands itself on a network with no DHCP server |
| 4.1.0 | **Output factory formats 3840 × 2160 @ 29.97 Hz and 3840 × 1080 @ 59.94 Hz** added. The manual's output chapter predates both |
| beta 0.57.2 | Firmware fix for **banding on gradients over SDI** |
| beta 0.56.6 | Fix for **SDI input edges showing a blue/brown/black line** along one or more edges |
| beta 0.55.0 | Output firmware fix for **artifacts on odd-numbered outputs** |
| beta 0.55.1 | Output board firmware updated **to support newer production power supplies** — relevant to mixed-vintage frames |
| beta 0.54.1 | **A 24 Hz or 30 Hz VI was not being configured correctly and actually ran at NTSC.** Any pre-4.0.1 system claiming a 24/30 Hz VI was lying |

### 12.3 HDCP work across the line

HDCP got attention in almost every release, which is itself the useful signal: **on older software
HDCP on X20 was unreliable.**

- beta 0.54.10 — fix for **sync dropout on certain X20 outputs in HDCP mode** (experimental)
- beta 0.55.5 — **HDCP output enumeration separated by frame boundaries**, to cut the number of
  downstream devices reported to inputs. Directly relevant to the 127-device repeater limit in §6
- 4.0.3 — "issue with SDI and HDCP" fixed
- beta 0.58.1 — "increased robustness of HDCP on outputs"
- 4.0.6 — a further "HDCP enhancement feature"

**If an HDCP chain misbehaves on an X20, the software version is a first-order suspect.**

### 12.4 Stereo fixes — read alongside the stereoscopic document

None of these appear in the SSO manual, which was never revised:

- Alternate-eye **transparency changes not propagating** from the primary eye (beta 0.56.5)
- **Active stereo sources recalled to program by command key** not recalling the alternate eye
  correctly (beta 0.54.3)
- **Dropping a stereo source onto a PixelSpace overwriting layers** (beta 0.56.2)
- Switching between **stereoscopic inputs and 2D content** giving incorrect results (beta 0.56.4)
- **Left-eye/right-eye correlation lost across reboots** on parallel stereo frames (beta 0.55.2) —
  ⚠️ the fix **"requires genlock and a 50/59.94/60 Hz VI configuration"**, one of the very few
  places genlock is mentioned at all
- **Passive stereo input through an upstream router** not patching properly (beta 0.55.9)
- **Blend overlay not rotating correctly** when an output was rotated in active stereo (beta 0.55.0)
- Input configuration for **stereo and dual-link inputs not updating on the alternate layer during
  autosync** (beta 0.56.0)
- 4.1.0 — **analog/SDI input not outputting video when the next input has been used as stereo**

That last one is the same input-pairing mechanism dual link uses (§5). **Black on an input
adjacent to a stereo input is a known, fixed bug, not a cabling fault.**

### 12.5 Expansion and parallel systems

- beta 0.54.5 — **support added for different VI heights between multiple X20 frames connected via
  USB expansion.** ⚠️ **"USB expansion"** — the manual describes expansion only over InfiniBand
  (§7). Whether USB is a second expansion path, a diagnostic link, or loose wording in the notes
  is **unresolved**; note that beta 0.54.9 also refers to attaching to a **USB connection index**
  when opening low-level diagnostics on a parallel system
- beta 0.54.5 / 0.54.9 — several **linear key** failures on expanded and parallel frames, including
  **cut and fill arriving on different input boards of an X20 1608** (beta 0.54.7). Confirms the
  1608 has more than one input board and that board boundaries matter for linear key
- beta 0.54.8 — X20 preview showing **only the first 4 preview layers per input board**

### 12.6 Router protocols added across 4.x

The manual names no router list, so this is the only inventory that exists. Added over the line:
**Atlona · Gefen 3 · Gefen IV (IP) · Gefen III IP · AJA Kumo (IP) · Utah Scientific RCP-3 · Utah
Scientific 100 IP · DTrovision PureLink PM-32X (IP and serial) · Dtrovision III IP · Pesa Cougar
P1N · Pesa PN1 over IP · Barco Matrix Pro II · Imagine Platinum.** Fixes also touched Lightware,
Extron IP, Sierra, RGB Linx, Quartz/Magnum and NVision Compact.

### 12.7 The 4.1.0 upgrade procedure

1. Start Vista Advanced 4.1.0 on the client PC.
2. Go to **Server → Connection Manager**.
3. Choose **Select Server** and enter the frame's IP address. If the frame is on any other version,
   **the Connect tab becomes Update**. Selecting Update starts the process.
4. Wait — **approximately 10–15 minutes.**
5. When the front LCD prompts **Power Cycle Now**, toggle the front panel button to shut down,
   **pull the power cords from the power supplies, wait 10–15 seconds, and reinsert them.**
6. Toggle the front panel button to restart. **The front LCD reads v4.1.0** when complete.

The client drives the frame update; there is no separate firmware file. **The release notes'
standing advice for any upgrade is to back up system data first** — and note that the notes'
phrasing predates the Backup and Recovery feature 4.1.0 itself added.

⚠️ **Every 4.x release carries its own FPGA version set** (XP, IP, FRC, CP, VIC, OP, plus input and
output CPLD and power). They change between releases — IP went 5.23.6.16 → 6.3.7.2 at 4.0.4, OP
moved four times. **A frame and a client on mismatched versions are a real failure mode**, and the
front panel is where the running version is read.

---

## 13. Manufacturer spec table — what it adds, and where it conflicts

**Source: the Christie Spyder X20 product page, fetched 2026-08-10.** `[Official]` — Christie's own
site — but a **marketing spec table, not an engineering document**, and it carries no revision or
last-edited date. Treat it as authoritative for figures the manual simply lacks, and as *one of
two* readings wherever it disagrees.

**Figures the manual does not contain at all:**

| | Spec-page figure |
|---|---|
| **Output count and how it trades** | **8 outputs at under 2048 × 1200**, or **4 at 2560 × 1600**, or a **combination of 4 dual-link and 4 single-link**. Four outputs are dual-link capable — consistent with the manual's "odd outputs only" |
| **Latency** | **Low delay, under 1.5 interlaced frames.** The manual gives no latency figure anywhere |
| **Output synchronisation** | **Free-run, or vertically referenced to NTSC/PAL black burst.** The manual never mentions genlock or a reference input |
| **Output pixel clock** | **Analog up to 165 MHz, DVI up to 265 MHz** — ⚠️ **note the asymmetry: the input side goes to 330 MHz, the output side stops at 265 MHz.** The manual states 330 MHz for inputs and outputs together and does not distinguish |
| **Raster ceilings** | Horizontal to 2560 and vertical to 2160 within 330 MHz, in and out; output resolution described as "including 4K" |
| **Channel cost of a big raster** | **Any resolution above 2048 × 1200 uses two input channels** — the resolution-side statement of the dual-link pairing in §5 |
| **Scan rates** | Up to 120 Hz in and out, bounded by the pixel-clock ceiling |
| **Bit depth** | **10-bit analog inputs and outputs** |
| **De-interlacing** | Motion-adaptive, SD and HD; **3:2 and 2:2 pull-down detection** |
| **Layer count** | 16 video layers of unrestricted blending, windowing, mixing and scaling — marketing phrasing, consistent with the 1608's 16 input cards |
| **Keying** | A luminance keyer and a chroma keyer on **every** input, plus alpha-channel bitmaps on every input |
| **Still store** | Read/write — load or capture BMP, PNG, TIFF, JPG on any input |
| **Control** | **RS-232 in/out** is the only control interface listed. ⚠️ The page does not mention the Ethernet/UDP path the manual documents in full — an omission, not a contradiction |
| **Environment** | 40–95 °F (5–35 °C), 20–80% non-condensing |
| **Heat** | Under 750 BTU/hr |
| **Regulatory** | UL/CSA/IEC 60950 3rd Ed., FCC Class A, CE, CCC, RoHS, WEEE |
| **Warranty** | 2 years parts and labour |
| **Part numbers** | 120-052108-XX, 120-064101-XX |

**Direct conflicts with the manual — both readings kept:**

| Item | Manual (020-000916-01) | Product page | Status |
|---|---|---|---|
| Power | **1000 W max**, internal auto-resetting fuse | **900 W**, 9.0 A @ 100 VAC | ⚠️ Unresolved. The manual's figure is a maximum; the page's may be typical. Neither says which |
| Weight | ~70 lb | **59 lb (27 kg)** and **70.5 lb (32 kg)** listed together, with 70.5 lb repeated as the shipping weight | ⚠️ Unresolved. Reads as unit vs shipping weight with the field mislabelled, but the page does not say so |
| Output DVI pixel clock | 330 MHz, stated for the dual-link capability generally | **265 MHz on outputs**, 330 MHz on inputs | ⚠️ Unresolved and load-bearing for output raster planning |

**Lifecycle:** **end of production 2024-01-02.** Christie states support for three years from that
date — **until 2027-01-02** — while parts last, or for the applicable warranty period if longer.

---

## 14. Not yet verified — open items

**Closed on 2026-08-10** — kept visible so a future session sees what settled them:

| Was open | Settled by |
|---|---|
| ~~4.x behaviour uncovered~~ | Release notes for 4.0.0–4.0.6 and 4.1.0 read in full (§12). **Only 4.0.7's own delta remains** |
| ~~X20 output counts inferred from the model name~~ | Product page — 8 outputs with the resolution trade (§13) |
| ~~No latency figure~~ | Product page — under 1.5 interlaced frames (§13) |
| ~~No genlock or reference input described~~ | Connector confirmed on the output board in the SSO manual's figure; capability stated on the product page. **Type and behaviour still undocumented** — now item 4 below |
| ~~No SDI level A/B statement~~ | Partly. **4.0.4 added SDI Level B on inputs** (§12.2). Output-side level and a rate table are still absent |
| ~~SSO manual not in hand~~ | Supplied and read; filed as `christie-spyder-x20-stereoscopic.md` |

**Still open:**

1. **The 4.0.7 release notes (020-000917-01) have not been read.** Everything else in the 4.x line
   is covered. This is a single short public PDF and the last piece of the version history.
2. **The stereo VI contradiction** — this manual says SSO halves VI capacity; the SSO manual says
   20 M per eye, 40 M total. Recorded in full in the stereoscopic document §2. **Unmeasured, and
   it changes stereo system sizing by a factor of four.**
3. **Three unresolved manual-vs-product-page conflicts** — power, weight, and output DVI pixel
   clock (§13). The 265 vs 330 MHz output clock is the one that affects what raster an output
   carries.
4. **The genlock connector's type and behaviour.** Confirmed present on the output board; no
   signal spec, no menu path, no statement of what happens on reference loss, and no explanation
   of how reference interacts with an expansion chain. The only functional mention anywhere is a
   4.x stereo bug fix that "requires genlock and a 50/59.94/60 Hz VI configuration."
5. **"USB expansion"** (§12.5) — the notes twice refer to X20 frames connected by USB, while the
   manual describes expansion only over InfiniBand. Second path, diagnostic link, or loose
   wording? Unresolved.
6. **Two different VI capacity tables for the 200/300 series** in the same manual (§2).
7. **No SDI rate detail for X20** — no bitrate, no cable length, no output-side level statement,
   no format table. 3G-SDI is named as SMPTE 424M and nothing more.
8. **What the two 4.1.0 4K output formats cost the VI budget.** 3840 × 2160 @ 29.97 is 8.3 Mpx of
   20 Mpx on one output. Whether two fit alongside anything useful is arithmetic nobody has run
   against a real configuration.
9. **Whether the 1860 px still/shape restriction survives 4.x** — the manual says "all versions",
   written before 4.x existed, and no release note mentions it.
10. **What the Backup and Recovery feature (4.1.0) actually covers** — "system configuration
    files" and nothing else. No file location, no restore procedure.
11. **X20 front-panel operation** is deferred to a separate operator's manual not in hand — which
    matters more now, since §12 shows the front panel is where the running version is read and
    where the upgrade prompts appear.
12. **X20 accepted input format list** — the only format list in the manual sits under the 200/300
    section and may not be current for X20.
13. **Montage II control surface** is named as a control option and never described.
14. **DX4 output module** appears only in protocol arguments — no specification, no channel
    behaviour, no statement of which chassis take it.
15. **The FPGA version sets per release** (§12.7) are recorded in the notes but nothing explains
    what mismatches cause, or how to read the running set off a frame.

---

## Verification status

| Section | Source and tier |
|---|---|
| §1 families, model numbers | Manual — **Verified [Official]**. X20 input counts **Derived** from the dual-link layer table; **output counts Verified from the product page** |
| §2 VI capacity and budgeting | Manual — **Verified [Official]**; budgeting formula restated is **Derived** from the manual's own worked example and checks exactly. Two contradictions flagged in place, one internal and one against the SSO manual |
| §3 layers, priority, backgrounds | Manual — **Verified [Official]** |
| §4 connectors and formats | Manual — **Verified [Official]**; SDI Level B from the 4.0.4 notes; genlock from the SSO manual's figure and the product page, marked in place |
| §5 dual link | Manual — **Verified [Official]**; the ">2048 × 1200 costs two input channels" restatement is from the product page |
| §6 HDCP | Manual — **Verified [Official]**; §12.3 adds the software history |
| §7 expansion | Manual — **Verified [Official]**; the USB-expansion question from the notes is flagged, not resolved |
| §8 physical and power | Manual — **Verified [Official]**, with the product page's conflicting power and weight figures flagged |
| §9 client install and network | Manual — **Verified [Official]**, 3.x era |
| §10 feature set | Manual — **Verified [Official]**, 3.x era |
| §11 output configuration | Manual — **Verified [Official]** |
| §12 the 4.x line | **Release notes — Verified [Official]**, four documents read in full. ⚠️ **Entries are one-line summaries**: a feature named here is confirmed to exist and nothing more. The grouping into 12.2–12.6 is this document's editorial arrangement, not Christie's |
| §13 spec table | **Product page — [Official]** but marketing-grade, undated. Conflicts recorded rather than resolved |

**Nothing in this document is from memory.** Where every source is silent, §14 says so rather than
filling the gap.

**Companion documents:**
- `christie-spyder-x20-stereoscopic.md` — the SSO option in full
- `creative-coding/references/protocols/christie-spyder-external-control.md` — the ASCII command set
