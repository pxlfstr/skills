# Open-Source Repos (third-party video makers)

GitHub (and other open) repositories for the non-LZX makers, with what's in each and the circuit building-blocks the BOMs reveal. Pairs with `cadet-circuits.md` — the same canonical parts keep showing up (LM6172 video op-amp, TL072 CV op-amp, TL431 1 V reference, CD4053 mux), which is how to reason about how any of these modules work.

## Confirmed repositories

| Maker | Repo / location | Contents |
|---|---|---|
| **Teletect** (Philip Baljeu) | github.com/Teletect | Per-module repos, each with README + BOM CSV + schematic (PDF/JPG) + gerbers: **VS-002 Dual Enhancer**, **IP-Differentiator**, **VS-009 BNC Adapter**, **VS-010 Linear PSU** |
| **Martin Devices** (phosphenes) | github.com/martindevices | `Martin-Devices` — Soft Key BOMs (V2.1, V2.2) + docs |
| **Foxing Hour** | github.com/foxinghour/foxdocs | Build guides + BOMs + PCB art for the whole line: SHUTTER, VEIL, RECT, ACCESS, GAMMA, LUMA (RGB2YRGB), NVRT, PASS4, MULT A/B, SW6 |
| **Reverse Landfill** | github.com/reverselandfill | `LZX_VCA` (triple VCA, EAGLE schematic + gerbers), `sampler` (lo-fi sampler) |
| **Syntonie** | github.com/Syntonie | Reference **archives** (not module designs) — see below |
| **Special Stage Systems** (Ming Mecca) | github.com/beaugunderson/special-stage-archive | Community archive of the (officially open-sourced) Ming Mecca / Ming Micro schematics + firmware; original SSS site is defunct. Related: Chris Novello's **Illucia** is also open-source |

## Syntonie's reference archives (a genuine goldmine — large, browse online)
Syntonie maintains curated open archives that are useful well beyond their own modules:
- **videomanuals** — video gear user & service manuals
- **videoicdatasheet** — datasheets for video ICs
- **videomagazines** — articles from hobbyist electronics magazines about video
- **documentation** — Syntonie's own module docs (HTML)

These are large (many PDFs); reference them online rather than bundling. For Syntonie's *module* designs (CBV001/CBV002/Rampes/Solaire/Seuils) see syntonie.fr.

## Not open-source / no confirmed public repo
- **Sleepy Circuits (Hypno)** — docs live on GitBook (sleepycircuits.gitbook.io) and firmware ships as downloadable images; **Hypno 2 uses a proprietary "sleepy" codebase**, so there's no public source repo.
- **Tsyklon Labs PLITKA** — described by the maker as open-source hardware, but files are on tsyklon.com, not a confirmed GitHub repo.
- **Melted Electronics (Glitch Boy)** — firmware described as open-source/hackable, but no public repo could be reliably attributed (the GitHub user "melted" is an unrelated developer).
- **Gieskes** — hosts schematics on gieskes.nl, not GitHub.

---

## Circuit building-blocks revealed by the BOMs
(Extends `cadet-circuits.md`. These confirm the shared LZX-ecosystem parts vocabulary.)

**Foxing Hour SHUTTER** (triple 2:1 video mux) — `CD4053` triple analog mux (the switching element) + 6× `LM6172` (video op-amp buffers/drivers) + `TL072` (CV op-amp) + `7805` reg. Same mux topology as the LZX/Cadet switchers.

**Teletect IP-Differentiator** (4 HP, Sandin-IP differentiator, from the LZX design) — a single `LM6172` video op-amp + 6× `2N3904` NPN transistors, with precision C0G caps (2–470 pF). A differentiator = high-pass/edge-and-transient extractor (cf. the Visionary TVMF "outline" outputs).

**Teletect VS-002 Dual Enhancer** (from the Archer Video Enhancer) — **fully discrete**: 4× `2N3904` (NPN) + 2× `2N3906` (PNP), no op-amps. A transistor-based video peaker/sharpener — a good example that not every video stage needs a video op-amp.

**Martin Devices Soft Key** (4 HP) — the textbook soft-key build described in `keying-dictionary.md`: `TL431` precision 2.5 V shunt reference (for the precise 0–1 V clip window) + 4× `1N5711` Schottky diodes (fast precision clipping) + a **5× `LM6172` gain cascade** (the "stack several ~5× stages" high-gain front end) + `TL072` on the CV/threshold path. Gain ×0–×50 (trim to ×100). 4-layer board to keep noise down at high gain.

Takeaway: across makers, **LM6172** = the workhorse video-rate op-amp, **TL072** = the slow CV/control op-amp, **TL431** = the 1 V-domain voltage reference, **CD4053** = the analog switch/mux. Recognizing these four in any BOM tells you most of what a module is doing.
