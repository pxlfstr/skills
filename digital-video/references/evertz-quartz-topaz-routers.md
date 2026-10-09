# Evertz (Quartz) Topaz Routers

Small fixed-size Quartz-family matrix routers. Scoped to the **QT-3232N** — the
32×32 analog (composite) video frame — as the unit in hand. SD, HD and analog
audio Topaz frames appear only where the manual treats the line as one.

## Provenance

**Single source, Verified [Official] throughout:** *Topaz Routing System
Manual*, Evertz Microsystems, **Version 2.0, January 2009**, 38 PDF pages
(numbered pp. i–vi, 1–28), user-supplied 2026-10-08 (md5
`a98ffb56799ccc3f66db28541d34fb4d`). Text layer extracted and read end to end;
pages carrying figures needed for this document (PDF pp. 14, 17, 26, 34, 35)
were also read as images. The PDF is copy-restricted; nothing here is pasted
from it — figures are transcribed, prose is paraphrased.

**Revision history (p. i):** 1.09 "Quartz Version" Mar 2006; 2.0 "Evertz
Formatting" Jan 2009. So the content is Quartz-era, re-badged by Evertz. Whether
a later revision exists has not been checked.

**Never read:** any Topaz datasheet or product page, the Quartz protocol
specification, Quartz **MANUAL-05** (Q-Link panels, named in §3.10), the WinSetup
help system, or any Evertz/Quartz source giving network port numbers.

**Two user-reported bench results** (§6.3) — the only non-manual facts here:
the EQT's ports are not open, and **TCP 255 is**.

**Contradictions internal to this manual, kept unresolved:** frame depth (§2),
DIP switch numbering (§7), and whether third-party control runs over Ethernet
(§6.4). All are Evertz/Quartz against itself.

**The headline negative:** this manual gives **no TCP/UDP port number, no
default IP address, and no method for setting an IP address** anywhere (§6.3).

---

## 1. The line

**Verified [Official]** — §1, §1.1 pp. 1–2, §3.1 p. 11.

Fixed-size stand-alone routers, one signal format per frame, each with a
built-in controller. **I/O is fixed and cannot be expanded** beyond the frame
size (8, 16 or 32).

| Format | Manual's part names | Size |
|---|---|---|
| Analog video (AV) | QT-1616N / QT-3232N (§1.1, §4.1); QT-AV-1616 / QT-AV-3232 (§3.1.1.1) | 16×16, 32×32, 2RU |
| SD digital | QT-…S; QT-SD-1616 / -3232 | 16×16, 32×32, 2RU |
| HD/SD digital | QT-…H; QT-HD-1616 / -3232; QT-0808H | 8×8, 16×16, 32×32, 2RU |
| Analog audio | QT-…-AA; QT-AA-1616 / -3232 | 16×16, 32×32, 2RU |

⚠️ **The manual uses two naming schemes and never maps them.** That QT-3232N =
QT-AV-3232 is **inferred** from both being the 32×32 analog video frame — not
stated.

Options (§3.1.1.2): QT-PS spare/backup PSU, QT-TR and QT-TL PSU mounting trays.
Frames can be stacked for multi-level (video + audio, or component on three
frames) or split into virtual levels; up to three can cascade to 64×16 for
monitoring (§3.8.1).

---

## 2. Physical — QT-3232N

**Verified [Official]** — §4.1.10 p. 18, §2.2.1 p. 3.

| Item | Figure |
|---|---|
| Height | 3.5" (90 mm), 2RU |
| Width | 19" (483 mm) |
| Weight | Frame 1.45 kg, PSU 0.4 kg |
| Operating temp | 0–40 °C ambient; spec maintained 10–30 °C |
| Humidity | 10–90% non-condensing |
| Cooling | Natural convection, silent |

### 2.1 ⚠️ Depth contradiction — three figures

| Source | Says |
|---|---|
| §4.1.10 (QT-N spec) | **4.75" (260 mm)** |
| §2.2.1 (installation) | Analog Video frames **275 mm** plus connectors |
| §4.2.8 / §4.3.8 (SD/HD spec) | 4.75" (120 mm) |

Arithmetic: 4.75" × 25.4 = **120.65 mm**; 260 mm ÷ 25.4 = **10.24"**; 275 mm ÷
25.4 = **10.83"**. So the QT-N row's inch and mm figures disagree with each other.
The 4.75" looks copied from the SD/HD rows — reasoning, not proof. **Design
for 275 mm plus connectors and cable bend** until measured.

---

## 3. Video — QT-3232N

**Verified [Official]** — §3.4 p. 13, §4.1.2–§4.1.6 pp. 17–18.

