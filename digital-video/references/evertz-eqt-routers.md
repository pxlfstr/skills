# Evertz EQT Series Routers

Compact Quartz-protocol SDI matrix routers. Scoped to the **coax, non-Clean-Switch**
line, and within that to the **EQT-1616-3G** as the unit actually in hand.

## Provenance

**Single source, Verified [Official] throughout:** *EQT Series Routers System
Manual*, Evertz Microsystems, document revision **1.9.1, January 2014**, 76 pp.,
user-supplied PDF (md5 `ab42313909b6b4c7b138411edb59f8b6`), text layer extracted
and read end to end **except** the sections listed below. Every figure here is
transcribed from that extraction; nothing is remembered, estimated, or rounded.

**Deliberately NOT read**, at user instruction — all fiber and Clean Switch
material, which the user does not own:

| Section | Subject |
|---|---|
| §2.3.2 | Video Reference (the §2.8 reference material WAS read and is used here) |
| §2.5 | Micro-D serial connection (-CS and EQT-3224 new rear plate only) |
| §3.1.4, §3.1.5 | Fiber inputs and outputs (-F version) |
| §4.2.10 | Clean Switch configuration menu (-CS only) |
| §5.9–§5.12 | Clean Switch module / audio / mixer / fault VistaLINK tabs (-CS only) |
| §7.2 | Firmware upgrade path for -CS versions |

**Also not read in the first pass and recovered on a second:** the revision
history page (p. i), now folded into §1.1. Nothing else in the document was
skipped.

**Never read:** any Evertz datasheet, product page, application note (AN-0008 is
named in §2.8.1 and not held), the Quartz protocol specification (§2.4 and §4.4.3
both say "contact Evertz service"), the VistaLINK MIB, the WinSetup help system,
or any manual for the CP-2402e or any other Quartz control panel.

**Nothing here is bench-tested** except the one item marked user-reported in §7.1.

**Two contradictions internal to this manual are recorded and left unresolved** —
frame depth (§2.1) and Ethernet link rate (§6.3). Both are Evertz against Evertz.

**One transcription caution:** §3.1.2's cable-equalization row mixes units and
letter case in Evertz's own text. It is quoted verbatim in §3.2 and must not be
tidied — an earlier session silently normalized it and that was an error.

---

## 1. The model line

**Verified [Official]** — §1, §1.1 pp. 1–2.

A matrix router for small routing applications: 32×32 in 2RU, or 16×16 / 16×4 /
16×2 / 32×4 / 32×24 in 1RU. **Input and output stages are fixed and not
expandable** — there is no card-add path on any model.

Format-independent data paths carrying **3 Mb/s to 3 Gb/s** on the 3G coax
versions, **3 Mb/s to 1.5 Gb/s** on the -H versions. Supported: SD-SDI, HD-SDI,
DVB-ASI, SMPTE 310.

Full model list as printed in §1: EQT-3232-H, EQT-3232-3G, EQT-3232-3G-F,
EQT-1616-H, EQT-1616-3G, EQT-1604-H, EQT-1604-3G, EQT-1602-3G-CS, EQT-3204-3G-CS,
EQT-3224-3G.

Suffix meaning, read off that list and §1: **-H** = 1.5 Gb/s ceiling, **-3G** =
3 Gb/s, **-F** = fiber, **-CS** = clean switch. The 1616 exists only as -H or -3G;
there is no 1616 fiber or clean-switch variant.

### 1.1 Revision history of this manual

**Verified [Official]** — p. i. Useful because it dates individual figures.

| Rev | Change | Date |
|---|---|---|
| 1.2 | Added panel configuration information | Jun 2009 |
| 1.3 | Revised configuration information; **added 16x16 and 16x4 versions** | Mar 2010 |
| 1.4 | Removed references to using Q-Link to connect frames, in Manual Remote Control | Jul 2011 |
| 1.5 | Added -CS Clean Switch version information | Aug 2011 |
| 1.6 | Updated "RS-422 Pin Out" table | Jun 2012 |
| 1.7 | Added NEBS documentation | Oct 2012 |
| 1.8 | Updates throughout | May 2013 |
| 1.8.1 | Added additional NEBS warning re shielded Cat-5 cables | May 2013 |
| 1.8.2 | **Updated Cable Equalization information** | Jul 2013 |
| 1.9 | Updates throughout | Dec 2013 |
| 1.9.1 | Updated notes and figures | Jan 2014 |

