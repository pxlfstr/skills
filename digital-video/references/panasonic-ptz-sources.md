# Panasonic PTZ — AW-UE150 / AW-HE145 / AW-RP150 source registry

Verified document locations for the Panasonic PTZ gear in the user's festival rig, plus the facts
actually read from them.

**Status: source registry, not a full extraction.** URLs below were located and confirmed
2026-07-19. The full PDFs have **not** been read end to end into this file. Anything not listed
under "Facts read" must be pulled from the linked document before use — do not answer from memory.

---

## Documents

| Document | Covers | Tag | URL |
|---|---|---|---|
| AW-UE150/AW-HE145 Interface Specifications | External control protocol — pan/tilt and camera command sets, HTTP/TCP control, RS-422 serial, update notifications | `[Official]` | https://eww.pass.panasonic.co.jp/pro-av/support/content/guide/DEF/UE150/AW-UE150HE145_InterfaceSpecification_E.pdf |
| AW-UE150 Operating Manual | Camera operation, menus, IP setup, authentication, output formats | `[Official]` | https://eu.connect.panasonic.com/sites/default/files/media/document/2025-01/AW-UE150%20Operating%20Manual.pdf |
| AW-UE150W/K Specifications | Format table, output specs, cabling requirements | `[Official]` | https://pro-av.panasonic.net/en/products/aw-ue150/spec.html |
| Operating guide for AW-RP150 Ver2 | Version 2.00 feature additions and menu paths — ROP link, switcher link, TMEM, CAMSEL OP, IRIS LIMIT, preset name editing | `[Official]` | https://eww.pass.panasonic.co.jp/pro-av/support/content/download/EN/ep2main/soft/rp150/AW-RP150_Ver2.pdf |
| AW-RP150 Operating Instructions (DVQP1819WA) | Controller operation, connection topology, camera registration | `[Official]`, third-party host | https://www.lensrentals.com/product-assets/8dcaeee3-2694-458d-93de-4402601ba432/Controller%20Manual.pdf |
| FAQ — AW-RP150 | Common setup failures, menu answers | `[Official]` | https://eww.pass.panasonic.co.jp/pro-av/support/content/faq/EN/faq_rp150.htm |
| FAQ — AW-UE150 / AW-HE145 | Compatibility, output behavior, control options | `[Official]` | https://eww.pass.panasonic.co.jp/pro-av/support/content/faq/EN/faq_ue150.htm |
| Remote Camera Controller Interface Specifications | Controller-side command protocol (RP50/RP120 doc; notes commands added for RP150) | `[Official]` | https://eww.pass.panasonic.co.jp/pro-av/support/content/guide/DEF/RP50_120/RemoteControllerInterfaceSpecifications-E.pdf |

The AW-RP150 Operating Instructions link is a third-party mirror of an official Panasonic document.
Prefer Panasonic's own manual portal where possible:
https://pro-av.panasonic.net/manual/en/02_search.html

---

## Facts read this session

Only what was directly read. Everything else requires opening the source.

**AW-UE150/HE145 interface protocol** — Interface Specifications `[Official]`

- Two distinct command types: **pan/tilt head control commands** and **camera control commands**.
  They are not one flat command set.
- Camera control commands are framed with **STX (0x02)** at the start and **ETX (0x03)** at the
  end, with a `:` required before the data field.
- Control runs over **HTTP on TCP** as the host protocol. Serial control is **RS-422**.
- Pan/tilt head control commands must be sent with a gap of **40 ms** between commands.
  *(This is the documented origin of the 40 ms throttle in the TD control surface — the throttle is
  a protocol requirement, not a tuned constant.)*
- An **update-notification** mechanism exists: a terminal can opt in to be notified when another
  terminal changes gain or other settings. Intended for one camera controlled by multiple terminals.

**AW-RP150 controller** — Operating Instructions `[Official]`

- Controls up to **200 remote cameras over IP**, or up to **5 over serial**. IP and serial cameras
  can be mixed; the 200 total is the registration ceiling across both.

**AW-RP150 Ver 2.00 additions** — Operating guide for AW-RP150 Ver2 `[Official]`

- ROP linkage: set the RP150's port as RECEIVE PORT, run INFO UPLOAD, set **AW CONT LINK** to ON;
  on the ROP set ROP IP and PORT and run UPLOAD. Cameras mapped via **CAMSEL** (RP150) against
  **ROP CAM** (ROP); unassigned entries set to **NON**.
- Switcher linkage with **AV-HS6000**; camera numbers assignable against SW INPUT 1–34.
- TMEM bulk delete: `MENU > PMEM/TMEM > TMEM > MODE > DEL ALL`.
- Camera selection during motion: `MENU > MAINTENANCE > RP SETTING > CAMSEL OP > [SINGLE/MULTI]` —
  MULTI allows selecting another camera mid-PTZ move.
- Iris limit (close direction only): `MENU > FUNCTION > PTZ INFP1 > IRIS LIMT > [ON/OFF]`.
- Preset name editing: `MENU > PMEM/TMEM > NAME EDIT > PMEM1–PMEM100`.
- I.ZOOM assignable to a user button: `MENU > FUNCTION > USER ASSIGN > USER1–10 > I.ZOOM`.

**AW-RP150 ↔ AW-UE150 setup gotchas** — FAQ `[Official]`

- IP control will not work until **user registration is completed on the camera** via a web
  browser. AUTO IP SET on the RP150 will appear to fail — the controller simply won't see the
  camera — until a username and password have been registered on the UE150 itself. This is the
  single most common "controller can't find the camera" cause.
- Power-on-all-cameras with the controller: `SYSTEM > 1. CAMERA > AUTO POWER = ON`. Power-on only;
  it does not turn cameras off.
- The crop-marker function on the RP150's built-in LCD requires feeding MONITOR OUT of the UE150
  into the RP150's 3G-SDI input, then pressing PICTURE. **UE150-only feature.**

---

## Not yet extracted — open items

- Full AW protocol command tables (`#O0`/`#O1` power, `#RER` error codes, `#INS` install position,
  `q[nn]` queries, `man_session`, the 5-terminal notification limit). These were researched in a
  previous session and the working notes were lost; re-extract from the Interface Specifications.
- Digest authentication specifics for the HTTP CGI control path.
- UE150 motor origin/MR-sensor initialization behavior on power-up.
- RP150 SD card formatting and firmware upgrade procedure (card type limits, upgrade duration).
- RP150 SYSTEM menu definitions: ROP Link, SW Link Setting, SW Link Assign, Ext Control,
  PTZCC Link — and **VR Control, which was never found in any source.**

## Consumers

`creative-coding/references/` depends on this file for AW protocol facts — the PTZ control surface
and any AW sender. Code lives there, protocol facts live here. Do not duplicate.
