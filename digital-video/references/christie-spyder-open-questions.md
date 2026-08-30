# Christie Spyder — open questions and unverified theories

**A test plan, not a reference.** Everything here is either undocumented by Christie, contradicted
between Christie's own documents, or reasoning that has never been checked against hardware. The
three Spyder reference documents state facts; this one collects what they cannot.

**Read this before quoting anything from the Spyder documents to a client**, and **before spending
an hour in front of a frame** — most of these resolve in under a minute each, and nobody has done
it.

Companions:
- `christie-spyder-x20.md` — device, VI, HDCP, connectors, the 4.x software history
- `christie-spyder-x20-stereoscopic.md` — the SSO option
- `creative-coding/references/protocols/christie-spyder-external-control.md` — the ASCII protocol

## Provenance

- **Compiled 2026-08-12** from the four Christie documents in the library (user manual
  020-000916-01, SSO manual 020-000875-01, release notes 020-000917-01/-02/-04/-06/-07/-08),
  Christie's product page and brochure, two chassis photographs, three screenshots of a running
  Advanced 4.1.0 client, and trade press from the June 2009 launch.
- **Nothing in this file is Verified.** Each item states its tier: **Contradiction** (two sources
  disagree), **Undocumented** (exists, nobody describes it), or **Theory** (reasoning, never
  tested).
- ⚠️ **No Spyder hardware was available.** Not one command was sent, not one menu opened. Every
  test below is proposed, none performed.

---

## 1. Contradictions between Christie documents

These are not gaps. Two official sources disagree, and someone has to measure.

### 1.1 Stereo VI capacity — a factor of four

| Source | Claim |
|---|---|
| User manual 020-000916-01 | *"When using the Stereoscopic Option VI capacity is halved"* |
| SSO manual 020-000875-01 | **20 M pixels per eye, up to 40 M total**; *"whether the VI is running in 2D or a stereoscopic mode, the maximum VI size remains at 20 million pixels"* |

Both Rev. 1 (04-2016). Neither supersedes the other. **The gap between 10 M and 40 M usable is the
difference between a stereo job being possible and not.**

**Reasoning, not proof:** the SSO manual is X20-specific, more detailed, and internally consistent
with its own worked example; the user manual's line sits in a general VI section written around
the 200/300 series, where halving may well be true. **Prefer the SSO manual for X20 — and verify
before committing.**

**Test:** build a stereo configuration and add PixelSpaces until the client refuses. Compare the
ceiling against 10 M, 20 M and 40 M.

### 1.2 Power — three figures, none agreeing

| Source | Figure |
|---|---|
| User manual | 1000 W max |
| Product page | 900 W, 9.0 A @ 100 VAC, <750 BTU/hr |
| **Chassis nameplate** | **`100-240V~ 50-60Hz 12.0A`** |

The plate is the regulatory marking, so **size a circuit from it** — 12 A at 100 V is 1200 VA,
above both published numbers. Most likely the plate is rated maximum and the published figures are
typical or measured, but **no source says that.**

**Test:** a clamp meter on a loaded frame.

### 1.3 Output DVI pixel clock — 265 or 330 MHz — **CLOSED 2026-08-30**

The manual stated 330 MHz for dual link generally, without separating input from output. The
product page stated **DVI up to 265 MHz on outputs, 330 MHz on inputs.**

**Settled without the test.** The 4.1.0 `3840x2160 @29.97Hz` output factory format, read off a
running client, has HTotal 4000 × VTotal 2191 × 29.97 = **262.66 MHz** — 2.3 MHz under the product
page's ceiling and 67 MHz under the manual's. Christie would not build a shipped factory format to
land just beneath a limit that was not real. **Product page believed; the manual's 330 MHz output
figure is treated as wrong.** Full timing in `christie-spyder-x20.md` §5.1.

⚠️ **Not closed by measurement.** No format between 265 and 330 MHz was ever attempted, so the
ceiling itself remains uncrossed — this is a strong inference from a shipped artefact, not a bench
result. The original test still stands if a frame is ever available.

**New question opened by the same screenshots:** that format sets **SyncType TriLevel** and
**UseAlternateOutputSynchro True**, neither of which appears in any Christie X20 document; §13
describes output sync as free-run or vertically referenced to NTSC/PAL black burst only.

### 1.4 Weight