Two things this dates: the 1616 is a **2010 addition** to a line that started as
the 3232, and the cable-equalization figures in §3.2 are the **most recently
revised numbers in the document** (Jul 2013).

Evertz's own front matter states that information is periodically updated and
that changes are incorporated into subsequent editions. **1.9.1 is the newest
revision held**; whether a later one exists has not been checked.

---

## 2. Physical

**Verified [Official]** — §3.1.8 p. 22.

| | 1RU frames (incl. EQT-1616) | 2RU (EQT-3232) | -CS |
|---|---|---|---|
| Height | **1.75" / 44.5 mm** | 3.5" / 89 mm | — |
| Width | **19" / 483 mm** rack mount | 19" / 483 mm | — |
| Depth | **11.2" / 284 mm**, over hinges and BNCs | 10.3" / 262 mm, over hinges and BNCs | 18.75" / 477 mm, over hinges and BNCs |

**Weight: 6 kg fully loaded.** Stated once, with no per-model split — it is not
known whether 6 kg is the 1RU figure, the 2RU figure, or a line-wide
approximation. ⚠️ Do not quote it as the 1616's weight specifically.

Operating temperature **0 °C to 40 °C**. Cooling is **fan-assisted convection,
front to rear** (§2.2.1, §3.1.8); -CS frames are left-to-right instead.
§2.2.1 notes power dissipation is low across the line.

### 2.1 ⚠️ Depth contradiction — Evertz against Evertz

| Source | Claim |
|---|---|
| §2.2.1 p. 7 | "The depth of all the frames is 262mm, except the –CS and EQT-3224 versions which are 477mm deep" |
| §3.1.8 p. 22 | 262 mm **2RU**, **284 mm 1RU**, 477 mm -CS |

**284 mm is the figure to design against**, on three grounds, stated as
reasoning and not as a resolved fact:

1. §3.1.8 breaks depth out by frame size — three entries, each with its own inch
   conversion. §2.2.1 gives one blanket number inside an installation note.
2. Both sections agree on 477 mm for -CS, so they are not independent
   measurements; §2.2.1 reads as the 2RU figure generalized with the 1RU case
   missed.
3. The gap is 22 mm — under an inch, and in the conservative direction.

**Unresolved until someone puts a tape on a 1RU frame.** Neither figure has been
measured. Both are kept.

Separately, §2.2.1 warns that rack allowance must be made for the rear cabling on
top of the chassis depth. With 16 in + 16 out on BNC, the bend radius of the coax
is the real depth constraint, not the 284 mm — reasoning, not a manual claim.

### 2.2 Front access

**Verified [Official]** — §4.1.1 p. 26.

The front door opens on **two thumb screws**. With it open, **both power supplies
and the main processing module pull from the front**, so a PSU or main-module
swap does not require pulling the frame or disturbing rear cabling. (-CS frames
have no front access to electronics or supplies.)

---

## 3. Video signal

### 3.1 Inputs

**Verified [Official]** — §3.1.2 p. 21.

| Parameter | Value |
|---|---|
| Standards | SMPTE 259M, SMPTE 292M, SMPTE 310M, SMPTE 424M, ASI |
| Signal level | 800 mV p-p |
| Impedance | 75 Ω terminating |
| Return loss | >15 dB typical (5–1485 MHz) |
| Connectors | BNC per IEC 61169-8 Annex A |

### 3.2 Cable equalization — quoted verbatim

**Verified [Official]** — §3.1.2 p. 21. Evertz's line, unaltered:

> Belden 1694A 200m @ 270MHz, 150m @1.5Gb/s, 100M @ 3Gb/s

⚠️ **Two oddities in Evertz's own text, kept deliberately.** The first figure is
given in **MHz** while the other two are in **Gb/s** — a mixed-unit row. And the
third distance is written **100M**, capital M, where the other two are lowercase
`200m` / `150m`. Read in context it is plainly 100 metres, but it is not written
that way, and this row was the subject of the Jul 2013 revision (1.8.2), so it is
the most deliberately-set text in the spec table. **Do not normalize either
oddity when quoting.**

Practical reading, as reasoning: roughly 200 m at SD, 150 m at 1.5 Gb/s, 100 m at
3 Gb/s on 1694A.

