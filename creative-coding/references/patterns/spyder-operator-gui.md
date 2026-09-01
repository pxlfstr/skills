# Spyder operator GUI — design record for a browser-based control surface

A GUI utility for operating a Christie Spyder X20 over the UDP ASCII protocol, visually modeled
on Christie's own client software. This document records the design decisions, the safety
boundary, the interaction specs agreed so far, and what the two Christie clients taught us about
the interface. **The code itself is deliberately not in this repo** — the user archives it
locally. What's here is everything needed to rebuild or extend it.

**Vendor and protocol facts are not restated.** Protocol commands cite to
`protocols/christie-spyder-external-control.md`; device and client-software facts to
`digital-video/references/christie-spyder-x20.md` and its open-questions companion.

---

## Provenance

**Document type:** a design record. **Tier: Designed throughout** — as of 2026-08-31 the GUI
exists only as static HTML mockups; **nothing has ever been sent to a frame**, and no wiring to
the protocol has been written.

**Sources, all user-supplied 2026-08-31:**
- Spyder Studio User Guide 020-102579-04 Rev. 1 (1-2019, X80 platform) — read in full for GUI
  concept and structure only, per the user's explicit scoping; its X80 hardware facts were not
  compared or stored.
- Screenshots: default layouts of Vista Advanced 4.1.0 and Spyder Studio side by side; the
  Sources/Properties panels of both (new-source form and created-source view, both skins); the
  View menus of both; the Advanced source-bank right-click menu and its Studio counterpart.
- The user's own operator experience — flagged inline where it contradicts or exceeds the manuals.

**Not read / not done:** no Spyder Studio session was ever operated by us; every Studio behaviour
below is from the guide or screenshots. The mockups have not been shown to any other operator.

---

## 1. What the tool is, and the safety boundary that shapes it

**An operator's GUI.** The EIC digs into Vista Advanced for system work; this tool is for the
person running the show. That one sentence drove every scoping decision below.

**The user's hard requirement: nothing in the tool may adjust hardware config** — the fear is a
vibecoded utility bricking a frame's stored configuration. The command set separates cleanly:

- **Whitelist, not blacklist.** The tool's sender knows only the safe commands; everything else
  is structurally impossible to emit. Safe set: the layer/KeyFrame geometry and look commands,
  routing/transition commands, and readback (`protocols/christie-spyder-external-control.md`
  §5a–5b, §7).
- **Excluded by design:** shutdown/restart, the save-to-non-volatile command (the one command
  that makes anything permanent), all output configuration, and input-config slot writes.
- Whether un-saved runtime changes survive a frame restart is untested — but that cuts the safe
  direction: a tool that never saves cannot make a mistake permanent.

## 2. Platform: browser page + bridge, not TouchDesigner

- **Browsers cannot send UDP**, and the frame listens on UDP. Standard shape: a small local
  bridge (WebSocket in, UDP with the protocol header out). All real work lives in the page; the
  bridge is trivial and never changes.
- Chosen over TouchDesigner panel COMPs because HTML/CSS can copy the Christie skin almost
  exactly, and because a TD GUI build was new ground for us while the page was not.
- Middle option kept in reserve: **TD as the bridge** (Web Server DAT serving the page, UDP Out
  DAT to the frame) — same page, drops into a show file later if wanted.

## 3. What the two Christie clients taught us

**Same skeleton, two skins.** Advanced 4.1.0 (blue/silver XP-era) and Spyder Studio (dark) share
a five-region layout: Sources rail · Simulator (alignment toolbar, View Stack/Duration bar,
Program stacked over Preview) · Command/Function Keys column · Properties with Back/Forward ·
Script + System Patch strip. Studio's skin: near-black ground, dotted grid on the simulator
canvas, flat controls, **red/pink rule for Program and amber for Preview**, blue accent for
selection, colored layer chips in the patch view, status chips bottom-right.

**View-menu census** (from both menus): 17 views common to both; Studio adds Simulator,
Properties, Multiviewer Setup, Configuration Manager (the first two because Studio makes them
closeable panels); nothing in Advanced is absent from Studio.

## 4. Scope: the operator view set

Kept: **Simulator · Sources · Stills · Treatments · Command Keys · Function Keys · Properties ·
Router XY · Devices**. `Basic Presets` is undecided — no document read describes what it holds.

