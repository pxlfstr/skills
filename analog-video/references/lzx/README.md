# LZX Industries — Reference Pack

Distilled from the official LZX Industries GitHub documentation (the `lzxtm` Technical Manual repo, plus `lzxdocs`, `lzxmodular`, `lzxcadet`). This pack closes the "LZX specifics" gap the skill previously flagged as low-confidence: module specs, signal standards, and per-module circuit/interface detail now come from LZX's own docs rather than memory.

## What's in here

| File | Contents | Reach for it when… |
|---|---|---|
| `module-specs.md` | Full specs table — every module (current + legacy): series, width/depth, ±12V draw, power type, sync | you need exact HP, power budget, or whether a module needs sync |
| `standards.md` | LZX signal standard: voltage scales, bandwidth, impedance, IRE mapping, mechanical dims, supported video formats | any question about levels, patching across signal types, or format support |
| `glossary.md` | LZX's own glossary of video-synthesis terms, with module cross-references | defining a term, or finding which modules perform a named function |
| `functional-map.md` | Modules grouped by role, with substitution notes **+ the owner's preference filter** | "what else can do X," "which module should I use for Y," planning a system |
| `cadet.md` | Cadet series (all 4 HP, non-Orion DIY) — full C1 manual detail + C2–C10 functions/specs | any Cadet question; a favored series under the owner's preference |
| `cadet-circuits.md` | Canonical LZX circuit building blocks distilled from Cadet BOMs (LM6172, TL431, LM1881, LM361, AD724, LT1251…) | "how does LZX do X," reasoning about any module's analog stages, repair/DIY |
| `expedition/*.md` | Per-module Expedition docs (owner's manuals / reference cards), incl. Visual Cortex technical manual and **Pendulum** (dual animator) | the owner's **strongest-preference** series — controls, jacks, specs, patches |
| `visionary.md` | The original Visionary series (~19 modules) — functions, specs, TVF&KG patch cookbook | legacy non-Orion modules; encoders/decoders (CVE/CTBC/TVI) |
| `castle.md` | Castle DIY binary/logic series (8 modules, all 4 HP) — 3-bit concept, specs, build note | logic/binary patching, posterize/pixelate, a favored 4 HP series |
| `sandin.md` | LZX Sandin IP adaptations (Differentiator, Function Generator; 4 HP) | edge extraction & tone/solarization waveshaping; Sandin IP lineage |
| `keying-dictionary.md` | LZX's keying terminology + every module's keying role across series + soft-key circuit notes | any keying question; choosing a keyer; DIY soft-key |
| `vhs.md` | VH.S (Video Headroom Systems) — **verified full catalog** (10 ModularGrid modules + VIDEO GRIP from the maker site, with functional detail); Gen3-powered LZX-format | LZX-format third-party gear; owner owns SUBMIX |
| `brownshoesonly.md` | brownshoesonly — **verified full catalog** (14 entries, MSRP/HP) for the earlier brand by the **same maker as VH.S**; VH.S successor map | third-party LZX support modules; comparing his two brands |
| `third-party-video.md` | 26 other video makers — Dave Jones, Erogenous Tones, Foxing Hour, Gieskes, Lone Vidiot, Luix, Malekko, Martin Devices, Melted, mfb, Nonlinearcircuits, Omiindustriies, Plankton, Razmasynth, Reverse Landfill, Scopic Modular, Sismo, Sleepy Circuits, Soundmachines, Special Stage Systems, Steady State Fate, Synthrotek, Syntonie, Teletect, Tsyklon, Visible Signals | any non-LZX/non-VH.S video maker; format tags (LZX vs audio-rate vs standalone) |
| `open-source-repos.md` | GitHub repo catalog for third-party makers + circuit building-blocks from their BOMs (Teletect, Martin Devices, Foxing Hour, Reverse Landfill, Syntonie archives, Ming Mecca) | open-source designs; how a module works from its parts; DIY |
| `modules/*.md` | Per-module docs (overview, key specs, panel controls, jacks) for the 26 active modules | detailed control/jack behavior for a specific module |
| `what-is-a-video-synthesizer.md`, `your-first-patch.md` | Conceptual intros | onboarding context, explaining fundamentals |

## How to use it

1. For **system-level / "which module" questions**, start with `functional-map.md`, then drill into `modules/<name>.md` for specifics.
2. For **exact specs** (power, size, sync), `module-specs.md` is authoritative.
3. For **signal/patching** questions, `standards.md` governs — this is the area where guessing is dangerous, so cite it.
4. **Legacy modules** (Orion, Expedition, Cadet, Visionary series) appear in `module-specs.md` but most don't have a cleaned per-module doc here. For deep legacy detail, note that the full manual lives at `github.com/lzxindustries/lzxtm` and the Cadet DIY schematics at `github.com/lzxindustries/lzxcadet` — fetch on demand.

## Source & currency

- **Origin:** github.com/lzxindustries (official). Technical Manual repo `lzxtm` was last updated within days of ingest, so this reflects the current product line.
- **Images/diagrams stripped:** the source docs embed front-panel images and line-art diagrams (in the repo's `static/` tree). Those aren't bundled here — text, specs, and tables are. If a user needs a panel diagram, point them to the live manual.
- **Not authoritative for:** pricing, stock, current production status beyond the "Active/Legacy" flag in the specs table, and anything LZX has changed since ingest. Re-pull the repo to refresh.