### 3.3 Outputs

**Verified [Official]** — §3.1.3 p. 21.

| Parameter | Value |
|---|---|
| Signals supported | SMPTE 259M, 292M, 310M, 424M, ASI |
| Reclocking | Configurable (also configurable non-reclocking) |
| Signal level | 800 mV p-p ± 10% |
| Impedance | 75 Ω terminating |
| Return loss | >15 dB typical (5–1485 MHz) |
| DC offset | 0 ± 0.5 V |
| Output jitter | 0.2 UI |
| Connectors | BNC per IEC 61169-8 Annex A |

### 3.4 Rate handling

**Verified [Official]** — §1.4, §1.5 p. 2.

**Automatic Bit Rate Detection on the input equalizer allows any mix of HD and SD
signals in the same frame** — no per-input standard setting is required for a
mixed rack.

The feature list states **143 to 540 Mbit** compatible SDI and **143 Mbit to
2.97 Gbit** compatible HD-SDI/SDI for coax versions, plus **equalizer bypass for
sub-143 Mbit operation**. ⚠️ Note this sits alongside §1's blanket "3 Mb/s to
3 Gb/s" — the 3 Mb/s floor is reachable only with the equalizer bypassed. The
manual states both and reconciles neither.

### 3.5 Video is not processed

**Reasoned from the block diagram (§4.1, Figure 4-1 p. 23), not stated as a
latency figure anywhere.** The signal path is EQ → crosspoint → reclocker. There
is no frame store, no scaler, no format conversion on the standard coax models —
clean/quiet switching and line buffering exist only on -CS frames.

⚠️ **No latency, delay, or propagation figure for the EQT appears anywhere in this
manual.** Checked: §3.1.2, §3.1.3, §3.1.6, §3.1.7, §3.1.8, §3.1.9, §4.1. It is a
verified absence, not an oversight in reading. **No EQT latency number may enter
a show plan or a client quote from this library** until one is measured or a
datasheet supplies it.

---

## 4. Reference and switching

**Verified [Official]** — §2.8 p. 16, §3.1.6 p. 22.

| Parameter | Value |
|---|---|
| Switching reference | Analog 525 / 625 / tri-level HD, **looping** |
| Signal level | 1 V p-p ± 3 dB |
| Impedance | 75 Ω |
| Connector | BNC per IEC 61169-8 Annex A |
| Switching line | Lines 10/273 (525), Lines 6/319 (625), Line 7 (HD) |

**Ref 1 is the terminated input; Ref 2 is a passive loop-through.**

**An analog reference must be present for crosspoint changes to fall in the
field-blanking interval. With no reference, routing happens asynchronously** —
§2.8.1 is explicit about this, and it is the single most show-critical line in
the manual. §2.8.1 refers clean-switching problems to Evertz application note
**AN-0008**, which is not held.

**Termination is a jumper, not a menu item:** **J21**, at the rear of the main
module, `75R` to terminate the reference loop input, `HI-Z` for high impedance.
Physical access required.

Front-of-rack indication is via two rear LEDs — see §5.

---

## 5. Rear panel indicators

**Verified [Official]** — §2.8.1 p. 16, §2.9 pp. 16–17.

| LED | Colour | Meaning |
|---|---|---|
| REF LOCK | Green | On = valid reference on the REF BNC; off = none applied |
| GEN ERROR | Red | On = error detected with the reference; off = reference valid |
| PWR1 | Green | On = **left** supply (viewed from the front) functional |
| PWR2 | Green | On = **right** supply (viewed from the front) functional |
| PROC OK | Green | On = main board booted and in operating mode; off = boot problem |
| 10/100 | Amber | On = 100Base-TX last detected; off = 10Base-T last detected. **Off at power-up** until rate detection completes |
| LN/ACT | Green | On = valid link to the hub; blinking = sending/receiving; off = no valid connection |

GEN ERROR and PROC OK are **absent** on EQT-1602-CS, EQT-3204-CS and EQT-3224
newer rear plates — present on the 1616.

---

## 6. Control

### 6.1 Q-Link

**Verified [Official]** — §2.3.4 p. 10, §2.3.4.1 p. 11, §4.4.2 p. 36.

Evertz's proprietary single-transmission-line control bus, coax versions only
(not available on -F fiber).

