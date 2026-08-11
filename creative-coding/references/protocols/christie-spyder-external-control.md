# Christie / Vista Spyder — external control protocol (ASCII)

The command interface shared by the Spyder 200/300 series and the Spyder X20. Device, signal and
capacity facts are **not** here — they live in
`digital-video/references/christie-spyder-x20.md`. Cite across; do not restate a number from
there.

## Provenance

**Three source groups, all read in full.**

1. *Spyder X20 User Manual*, Christie document **020-000916-01 Rev. 1 (04-2016)** `[Official]`,
   "External Control Protocol" chapter (manual pages 111–128) plus the register and
   layer-alignment sections. Supplied by the user as a 180-page PDF (manualslib.com capture of the
   Christie PDF). Text extracted and read end to end. **Confirmed 2026-08-10 to be the final X20
   manual** — Christie still posts this same document number and there is no later revision.
2. *Christie Spyder X20 v4.1.0 Software Release Notes*, **020-000917-08 Rev. 2 (1-2017)**
   `[Official]` — supplied by the user, read in full. **4.1.0 is the final X20 software release**,
   and it lists no protocol change.
3. **The 4.0.x release notes, fetched from Christie 2026-08-10 and read in full** `[Official]` —
   **020-000917-02** (v4.0.0), **-04** (v4.0.3), **-06** (v4.0.5), **-07** (v4.0.6). Cumulative:
   the 4.0.6 document carries every entry back to 4.0.0 including all intervening betas. Plus
   **020-000917-01 Rev. 1 (3-2016)** (v4.0.7), supplied by the user and read in full.
   ⚠️ **This changes the picture substantially — §8 lists eight commands and several argument
   changes the manual does not contain.** **The 4.x history is now complete: every release from
   4.0.0 to 4.1.0 is accounted for.**
- **Sourcing tier: `[Official]` throughout.** Every command, argument, range and response code
  below is transcribed from that chapter. Nothing is recalled and nothing is inferred except where
  marked.
- **Web sources:** none. No page fetched, so no last-edited date or oldid exists to record.
- **What was NOT read:** no wire capture was taken, **no command in this document has ever been
  sent to a frame**, and no behaviour below has been tested. The manual's figures were not
  transcribed. **No protocol addendum or SDK covering the 4.x additions was found** — if Christie
  published argument documentation for `AIR`, `RRD`, `RIF`, `RSCC`, `RSEC`, `RSCD`, `ASC` or `OCC`,
  it is not in hand.
- ⚠️ **Version gap, and the answer is not what the manual implies.** The manual predates 4.x, and
  **Christie never revised it for the 4.x line.** The 4.0.x notes record **eight commands added
  and at least four existing commands changed** — none of which appears anywhere in the manual.
  **§5 is the 3.x command set as documented; §8 is everything 4.x added, as named.** A control
  system written from §5 alone will work, and will be missing capability it could have had.
- ⚠️ **Release notes are one-line summaries, not documentation.** They give a command's name and
  purpose and **never its arguments, ranges, response format or error behaviour.** Every command
  in §8 is **confirmed to exist and nothing more.** Writing one from its name is exactly the
  failure this library exists to prevent — the arguments must come from a frame or from Christie.
- **Open contradiction, left in place:** the chapter's own command overview table **omits `KPS`
  and `RCR`**, both of which get full argument descriptions a few pages later in the same chapter.
  Both are documented below and marked.

---

## 1. Transport

Both transports accept the **same ASCII strings** and **can be used concurrently**.

### Serial

- **RS-232, 9-pin**, on one of the three serial ports on the back of the frame. The port must first
  be assigned to external control from Vista Basic or Vista Advanced.
- **Pinout:** pin 2 = Receive (RX), pin 3 = Transmit (TX), pin 5 = Ground.
- **Every command must be terminated with a carriage return.**

### Ethernet

- **UDP to port 11116** on the frame. **No configuration required** on the Spyder side.
- **Every message must be preceded by a 10-byte header**:

| Index | Byte |
|---|---|
| 0 | `s` |
| 1 | `p` |
| 2 | `y` |
| 3 | `d` |
| 4 | `e` |
| 5 | `r` |
| 6–9 | `0x00` × 4 |

- **No argument delimiter between the header and the command** — the command text starts
  immediately at byte 10.

### Encoding rules, both transports

- **Commands and arguments are delimited by a single space character.**
- **Spaces inside a string argument must be replaced with the three-character ASCII string `%20`.**
  This applies to responses too — returned values containing a space come back `%20`-escaped.
- Arguments shown in the manual as `Argument x ~ XX` are **repeatable** — supply as many as needed
  in one command.
- Arguments marked with `*` are **optional**, but once one is skipped **no further arguments may
  follow**.

---

## 2. Responses

**Every command returns a response**, and **the first argument is always the error code.**