| Item | Figure |
|---|---|
| Nominal level | Video 1 V p-p; sync pulse (separate H+V) 2 V p-p |
| Max level, DC-restored inputs | Video +6 dB; sync 2.5 V p-p |
| Max level, DC-coupled inputs | Video ±0.7 V |
| Input impedance | 75 Ω terminating |
| Input return loss | 40 dB, 5–270 MHz |
| DC on input (DC restored) | ±3 V |
| Output impedance / return loss | 75 Ω; 40 dB to 5.5 MHz |
| DC on output | ±50 mV |
| Insertion gain | ±0.1 dB; spread between inputs ±0.05 dB |
| HF response | ±0.1 dB 15 kHz–5.5 MHz; ±0.2 dB 5.5–10 MHz; +0.5/−1.0 dB 10–100 MHz; smooth roll-off above |
| LF tilt at 50 Hz | ±0.5% |
| Y-C gain / delay inequality | ±0.5% / ±5 ns |
| Diff gain / diff phase (10–90% APL) | 0.25% / 0.15° |
| Path length | 13 ns typical |
| Crosstalk at 5.5 MHz | −60 dB worst case |
| Noise to 5.5 MHz | −70 dBrms |
| Connectors | BNC per IEC 61169-8 Annex A |

§3.4: DC-coupled inputs so it handles composite **or component**; output
bandwidth over 100 MHz, adjustment-free. **DC restore is switchable** — SW1-8 on
QT-AV (§7). §3.4 also says the AV frame can route **unbalanced AES** (§2.3.3,
§3.6.2 agree: AES3-ID on 75 Ω through a video router).

**Dual outputs** (§2.3.1): on 32×32 frames, outputs **15, 16, 31, 32** have two
feeds; all others one.

**Path length 13 ns is the only delay figure in the manual.** For an analog
crosspoint this is the whole signal path — no frame store is described anywhere.

---

## 4. Reference and switching

**Verified [Official]** — §2.3.2 p. 5, §2.5.3.1 p. 9, §4.1.8 p. 18.

- Looping **Ref** input, any standard analog video with standard sync.
  Analog 625 or 525, 1 V p-p +6/−3 dB, 75 Ω.
- Vertical-interval switching per **SMPTE RP-168**: lines **6/319 (625)** or
  **10/273 (525)**, chosen by SW1-6.
- Field or frame switching by SW1-5 (frame-only matters for some editing).
- ⚠️ **No reference connected → crosspoints change at about 40 Hz**, i.e. not on
  the vertical interval. A missing Ref means visible switch glitches.

---

## 5. Power

**Verified [Official]** — §2.4 p. 7, §3.7 p. 14, §4.1.9 p. 18.

External auto-ranging brick, 100–240 V AC 50/60 Hz → 12 V DC, IEC inlet, about
1.7 m DC lead to a **two-pin bayonet locking** connector. **20 W.** Optional
redundant second brick (QT-PS). **No power switch** — pull the cord to service.
Power-fail alarm: relay contact rated 250 mA, 50 V, screw terminals.

---

## 6. Control paths

**Verified [Official]** — §1.1 pp. 1–2, §2.3.4–§2.3.7 pp. 6–7, §3.8 pp. 14–16,
§4.1.7 p. 18. Rear-panel labels read off Figure 2-5 (p. 4, low resolution):
`DIAGNOSTIC LEDS`, `SETUP` (DIP block), `FRAME ADDRESS`, `SERIAL COMMS`,
`ETHERNET`, `REF`, `Q-LINK`, `POWER`, `ALARM`.

### 6.1 Q-Link

75 Ω video cable, daisy-chained frame to frame and panel to panel, **500 m
maximum**, **75 Ω terminator at each end**, and terminate unused Q-Link ports
too. **No stubs** — panels join through a **T-piece**, which also lets one be
swapped without breaking the chain. **32 devices maximum**, frames and panels
together. Each device has a unique address on two rotary hex switches (00–3F).

### 6.2 Serial — D9 socket, RS-232 or RS-422

Always live; mode set by DIP switches (§7). Pinout for Ethernet-equipped Topaz
units (Figure 2-10):

| Pin | RS-232 | RS-422 |
|---|---|---|
| 1 | GND | GND |
| 2 | RTS | TX− |
| 3 | RXD | RX+ |
| 4 | 0V | RX 0V |
| 5 | Not used | Not used |
| 6 | 0V | TX 0V |
| 7 | TXD | TX+ |
| 8 | CTS | RX− |
| 9 | Not used | Not used |

⚠️ Earlier **QT-SD** units have TX± and RX± **inverted** on RS-422.