- **One terminated 75 Ω BNC plus a second BNC as loop-through** on the rear.
- Standard 75 Ω video cable, **daisy-chained panel to panel, 500 m maximum.**
- **The installer must fit a 75 Ω terminator at each end of the cable.**
- **Stubs are not supported.** §2.3.4.1 warns that running spurs to save cable
  may cause data errors under some conditions — daisy-chain only.
- Every device on the chain needs a **unique Q-Link address**, set in
  configuration (front panel `QLAD`, or telnet menu — §7, §8).

### 6.2 Serial

**Verified [Official]** — §2.4 pp. 11–12, §4.4.3 p. 36.

One **DB9 female** connector. **Quartz (-1) protocol, slave end** — any control
device speaking Quartz can drive the router. Protocol documentation is not
public: §2.4 and §4.4.3 both say contact Evertz service.

RS422 is standard; RS232 is an option.

| Pin | RS422 | RS232 |
|---|---|---|
| 1 | 0V | 0V |
| 2 | Tx+ | TXD |
| 3 | Rx+ | RXD |
| 4 | 0V | 0V |
| 5 | — | — |
| 6 | 0V | 0V |
| 7 | Tx− | RTS |
| 8 | Rx− | CTS |
| 9 | — | — |

The RS-422 table was revised in manual rev 1.6 (Jun 2012) — see §1.1.

### 6.3 Ethernet

**Verified [Official]** — §2.6 pp. 13–14, §3.1.7 p. 22, §4.4.1 p. 35.

One RJ-45. Straight-through cable, Cat 5 required for 100Base-TX.

⚠️ **Link-rate contradiction — Evertz against Evertz:**

| Source | Claim |
|---|---|
| §2.6.1 p. 13 | "The EQT uses 10Base-T (10 Mbps), 100Base-TX (100 Mbps) or **Gigabit (1Gbps)** twisted pair Ethernet cabling systems" |
| §3.1.7 p. 22 | "Ethernet: **10/100baseT**, 1x RJ45" |

Unresolved. The rear-panel LED is labelled **10/100** and §2.6.1's own LED
description covers only the 10 vs 100 states, which leans toward 10/100 —
reasoning, not proof. **Design for 10/100.** A control link does not need more,
so this matters for switch-port planning and nothing else.

Cable runs: **90 m (300 ft) router to switch; 205 m (675 ft) combined between any
two endpoints.**

**Quartz (-1) protocol over Ethernet, slave end.** §4.4.1 names the **CP-2116E**
and **CP-2232E** as panels offering direct router control, and otherwise refers to
"Ethernet panels" generically.

### 6.4 Panel count ceiling

**Verified [Official]** — §4.4.3 p. 36. Stated once, as a note:

> **Maximum 6 Q-Link panels, or 20 R-Link panels.**

⚠️ **"R-Link" appears exactly once in the entire manual, here, and is defined
nowhere in it** — not in §1.8's glossary, not in the control sections. Whether it
means the Ethernet panel path (RouterLink, §10.1) under another name is
**unconfirmed**. Treat the 20 as unattributable until an Evertz source defines
the term.

### 6.5 Alarm contact

**Verified [Official]** — §2.7 p. 15.

2-pin terminal, **isolated closure**, two states: open (device OK) or closed
(internal fault detected, **or power lost**). Requires an external indicator and
supply: **12 VDC maximum, current limited to 20 mA.**

Not available on EQT-1602-CS, EQT-3204-CS or EQT-3224 newer rear plates —
present on the 1616.

---

## 7. Front-panel menu

**Verified [Official]** — §4.2.1 p. 28. Present on all models **except EQT-3224
and -CS versions** — so present on the 1616.

Shaft encoder plus a four-digit dot-matrix display. Rotate the encoder in either
direction to enter the menus. Each menu offers **View**, **Set** and **End**.
Press the encoder on a parameter to select it — it underlines and flashes — turn
to change, press again to commit, then scroll to End.

| Code | Sets |
|---|---|
| `QLAD` | Q-Link address |
| `IPAD` | IP address |
| `NETM` | Subnet mask |
| `DHCP` | DHCP on/off |

**The router must be rebooted for network changes to take effect** — stated twice
(§4.2.1, §4.2.5).

§4.2.3 adds that the dot-matrix display shows the router's current TCP/IP address
at rest, which makes the front of the frame the fastest way to read an address
you have lost.