| Code | Name | Meaning |
|---|---|---|
| 0 | Success | Processed |
| 1 | Empty | Requested data is not available |
| 2 | Header | Invalid command |
| 3 | Argument Count | Below the required minimum argument count |
| 4 | Argument Value | One or more arguments invalid |
| 5 | Execution | Error while processing — check the alert log in Basic / Advanced |
| 6 | Checksum | *Reserved* |

⚠️ **This table is the manual's, and it is incomplete for 4.x.** Release 4.0.2 added a response
code for retrieving message data past a 1400-byte ceiling — see §8.3. Its value is not stated
anywhere in hand. **A parser that treats codes above 6 as invalid may reject a legitimate
response.**

Multi-value responses use the same space delimiter and the same `%20` escaping.

---

## 3. Two addressing rules that break naive code

### Layer IDs start at 2

**Layer ID 0 and 1 are reserved for the system's two background layers.** A control surface that
maps "layer 1" to ID 1 will address a background.

`RLC` (Request Layer Count) **returns the logical count including both backgrounds** — subtract two
to get the usable layer count.

### Register pages are encoded arithmetically

To reach a register on a page above the first, **add (page number × 1000) to the register ID**.
Register ID 2 on page 3 is sent as **3002**. This applies to `RSC` and `FKR`, and to anything else
taking a register ID.

### Register ID vs data ID — not the same number

A command key has a **register ID** (its slot position in the list, shown top-left in the UI) and a
**script / data ID** (stable, set on creation). **Reordering the list changes the register ID and
leaves the script ID alone.** `RSC`, `SCR` and `DCK` all take an optional trailing argument
selecting which one you mean (`S` = ScriptID, `R` = RegisterID).

The register indirection is deliberate and useful: point an external system at a register ID, then
change what sits in that register to change what the button does, without touching the control
system.

### Register type IDs

Any command taking a register type wants the ASCII representation of this index:

| ID | Type |
|---|---|
| 0 | Effect |
| 1 | PlayItem |
| 2, 3 | *not used* |
| 4 | Command Key / Script |
| 5 | Treatment |
| 6 | Source |
| 7 | Function Key |
| 8, 9 | *not used* |
| 10 | Still Image |

---

## 4. Device indirection — `<DVCEn:BUS>`

Any argument that takes a layer ID will also accept an encoded **device** reference, resolved by
the frame at runtime. **The angle brackets are required.**

```
<DVCE2:PGM>    device index 2, program bus
<DVCE3:PVW>    device index 3, preview bus
```

Used inline, e.g. `KSZ 800 <DVCE0:PVW>` sets the layer behind device 0's preview bus to 800 px
wide.

This is the right addressing mode when the show is built around mixer devices — the control system
stops caring which physical layer is currently on which bus.

---

## 5. Command reference

Grouped by what they do rather than the manual's order. `*` marks optional arguments.

⚠️ **This is the 3.x set as documented.** Seven further commands and several argument changes
arrived across the 4.x line and are in **§8** — including a fifth argument on `ILA`, a second
accepted form for `LCC`, and a **behaviour change to `RLK` that breaks a common visibility check.**
Read §8 before writing anything against `ILA`, `LCC` or `RLK`.

### 5a. Layer geometry

| Command | Arguments |
|---|---|
| **`KSZ`** Layer size | 1 horizontal size (px) · 2~XX layer IDs. Vertical size follows the source aspect ratio automatically |
| **`KPS`** Layer position ⚠️ *omitted from the manual's own command table* | 1 mode (0 = absolute, 1 = relative) · 2 H position · 3 V position · 4~XX layer IDs. Position is in **pixels relative to the top-left corner of the layer's PixelSpace** |
| **`LSP`** Layer size and position | 1 mode (0 = absolute, 1 = relative) · 2 H position · 3 V position · 4 H size (px) · 5~XX layer IDs. **Preferred over `KSZ` + `KPS` when both change** |
| **`CRP`** Crop | 1 left · 2 right · 3 top · 4 bottom, each **0.0–1.0** · 5~XX layer IDs |
| **`ZPA`** Zoom / pan | 1 mode (0 = absolute, 1 = relative) · 2 zoom **0.0–20.0** · 3 H pan **−2048 to 2048** · 4 V pan **−2048 to 2048** · 5 layer ID |
| **`ARO`** Aspect-ratio offset | 1 type (`t` = set total A/R, `o` = set KeyFrame A/R offset, `a` = adjust existing offset) · 2 float value · 3~XX layer IDs |
| **`IRA`** Input raster | 1 layer ID · 2 edge (`L`/`R`/`T`/`B`, or `A` = auto-raster, **analog only**) · 3* pixels to move — **negative moves the video edge inward, positive outward** |
| **`LAC`** Layer alignment | 1 effect ID (§6) · 2 duration in frames · 3~XX layer IDs |