**PC cable, RS-232, three wires** (Figure 2-11), PC D9 socket → router D9 plug:

| PC pin | Router pin |
|---|---|
| 2 RXD | 7 TXD |
| 3 TXD | 3 RXD |
| 5 GND | 6 GND |

Not a standard null-modem cable — the router's TXD is on pin 7.

### 6.3 Ethernet — RJ45

Supports TCP/IP for exactly two stated functions: **setup download from
WinSetup** and **router control**.

⚠️ **Verified negative — the manual states none of the following anywhere:**
port numbers (TCP or UDP), default IP address, subnet, how to set or read the
IP, link rate, or which WinSetup build supports Ethernet download. Every search
of the text layer for a port or address came back empty, and the two WinSetup
figures read as images (pp. 24–25) show no network fields.

**Do not borrow the EQT's ports.** `evertz-eqt-routers.md` §8 and §10 give
2500 (download), 90 UDP (panels), 3737–3740 (control) and 4000 (telnet) — a
different, later product sharing only the WinSetup editor.

**User-reported, 2026-10-08:** on the user's QT-3232N, a PowerShell
`Test-NetConnection` check found **none of TCP 2500, 3737, 3738, 3739, 3740 or
4000 open.** ⚠️ Not yet established whether the IP tested was the router's and
reachable (no ping result recorded), so this rules out those ports **only if
the address was right.** UDP was not tested.

**User-reported, 2026-10-08 — TCP port 255 open.** An Nmap TCP scan of the
user's QT-3232N at its configured address (nmap reported the host up) found
**port 255 open**. ⚠️ Caveats, all open:
- A full-range `-T4 --min-rate 1000` scan hit Nmap's retransmission cap
  (the frame dropped probes), so **other open ports may have been missed**.
- **What 255 does is unknown** — WinSetup setup download, router control, or
  both. The manual names both functions over TCP/IP and gives no port.
- Not yet tested from WinSetup.

### 6.4 ⚠️ Third-party control path — manual contradicts itself

| Source | Says |
|---|---|
| §1.1 p. 2 | Third-party control **via the serial port** |
| §3.8.1 p. 14 | Third-party control via **serial port or Ethernet** |
| §1.1 Feature Summary | Lists "Ethernet control" |
| §1.1 Control para | Controller supports "a single Q-Link and Serial port" — no Ethernet mention |

Also §3.8.1: remote panels connect "via Q-Link **or Ethernet**", while §3.10
mentions Q-Link panels only. Protocol on serial: **Quartz standard**
(Figure 5-3), documentation not in this manual.

### 6.5 Panels

- **Local panel CP-2402-LP** fits QT-1616N/H and QT-3232N/H in place of the
  blank front (§1.1, §3.9). Figure 3-5 shows 24 source keys, TAKE, two
  up/down-paged displays.
- Passive panels CP-1601A-P, CP-1604-P via PI-1604 / PI-1608 parallel interface.
- Any Quartz Q-Link remote panel (MANUAL-05).

⚠️ **CP-2402-LP vs CP-2402e:** similar part numbers; whether they are the same
panel or related is **unknown** from this manual.

---

## 7. DIP switches and address

**Verified [Official]** — §2.3.6 p. 6, §2.5.1–§2.5.2 pp. 8–9.

8-way block, labelled `SETUP` on the rear:

| Switch | Up / On | Down / Off |
|---|---|---|
| SW1-1 | Force Quartz standard protocol and baud rate | Use WinSetup comms parameters |
| SW1-2 | Diagnostics mode | Protocol (remote control) mode |
| SW1-3 | Q-Link slave | Q-Link master |
| SW1-4 | Two PSUs fitted, alarm if one fails | One PSU |
| SW1-5 | Field-rate switching | Frame-rate switching |
| SW1-6 | 625 (lines 6/319) | 525 (lines 10/273) |
| SW1-7 | RS-232 | RS-422 |
| SW1-8, QT-AV | DC restore on | DC restore off |

⚠️ **Numbering contradiction:** §2.3.6 calls them "three rear panel DIP
switches" SW-1, SW-2, SW-7; §2.5.1 calls the same functions SW1-1, SW1-2,
SW1-7 on an 8-way block. Same switches, read as the §2.5.1 block.

On earlier Topaz SD units **without Ethernet**, SW1-4 instead chose
last-crosspoint vs forced-input at power-up. **Ethernet-equipped units always
power up on the last crosspoints** (§2.5.1); §3.8.1 adds that crosspoint state
survives power-down.

**Address:** two rotary hex switches, `FRAME ADDRESS`, range **00–3F**. Must be
unique on the Q-Link (§2.5.2). That it must also equal the frame's Q-Link
address in WinSetup's Edit Frame dialog is **reasoning** — this manual doesn't
say so (the EQT manual does, for the EQT).