Cut as system-oriented (EIC territory or no protocol path at all): Alert Viewer, Configuration
Manager, Dynamic Help, Front Panel, Multiviewer Setup, PlayItems, Stereo Sync, System Patch,
System Layout, Script (editing is build-time; operators fire scripts through Command Keys),
Router Patch (the patch definition is config; the XY crosspoint panel is the operator action).

**Operator knowledge worth keeping:** the manual frames Devices as deck configuration; the user's
correction from operating the real system is that **Devices is an essential mix/transition
control**. Filed as first-hand operator testimony exceeding the documentation.

## 5. Style decisions (user preferences, binding for this project)

- **Font: Tahoma** everywhere (Verdana fallback) — the user prefers Advanced's face over
  Studio's; Tahoma is what Advanced actually renders.
- **Chrome and palette: Spyder Studio's dark skin** (see §3), including the Program/Preview rule
  colors and the bordered status chips (`Last Backup` / `Not Connected`).
- **Context menus: Advanced's style** — light menu, gradient icon gutter on the left, colored
  icons (green ＋ add, page-pair copy, blue ↓ insert, red ✕ delete), XP-blue hover.

## 6. Interaction specs agreed so far

### Sources + Properties (built as mockup, approved)

- Two panels; **Properties starts blank** and empties when nothing is selected. Long-term intent:
  Properties becomes a context view for whichever View was last interacted with.
- Click an empty bank → new-source form: Name · Input Type (Analog/SDI/DVI) · Router
  (`<Direct to Layer>` / `X20 Internal`) · a 1–16 spinner whose label flips **Layer:** ↔
  **Input:** with the router choice · a Studio-style link **Create and Configure Input**.
- On create, the bank fills like the real client — bold name over `Layer: N` or
  `In: N RTR: X20 Internal` — and the created view adds a **Config** dropdown defaulting to
  `<AutoSync>`. **No Input Configuration tab**: manual input configuration stays in Advanced;
  the GUI is meant to detect configs created there and add them to the dropdown.
- ⚠️ **Open problem for the wiring phase:** no documented protocol command lists input configs,
  so "detect new configs" has no clean implementation yet — candidate workarounds are a manual
  refresh action or probing recall slots. Bench question.
- **Right-click context menu** on every bank: Add new Source · Copy Source · Insert · Delete
  (Advanced's config-mode items deliberately excluded). Insert pushes an empty bank in above the
  clicked one, everything below shifts down, the bottom bank drops off. Copy duplicates into the
  next empty bank. Copy/Delete gray out on empty banks.
- **Drag and drop:** filled banks drag; the hovered target highlights as a whole bank (same
  treatment as selection); on release the dragged source **takes over the target bank** — an
  empty bank simply fills, a filled bank's occupant pushes down one slot — and the source's old
  bank goes blank.

### KeyFrame panel (from the Studio guide, not yet built)

Properties structure to copy: expandable **KeyFrame** section — X/Y position, width with
aspect-locked height — with attribute tabs **Crop · A/R · Pan & Zoom · Motion · Transparency**
(sliders paired with numeric entry, per-tab Reset), a separate **Border/Shadow** section with
Fill and Shape tabs, and a Treatments list applied by drag or double-click.

**A gift from the protocol:** the client UI's relative ±1.0 position space never has to be
implemented — `KPS`/`LSP` position in pixels from the PixelSpace top-left
(`protocols/christie-spyder-external-control.md` §5b), so the GUI can be pixel-native throughout.
The ±1.0 endpoint ambiguity is recorded as
`digital-video/references/christie-spyder-open-questions.md` §2.13 and does not block this tool.

## 7. Build lessons (mockup phase)

- **Anchor-tag links navigate inside embedded viewers.** The first mockup's
  "Create and Configure Input" was an `<a href="#">` and clicking it navigated the host page.
  Styled non-anchor elements for every in-app action; reserve real anchors for real navigation.
- Native HTML5 drag events cover the bank drag-and-drop completely — no library needed; the
  whole-bank drop highlight is the same CSS as selection, which reads instantly as "this bank
  takes it."
- Christie's own two skins over one skeleton is a useful decomposition: build structure once,
  keep the skin in CSS variables. The mockups already run on a ~10-variable palette.
