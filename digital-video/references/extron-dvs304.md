## Provenance

**Verified [Official]** — *Extron DVS 304 Series Digital Video Scalers: Specifications*, document code 8.0-010411-D18-112012, user-supplied PDF, read in full (3 pages). No remembered or estimated figures. Not read: any separate DVS 304 installation/user guide (this document is spec-sheet only) — no frame-latency figure exists anywhere in what was supplied, only the 40 ns sync-pass-through propagation delay, which is not a video-latency number. No open contradictions.

---

## 1. What it is

An **analog-domain scaler and standards converter** — not an ADC or a DAC in the sense of bridging digital and analog. Every input and every output on every DVS 304 variant is analog. It takes one analog format in, decodes it, and outputs a scaled or format-converted analog signal. Four variants: DVS 304, DVS 304 D (adds SDI input), DVS 304 A (adds audio), DVS 304 AD (both).

## 2. Video input

| | |
|---|---|
| Signal types | RGBHV, RGBS, RGsB, RGBcvS, component (YUVi or YUVp/HDTV), S-video, composite; pass-through available for RGBHV/RGBS/RGsB only |
| Second input | composite, S-video, component (YUVi or YUVp/HDTV) |
| SDI input | 1, **optional — DVS 304 D and DVS 304 AD only.** Base DVS 304 has no digital input of any kind |
| Third input | composite video only |
| Connectors | 1 female 15-pin HD (RGBHV/RGBS/RGBcvS/component/S-video/composite); 3 female BNC (component/S-video/composite); 1 female BNC SDI (D/AD only); 1 female 4-pin mini-DIN (S-video); 1 female BNC (composite) |
| Resolution range | 640×480 to 1920×1200, 480p, 576p, 720p, 1080i, 1080p |
| Horizontal frequency | 15 kHz–100 kHz |
| Vertical frequency | 50 Hz–120 Hz |
| Impedance | 75 ohms |

## 3. Video processing

| | |
|---|---|
| Decoder | 9-bit digital |
| Digital sampling | 24-bit, 8 bits/color; **13.5 MHz standard for video**, **194 MHz standard for RGB** |
| Colors | 16.78 million |

The 13.5 MHz video-sampling figure is the ceiling on luma/chroma detail extracted from a composite or component source, regardless of what it's re-encoded to on output — this is shared by every output path, since there is one decoder feeding all outputs.

## 4. Video output

| | |
|---|---|
| Signal types | 2 scaled or pass-through RGBHV, RGBS, RGsB, or scaled component (Y, R-Y, B-Y) |
| Connectors | 5 female BNC, 1 female 15-pin HD |
| **No digital output of any kind, on any variant** | |
| Scaled resolution list | 640×480 through 1600×1200 at various rates (50/60/72/96/100/120 Hz depending on format), plus HDTV 480p/576p/720p/1080i/1080p/1080p Sharp/1080p CVT |

**No frame/pixel-count comparison performed between the scaled-resolution list entries** — see Rule 3a. If a ranking between any two entries in this list is needed, compute it before stating one.

## 5. Sync

| | |
|---|---|
| Input types | (RGBHV, RGBS, RGsB) pass-through, RGBHV, RGBS, RGsB, RGBcvS, bi-level or tri-level component |
| Output types | RGBHV, RGBS, RGsB, component tri-level |
| Standards | NTSC 3.58, NTSC 4.43, PAL, SECAM; optional SDI input adds SMPTE 259M-C |
| Max propagation delay | **40 ns** — this is the sync pass-through path only, not a video-processing latency figure |

## 6. Control

RS-232 (9600 baud, 8N1), Ethernet (10/100Base-T; ARP/ICMP/IP/TCP/UDP/DHCP/HTTP/SMTP/Telnet), contact closure, optional IR (Extron IR 902). Program control via Extron SIS, browser, or Telnet.

## 7. What this document does not answer

- **No stated frame or field latency for video processing.** Only the 40 ns sync-pass-through propagation delay is given, and that is not the video-signal delay figure.
- Whether composite-in/RGBHV-out and composite-in/component-out share identical latency was reasoned (both go through the same decoder and scaling engine per §3, so no separate faster path exists for either), not measured or stated by the manufacturer.

---

## Verification status

| Claim | Status |
|---|---|
| All input/output signal types, connectors, resolution ranges | **Verified [Official]** — spec sheet, read in full |
| Sync propagation delay (40 ns) | **Verified [Official]** — explicitly stated, but scoped to sync pass-through, not video latency |
| Video processing latency (frames/ms) | **Not available in this document** — not stated anywhere in the spec sheet |
| Whether composite→component and composite→RGBHV share identical latency | **Reasoned only** — inferred from shared decoder/scaling architecture in §3, not a measured or vendor-stated figure |

## Not yet verified — open items

- Actual video processing latency in frames or ms — would require the DVS 304 installation/user guide (if one publishes it) or a bench measurement.
- Whether the optional SDI input (D/AD models) shares the same 13.5 MHz decode path or has separate digital processing — not addressed in this spec-sheet-only document.