### 5b. Layer look

| Command | Arguments |
|---|---|
| **`KBD`** Border | 1 layer ID · 2 thickness **−255 to 255**, **negative = outside softness** · 3* R · 4* G · 5* B (**0–255; all three or none**) · 6* H-bevel offset 0–255 · 7* V-bevel offset 0–255 · 8* inside softness 0–255 |
| **`KSH`** Shadow | 1 layer ID · 2* H position · 3* V position · 4* size · 5* transparency · 6* outside softness — all **0–255** |
| **`LCC`** Clone | 1 layer ID · 2 mode (**0 = Off, 1 = Offset, 2 = Mirror**) · 3* clone offset in relative coordinates; omitted uses the KeyFrame's stored offset |
| **`ILA`** Input levels | 1 brightness **0.0–2.0** · 2 contrast **0.0–2.5** · 3 hue **−180 to 180** · 4 saturation **0.0–2.0** · 5~XX layer IDs |
| **`ILK`** Luma key | 1 enable (0/1) · 2 clip **0–512** · 3 gain **0–512** · 4~XX layer IDs. **Mutually exclusive with `ICK` — sending this disables colour key** |
| **`ICK`** Colour key | 1 enable (0/1) · 2–4 colour R/G/B **0–255** · 5–7 range R/G/B **0–255** · 8 colour gain **0–512** · 9~XX layer IDs. **Sending this disables luma key** |
| **`FRZ`** Freeze layer | 1 (1 = freeze, 0 = unfreeze) · 2~XX layer IDs |
| **`KTL`** Learn treatment | 1 treatment ID (**−1 = next available**) · 2 layer ID · 3*–7* learn position / crop / clone / border / shadow |
| **`KTR`** Recall treatment | 1 treatment ID · 2~XX layer IDs |

### 5c. Layer routing and transitions

| Command | Arguments |
|---|---|
| **`LAP`** Assign PixelSpace | 1 PixelSpace ID · 2 make visible (0/1) · 3~XX layer IDs. **Assign invisible, configure, then `TRN` on** — that's the documented sequence |
| **`TRN`** Transition layers | 1 (0 = mix off, 1 = mix on) · 2 duration in frames · 3~XX layer IDs |
| **`SRA`** Apply source | 1 source name · 2~XX layer IDs |
| **`ARL`** Apply register to layers | 1 register type · 2 register ID · 3~XX layer IDs |
| **`ICR`** Input config recall | 1 config ID (**−1 forces auto-sync**) · 2 layer ID · 3* if arg 1 is −1, connector type to switch to and auto-sync: **0 = HD15, 1 = DVI, 2 = SDI, 3 = Composite, 4 = S-Video** |
| **`ICL`** Input config learn | 1 config ID to save to · 2 layer ID |

### 5d. Stills and backgrounds

| Command | Arguments |
|---|---|
| **`SLD`** Still load on layer | 1 file name · 2~XX layer IDs |
| **`SCL`** Still clear on layer | 1~XX layer IDs |
| **`BLD`** Background load | 1 file name · 2 PixelSpace ID · 3 (0 = load next, 1 = load current). **Auto-scales to the PixelSpace** |
| **`BTR`** Background transition | 1* duration in frames. **Transitions backgrounds across every PixelSpace — per-PixelSpace background transition is not possible** |
| **`LSO`** Still load on output | 1 file name · 2 output ID · 3* DX4 channel 0–3. Loads **unscaled**, straight onto the output — intended for custom test patterns. **The file must already exist in the `Stills` directory on the server** (reachable by FTP or the client) |
| **`CSO`** Still clear on output | 1 output ID · 2* DX4 channel 0–3; **omitted on a DX4 clears all four channels** |

### 5e. Output configuration

| Command | Arguments |
|---|---|
| **`OCF`** Format | 1 output ID (**zero-based**) · 2 H active · 3 V active · 4 refresh (float, e.g. 59.94) · 5 interlaced (0/1) · 6* reduced blanking (0/1). **VESA formats only**; an unsupported refresh snaps to the nearest available |
| **`OCM`** Mode — Normal | 1 output ID · 2 the literal string `Normal` · 3* H start on the VI · 4* V start on the VI · 5* DX4 channel 0–3 |
| **`OCM`** Mode — OpMon | 1 output ID · 2 `OpMon` · 3 program PixelSpace ID (a preview ID resolves to its program space) |
| **`OCM`** Mode — Scaled | 1 output ID · 2 `Scaled` · 3 program PixelSpace ID |
| **`OCR`** Rotation | 1 output ID · 2 angle — **0, 90, 180 or 270 only**, and **not supported on every output module type** |
| **`OCB`** Blending | 1 output ID · 2 edge (**`L` or `R` only**) · 3 enable (0/1) · 4* blend width in px · 5* mode — **`Bezier`, `Gamma` or `Velocity`** · 6* curve param 1 **0.000–1.000** · 7* curve param 2 **0.000–1.000** |
| **`OCS`** Save | 1 output ID. ⚠️ **Must be called after output changes or they are lost on restart** |
| **`OFZ`** Output freeze | 1 (1 = freeze, 0 = unfreeze) · 2~XX output IDs. **Universal outputs only — DX4 outputs do not support individual freeze** |