### 7.1 Factory default IP — ⚠️ unverified for the 1616

The only default IP addresses in the manual are in **§4.2.2 p. 28**, a section
titled *"Setting the IP Addressing for the EQT **Clean Switch**"*, covering the
EQT-3224-3G, EQT-1602-3G-CS and EQT-3204-3G-CS. It lists:

| Component | Default |
|---|---|
| Router component | **192.168.9.190** |
| Clean/quiet switch component | 192.168.9.191 (and .192 on the 3204) |
| Control panel component | 192.168.9.193 |

with a note that the router and control-panel defaults "always stay the same."

⚠️ **Whether 192.168.9.190 is also the factory default on a standard EQT-1616-3G
is not stated anywhere in this manual.** The section is written for multi-component
CS frames; the note's "always" is scoped to those components. It is a plausible
line-wide default and it is **not confirmed** — do not put it in a commissioning
sheet as the 1616's default.

What settles it: a factory-reset 1616, or any 1616 still on its shipped address,
read off the dot-matrix display.

**User-reported, this session:** the user has already re-addressed their
EQT-1616-3G using the front-panel dot-matrix menu above, which confirms §4.2.1's
menu is present and functional on the 1616-3G in the field. Their unit is
therefore no longer on any factory default, and cannot be used to settle the
question above.

---

## 8. Telnet configuration and monitoring menu

**Verified [Official]** — §4.2.3–§4.2.9, §4.2.11 pp. 31–35.

Reached over **TCP port 4000**:

```
telnet 192.168.9.190 4000
```

⚠️ **Port 4000 cannot be used for controlling the router or for connecting to
Magnum** — it is the config/monitor server port only. Router control lives on the
WinSetup-defined ports (§10.4).

Menu items are selected by the number printed beside them. Exit with **Ctrl-D**
or by closing the session.

Top level:

| Menu | Purpose |
|---|---|
| Network Configuration | Network settings |
| SNMP Setup | SNMP settings |
| Status Monitoring | Crosspoint and signal path monitoring |
| Engineering/Debug | Video signal and frame configuration |

**Network Configuration** — Set IP Address, Set Netmask, Set Gateway, Set
Broadcast Address, Use DHCP, View Live Network Settings. Reboot required.

**SNMP Setup** — Set Trap IP Address, Remove Trap IP Address, Set Read Only
Community String, Set Read Write Community String.

**Status Monitoring** — two items, both useful cold:

- **View Live XPT Status** — which input is currently mapped to each output.
- **View Video Signal Information** — per input and output: locked status, video
  standard, reclocker status.

**Engineering/Debug** — View/Set Frame Configuration, View/Set Video Signal
Configuration, View/Set Test Modes (enables/disables **Chop Switch Test mode**),
Trace Information (crosspoint, serial port and socket port traces), Reboot.
§4.2.8 warns that anything in this menu not documented in the manual should not
be touched under normal circumstances.

**View/Set Frame Configuration** (§4.2.9) — View Frame Information, Set QLink
Address, Set Number of Inputs, Set Number of Outputs, **Set Level Number
(currently only Level 1 is supported)**, **Set Xpt Restore at Bootup**.

The Q-Link address set here **must match the one entered in WinSetup's frame
dialog** (§10, step 2).

### 8.1 Video signal configuration

**Verified [Official]** — §4.2.11 pp. 34–35. The per-signal controls:

| Item | Effect |
|---|---|
| View Video Signal Configuration | Input standard, output cable driver and reclocker status |
| Set Video Input Standard | Sets the device's input video standard |
| Set Cable Driver Slew Rate Control | Automatic or Manual |
| Set Cable Driver Slew Rate | HD or SD — **only when control is set to Manual** |
| Enable/Disable Cable Driver | Output driver on/off |
| Set Output Reclocker Data Rate Mode | Auto or Manual |
| Set Output Reclocker Data Rate | SD, HD or 3G — **only when mode is Manual** |
| Enable/Disable Output Reclocker | Reclocker on/off |
| Set Output Reclocker Routing Mode | Bypassed or Auto Bypassed |
| View Live Video Signal Configuration | Current state |

The slew-rate and reclocker pairs are the practical controls for a
non-standard-rate or ASI feed: force the reclocker off or bypassed rather than
letting auto-detect fight a rate it does not recognize — reasoning, not a manual
recommendation.