Manual ~70 lb; product page lists **59 lb (27 kg)** and **70.5 lb (32 kg)** together, with 70.5 lb
repeated as shipping weight. Reads as unit vs shipping with a mislabelled field. Not stated.

### 1.5 Which layers a stereo source may use

The main manual lists dual-link-capable layers as a fixed set — **1, 4, 7, 9, 12, 15**. The SSO
manual says a stereo source *"will use any two adjacent layers."* Either stereo sources are freer
than dual-link sources, or one manual is loose.

### 1.6 The 200/300 VI table, twice

The user manual gives two different VI capacity tables for the same 200/300 hardware in two
different chapters. Recorded in `christie-spyder-x20.md` §2; unresolved.

---

## 2. Undocumented features — they exist, nobody describes them

### 2.1 `Colocate` — ⚠️ highest priority, because it may move things

**Tier: Undocumented.** An option on the **right-click context menu of a screen in the Vista
Advanced display simulator**. Appears in **no Christie document** — not either manual, not any of
the nine release notes, not the Spyder Studio guide for the successor platform, not anywhere
findable on the web.

**What the manual does establish**, without naming it: the simulator builds a **view stack**
*"every time multiple PixelSpaces occupy the same space, allowing a user to view a PixelSpace that
might otherwise be obscured by another."* So overlapping PixelSpaces is a supported condition.

| Reading | Effect | Cost if wrong |
|---|---|---|
| **Positional** (more likely) | Moves the selected PixelSpace to the same VI X/Y as another, creating a view stack. Both read the same canvas region, so **one layer can feed two screens** | A show planned around shared layers that are not actually shared |
| **View-only** | A simulator drawing convenience | Assuming it is cosmetic while it silently relocates a PixelSpace on a live system |

**Test — decisive, one minute.** `RPD` returns PixelSpace coordinates
(`<ID> <Name> <CurrentBackground> <NextBackground> <X> <Y> <Width> <Height> <RenewalGroupID>`).
Record X and Y, apply Colocate, read again. **Moved coordinates mean positional.** ⚠️ Run it
offline or on a frame feeding nothing.

### 2.2 `SourceMon` — the built-in multiviewer

**Tier: partly resolved.** An output mode, confirmed from a running 4.1.0 client. Christie's user
manual never mentions it.

**Known:** all sources on a single output, **tiled 4×4 on the X20-1608 and 4×2 on the X20-0808** —
one tile per input, real-time, full frame rate. It **renders source names** (a 4.1.0 fix addressed
incorrect names on SourceMon in parallel configurations).

**Unknown:** whether tiles indicate preview/program state; whether it consumes VI pixels the way
an OpMon output does; whether it coexists with OpMon on separate outputs; what happens to the
array when inputs are unpopulated.

**Test:** set a spare output to SourceMon, photograph the result, then check the VI budget before
and after.

### 2.3 `SourceConfig` — the single-source monitor

**Tier: Theory.** An output mode in 4.1.0. The manual separately describes setting an output as a
*"(source) configuration output"* by right-clicking it in the patch — almost certainly the same
thing exposed as a mode. A 4.0.6 note lists a *"Source Config monitor fix"*.

**Theory:** it shows the one source currently under configuration, full raster, so input-level
work — brightness/contrast/hue/saturation, luma and chroma key clip and gain, input rastering —
can be judged without putting it on program.

**How the source is chosen — resolved.** It is an explicit mode, not a plain click: *"A wrench
symbol by a listed source indicates it is the current source in the input configuration mode.
Right click the source and select 'Exit configure source' to exit."* One source at a time; the
wrench marks which. The output itself is assigned by **right-clicking an output** in the patch
grid, separately from setting an Operator's Monitor (which is done by **dragging a PixelSpace**
onto an output).

⚠️ **What "the same output can be used for source configuration and Operator's Monitor overlay"
means is NOT resolved.** An earlier reading of this file claimed both appear **simultaneously**.
**That was an overstatement** — the manual says the output *can be used for* both roles and never
says both pictures appear at once, and physically they cannot: a config monitor shows one source
at full raster, an op mon shows a program PixelSpace. **Likely reality, marked as inference:** the
output serves as op mon normally and **switches to the source while configure-source mode is
active.** One output, two roles, **by mode rather than overlaid.**