### 5f. Presets, scripts, function keys, devices

| Command | Arguments |
|---|---|
| **`BPL`** Learn basic preset | 1 preset ID · 2* duration (**default 60**) |
| **`BPR`** Recall basic preset | 1 preset ID · 2* duration (**default 60**) |
| **`RSC`** Recall script cue | 1 ID to recall · 2 script cue · 3* ID type (`S` = ScriptID default, `R` = RegisterID) |
| **`FKR`** Function key recall | 1 function key ID · 2*~XX layer IDs (for relative function keys) · 3* ID type (`F` default, `R`) |
| **`LCK`** Learn command key | 1 learn as (0 = absolute, 1 = relative) · 2 name · 3 register ID · 4 learn from (**1 = preview only, 2 = program only, 3 = both**) · 5 learn as mixers (0/1). Response: `<result> <CommandKey ID> <Script ID>` |
| **`DCK`** Delete command key | 1 ID · 2* ID type (`S` default, `R`) |
| **`DMB`** Device mixer bus | 1 duration in frames · 2 bus — **`OFF`** (both device layers off screen), **`PVW`** (program layer in preview, preview layer off screen), **`PGM`** (both visible in their PixelSpaces) · 3~XX device indexes (zero-based) |
| **`DMT`** Device mixer transition | 1 duration in frames (**set 1 for a cut**) · 2~XX device indexes |

### 5g. Routers

| Command | Arguments |
|---|---|
| **`RCR`** Router crosspoint recall ⚠️ *omitted from the manual's own command table* | 1 router ID · 2* `L` = switch logical output (the Spyder-side patch) or `P` = physical · 3 output (**zero-based**) · 4 input (**zero-based**). **Args 3 and 4 repeat** to stack switches into one command — Spyder uses the router's stack-and-trigger if the router and its Spyder driver support it |
| **`QRC`** Query crosspoints | 1 router ID · 2* output ID; **omit to return all outputs**. Response `<result> <RouterID> <Output>:<Input> …`, **zero-indexed**, and **−1 for a disconnected output** |

### 5h. Queries

| Command | Response |
|---|---|
| **`RPD`** PixelSpace definitions | `<result> <count>` then per space: `<ID> <Name> <CurrentBackground> <NextBackground> <X> <Y> <Width> <Height> <RenewalGroupID>` |
| **`RSN`** Source names | Space-separated list of source names |
| **`RLC`** Layer count | Logical layer count **including the two backgrounds** |
| **`RAR`** Aspect ratio | 1 source name **or** layer ID |
| **`RLS`** Layer source | `<result> <SourceName> <SourceRegisterID>`. **`Empty` result code with no parameters if no source is loaded; register ID −1 if the source has no register** |
| **`RLK`** Layer KeyFrame | `<result> <RelHPos> <RelVPos> <X> <Y> <Width> <Height> <BorderThickness> <BorderR> <BorderG> <BorderB> <BorderHBezel> <BorderVBezel> <BorderInsideSoftness> <BorderOutsideSoftness> <OutsideEdges> <ShadowHOffset> <ShadowVOffset> <ShadowHSize> <ShadowSoftness> <ShadowTransparency> <CloneMode> <CloneOffset> <LeftCrop> <RightCrop> <TopCrop> <BottomCrop> <CropAnchor> <AROffset> <Zoom> <HPan> <VPan> <PixelSpaceID> <Transparency>`. ⚠️ **The manual warns that later firmware may append values — parse positionally from the front and tolerate extra trailing fields** |
| **`RCS`** Connection status | 1 layer ID. Response `<result> <LayerID> <ConnectorType> <ConnectionStatus>`. Status **0 = disconnected, 1 = connected, 2 = unknown**; connector **0 = HD15, 1 = DVI, 2 = SDI, 3 = Composite, 4 = S-Video**. ⚠️ **Do not poll faster than once per second — the manual warns of degraded system performance** |
| **`RPS`** I/O processor status | 1* truncate length. Response `<result> <Progress 0–100> <StatusMessage>`. **Asynchronous work such as still loading is processed serially, one at a time** — poll this to gate a script on load completion. **Idle returns 0 and an empty message** |
| **`RRC`** Register count | 1 register type · 2* page (zero-based, **−1 for all**) |
| **`RRL`** Register list | 1 register type · 2* page · 3* start index · 4* max count · 5* truncate names to N chars. Response `<result> <ReturnCount>` then `<ID> <Name>` pairs |
| **`RBL`** Basic preset list | 1* start index · 2* max count · 3* truncate length. Response `<result> <ReturnCount>` then `<ID> <Name>` pairs |
| **`SCR`** Script cue request | 1 ID · 2* ID type (`S`/`R`). Returns the current cue, or **−1 if the script is not executing on any layer** |