---

## 9. VistaLINK / SNMP

**Verified [Official]** — §5.1–§5.8 pp. 37–44. (-CS tabs §5.9–§5.12 not read.)

Evertz's SNMP monitoring platform. The MIB is available from Evertz on request
for third-party managers. §4.3 adds that system monitoring covers power supply
voltages and interior temperatures, and that the alarm contact is user
configurable.

**General tab (Table 6):** Video Input Standard (settable), Card Type, Q-Link
Address, Number of Video Inputs, Number of Video Outputs, **Reference Detected**,
**Reference Standard**, PSU 1 Status (left, from front), PSU 2 Status (right),
**Temperature**, Serial Port 1 Standard (RS-232 or RS-422).

**Input Monitor (Table 7):** Input Status — Valid or Invalid, per input.

**Output Control (Table 8):** Output Status — enables or disables video on each
output BNC.

**Reclocker Control (Table 10):** Reclocker Status — enable/disable per output.

**Crosspoint Control (Table 11):** Crosspoint Control — sets the input routed to
each output BNC. **This is the SNMP route to taking crosspoints.**

**General Faults (Table 12):** Temperature Warning, Right Power Supply Failure,
Left Power Supply Failure — each raises a trap.

Note the asymmetry worth knowing before building a monitoring plan: **reference
presence and standard are readable on the General tab but raise no trap** in
Table 12. The only trap sources on a standard frame are temperature and the two
supplies. Loss of reference — the thing that silently turns clean switching into
asynchronous switching (§4) — **is not a trap.**

---

## 10. Configuration with WinSetup

**Verified [Official]** — §6 pp. 49–55.

WinSetup defines signal levels, frames, source and destination names, and panel
behaviour.

⚠️ **A specific version of WinSetup is required.** Check **Options ▸ System
Version**; the correct build lists **SC-500E as the only system** inside the
Routing System Controller box. Press F1 from any dialog for the help system.

Order of work — menus grey out deliberately to enforce it:

1. **Levels** — name each signal level. **Do not tick "Complex"** at this stage.
2. **Frames** — New, pick the router from the list. The only change needed in
   Edit Frame is the **Q-Link address**, which must be unique across the system
   and **must match the address set on the router** per §8 / §7.
3. **Sources** — Add to fill the table with SRC-1…SRC-X; rename later.
4. **Destinations** — same method.
5. **Panels** — New lists every Evertz panel **by part number. Select the part
   number printed on the panel's serial-number label; ignore the A/E
   designation**, because the connection method is set in the panel config
   dialog instead. Program each button in the Key section, name the panel, and
   set its power-up defaults. Q-Link address is auto-allocated and editable.
6. **Download** — System ▸ Download-to-Router.

**Two hard constraints on the download:**

- **Ethernet only. The EQT configuration cannot be downloaded serially.**
- **It must use port 2500.**

⚠️ **Save the WinSetup file. The configuration CANNOT be retrieved from the
router.** There is no read-back. A lost setup file is a rebuild from scratch.

### 10.1 Control panel Ethernet interface

**Verified [Official]** — §6.1.1 p. 53. Edit Frame ▸ Port Setup.

Defined as a **UDP interface using the RouterLink protocol**, and **the port is
always 90**. One interface serves all Ethernet-connected panels.

In each panel's own configuration, **tick "Use Ethernet"** and enter **the
panel's IP address** — that checkbox is what distinguishes an Ethernet panel from
a Q-Link one.

### 10.2 Control panel Q-Link interface

**Verified [Official]** — §6.1.2 p. 54. Defined as a **QLINK1 interface using the
Qlink (Hosted Panels) protocol**. Panels then connect to the physical BNC labelled
**Q-Link 1** on the rear.

### 10.3 Serial interface

**Verified [Official]** — §6.1.3 p. 55. Defined as a **COM1 interface using the
Quartz protocol**, for external automation. Baud rate, parity, data bits, stop
bits and standard (RS232 or RS422) are all set in this dialog.

### 10.4 Ethernet control interface

**Verified [Official]** — §6.1.4 p. 55. For external control over Quartz protocol.
**Up to four control ports: 3737, 3738, 3739, 3740.**

### 10.5 CP-2402e — what this manual does and does not say

The **CP-2402E appears exactly once in the whole document**, in §6 step 5 p. 52:

> For -CS versions that are equipped with a local control panel, an Ethernet
> panel configuration must be defined using the type CP-2402E.

That is the entire coverage. What follows from it, marked by tier:

- **Verified:** it is configured in WinSetup as an **Ethernet** panel type, and
  on -CS frames it is the built-in local panel.
- **Verified, general:** any Ethernet panel hosts on **UDP port 90, RouterLink**
  (§10.1), needs "Use Ethernet" ticked with its own IP, and is selected in
  WinSetup by the part number on its serial label.
- ⚠️ **Unverified:** whether a CP-2402e can be hosted by a **standard,
  non-CS** frame such as the EQT-1616-3G. Nothing in this manual forbids it, and
  §6.1.1's panel-Ethernet interface is described generically. But the only
  statement about this panel scopes it to -CS frames, and **absence of a
  prohibition is not a permission.**
- **Unknown entirely:** the panel's own addressing, button-count, layout,
  power, and firmware path. §4.4.1 and §4.4.2 both say to consult the panel's own
  instruction manual, which is not held.

**The CP-2402e manual is the highest-value missing document for this user's rig.**

---

## 11. Firmware upgrade

**Verified [Official]** — §7.1 pp. 57–59, §7.3 pp. 60–61. (§7.2, the -CS path,
not read.)

Standard path, for any EQT on firmware **1.0 build 001 or later** — browser only,
no special tool:

1. Browse to the router's IP in any standard web browser on the same network.
   The page shows the **current firmware version**.
2. **Browse…** and select the new **`.img`** file.
3. Upload — the system verifies the file is valid before an Upgrade button
   appears.
4. **Upgrade**, wait for the success message, then **restart the EQT** as
   instructed.

⚠️ **Only if the unit is on firmware older than 1.0 build 001** (§7.3), which
predates the built-in web server, the path is FTP plus telnet. Log in as **`root`
/ `evertz`**. Put the `.img` in `/tmp`:

```
type binary
```

```
cd /tmp
```

```
put C:\temp\LATEST_IMAGE.img
```

```
close
```

```
quit
```

Then, **without powering down**, telnet in and run:

```
cd /tmp
```

```
ls
```

```
upgrade LATEST_IMAGE.img
```

A success message prints at the Linux prompt. **Power cycle and verify the new
code is loaded and booting.**

---

## 12. Power

**Verified [Official]** — §2.9 pp. 16–18, §3.1.9 p. 22.

| Parameter | Value |
|---|---|
| Input voltage | Auto-ranging 100–240 V AC, 50/60 Hz, auto-sensing |
| Input power | **60 W (1RU)** / 200 W (2RU) |
| Fuse, EQT-16xx | **2 A, 250 V, time delay, 5 × 20 mm** |
| Fuse, EQT-3232 | 3.15 A, 250 V, time delay, 5 × 20 mm |
| Cord | Minimum 18 AWG, type SVT marked VW-1, 2.5 m maximum |

The power entry modules carry a standard IEC inlet and an EMI line filter; the
fuse holder is **inside the power supply module**.

**Redundancy is optional and hot-swappable.** EQT-3232, EQT-1616, EQT-1604 and
EQT-3232-3G-F take a supply on one side and an optional second on the opposite
side. Either can be removed for service without pulling the frame.

⚠️ **Before pulling a supply, remove the rear screw labelled "PSU Mount."** On
earlier frames that screw may be unlabelled — §2.9.1 Figure 2-8 p. 18 shows the
locations per model.