**Still unknown:**
- **Which "selected" drives it** — a plain click in the source list, or the explicit configure-source
  state the manual describes entering and exiting?
- ⚠️ **What stage of the pipeline it shows.** For it to be useful it must be **raw input** —
  pre-KeyFrame, pre-crop, pre-size. If it shows the composited layer, tuning through it means
  chasing your own scaling.

**Test:** set an output to SourceConfig, click a source, then size that layer down to a small tile.
If the monitor changes, it is showing the layer, not the input.

### 2.4 `Op Mon Input` and the capture path

**Tier: Theory.** A DVI-D connector, one per output board. The manual mentions it **once**, and not
in connection with operator monitors: the Still Server's DVI output is *"captured directly into
memory at the X20 OpMon input connector."*

A 4.x note records that when **no source monitor is configured, a warning icon appears beside the
Capture button** in source properties. So capture depends on a monitor existing.

| Reading | How capture works |
|---|---|
| **Internal** (now favoured) | Setting SourceConfig/SourceMon allocates an internal path and Capture reads from it. **No cable** |
| **Physical loop** | An output is looped back into `Op Mon Input` and grabbed there |

**Revised reasoning:** internal is more likely. No Christie document ever mentions looping an
output back, and the still server needs the physical port precisely because its source is an
*external* PC.

**Test:** with SourceConfig set and **nothing cabled into `Op Mon Input`**, press Capture. A
thumbnail means internal.

### 2.5 Devices — `Single Layer` vs `Dual Layer` vs `Mixer`

**Tier: Undocumented for two of three.** The manual gives Devices roughly a paragraph: *"A device
can be a single layer device, a dual layer, or a mixer,"* eight maximum, assignable *"to be a
mixer, for layers 1 and 2, for instance."* **It never defines single or dual.**

**Mixer is understood:** two layers as an A/B pair with a transition in place — how a source
changes in a window without cutting to black. Confirmed by the expansion chapter's worked example
(four layers as two mixers). `DMB` selects the bus, `DMT` fires the transition, duration 1 for a
cut.

**Dual Layer — two coherent readings, no way to choose:**

| Reading | Argument for |
|---|---|
| **Key/fill or dual-link pair grouping** | Linear key needs two adjacent layers with the cut on the lower; dual-link sources also consume two adjacent layers. Both must move and size together and never be separated |
| **Cut-only PGM/PVW pair** | Explains why it is a separate type at all — a mixer with duration 1 would otherwise cover it |

**The protocol is a clue:** `DMB` and `DMT` are both documented as *"intended for devices
configured as Mixers."* **No dual-layer counterpart exists.** So a dual layer device has no
documented bus selection and no transition command — consistent with cut-only, and equally
consistent with it not being a switching abstraction at all.

**Test:** create a dual layer device and read its properties panel. **A duration box means it
transitions. A bus control means it is a PGM/PVW pair. Neither — just two layer assignments —
means it is a grouping construct** and the key/fill reading wins.

### 2.6 The `Morph` checkbox

**Tier: Theory.** Named once in the device configuration paragraph — *"Check the Morph box if the
Morph effect is desired"* — and never explained.

**Theory:** on a mixer transition, instead of cross-fading A into B at fixed geometry, the layer
**animates from A's KeyFrame to B's** — size, position and so on interpolating over the duration.
Fits Spyder's architecture exactly: KeyFrames are already interpolatable and script elements
already tween between them over cue durations.

**Unknown:** what it interpolates (position and size certainly; border, shadow, crop, pan/zoom
unstated), and whether the video cross-fades during the move or holds and cuts at arrival.
⚠️ **No protocol equivalent** — `DMT` takes a duration and nothing else, so a control system
cannot toggle Morph per transition.

### 2.7 `SpyderRouter`

**Tier: Undocumented.** An entry in the Router Type dropdown — **a Spyder driving another Spyder as
a router.** Fits the Function Key type for *external command key recall on a remote Spyder*. No
documentation of it exists anywhere.

### 2.8 Genlock