### 5i. System

| Command | Arguments |
|---|---|
| **`SDN`** Restart / shut down | 1 (**0 = power off, 1 = restart**) |
| **`SAV`** Force save | none. Flushes all configuration and user data to non-volatile storage |

**`RLK` field notes:**

- **Outside Edges** is a hex bitfield in the low 4 bits — `0x01` top, `0x02` bottom, `0x04` left,
  `0x08` right.
- **Clone Mode** — 0 Off, 1 Offset, 2 Mirror.
- **Crop Anchor** — 0 input centre, 1 window centre.

---

## 6. Layer alignment effect IDs (`LAC` argument 1)

The same effects the simulator exposes in the Vista client. "Minimum layers" is the count the
effect needs to do anything; **the first layer listed is the reference** for every align and
match effect.

| ID | Effect | Min layers | Behaviour |
|---|---|---|---|
| 0 | Align Bottom | 2 | Bottom edges match the first layer |
| 1 | Align Center | 2 | Horizontal centres match the first layer |
| 2 | Align Left | 2 | Left edges match the first layer |
| 3 | Align Middle | 2 | Vertical centres match the first layer |
| 4 | Align Right | 2 | Right edges match the first layer |
| 5 | Align Top | 2 | Top edges match the first layer |
| 6 | Center Horizontal | 1 | Centres the layers **as a group** horizontally in their PixelSpace |
| 7 | Center Vertical | 1 | Centres the layers as a group vertically |
| 8 | Horizontal Decrement | 2 | Decreases horizontal spacing between layers |
| 9 | Horizontal Increment | 2 | Increases horizontal spacing between layers |
| 10 | Make Horizontal Equal | 3 | Spacing between all layers becomes the spacing between the first two |
| 11 | Make Same Height | 2 | All match the first layer's height, aspect ratio preserved |
| 12 | Make Same Width | 2 | All match the first layer's width, aspect ratio preserved ⚠️ *the manual's description text for ID 12 says "same height" — a copy-paste error in the source, left flagged rather than corrected* |
| 13 | Make Vertically Equal | 3 | Vertical spacing between all layers becomes the spacing between the first two |
| 14 | Remove Horizontal Spacing | 2 | Stacks layers horizontally, in the order specified |
| 15 | Remove Vertical Spacing | 2 | Stacks layers vertically, in the order specified |
| 16 | Size to Display Height | 1 | Fills the PixelSpace vertically; horizontal position untouched |
| 17 | Size to Display Width | 1 | Fills the PixelSpace horizontally and centres vertically |
| 18 | Snap to Bottom | 1 | Bottom edges to the PixelSpace bottom |
| 19 | Snap Left | 1 | Left edges to the PixelSpace left |
| 20 | Snap Right | 1 | Right edges to the PixelSpace right |
| 21 | Snap Top | 1 | Top edges to the PixelSpace top |
| 22 | Stack Horizontal | 2 | Equal heights, vertically centred on the first layer, arrayed to the **right** of it |
| 23 | Stack Vertical | 2 | Equal widths, horizontally centred on the first layer, arrayed **downward** from it |
| 24 | Swap Windows | 2 | Swaps horizontal position and size between two layers |

---

## 7. Writing against this — what to get right first

Ordered by how expensive the mistake is, not by how likely it is.

1. **Offset layer numbering by 2** in every mapping table, and subtract 2 from `RLC` before showing
   a layer count.
2. **`%20`-escape string arguments on the way out, and un-escape on the way back in.** Source names
   with spaces are normal.
3. **Call `OCS` after any `OCF` / `OCM` / `OCR` / `OCB`.** Unsaved output config survives until the
   next restart and no longer.
4. **Gate still loads on `RPS`** rather than a fixed sleep — the I/O processor runs them one at a
   time.
5. **Rate-limit `RCS` to 1 Hz or slower.** The manual names this one specifically as a performance
   risk.
6. **Parse `RLK` tolerantly** — trailing fields may appear in later firmware.
7. **Decide register ID vs script ID once, per show**, and be explicit in every `RSC`, `SCR` and
   `DCK`. Register IDs move when someone reorders a list in the client.
8. **Prefer `LSP` to `KSZ` + `KPS`** when both size and position change — one command, one frame,
   no intermediate state on screen.
9. **Use `<DVCEn:PGM|PVW>`** rather than hard layer IDs when the show is built on mixer devices.
10. **Do not test `RLK`'s PixelSpace ID against −1 to decide whether a layer is visible.** That was
    3.x behaviour; on 4.x the real PixelSpace comes back and **the transparency argument is the
    visibility check** (§8.2).
