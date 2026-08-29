## Provenance

**Mixed sources, tagged individually.** Primary source: *Blackmagic Teranex Processors* manual (English section, ~120 pp., user-supplied PDF, dated 2017 per cover page — current official manual as of this writing, covers Teranex 2D, 3D, AV, and Express in one document). Supplemented by web search (retailer spec pages, a 2012 product-launch article) for historical/discontinued-model context the manual doesn't carry. A real, unresolved physical-unit identification case runs through this document — see §4 — recorded honestly rather than forced into a clean answer.

---

## 1. The model family, as documented in the current manual

| Model | Max SDI | Analog video I/O | Audio | Notes |
|---|---|---|---|---|
| **Teranex 2D** | 3G-SDI | Yes — component (Y/B-Y/R-Y) | XLR ×2 in, ×2 out (analog/AES selectable per manual context) | Single-channel processor |
| **Teranex 3D** | 3G-SDI | Yes — component (Y/B-Y/R-Y), 3 in / 3 out per channel | XLR ×2 in, ×2 out, **plus dedicated XLR timecode in/out** | Adds dual-link/stereoscopic-3D SDI A/B pair — see §2. Documented with **redundant dual-IEC power** |
| **Teranex AV** | 12G-SDI + quad 3G-SDI (auto-switching) | **No** — manual explicitly separates analog-video behavior as "Teranex 2D or 3D" only, contrasted with AV's alternate-SDI-input behavior | Not detailed in what was read | Adds HDMI in/loop/out, live-event features (still store, freeze), can generate its own reference signal |
| **Teranex Express** | 12G-SDI (auto-switching to 6G/3G/HD/SD) | Not confirmed either way from what was read | Not detailed | "World's first" 12G-capable Teranex; reference in/out stated as black burst (SD) or tri-level (HD) |

**2012 launch context** (web-sourced, not from the manual): the original 2D/3D pair launched in 2012, per contemporaneous trade coverage — before 6G-SDI existed as a broadcast standard, which is why neither model was ever documented with 6G capability at launch or in this current manual.

## 2. Teranex 3D — single vs. dual link, what the A/B pair actually means

**[Verified — manual, "SDI Output Menu for Teranex 3D Processor only"]:**

The 3D's SDI Outputs A/B operate in one of two mutually exclusive modes — never both signals independently at once:

- **Single Link** — A and B carry the **same signal, redundantly** (mirrored for failover/redundancy), not two different channels.
- **Dual Link** — A and B together carry **one higher-bandwidth signal split across two links** (e.g. Level B 1080p at 3Gb/s = 2× 1.5Gb/s split across both), used to carry sampling depths (4:4:4) a single link can't.
- **Stereoscopic 3D use** (the model's namesake) is the one case where A/B carry genuinely different content — left eye / right eye — but this is still one matched stereo *program*, not two independent unrelated channels.

**Net: Teranex 3D processes one video channel at a time.** The "3D" in the name refers to how a signal is carried (redundant, bandwidth-split, or stereo pair) — not to simultaneous multi-channel operation. It is a converter/processor, not a switcher or router.

## 3. Quad-link SDI (A/B/C/D) — Teranex AV specifically

**[Verified — manual, Teranex AV connector section, item #17]:**

> "Quad 3G-SDI Out – CH A, B, C, D — 4x BNC – Quad 3G-SDI outputs, active with applicable Ultra HD output formats up to 2160p60. If output format is not Ultra HD, these become 4 replicated SDI outputs."

A/B/C/D-labeled SDI banks, where found on a Teranex product, indicate **quad-link capability**: one 4K/UHD signal split across four 3G-SDI links when outputting UHD, or four replicated (redundant) copies of a lower-resolution signal when not. Confirmed specific to Teranex AV's documented section — not present in the 2D/3D sections read.

## 4. Waveform/vectorscope monitoring — not on-device

**[Verified — manual, "Waveform Monitoring with Blackmagic UltraScope" section]:**

Teranex hardware does **not** generate scopes internally. **Blackmagic UltraScope** is a separate, free companion application that reads the Teranex's output over its **Thunderbolt** connection. Provides, simultaneously (6 scopes, needs 2560×1440+ display; 2-up view needs 1280×800 minimum): RGB Parade, Waveform, Vectorscope, Histogram, and an audio metering display. Confirmed present across the 2D/3D/AV/Express family via the shared Thunderbolt port documented on each.

## 5. ⚠️ Unresolved: a physical unit that doesn't match any documented model

**This is recorded as an open case, not a settled fact — do not treat any single-model conclusion below as confirmed.**

A physical unit was examined (rear-panel photos, direct description) with the following confirmed traits:

| Trait | Matches |
|---|---|
| Connector layout: dual XLR audio in/out, dual XLR timecode in/out, REF IN, HDMI, component video (Y/B-Y/R-Y) | **Teranex 3D**, exactly, connector-for-connector, per the manual's 3D section |
| Rear panel text: "SD/HD/**3G/6G**-SDI IN/OUT" | **Matches no documented model.** 2D and 3D are both documented as 3G-only, in this current manual and every web source checked. No source documents a 6G variant of either. |
| SDI port count: **9 total (4 in / 4 out / 1 monitor out)** | **Does not match the documented 3D** (which has 2 in / 2 loop / 2 out = 6, no monitor out). The A/B/C/D + "quad" naming pattern and monitor-out port instead match **Teranex AV's** documented quad-SDI architecture (§3) |
| Power: single IEC, **no redundant/backup supply** | **Does not match the documented 3D**, which is specifically described with dual-IEC redundant power |
| USB-B, Ethernet, Thunderbolt | Matches 3D's documented control/connectivity layer exactly |
| Component analog video I/O present | Matches 2D/3D. **Explicitly contradicts Teranex AV**, which the manual states does not have this — see §1 |

**The contradiction, stated plainly:** the SDI architecture (6G, quad A-D, monitor out) points toward Teranex AV. The analog component video I/O points away from AV and specifically toward 2D/3D (the manual draws this line explicitly). These two facts cannot both be true of any single model documented in this manual. Everything else on the unit (audio, timecode, control ports) matches Teranex 3D precisely.

**Working theory, held loosely:** given how precisely everything *except* the SDI bank and power supply matches the documented 3D, the most plausible explanation is an undocumented hardware revision or variant — e.g., a 3D chassis built at some point with an upgraded/expanded SDI daughtercard (higher generation, more ports, monitor out) and single rather than redundant power — rather than a genuinely different, unrelated product. This is speculation, not a finding, and should not be treated as fact in future sessions.

**This was not resolved by any documentation, web search, or manual available this session.** The only paths to resolution: the unit's actual nameplate/serial number cross-referenced against Blackmagic's support/warranty system, or a direct inquiry to Blackmagic support with photos.

---

## Verification status

| Claim | Status |
|---|---|
| 2D/3D max SDI = 3G, no 6G variant documented anywhere | **Verified** — current manual + multiple independent web sources, fully consistent |
| 3D single/dual-link A/B behavior | **Verified** — manual, direct quote |
| AV quad-link A/B/C/D behavior | **Verified** — manual, direct quote |
| AV lacks analog component video I/O | **Verified** — manual states this distinction explicitly |
| UltraScope is external/Thunderbolt-based, not on-device | **Verified** — manual, direct section |
| The physical unit examined this session is a genuine, standard Teranex 3D | **Not verified — actively contradicted by SDI/power findings.** See §5 |

## Not yet verified — open items

- **The §5 identification case is the single largest open item.** Needs the unit's serial number checked against Blackmagic's own records, or direct manufacturer contact.
- Teranex AV and Express audio I/O — not read/confirmed from the manual this session, only 2D/3D audio was directly checked.
- Whether Teranex Express has analog component video I/O — not confirmed either way.