**Tier: partly resolved.** A **BNC labelled `Genlock`** on the output board, confirmed on two
independent images (the SSO manual's Figure 10 and a chassis photograph). The **user manual never
mentions a reference input at all.**

**Known only from the product page:** free-run, or vertically referenced to NTSC/PAL black burst.

**Unknown:** menu path, reference-loss behaviour, how reference interacts with an expansion chain.
The only functional mention anywhere is a 4.x stereo bug fix whose remedy *"requires genlock and a
50/59.94/60 Hz VI configuration."*

⚠️ **A second BNC sits beside `Genlock`** in the photograph, unlabelled at that resolution and
unidentified. Recorded rather than guessed.

### 2.9 "USB expansion"

**Tier: Undocumented mechanism, confirmed existence.** Three release-note entries establish it:
support for different VI heights between X20 frames *"connected via USB expansion"*; choosing a
**USB connection index** when opening low-level diagnostics on a parallel system; and **4.0.7
adding "USB redundancy for expanded systems."**

⚠️ **The manual describes expansion only over InfiniBand.** The rear panel shows one InfiniBand
port and one USB Type-B `Control` port per output board. **Whether USB expansion uses that Control
port, the internal PC's USB, or something else is stated nowhere.**

**Certain:** USB carries inter-frame traffic in expanded systems, and 4.0.7 made it redundant.

### 2.10 Front panel behaviour

**Tier: layout known, behaviour undocumented.** Labels are legible from a photograph — `Home`,
`Config`, `Health`, `T/L`, `B/R`, `Auto`, `Undo/Cancel`, `Save/Ok`, plus `CKey` / `FKey` / `Lock`
soft keys and a `1- PG1 … 57- PG8` page strip. **No menu structure, no key semantics, no display
states are documented anywhere.** The manual defers to an operator's manual not in hand.

⚠️ **The panel pages command keys in eights (PG1–PG8); the external protocol pages registers as
page × 1000 + ID.** Two different schemes, no stated relationship.

### 2.11 Keyboard shortcuts in Vista Advanced

**Tier: absence, not gap.** No shortcut list exists — not in the manual, not in any release note,
not on Christie's site, not in the community. The only keystroke documented anywhere in the Spyder
material is **ALT+F4 to close the still server**. In Christie's vocabulary the shortcut layer *is*
Function Keys and Command Keys. ⚠️ Undocumented accelerators may still exist; check the menus.

### 2.12 `40808i`

**Tier: Undocumented.** An early-production model string observed on a used **08/09** unit in the
resale market. Christie only ever published **X20-0808** and **X20-1608**. The X20 launched at
InfoComm June 2009, so an 08/09 unit is among the earliest — the string is most plausibly a
Vista-Systems-era or transitional designation. ⚠️ **The `4` prefix and `i` suffix are not
decoded.** Do not assume `4` means four slots without counting bays.

---

## 3. Protocol unknowns

### 3.1 Arguments for every 4.x command — ⚠️ the single largest gap

Eight commands were added across the 4.x line and are **named and nothing else**: `AIR`, `RRD`,
`RIF`, `RSCC`, `RSEC`, `RSCD`, `ASC`, `OCC`. **No argument list, no order, no ranges, no response
format.** Release notes are one-line summaries.

**`OCC` (Output Config Connection, 4.0.7) matters most.** Every other output property has a
command; **which connectors are live has never had one.** If the name means connector selection,
`OCC` is what a control system needs to switch an output between DVI and SDI without a client PC.
⚠️ **That reading is inference — the note is six words.**

**Test:** the **UDP Console Simulator inside Vista Advanced** (its existence is known only from a
bug fix). Fastest path to capturing real arguments without writing a client.

### 3.2 The 1400-byte response ceiling

4.0.2 *"added external control response code and option to retrieve additional message data beyond
1400 bytes in a single response."*

- ⚠️ **A 1400-byte limit exists and the manual never mentions it.** On 3.x, `RRL` or `RSN` against
  a large system would silently truncate. 1400 is a UDP-payload-sized number.
- ⚠️ **Neither the new response code's value nor how the option is requested is stated.** The
  manual's response-code table (0–6) is **incomplete for 4.x**, so a strict parser can reject a
  valid response.
- **Unknown:** whether the ceiling applies on serial as well as UDP.

### 3.3 `OCM` covers three of at least five output modes

Documented: Normal, OpMon, Scaled. Observed in 4.1.0: **plus SourceConfig and SourceMon.** The SSO
manual's 3.x screenshot separately shows **PassiveLeft, PassiveRight, ActiveStereo**.

**So five to eight modes exist and three have a documented protocol form.** Unreachable from a
control system: the multiviewer, the source-config monitor, and **every stereo mode.**

**Test:** the three documented modes take the mode name as a literal ASCII string. `OCM <output>
SourceMon` either works or returns error code 4. One command per mode name.

### 3.4 Other protocol gaps

- **No command reports the frame's software version.** It is read on the front panel. Given how
  much changed across 4.x — command set, `RLK` behaviour, response codes — a control system that
  must adapt to version **cannot currently discover it.**
- **Where VDCP sits** (added 4.0.5) — Spyder as controller or controlled, on which transport,
  coexisting with the ASCII protocol or not.
- **No TCP interface documented.** UDP only per the manual; whether 4.x added one is unknown.
- **Serial line settings** — baud, parity, stop bits, flow control — **never stated.** The pinout
  is given and the settings are not.
- **Whether UDP responses return to the source port** or a fixed port. Determines how a listener
  is written.
- **No response timing, timeout guidance or rate limit** beyond the explicit *"do not poll `RCS`
  faster than 1 Hz."*
- **Response code 6 is reserved for a checksum** that is never described.
- **`KPS` and `RCR` are absent from the manual's own command table** while being described in full
  a few pages later.
- **Alignment effect 12's description** says "height" where the effect name says width.

### 3.5 Router driver coverage by model

The Router Type dropdown names **brands and generations, not models** — `Sierra` / `Sierra IP`
must cover every Sierra generation including the Aspen line. ⚠️ **If a router connects but
crosspoints do not take, suspect a protocol-generation mismatch, not the network.**

---

## 4. Signal-path questions

### 4.1 Is the internal crosspoint non-blocking?

**Tier: Theory.** The chassis is a **URS — Universal Routing Switcher**, and the X20 inherited the
matrix switching of the Christie Vista URS product line. Any input reaching any layer is the
implied behaviour and **never stated as a guarantee.**

**Test:** patch a source to a distant layer and see whether the assignment is refused.

### 4.2 What does a layer show when its input switches connector?

Two sources can target the same physical input on different connectors (composite and SDI), but
**only one connector/signal type can be selected per input at a time.** Applying source B changes
the input's connector selection.

⚠️ **What layer A displays afterward — black, last frame, or garbage — is undocumented**, as is
how long the input takes to re-detect and re-lock. **This is not a clean switch and should not be
rehearsed as one.**

### 4.3 Which BNC actually carries composite

The chassis silkscreen groups four analog BNCs as **`Cr-Pr-C`, `B-Pb`, `G-Y-Comp`, `Comp Sync`**.
`G-Y-Comp` reads as composite on the G/Y position, standard for Spyder. ⚠️ **But the manual says
composite *"shares BNC with composite analog sync signal,"*** which points at `Comp Sync` instead.

**Test:** feed composite to `G-Y-Comp` first. If nothing, try `Comp Sync` before suspecting a
cable.

### 4.4 Does SD-SDI work reliably on X20 outputs?

The silkscreen reads `3G/HD/SD-SDI` on both input and output BNCs, and the 200/300 output notes
confirm the platform outputs 480i/575i. ⚠️ **But no SDI rate table exists for X20 anywhere** — no
bitrate, no cable length, no output-side level statement. The platform is far more comfortable at
HD.

**If SD-SDI out misbehaves, that is the reason.** Safer path for CVBS: let the X20 stay at HD and
put the standards conversion in a dedicated box.

### 4.5 What active raster does Spyder present NTSC composite as?

720 × 480 or 720 × 486? BT.601 defines 486 active lines for 525/60; 480 is the DV and MPEG
convention. **No X20 format table exists**, so which one the input reports is unknown — and it
shifts every vertical number in a tiling layout.

### 4.6 Does audio pass through?

**Tier: Theory, and the answer is almost certainly no.** **No source in the library mentions audio
at all** — no embedded audio handling, no de-embedder, no pass-through, no audio spec.

**Reasoning:** the X20 decodes SDI to baseband, composites into the VI, and re-encodes on output.
Embedded audio is not part of that pipeline. With four inputs tiled onto one output there is **no
coherent answer to whose audio it would be.** The only audio connectors on the chassis are the
internal PC's mic and speaker jacks, marked factory use only.

**Plan shows as if audio does not survive the box.** ⚠️ Test before relying on it either way.

### 4.7 Does a dual-link input consume the neighbour's SDI as well as its analog?

**Tier: resolved toward the broad reading, still untested.** The manual: *"the preceding analog
input connector is disabled... When a dual-link source is used on input 2, the system will utilize
the resources from Input 1, therefore disabling the connector."*

⚠️ **An earlier reading of this file treated "analog" as a precise carve-out sparing SDI. That was
wrong.** Odd inputs have no DVI, so "the preceding analog input connector" is simply how Christie
names the odd neighbour by its type. The second sentence — *"utilize the resources from Input 1,
therefore disabling the connector"* — reads as **the whole input channel**, SDI included.

**Mechanism:** DVI-I dual link carries all its TMDS pins on one connector, so it needs nothing
physically from the neighbour. What it needs is **processing bandwidth** — twice the pixel rate has
to be handled somewhere, so the X20 borrows the adjacent channel's input processing.

**Plan on the broad reading.** **Test:** patch a dual-link source on input 2, then attempt autosync
on input 1's SDI.

### 4.8 Input pool vs output wiring — and the layer-pair puzzle

**Tier: Theory (the asymmetry), Contradiction (the pairs).**

The two sides behave oppositely, and the silkscreen shows why: **every X20 DVI input is marked
`Dual DVI-I`, but only odd outputs are.**

| | Behaviour |
|---|---|
| **Inputs** | A **resource pool** — 16 dual-capable connectors on a 1608, only **6** simultaneous dual-link sources, each consuming the preceding odd input and an adjacent layer |
| **Outputs** | **Fixed wiring** — even outputs were never dual-capable, so nothing is taken from anything. All 8 connectors remain available; only the raster they carry changes |

⚠️ **The layer-pair table does not map cleanly onto physical inputs.** Dual-link layer pairs are
given as **1/2, 4/5, 7/8, 9/10, 12/13, 15/16** — skipping 3 and 6. But the DVI must sit on an even
channel, and pair 4/5 would place it on an odd one. Either layer numbering is not 1:1 with input
numbering (plausible — the crosspoint routes sources to layers), or the table is loose. **This
decides which physical inputs can actually carry six dual-link sources on a 1608.**

### 4.9 Does a dual-link output cost anything?

**Tier: Theory.** Nothing states what a dual-link output consumes, if anything. The odd/even split
reads as fixed capability rather than contention, and the SSO output table lists odd and even
connectors working at the same rates simultaneously — which would be impossible if odd stole from
even. **Test:** set output 1 to a dual-link format and check whether output 2 still passes video,
and whether output 1's SDI checkbox greys out or merely fails.

### 4.10 SDI Level B on outputs

**4.0.4 added SDI Level B on inputs.** Nothing states the output side. Unknown whether X20 outputs
level A, level B, or either.

---

## 5. Hardware and lifecycle

### 5.1 Adding an input card to convert an 0808 to a 1608

**Architecturally supported.** The manual: the chassis is *"populated at the factory with various
combinations,"* *"not all slots must be filled,"* and this is *"an easy hardware upgrade path for
systems that may need to increase capacity over time."* Chassis sizes start at three slots; a 1608
photograph shows three card rows (inputs 1–8, inputs 9–16, outputs 1–8), and **only one X20 chassis
size is specified anywhere.**

**Gains 8 layers → 16.** ⚠️ **Gains no VI capacity** — 20 M pixels regardless of cards fitted.

**Unknown:**
- **Firmware/FPGA compatibility across board vintages.** Every release carries its own CPLD and
  FPGA set, and one release updated output board firmware *"to support newer production power
  supplies"* — proof that Christie shipped boards across hardware generations. **A board's vintage
  relative to the chassis is the real risk.**
- **Whether a card add self-detects**, or requires reconfiguration beyond setting the model type in
  Configuration Manager.
- **Where the running FPGA set is displayed.** The front panel shows the *software* version;
  nothing documents an FPGA readout. `Health` on the front panel or Real-Time Protection in
  Advanced are the likely places.

**Procedure that most likely works:** update the frame to 4.1.0 **first**, note the front-panel
version and I/O count, fit the card, boot, then re-run the update from Connection Manager so it
flashes the new board.

⚠️ **Board boundaries are functionally real** — a 4.x release fixed linear key failing when cut and
fill landed on **different input boards of an X20 1608**. Keep linear-key pairs on one board.

### 5.2 Live power supply swap

**Redundant hot-swappable supplies** are stated in Christie feature copy. ⚠️ **The user manual
never mentions this**, and **no procedure for a live swap is documented anywhere.** Capability
established; method not.

### 5.3 Parts, after January 2027

End of production 2024-01-02; support to **2027-01-02, while parts last.** Used pricing has
collapsed — a 1608 that listed around £40,000 in 2014 now trades near $2,000, an 0808 under $1,000.
**Buying a whole 0808 to harvest an input card may be cheaper than sourcing the card**, and leaves
a spare chassis, supplies and output board.

---

## 6. Corrections log

Assertions made during this work that turned out to be wrong. Recorded because the **reasoning
failures repeat**, not just the facts.

| Claimed | Actual | Why the error happened |
|---|---|---|
| Four composite sources lock you to **layers 1, 3, 5, 7** | Composite is odd-**inputs** only, but **any layer** can be used — the internal crosspoint routes sources to layers | Read *"1-to-1 relationship between the number of layers and the number of physical input cards"* as a fixed input→layer mapping. It is a statement about **count** |
| **Blackmagic Videohub is not supported** | `BlackMagic VideoHub` is in the Router Type dropdown | Built an "inventory" from release notes. **Release notes are a changelog** — anything shipping before 4.0.0 is invisible to them |
| The **Sierra driver is probably serial-only** | Both `Sierra` and `Sierra IP` exist | Inferred from the absence of an "IP" suffix in the release notes. Same root cause as above |
| Use the **Single Widescreen** template for one 1080p output | **Individual Screens → Add Additional Discreet Screen**. Widescreen is for one PixelSpace spanning multiple outputs with a blend overlap | Reached for the first template named in the manual's worked example without checking its purpose |
| **Any output connector combination works** if the format is valid for each | **DVI and SDI are mutually exclusive** — Advanced warns and disables one. The rule is one digital path plus analog | Quoted the manual's general sentence without noticing that **both of its own examples pair analog with one digital path**, never DVI with SDI |
| A dual-link input disables only the neighbour's **analog**, sparing its SDI | The **whole input channel** is consumed | Read "the preceding analog input connector" as a precise carve-out. Odd inputs have no DVI — "analog" is just how Christie names that neighbour |
| One output can be a config monitor and a layer-labelled op mon **simultaneously** | It can be **assigned** both roles; nothing says both images appear at once, and they cannot | Turned "can be used for" into "at the same time" |
| X20 outputs do **RGBHV only** on the analog pins, no component | **Analog RGB (SOG, composite or separate sync) and Analog YUV** are both in the output format list | Described the DVI-I pin arrangement and mistook it for the format list |
| The `Op Mon Input` capture path probably needs a **physical output loopback** | **Internal is more likely** — no Christie document mentions looping an output back, and the still server needs the physical port because its source is an external PC | Over-weighted the connector's name |

**The recurring failure is treating a partial source as complete** — a changelog as an inventory,
a count as a mapping. ⚠️ **When a list comes from release notes, say so and say what it cannot
contain.**

---

## 7. Test plan — ordered by value per minute

If a Spyder is ever available, this is the order:

1. **`Colocate`** — `RPD`, apply, `RPD` again (§2.1). Offline. **One minute, settles a command that
   may silently move a PixelSpace.**
2. **Dual layer device properties** (§2.5). Open the panel and look. Settles a two-way ambiguity.
3. **`OCM <output> SourceMon`** in the UDP Console Simulator (§3.3). One command; opens or closes
   external control of the multiviewer.
4. **Capture with nothing in `Op Mon Input`** (§2.4). One button press.
5. **`SourceConfig` raw-vs-layer** — resize the layer and watch the monitor (§2.3).
6. **Arguments for the eight 4.x commands** (§3.1) via the Console Simulator. Longest task,
   highest value for any future control work.
7. **Stereo VI ceiling** (§1.1). Build until it refuses.
8. **Composite on `G-Y-Comp` vs `Comp Sync`** (§4.3).
9. **Clamp meter on a loaded frame** (§1.2).
10. **Pull one power cord** (§5.2).

**Anything learned goes back into the three reference documents**, not here. This file holds
questions; answers get promoted.