11. **Assume responses can exceed one datagram.** A `RRL` or `RSN` against a large system will hit
    the **1400-byte ceiling** (§8.3). Request registers in pages with `RRL`'s start-index and
    max-count arguments rather than asking for everything at once.
12. **Establish the frame's software version before trusting any of this.** The command set,
    `RLK`'s behaviour and the response-code table all differ between 3.x and 4.x, and there is no
    documented command that reports the version. **The front panel's status LCD shows it** — the
    second line reads `Ver:` — confirmed from a chassis photograph in
    `digital-video/references/christie-spyder-x20.md` §8.3. Read it before writing anything.
13. **Use the UDP Console Simulator in Vista Advanced** to confirm any identifier before shipping
    it (§8.6). It is faster than writing a client and it is the only verification path available
    without Christie.

---

## 8. The 4.x additions — commands the manual does not contain

**Source: release notes 020-000917-01, -02, -04, -06, -07 and -08 — all nine 4.x releases, read in
full.** Everything in this
section is `[Official]` **as a statement that the thing exists.** ⚠️ **No argument, range, response
format or error behaviour is documented for any of it** — the notes are one-line summaries. Treat
every identifier here as `# UNVERIFIED:` until it is confirmed against a frame.

### 8.1 New commands

| Command | Name | Added | What the note says |
|---|---|---|---|
| **`AIR`** | *(unexpanded in the notes)* | beta 0.54.3, in **4.1** | Resize a layer **horizontally or vertically without adjusting the other axis** — i.e. break the aspect-ratio lock that `KSZ` enforces |
| **`RRD`** | Request Register Details | beta 0.54.0, in **4.1** | Added to the external control protocol. Presumably richer than `RRL`'s ID-and-name pairs — **presumably is doing work in that sentence** |
| **`RIF`** | Request Image File | beta 0.55.7, in **4.0.2** | — |
| **`RSCC`** | Request Script CueData Count | beta 0.55.7, in **4.0.2** | — |
| **`RSEC`** | Request Script Element Count | beta 0.55.7, in **4.0.2** | — |
| **`RSCD`** | Request Script CueData Details | beta 0.55.7, in **4.0.2** | — |
| **`ASC`** | Advance Script Cue | **4.0.6** | Advance a script cue, with an **optional ±X** argument |
| **`OCC`** | **Output Config Connection** | **4.0.7** | Named and expanded, nothing more. It joins `OCF` / `OCM` / `OCR` / `OCB` / `OCS` in the output-configuration family (§5e), and "Connection" most plausibly means **selecting which physical connector an output drives** — the manual's outputs can enable DVI and SDI simultaneously when the format allows (§5e), and nothing in the 3.x protocol exposes that choice. ⚠️ **That reading is inference. The note says six words.** |

**`OCC` is the one that plugs a real hole.** Every other output property — format, mode, rotation,
blending — has a command; which connectors are live has never had one. If the inferred meaning
holds, `OCC` is what a control system needs to switch an output between its DVI and SDI connectors
without a client PC. **Confirm it before relying on it.**

`RSCC`, `RSEC` and `RSCD` together are a **script introspection set** the 3.x protocol has no
equivalent of — the manual can ask which cue a script is on (`SCR`) but not what is in it. For any
control system that needs to render a script's contents, these three are the reason to care about
4.x at all.

### 8.2 Changes to commands that ARE in the manual

| Command | Change | Release |
|---|---|---|
| **`ILA`** | **Optional gamma parameter added.** §5b documents four value arguments; on 4.x there is a fifth | beta 0.55.8, in 4.0.2 |
| **`LCC`** | **Now accepts a raw pixel offset** for the clone offset, as well as the relative coordinate §5b documents | beta 0.54.0, in 4.1 |
| **`RLK`** | **Option `n` / `normalize` added** — scales the layer's absolute rectangle to compensate for the size of a preview PixelSpace | beta 0.54.7, in 4.1 |
| **`RLK`** | ⚠️ **Behaviour change, and it will break existing code.** Previously an invisible layer returned **PixelSpace ID −1**. It now returns **the actual PixelSpace ID**, and the note says to **check the transparency response argument instead** to decide whether the layer is on screen. Any parser testing `pixelspace == -1` for visibility is wrong on 4.x | beta 0.54.7, in 4.1 |
| **`LSP`** | Fixed — was **not working correctly on PixelSpaces with an X or Y offset greater than zero** | beta 0.56.6, in 4.0.3 |
| **`RRL`** | Fixed — internal error when a register with a **null name** existed | beta 0.54.4, in 4.1 |

### 8.3 Transport change — the 1400-byte response ceiling

beta 0.55.7 (in 4.0.2) **"Added external control response code and option to retrieve additional
message data beyond 1400 bytes in a single response."**