Each supply carries two LEDs: **green PSU STATUS** (that supply's health) and
**red FRAME STATUS** (whole-frame health, driven by the frame status bus).
FRAME STATUS is normally **off**. On any supply fault — cord out, switch off,
fuse blown, **rear fan stopped** — that supply's PSU STATUS goes off and **the red
FRAME STATUS lights on both supplies**, while the healthy supply's PSU STATUS
stays on. With VistaLINK connected, the fault also sends a trap.

§2.9 notes the supplies are short-circuit protected and **should not blow a fuse
under a short**; a blown fuse is grounds for contacting Evertz rather than simply
refusing.

NEBS installations (§2.10 p. 19): primary grounding is through the AC mains earth
connector, cords must be secured with the supplied retaining clips, and the cords
must run to an external surge protection device.

---

## 13. Verification status

| Section | Tier | Basis |
|---|---|---|
| §1 model line, §1.1 revision history | **Verified [Official]** | Manual §1, §1.1, p. i |
| §2 physical dimensions | **Verified [Official]**, one internal contradiction | §3.1.8 vs §2.2.1 |
| §2 weight | **Verified [Official]** but unattributed to a model | §3.1.8, single figure |
| §2.1 which depth to design against | **Reasoned** | Argument stated, not measured |
| §3 input/output/EQ specs | **Verified [Official]** | §3.1.2, §3.1.3 |
| §3.5 no processing / no latency figure | **Verified negative** | Seven sections checked |
| §4 reference and switching | **Verified [Official]** | §2.8, §3.1.6 |
| §5 rear LEDs | **Verified [Official]** | §2.8.1, §2.9 |
| §6 control paths and pinouts | **Verified [Official]** | §2.3.4, §2.4, §2.6, §4.4 |
| §6.3 Ethernet rate | **Contradiction, unresolved** | §2.6.1 vs §3.1.7 |
| §6.4 R-Link | **Verified [Official]** as printed; **term undefined** | §4.4.3, one occurrence |
| §7 front-panel menu | **Verified [Official]** | §4.2.1, §4.2.3 |
| §7.1 default IP for a 1616 | ⚠️ **Unverified** | §4.2.2 is CS-scoped |
| §7.1 front-panel menu works on a 1616-3G | **User-reported**, this session | User re-addressed their own unit |
| §8 telnet menus | **Verified [Official]** | §4.2.3–§4.2.9, §4.2.11 |
| §8.1 closing paragraph | **Reasoned** | Not a manual recommendation |
| §9 VistaLINK tabs | **Verified [Official]** | §5.1–§5.8 |
| §9 reference raises no trap | **Verified negative** | Table 12 contains three traps |
| §10 WinSetup | **Verified [Official]** | §6, §6.1.1–§6.1.4 |
| §10.5 CP-2402e on a non-CS frame | ⚠️ **Unverified** | Single scoped mention |
| §11 firmware | **Verified [Official]** | §7.1, §7.3 |
| §12 power | **Verified [Official]** | §2.9, §3.1.9, §2.10 |

**Nothing in this document is bench-tested.** No EQT was powered, no command
sent, no dimension measured.

---

## 14. Open items

1. **Frame depth: 262 mm or 284 mm?** One tape measure across a 1RU frame,
   front face to rear-most BNC. Closes §2.1 permanently.
2. **Is 6 kg the 1RU weight, the 2RU weight, or a line average?** One luggage
   scale. Matters for flight-case and shelf loading.
3. **Factory default IP on a standard EQT-1616-3G.** Needs a factory-reset unit
   or one still on its shipped address. §4.2.2's `192.168.9.190` is CS-scoped.
4. **Can a CP-2402e be hosted by a non-CS EQT frame?** The panel's own manual, or
   a bench attempt: define it in WinSetup as an Ethernet panel on port 90, give
   it an IP, see whether it takes crosspoints. **Highest-value open item for the
   user's actual rig.**
5. **What is "R-Link"?** Named once (§4.4.3) with a 20-panel ceiling, defined
   nowhere. Possibly RouterLink under another name — unconfirmed.
6. **EQT latency.** No figure exists in this manual. A two-leg 240 fps phone test
   against a known-good reference would give the library its first EQT number.
7. **Evertz application note AN-0008**, named in §2.8.1 for clean-switching
   problems. Not held.
8. **The Quartz (-1) protocol specification.** Both §2.4 and §4.4.3 refer to
   Evertz service. Without it, external control of this router cannot be written
   from this library — this is the gate on any TouchDesigner or Companion
   integration, and belongs in `creative-coding/references/protocols/` when
   obtained, **not here.**
9. **Whether a manual revision later than 1.9.1 (Jan 2014) exists.** Not checked.
10. **The WinSetup build that lists SC-500E**, and where it is obtained. §6 names
    the check but not the source.
11. **Does the 1616 rear plate physically label Q-Link 1 vs the loop-through?**
    §6.1.2 refers to "the physical port that is labeled Q-Link 1"; Figure 2-2's
    extracted labels show `Q-LINK` and `REF` without numbering. Unresolved from
    the text layer — a rear-panel photograph settles it.