---

## 8. WinSetup

**Verified [Official]** — §5 pp. 23–26, Figures 5-1 to 5-5.

Quartz System Configuration Editor. A factory default configuration is
installed (§3.1.1.2). F1 opens help from any dialog. Menus grey out to force
the order:

1. **Levels** — name each level. Don't tick **Complex** yet.
2. **Frames** — New, pick by the part number on the serial label; if no exact
   match, use a generic number. Figure 5-2's list shows analog video frames as
   `QXX00-AV-1604` … `QXX00-AV-3216`. Set the Q-Link address (hex) and attach the
   frame to its level. **Properties** tab (Figure 5-3): Master Frame, Boot with
   specific input, **Computer Interface fitted**, Protocol `Quartz standard`,
   optional override of comms parameters (screenshot defaults 9600 / None / 8 /
   1), Local Panel CP-1600 / CP-1600A. The manual calls this tab optional
   documentation.
3. **Sources** — Add fills SRC-1…SRC-x; rename later.
4. **Destinations** — same method.
5. **Panels** — New, pick by part number; program keys, name the panel;
   Q-Link address auto-allocated, editable.
6. **Download** — System ▸ Download-to-Router, **after setting the COM port
   and baud rate, normally 38400.**

⚠️ **The only download procedure in the manual is serial.** Ethernet download
is claimed in §2.3.5/§3.8.2 with no procedure.

⚠️ **The configuration cannot be read back from the router.** Save the file.

⚠️ **38400 vs 9600:** the download baud is "normally 38400"; the Properties
screenshot shows 9600 for the computer interface (automation port). Likely two
different settings — **reasoning, not stated.**

⚠️ **WinSetup version required for Topaz is not stated** (the EQT manual names
an SC-500E check; nothing equivalent here).

---

## 9. Verification status

| Section | Tier | Basis |
|---|---|---|
| §1 line, options | **Verified [Official]** | §1, §1.1, §3.1, §3.8.1 |
| §1 QT-3232N = QT-AV-3232 | **Inferred** | Two naming schemes, never mapped |
| §2 physical | **Verified [Official]**, depth contradicted three ways | §4.1.10, §2.2.1, §4.2.8 |
| §3 video specs | **Verified [Official]** | §3.4, §4.1.2–§4.1.6 |
| §4 reference / switching | **Verified [Official]** | §2.3.2, §2.5.3.1, §4.1.8 |
| §5 power | **Verified [Official]** | §2.4, §3.7, §4.1.9 |
| §6.1–§6.2 Q-Link, serial | **Verified [Official]** | §2.3.4–§2.3.7, §3.8.1 |
| §6.3 no port numbers | **Verified negative** | Full text layer + WinSetup figures |
| §6.3 EQT ports not open | **User-reported**, IP reachability unconfirmed | 2026-10-08 |
| §6.3 TCP 255 open | **Bench-observed, user-reported**; function unknown, scan lossy | Nmap, 2026-10-08 |
| §6.4 control path | **Contradiction, unresolved** | §1.1 vs §3.8.1 |
| §7 DIP / address | **Verified [Official]**, numbering contradiction | §2.3.6 vs §2.5.1 |
| §8 WinSetup | **Verified [Official]** | §5, Figures 5-1–5-5 |
| §8 38400 vs 9600 | **Reasoned** | Not stated |

**Nothing bench-tested** beyond the §6.3 port checks.

---

## 10. Not yet verified — open items

1. **What TCP 255 is, and whether it is the only port.** A scan found 255 open
   (§6.3). Settle by a WinSetup download pointed at it, and a slow rescan
   (`--max-rate 100`) to catch anything the lossy scan missed. Evertz service or
   the WinSetup F1 help would confirm. **Highest-value item.**
2. **How the Topaz IP address is set and read** — no front panel menu, telnet
   or DIP setting for it is described. Possibly set in WinSetup and downloaded
   serially — unconfirmed.
3. **Whether the §6.3 port check hit the right, reachable IP.** A ping and the
   switch's MAC/ARP table settle it.
4. **Which WinSetup build supports Topaz Ethernet download.**
5. **Frame depth** — tape measure, front face to rear-most BNC (§2.1).
6. **CP-2402-LP vs CP-2402e** — same panel or not.
7. **Quartz standard protocol specification** — not held; belongs in
   `creative-coding/references/protocols/` when obtained.
8. **Quartz MANUAL-05** (Q-Link panels) — not held.
9. **A revision later than 2.0 (Jan 2009)** — not checked.