Two things follow, and both matter for anyone writing a client:

- ⚠️ **A 1400-byte response limit exists** and the manual never mentions it. On 3.x, `RRL` or `RSN`
  against a large system would silently truncate. **1400 bytes is a UDP-payload-sized number** —
  consistent with the frame fitting one response into one datagram.
- **A response code and an opt-in mechanism were added** to retrieve the rest. ⚠️ **Neither the
  code's value nor how the option is requested is stated.** §2's table of response codes 0–6 comes
  from the manual and is **incomplete for 4.x.**

This is the most consequential undocumented item in the whole library entry: **a client can be
correct against the manual and still lose data on a big system.**

### 8.4 New control protocol — VDCP

**4.0.5 added support for VDCP for external control.** VDCP is the Video Disk Control Protocol,
used for machine control of video servers. Where it sits relative to the ASCII protocol here —
whether it drives Spyder, or Spyder drives devices with it, and on which port or serial line — is
**not stated.** Given §5f's machine-control commands and the manual's SourceMaster arrangement, the
likely reading is **Spyder controlling playback devices**, but that is inference and is marked as
such.

### 8.5 Router protocols added across the line

`RCR` and `QRC` (§5g) address routers by ID and are driver-agnostic, so no command changed — but
the set of routers a Spyder can drive grew considerably past whatever the manual assumed:

**Atlona · Gefen 3 · Gefen IV (IP) · Gefen III IP · AJA Kumo (IP) · Utah Scientific RCP-3 · Utah
Scientific 100 IP · DTrovision PureLink PM-32X (IP and serial) · Dtrovision III IP · Pesa Cougar
P1N · Pesa PN1 over IP · Pesa P1N redundancy (4.0.7) · Barco Matrix Pro II · Imagine Platinum
(4.1.0).**

**The Pesa P1N *redundancy* protocol at 4.0.7 is the only redundancy-aware router driver in the
line** — worth knowing when a rig has a redundant router and the control system needs to follow
its failover rather than fight it.

Fixes also touched Lightware response parsing, Extron IP TCP keep-alive, and Sierra / RGB Linx /
Quartz / NVision Compact behaviour in offline sessions.

### 8.6 Register and command-key integrity — a documented failure mode

§3 turns on register IDs being stable and meaningful. Across the line, three separate bugs say they
were not always:

- **Register lists could become corrupted**, requiring a "Data List Repair" (beta 0.54.2)
- **Register names could get out of sync with underlying command key names** (beta 0.55.4)
- **4.0.7** fixed **command keys missing after restoring the config file**, and command keys
  **losing their colour value when applying a Repair Data List**

⚠️ **A control system that addresses by register ID has a documented failure mode on older
software**, and the repair tool meant to fix it had its own bug until 4.0.7. Addressing by
**script ID** rather than register ID (§3) sidesteps the reordering problem but not the corruption
one. On any frame below 4.0.7, verify register IDs after a config restore rather than assuming.

### 8.7 Two more things worth knowing

- **The UDP Console Simulator** — beta 0.56.6 fixed it hanging the Advanced interface when no
  server connection could be established at form load. **Its existence is the useful part:**
  Vista Advanced ships a console for sending these commands by hand. That is the fastest way to
  confirm any `# UNVERIFIED:` identifier in this document without writing a client.
- **Expanded systems gained USB redundancy at 4.0.7.** Not a protocol matter, but it means a
  control system talking to an expanded X20 has a more resilient frame-to-frame path above 4.0.7 —
  see `digital-video/references/christie-spyder-x20.md` §12.5.

### 8.8 4.1.0's own changes

The 4.1.0 notes list eight items and **none is a protocol change.** Two still affect code:

| Change | Consequence |
|---|---|
| **Output factory formats 3840 × 2160 @ 29.97 and 3840 × 1080 @ 59.94 added** | `OCF` (§5e) takes explicit H/V/refresh, so these *should* be reachable — ⚠️ **reasoning, not a documented statement.** "Factory formats" is a UI preset list, and `OCF` is documented as "VESA output formats only". Untested |
| **Imagine Platinum router protocol** | One more entry in §8.5. No command change |
| Backup and Recovery for system configuration files | **No command exposes it.** `SAV` still flushes config to non-volatile storage; there is no protocol equivalent of a backup or a restore |

**One 4.1.0 fix is not a protocol matter but will look like one:** *analog/SDI input not outputting
video when the next input has been used as stereo*. That is the input-pairing mechanism dual link
uses. **If a control system switches a source onto a layer near a stereo input and gets black,
check the frame's software version before debugging the command.**

**Field note:** the 4.1.0 upgrade is pushed from Vista Advanced, takes 10–15 minutes, and
**requires pulling the power cords for 10–15 seconds at the prompt.** A control system holding a
session across an upgrade loses it; the frame returns with configuration intact and every
connection dropped.

---

## 9. Not yet verified — open items

**Closed on 2026-08-10:** the 4.x version gap, which turned out to matter far more than expected —
seven new commands, four changed ones, and an undocumented response ceiling (§8). Only 4.0.7
remains unread.

**Still open, roughly by cost of being wrong:**

1. **Arguments for every 4.x command.** `AIR`, `RRD`, `RIF`, `RSCC`, `RSEC`, `RSCD`, `ASC`, `OCC`
   are **named and nothing else.** No argument list, no order, no ranges, no response format. **The
   fastest fix is the UDP Console Simulator in Vista Advanced** (§8.6), or a request to Christie
   for a 4.x protocol addendum if one exists.
2. **The 4.x response code for oversized messages** (§8.3) — its value, and how the "option to
   retrieve additional message data" is requested. Until this is known, **§2's code table is
   incomplete and a strict parser can reject valid responses.**
3. **Whether the 1400-byte ceiling applies on serial as well as UDP.** The number smells like a UDP
   payload, but nothing says so. On serial it may not exist at all.
4. **What `OCC` (Output Config Connection) actually does** (§8.1). Reasoned as connector
   selection, never confirmed, and it is the only command that would give external control over
   which physical connector an output drives.
5. **Where VDCP sits** (§8.4) — Spyder as controller or as controlled, on which transport, and
   whether it coexists with this ASCII protocol on the same port or line.
6. **`OCM` covers only Normal, OpMon and Scaled** (§5e). The output Mode dropdown in Vista Advanced
   offers **Normal, Scaled, OpMon, Source, PassiveLeft, PassiveRight and ActiveStereo** — see
   `digital-video/references/christie-spyder-x20-stereoscopic.md` §8. **Four of the seven modes,
   including every stereo mode, have no documented protocol equivalent.** Whether `OCM` accepts
   those strings is unknown and directly limits what a control system can do on a stereo rig.
7. **Whether `OCF` accepts the two 4.1.0 factory formats** (§8.7). Reasoned yes, never tested, and
   the "VESA formats only" restriction cuts against it.
8. **Nothing here has been sent to a frame.** No command in this document is bench-verified.
9. **No TCP interface is documented** — Ethernet control is UDP only per the manual. Whether 4.x
   added one is unknown.
10. **No response timing, no timeout guidance, no rate limit** other than the explicit `RCS`
    warning.
11. **No statement on whether UDP responses return to the source port** or a fixed port. This
    determines how a listener is written and is unanswered.
12. **Serial baud rate, parity, stop bits and flow control are never stated.** The pinout is given
    and the line settings are not.
13. **`KPS` and `RCR` are absent from the manual's own command table** while being described in
    full a few pages later. Unresolved.
14. **Alignment effect 12's description** says "height" where the effect name says width (§6).
15. **Response code 6 is reserved for a checksum** that is never described.
16. **DX4 output module** appears only as a channel argument. No specification for it exists.
17. **No command reports the frame's software version.** Given how much the protocol changed
    across 4.x, this is a real gap: the version is readable on the front panel and, as far as
    every source in hand shows, **not over the wire.** If a control system must adapt to version,
    it cannot currently discover it.
18. **How front-panel command-key paging maps to the protocol's register paging.** The panel pages
    in eights across PG1–PG8; the protocol uses page × 1000 + ID (§3). **No stated relationship.**

---

## Verification status

| Section | Tier |
|---|---|
| §1 transport, header, escaping | **`[Official]`** — transcribed |
| §2 response codes | **`[Official]`** |
| §3 addressing rules | **`[Official]`** |
| §4 device indirection | **`[Official]`** |
| §5 command reference | **`[Official]`** — every argument and range transcribed; grouping is this document's, not the manual's |
| §6 alignment effects | **`[Official]`** — source's own ID 12 error flagged in place |
| §7 implementation notes | **Designed** — reasoning from the documented behaviour above. Nothing in §7 is a vendor statement and nothing has been run |
| §8 the 4.x additions | Release notes **`[Official]`** — five documents read in full — **for the existence and purpose of each item only.** ⚠️ **Every argument, range and response format is absent from the source**; identifiers here are `# UNVERIFIED:` by default. The `OCF` and VDCP readings in §8.4 and §8.7 are **Designed** and flagged in place as reasoning |

**No command in this document has been sent to a Spyder frame.** The 3.x set in §5 has full
argument documentation from the manual; **the 4.x set in §8 has none, and must not be written from
memory of this file.**

**Companion documents:** `digital-video/references/christie-spyder-x20.md` (device, VI, HDCP,
connectors — §12 there carries the same 4.x history from the signal side) and
`digital-video/references/christie-spyder-x20-stereoscopic.md` (the stereo output modes `OCM` does
not document).
