# Resolume — Control Interfaces (Complete Protocol Reference)

Vendor facts for controlling Resolume Arena/Avenue from outside. Integration *patterns* live in
`creative-coding/references/resolume-companion-glue.md`; this file holds only what the vendor
documents.

**Scope:** Every control protocol into and out of Resolume Arena / Avenue, what each can and cannot
reach, and the full REST endpoint inventory. Resolume 7.x — version-specific behavior drifts,
confirm against the running build.

*Expanded 2026-08-01 from a REST/OSC-focused note into full protocol coverage. All prior content
retained; new material is the protocol inventory, capability matrix, WebSocket/DMX/SMPTE/Link/MCP
sections, and the 295-operation REST appendix.*

**Sources read this session, all `[Official]`:**
- `swagger.yaml` — the Arena & Avenue REST API OpenAPI 3.0.1 spec (user-supplied file, `info.version: 0.0.1`, server base `/api/v1`). 258 paths / **295 operations**. This is the authoritative REST surface; the rendered Swagger page at `resolume.com/docs/restapi/` is JS-rendered and does not yield content to a plain fetch.
- resolume.com/support/en/restapi (v7.8) · websocket-api (v7.8) · osc (v7.18) · midi-shortcuts (v7.18) · dmx-shortcuts (v7.0.4) · dmx *(DMX Output, v7.22)* · smpte (v7.13) · link · mcp-servers (v7.26.0) · support index

**Version caveat:** doc pages carry different version stamps (7.0.4 → 7.26.0). The REST spec supplied
is undated beyond `0.0.1`. Re-verify anything version-sensitive against the build actually in use.

---

## 1. Protocol inventory

Everything Resolume speaks. "Control" = drives parameters/actions. "Sync" = clock/time only.
"Media" = pixels, listed for completeness but not a control path.

| # | Protocol | Direction | Class | Arena / Avenue | Transport |
|---|---|---|---|---|---|
| 1 | **REST API** | In (+ read) | Control | Both | HTTP, default port 8080 |
| 2 | **WebSocket API** | **Bidirectional** | Control + feedback | Both | `ws://addr:port/api/v1`, same port as REST |
| 3 | **OSC** | **Bidirectional** | Control + feedback | Both | UDP, default in port 7000; out to node/localhost/broadcast/manual IP |
| 4 | **MIDI** | **Bidirectional** | Control + feedback | Both | MIDI ports (USB/DIN/virtual) |
| 5 | **MIDI Clock** | In | Sync (BPM) | Both | MIDI |
| 6 | **DMX / Art-Net (input)** | In | Control | **Arena only** | Art-Net over Ethernet |
| 7 | **DMX / Art-Net (output)** | Out | Media (pixel data) | **Arena only** | Art-Net over Ethernet, ArtSync supported |
| 8 | **SMPTE LTC** | In | Sync (clip playhead) | **Arena only** | Audio input, 2 simultaneous inputs |
| 9 | **Ableton Link** | Bidirectional | Sync (BPM/phase) | Both | Network, peer-to-peer |
| 10 | **Keyboard shortcuts** | In | Control | Both | Local |
| 11 | **MCP servers** | Bidirectional | Control (agentic) | Both, **7.26.0+** | Local MCP, stdio to AI desktop app |
| 12 | **Pro DJ Link** | In | Sync | Arena | Network (Pioneer) |
| 13 | **StageLinQ** | In | Sync | Arena | Network (Denon) |
| — | NDI / Syphon / Spout | Both | Media only | Both | — |

**Two output-only-ish notes:**
- DMX *output* is pixel data to fixtures, not a control protocol — it sends the color/brightness of rendered pixels, organized into Lumiverses and fixtures. It is not a way to send Resolume's *state* anywhere.
- MIDI/OSC output are **feedback** paths (LED/state back to a controller), not general event buses — see gaps below.

### Default ports

| Interface | Default port | Source |
|---|---|---|
| OSC input | 7000 | [Resolume Support — OSC](https://resolume.com/support/en/osc) `[Official]` |
| REST API / web server + WebSocket | 8080 | [Resolume Support — REST API](https://www.resolume.com/support/en/restapi) `[Official]` |
| OSC output → Companion listener | 7001 | [companion-module-resolume-arena](https://github.com/bitfocus/companion-module-resolume-arena) `[Official]` (module README) |

All user-configurable. **Verified.** Wire's web server defaults to 8081.

---

## 2. Master capability matrix

Rows are capability classes. `✅` full, `◐` partial/conditional, `❌` not available.
"Shortcut protocols" (MIDI/DMX/Keyboard) all share one mapping engine, so they share most limits.

| Capability | REST | WebSocket | OSC | MIDI | DMX (Art-Net in) | Keyboard | MCP |
|---|---|---|---|---|---|---|---|
| Set any exposed parameter | ✅ | ✅ | ✅ | ◐ mapped only | ◐ mapped only | ◐ mapped only | ✅ |
| Read a parameter value | ✅ GET | ✅ `get` | ✅ send `?` | ❌ | ❌ | ❌ | ✅ |
| **Push feedback on change** | ❌ poll only | ✅ `subscribe` | ✅ OSC Output | ◐ mapped shortcuts | ❌ | ❌ | ❌ |
| Relative value math (`+ - *`) | ❌ | ❌ | ✅ | ◐ relative encoders | ❌ | ❌ | ❌ |
| Absolute-unit values ("a" 320px) | ◐ native units | ◐ native units | ✅ | ❌ | ❌ | ❌ | ◐ |
| Trigger clip / column | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Add / remove layers, columns, groups | ✅ | ✅ `post`/`remove` | ❌ | ❌ | ❌ | ❌ | ✅ |
| Add / remove / reorder effects | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Load media into clips | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Open / save / new composition | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Retrieve clip thumbnails | ✅ | ◐ via REST | ❌ | ❌ | ❌ | ❌ | ✅ |
| Monitor snapshots (PNG/JPG) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ◐ |
| Discover structure programmatically | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Stable IDs surviving reorder | ✅ `by-id` | ✅ `by-id` | ❌ index/selected only | ◐ "This" target | ◐ "This" target | ◐ | ✅ |
| Wildcard / all-layers addressing | ❌ | ❌ | ✅ output only | ❌ | ❌ | ❌ | ❌ |
| Advanced Output (slices/screens) | ❌ | ❌ | ◐ some params | ◐ mapped | ◐ mapped | ◐ | ❌ |
| Create/modify shortcut mappings | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Clip cue points | ❌ | ❌ | ◐ unverified | ◐ mapped | ◐ mapped | ◐ | ❌ |
| Parameter envelopes | ❌ | ❌ | ◐ unverified | ❌ | ❌ | ❌ | ❌ |
| Presets (effect/source/output/UI) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Record / render clips | ❌ | ❌ | ❌ | ◐ mapped | ◐ mapped | ◐ | ❌ |
| Sync BPM to external clock | ❌ | ❌ | ❌ | ✅ MIDI Clock | ❌ | ❌ | ❌ |
| Sync clip playhead to timecode | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## 3. Per-protocol detail and gaps

### 3.1 REST API — the structural workhorse

**Reaches:** everything structural. 295 operations across composition, decks, columns, layers,
layergroups, clips, effects, sources, files, monitors. Full CRUD on composition objects, media
loading, effect chain management, thumbnails, monitor snapshots.

**Three addressing modes**, per the spec's own preamble:
- **By index (1-based):** `/composition/layers/1` — position-based, changes when items reorder.
- **By unique ID:** `/composition/layers/by-id/1658311521181` — stable across sessions and reordering.
- **Selected:** `/composition/layers/selected` — whatever the user has selected; **404 if nothing selected**.

**Parameter access:** every parameter carries a numeric `id`. `/parameter/by-id/{parameter-id}`
gives GET / PUT, plus `/reset`, `/trigger`, and `/phase-source`. Parameter types are:
`BooleanParameter`, `ChoiceParameter`, `ColorParameter`, `EventParameter`, `IntegerParameter`,
`RangeParameter`, `StringParameter`, `TextParameter`, `FileParameter`, `ResetParameter`, plus
`ParameterCollection` (an unstructured name→parameter map, used for `dashboard`, effect `params`,
and `mixer`).

**Effect parameters ARE reachable** — `VideoEffect.params` is a `ParameterCollection`, so every
parameter of every effect on any clip/layer/group/composition is exposed through the object tree and
individually addressable via its parameter id. The `/effects/video/{offset}` endpoints are
add/remove/move/rename only; the *values* come through the object tree or `parameter/by-id`.

**REST gaps:**
- ❌ **No push.** HTTP request/response only — no change notification. Use WebSocket for that.
- ❌ **No relative value operators.** `set` is always absolute; to nudge you must read, compute, write.
- ❌ **No wildcard addressing.** One endpoint per object; no "all layers" in a single call.
- ❌ **Advanced Output** — slices and screens are not in the spec at all.
- ❌ **Shortcut mappings** (keyboard/MIDI/DMX/OSC) cannot be created or modified.
- ❌ **Clip cue points** — not present.
- ❌ **Presets** — effects, sources, parameter animations, output, UI layout: none applyable or editable.
- ❌ **Parameter envelopes** — not present.
- ❌ **Recording / clip rendering** — not present.
- ◐ **Deck scope limitation:** per Resolume's MCP documentation, only clips and files **in the current deck** are accessible to the REST API — though decks can be switched, then content modified.
- ⚠️ **Dashboard contradiction, unresolved:** the MCP page lists "Read or modify Dashboard dials" as *not* possible via REST, but the spec exposes `dashboard: ParameterCollection` on Composition, Layer, LayerGroup and Clip. One of the two is wrong or they mean different things (dial *definitions* vs dial *values*). **Test before relying on it.**

**URL encoding trap (from the spec preamble):** file paths in request bodies must be percent-encoded
— spaces as `%20` or `+`, and `#`/`&`/`?`/`=` escaped. Use three slashes after `file:` **even on
Windows**: `C:\Users\...\file 1.mov` → `file:///C:/Users/.../file%201.mov`. Forgetting this is
called out as a common failure.

**Avenue limitation:** all layergroup endpoints return **402** on Avenue. Layer groups are Arena-only.

**Web server enablement and quirks** `[Official]`: enabled per-application at **Arena/Avenue/Wire tab
→ Preferences → Web Server**; the panel shows machine IP, enable toggle, Listen Port and Listen
Address. Default listen address may show a non-real IP (e.g. 169.254.x.x) meaning "listen on all
active IPs" — use 127.0.0.1 for localhost-only. Two constraints:
- The web root **may not contain a folder named `API`**.
- A path ending in `/` is served `index.html` from that folder.

**The reference documentation is served by the running instance.** With the web server live, the API
reference page can send commands directly to it — the docs double as a test client and describe
*your* version rather than a generic one. This remains the authoritative way to confirm the command
list for a specific build, and is the check to run against the appendix below.

### 3.2 WebSocket API — the feedback layer REST lacks

Same port and address as REST, at `ws://address:port/api/v1`. All messages must be valid JSON.

**On connect you immediately receive three messages:** the composition state, all available sources
(`{"type":"sources_update","value":<sources>}`), and all available effects
(`{"type":"effects_update","value":<effects>}`). Composition is re-sent on **structural** changes
(layer/column added or removed); sources/effects re-sent when one is added or removed (e.g. a Wire
effect installed).

**Parameter actions** — `{ "action": <action>, "parameter": <parameter path> }`, never capitalised:

| Action | Effect | Response type |
|---|---|---|
| `subscribe` | Start receiving updates for that parameter | `parameter_subscribed` |
| `unsubscribe` | Stop | `parameter_unsubscribed` |
| `get` | Read current value | `parameter_get` |
| `set` | Write (needs extra `value` key, matching the documented type) | `parameter_set` |
| `reset` | Reset | *(no response)* |
| `trigger` | Fire a button-type parameter | *(no response)* |

Subscribed parameters push `parameter_update` whenever the value changes. **This is the direct
replacement for polling.**

Parameter path is either `/parameter/by-id/<parameter id>`, or the logical REST path minus `/api/v1`
with the parameter name appended — e.g. `/composition/columns/1/name`.

**Structural actions** use a different message shape: `action` of `post` or `remove` (not `delete` —
it's a JS/C++ keyword), plus `path` (REST path minus `/api/v1`), optional `body`, and an optional
`id` echoed back in the response for correlation.

**WebSocket gaps:** inherits every REST content gap above (no Advanced Output, no mappings, no cue
points, no presets, no envelopes, no recording, same deck scope). Adds no relative-value math and no
wildcard addressing. Thumbnails/snapshots remain REST-side.

### 3.3 OSC — widest parameter reach, weakest structural reach

Addresses are **fixed and predefined** — no assignment step, unlike MIDI/DMX/keyboard. Enabled in
the OSC preferences tab; default input port **7000**.

**Discovery:** there is deliberately no published master address list, because the address space
depends on composition layout. Resolume publishes only a sample list for a one-clip/one-layer
composition (`resolume.com/download/Manual/OSC/OSC list.txt`). The intended workflow is Shortcuts >
Edit OSC, click a control, read (and copy) its address from the Shortcuts panel.

**Absolute vs relative addresses:** most controls have both — e.g. an absolute
`/composition/layers/1/video/effects/goo/...` bound to layer 1, and a relative
`/composition/selectedlayer/...` form that follows selection. Sending to a relative address when the
effect isn't present is safe; it just does nothing.

**Type tags.** Selecting a UI item in OSC shortcut mode also displays its **Type Tag** — what value
types the address accepts and what they do. `[Official]` The types: `Float` (usually 0.0–1.0 normalised onto a real range — e.g. Transform scale 0.0–1.0
maps to 0–1000%; rotationz 0.0–1.0 maps to −180°..+180°), `Int` (e.g. blendmode 0–50 = 51 modes),
`Color` (`r` + 32-bit RGBA int, bitshifted), `String`. Floats sent to Int addresses are linearly
remapped.

**Two things only OSC can do:**
1. **Named/absolute-unit values** — `"a"` as first argument then the real value:
   `/composition/layers/1/clips/1/video/effects/transform/positionx "a" 320` sets 320 px. Blend modes
   accept the mode name as a string.
2. **Relative math server-side** — `"+"`, `"-"`, `"*"`:
   `/composition/layers/1/video/effects/transform/positionx "+" 50` nudges 50 px right.

**Polling:** send `"?"` to any address and Resolume replies on the same address with the current
value.

**OSC Output (feedback):** enabled separately; managed with OSC Shortcut presets. "Output All OSC
Messages" sends everything that changes — clip triggers, mouse and MIDI input, parameter automation,
clip playhead position — which adds up fast and is lossy over flaky wireless. Better practice is a
custom preset enabling output per UI item (right-click an item, or via the OSC Shortcuts panel).
**Wildcards** let you enable output for all clips/layers/groups at once, including clips not yet
added. **Custom addresses** let output be remapped to an arbitrary address for a foreign app.
Destinations: ZeroConf/Bonjour-discovered node, Localhost, Broadcast, or manual IP + port.
Bundles are toggleable.

**Input addresses are fixed and cannot be remapped.** Custom OSC *presets* affect output only, not
input. `[Forum]` — [OSC Arena 7.13.1](https://resolume.com/forum/viewtopic.php?t=22904)

**Listening interface.** Resolume displays one adapter's IP as information only; OSC actually listens
on all adapters, and sending follows the system routing table. A displayed APIPA address is cosmetic,
not a fault. `[Forum]` — [strange OSC IP Address??](https://resolume.com/forum/viewtopic.php?t=20559)

**`connect` vs `connected`** — a distinction that bites:
- `connect` is the clip **trigger action** — a mouse click. `1` = press, `0` = release.
- `connected` is the clip slot **state**.

Reported behavior: when switching decks with a clip connected, `0` is emitted for the outgoing deck's
clip — the release of the previous deck's clips. `[Forum]` — same thread, includes a Resolume
developer in the discussion. **Treat as a strong lead, not a spec.**

**OSC gaps:**
- ❌ **No structural operations** — cannot add/remove layers, columns, groups, or effects; cannot load media; cannot open/save compositions.
- ❌ **Cannot discover structure** — no way to ask "how many layers exist"; the address space must be known or scraped from the UI.
- ❌ **No stable IDs.** Addressing is by index or by selection only — there is no `by-id` equivalent, so reordering breaks absolute addresses. (REST/WebSocket `by-id` has no OSC counterpart.)
- ❌ No thumbnails, no monitor snapshots.
- ⚠️ Transport is UDP — unreliable and unordered by nature; the docs warn about message loss on wireless.

### 3.4 MIDI — mapped shortcuts with feedback

Enable input and output per device in the MIDI preferences. A built-in MIDI monitor shows all
messages sent/received. Nothing is addressable until a shortcut is assigned.

**Mapping model:** enter Shortcuts > Edit MIDI, click a control, press the physical control.
Shortcut identity = message type (Note/CC) + channel + number, plus **device identity**.

**Device disambiguation:** Resolume distinguishes which device a message came from, so two identical
controllers can drive different things **on the same channel with the same note numbers** — no Bomes
or channel-rewriting needed. Devices are marked first/second **by detection order, not by any
property of the device**, so the assignment can swap between sessions. "Any Device" input is
available if you'd rather not distinguish.

**Modes by message type:**

| Message | Modes available |
|---|---|
| Note | Toggle, Piano (momentary), Range, Value, **Velocity** |
| CC | Absolute, **Button**, Relative, Fake Relative |

- **Piano** = momentary; hold for on, release for off. Offers **Invert** (off while held).
- **Range** on a button-to-slider mapping sets the two values the slider jumps between on press/release.
- **Value** sets a slider to one specific value regardless of prior state.
- **Velocity** maps press force onto a range (controller must send it).
- **Button** mode is needed when a *button* sends CC rather than Note (Resolume names the Korg NanoKontrol series) — without it you lose Toggle/Piano/Value, because Resolume assumes a fader.
- **Relative** for endless encoders that send deltas; configurable Steps / Step Size (mutually dependent), plus Loop and Invert.
- **Fake Relative** for endless-feeling knobs that actually send absolute 0–127.

**Shortcut targets** (shared with DMX): **By Position** (follows order; default for layer/group
panels), **This** (bound to a specific clip/layer/group, survives moves, dies with deletion),
**Selected** (follows selection; default for clip-panel shortcuts).

**Shortcut Groups** — radio-button/dropdown controls (Clip Direction, Autopilot, blend modes).
Assign directly to one item; or use Select Next / Previous / Random Item to cycle; or assign the
same key to several items to toggle among them. A CC can cycle the whole group.

**Clip-trigger shortcut group:** a special group in front of the clip triggers lets one control fire
any clip in a layer — **a CC addresses clips 1–128 by value**. Works on columns too.

**Multiple shortcuts** per parameter via right-click > Duplicate Shortcut, each with its own settings.

**MIDI Out (feedback):** per-shortcut. Toggle/Value shortcuts let you set the velocity sent for Off
and On. **Clip triggers have five states**, each with its own velocity/color. Resolume ships colour
lookup tables for common controllers (APC40Mk2 has preview swatches). Output defaults to the
originating device; can be redirected to a specific device, All Devices, or disabled per shortcut.
If input and output device match, changing input auto-changes output — except where a device
reports different names for its in and out ports, in which case you're on your own.

**MIDI Clock (in):** set in MIDI preferences, not as a shortcut. Listens for Clock Start then follows
Clock Ticks, driving BPM as if tapped continuously. On Clock Stop, choose **Start/Stop** (BPM stops)
or **Switch to Manual** (keeps running). Resolume's own docs call MIDI Clock "notoriously wavy and
not really accurate" and recommend Ableton Link instead.

Device-specific mapping notes for the Behringer X-Touch Compact are in
`behringer-x-touch-compact.md` §6 and `behringer-xtouch-compact-resolume.md`.

**MIDI gaps:**
- ❌ Nothing works unmapped — no fixed address space, unlike OSC.
- ❌ No structural operations, no media loading, no composition open/save.
- ❌ Cannot read arbitrary parameter values; feedback exists only for mapped shortcuts.
- ❌ Cannot create or modify mappings programmatically (nor can any other protocol).
- ⚠️ Device order is detection-order, not identity — physical labelling does not bind.
- ⚠️ 7-bit resolution on CC unless the controller does 14-bit pairs.

### 3.5 DMX / Art-Net input — Arena only

Same shortcut engine as MIDI, different transport. Configured in the DMX preferences tab; there is
no USB-DMX support from Arena 6 onward (**Art-Net only** — Enttec-style USB devices require Arena 5).

**Lumiverses:** virtual input universes inside Resolume, each 512 channels, each mapped to a
Subnet/Universe (defaults to 0:0). They exist so shortcuts survive node disconnection and so
Subnet/Universe can be changed once rather than per-shortcut. Add more via New Input. A **Channel
Offset** shifts the first channel if other fixtures share the universe. Resolume announces available
inputs via ArtPoll.

**Per-shortcut options:** Invert, **16-bit** control, manual channel assignment, Lumiverse
selection, and **Range** to clamp a parameter (e.g. Scale limited to 100–200% instead of 0–1000%).

**Shortcut Groups** distribute values across the options — a 4-option group splits 1–63 / 64–128 /
128–191 / 191–255. The **clip-trigger group addresses clips 1–255 by value** (vs MIDI's 1–128).

**Universe counting:** Art-Net universe = Subnet × 16 + Universe + 1. 16 subnets × 16 universes =
256. Resolume follows the Art-Net spec and counts from 0 — noted because MadMapper and GrandMA each
count differently.

**Network:** adapter is selectable in DMX preferences and **this selection governs both DMX input
and output**. Localhost works "in most cases on Windows, some cases on OSX" and is officially
undefined behaviour because Art-Net uses one port for send and receive; start sender before
receiver. Node Name defaults to "Arena" + computer name. A built-in Art-Net monitor
(Artnetominator-style) shows subnet/universe/channel activity and per-channel history.

**No Auto-Map** since Arena 6 — mappings are built by hand, deliberately.

**DMX gaps:** everything MIDI lacks, plus: ❌ no feedback path at all (DMX in is one-way), ❌ 8-bit
per channel unless 16-bit is enabled per shortcut, ❌ Arena only.

### 3.6 DMX / Art-Net output — pixel data, not control

**Arena only.** Sends the colour/brightness of rendered pixels to fixtures. Organised as Lumiverses
containing fixtures; each fixture samples a region of the composition via Input Selection (position,
scale, rotation) and occupies a run of channels from a Start Channel (e.g. a 16-pixel RGB bar = 48
channels; the next starts at 49).

- **Auto Span** (default on) adds universes automatically past 512 channels, sent sequentially from the Lumiverse's Subnet.Universe.
- **Align Output** prevents a pixel's channels being split across a universe boundary — leave on unless spanning misbehaves.
- Targets: discovered Art-Net node by name (survives IP change), manual IP (survives device change), or Broadcast. Past ~30 universes, switch from broadcast to unicast + gigabit switching.
- Lumiverses have Opacity, Brightness, Contrast and Color like Screens; fixtures can be flipped H/V and brightness/contrast trimmed.
- **ArtSync** buffers frames at receivers and displays them on one broadcast message. Framerate and Delay are global to all universes; **default delay 40 ms** matches lights to projectors, set 0 for lights-only.
- A custom fixture can be built in the Fixture Editor.

**Gap:** this is not a state/event output. Resolume cannot send its own parameter state out over
Art-Net; only rendered pixel values.

### 3.7 SMPTE LTC — Arena only, playhead sync only

Audio-signal timecode (LTC) into an audio input, selected per input in the **Audio** preferences tab
along with framerate. **Two inputs simultaneously** (SMPTE 1 / SMPTE 2), so both tracks in a DJ mix
can be synced. Clips are assigned to an input via the Timeline dropdown; a layer-strip icon marks a
timecode-listening clip. SMPTE panel lives under the View menu.

- **Framerate** must match the *incoming signal*, not the clip. Commonly 25 or 29.97. A playhead jump at a regular 1-second interval means the wrong framerate is selected.
- **Offset** sets a clip's start timecode. Convention for multi-show nights: show 1 at 01:00:00:00, show 2 at 02:00:00:00.
- **Delay** compensation in frames, can be negative, for signal-flow lag / speed-of-sound on large stages.
- **Not available on clips with an audio track.**
- Arena accepts timecode **up to 35 hours** (the SMPTE spec stops at 24) — added in 7.0.4.

**SMPTE gaps — important:**
- ❌ **Does not trigger clips.** Only syncs the playhead of an already-active clip. The clip must be live in a layer or nothing shows. Column/clip launching from timecode requires third-party tooling.
- ❌ No output — Arena consumes timecode, does not generate it.
- ❌ Arena only.
- ⚠️ Mic-to-speaker capture does not work; needs a real line-level connection.

### 3.8 Ableton Link — BPM/phase sync, bidirectional

Hidden by default: View > Show Ableton Link, then a toolbar button. Peer-to-peer over the local
network; joins any session found automatically and shows the peer count. Keeps **BPM and position in
the measure** in sync both directions — change tempo anywhere and everyone follows.

**Deliberate limits:** Resync and Pause for BPM are **disabled** while Link is on, since a hard
measure reset or a global pause is considered bad practice in a session that assumes all peers are
equal. Anyone can change tempo as abruptly as anyone else, including x2.

Resolume's own docs recommend Link over MIDI Clock for tightness and setup simplicity.

**Gaps:** ❌ tempo and phase only — no parameter control, no triggering, no transport beyond tempo.

### 3.9 Keyboard shortcuts

Same shortcut engine and same Target/Group semantics as MIDI and DMX; the original of the three.
Local only, no feedback, no structural operations.

### 3.10 MCP servers — new in 7.26.0

Local MCP servers shipped with Arena/Avenue and Wire, driven from an AI desktop app (Claude Desktop,
Codex, or any MCP-capable client). Installed on **Windows** from
`C:\Program Files\Resolume Arena\mcp\resolume_arena_mcp_server.mcpb` via Claude Desktop >
Settings > Extensions > Advanced settings > Install Extension. Wire has its own server.

Intended for **building and modifying compositions, not live performance** — loading files and
sources, adding/removing effects, layers, columns, groups. Resolume recommends the latest Opus model
and notes that chat tool limits make Cowork the better surface for long sessions.

**MCP is explicitly capped at what REST can do**, and Resolume publishes the exclusion list — which
doubles as the clearest statement of the REST boundary:
- ❌ Advanced Output slices & screens
- ❌ Keyboard / MIDI / DMX / OSC mappings
- ❌ Clip cue points (create, modify or trigger)
- ❌ Presets — effects, sources, parameter animations, output, UI layout
- ❌ Parameter envelopes
- ❌ Dashboard dials (read or modify) — *see the contradiction flagged in §3.1*
- ❌ Recording the composition or rendering clips
- ◐ Only clips/files in the current deck; decks can be switched first

**Wire's own control surface** (separate from MCP): Wire supports both MIDI and OSC. OSC input is
enabled at **Preferences → OSC → OSC Input**, which displays the listening IP and incoming port.
`[Official]` — [TouchOSC manual — Setup: Resolume Wire](https://hexler.net/touchosc/manual/setup-resolume-wire).
Wire's REST/web server defaults to port **8081** and has its own API reference at
`resolume.com/docs/wirerestapi/`.

The **Wire** MCP server can drive most of Wire — creating and wiring nodes, setting inlet values,
renaming and colour-coding, dashboard parameter grouping, and writing ISF shaders — except
Dashboard presets, rendering patches, and compiling patches.

### 3.11 Pro DJ Link (Pioneer) and StageLinQ (Denon)

Network sync from DJ players so video follows the DJ's track. Documented separately by Resolume;
both are sync-class inputs, not general control. ProDJLink's own documentation describes the
practical path as SMPTE timecode over an audio cable with offsets configurable at both ends.

**Not verified this session** beyond the support-index listing and ProDJLink's page — read
`resolume.com/support/en/sync-to-pioneer-dj-players` and `.../sync-to-denon-players` before relying
on specifics.

---

## 4. Choosing a protocol — decision summary

| If you need… | Use |
|---|---|
| Build/modify composition structure | REST or WebSocket (or MCP, for authoring) |
| Push state back to a control surface | WebSocket `subscribe`, or OSC Output |
| Relative nudging, or values in real units (px, degrees, blend-mode names) | OSC |
| A physical control surface with LED/motor feedback | MIDI |
| Control from a lighting desk | DMX/Art-Net in (Arena) |
| Drive LED fixtures from video content | DMX/Art-Net out (Arena) |
| Lock clip playback to a show timeline | SMPTE LTC (Arena) — playhead only, does not trigger |
| Keep tempo aligned with musicians / other machines | Ableton Link |
| Stable references that survive reordering | REST/WebSocket `by-id` — **no OSC equivalent** |
| Anything involving mappings, presets, envelopes, cue points, slices, recording | **No protocol. UI only.** |

**Connection detectability, which matters for any control system** `[Official]`, from the Companion
module's documentation: OSC is **connectionless UDP and always reports OK** — a misconfigured OSC
path is undetectable and fails silently. REST errors on misconfiguration and is therefore
diagnosable. The Companion module falls back to OSC when the REST port is left blank. A control
system usually needs both enabled.

**OSC feedback path reminder:** Preferences → OSC → enable **OSC Output**, set destination IP and
port. Without this, nothing flows back and every downstream surface is open-loop.

**The universal gap:** shortcut mappings, shortcut presets, parameter envelopes, clip cue points,
Advanced Output slices/screens, effect/source/output/UI presets, and recording/rendering are
unreachable from *every* protocol. They are UI-only operations.

---

## 5. Appendix A — Full REST endpoint inventory

Generated from `swagger.yaml`: **295 operations across 258 paths**, grouped by primary tag.
Layergroup endpoints return **402 on Avenue**.


### `api` — 1 operations

| Method | Path | Summary |
|---|---|---|
| GET | `/product` | Retrieve product information |

### `files` — 1 operations

| Method | Path | Summary |
|---|---|---|
| POST | `/file-info` | Retrieve information about files |

### `sources` — 1 operations

| Method | Path | Summary |
|---|---|---|
| GET | `/sources` | Retrieve available sources for clips |

### `effects` — 2 operations

| Method | Path | Summary |
|---|---|---|
| GET | `/effects` | Retrieve available effects for clips |
| GET | `/effects/audio` | Retrieve available audio effects |

### `composition` — 30 operations

| Method | Path | Summary |
|---|---|---|
| GET | `/composition` | Retrieve the complete composition |
| PUT | `/composition` | Update the complete composition |
| POST | `/composition/action` | Undo or redo previously executed actions |
| POST | `/composition/copy-effects` | Copy effects to the composition |
| POST | `/composition/disconnect-all` | Disconnect all clips in the composition |
| POST | `/composition/effects/audio/add` | Add an audio effect to the entire composition |
| POST | `/composition/effects/audio/add/{offset}` | Add an audio effect to the entire composition at the given offset |
| POST | `/composition/effects/audio/move` | Move an audio effect to the end of the composition |
| POST | `/composition/effects/audio/move/{offset}` | Move an audio effect to the given offset in the composition |
| POST | `/composition/effects/audio/{effect-offset}/set-display-name` | Change the display name of an audio effect on the composition |
| DELETE | `/composition/effects/audio/{offset}` | Remove an audio effect from the entire composition |
| POST | `/composition/effects/by-id/{effect-id}/set-display-name` | Change the display name of an effect |
| POST | `/composition/effects/video/add` | Add an effect to the entire composition |
| POST | `/composition/effects/video/add/{offset}` | Add an effect to the entire composition |
| POST | `/composition/effects/video/move` | Move an effect to the end of the composition |
| POST | `/composition/effects/video/move/{offset}` | Move an effect to the end of the composition |
| POST | `/composition/effects/video/{effect-offset}/set-display-name` | Change the display name of a video effect on the composition |
| DELETE | `/composition/effects/video/{offset}` | Remove an effect from the entire composition |
| POST | `/composition/grow-to` | Grow the composition to at least the given dimensions |
| POST | `/composition/new` | Clear the composition, and start with a blank slate |
| POST | `/composition/open` | Open a new composition |
| POST | `/composition/save` | Save the composition |
| POST | `/composition/{parameter}/reset` | Reset a parameter in the composition to its default value. |
| GET | `/parameter/by-id/{parameter-id}` | Retrieve a parameter given its unique id |
| PUT | `/parameter/by-id/{parameter-id}` | Update a parameter given its unique id |
| DELETE | `/parameter/by-id/{parameter-id}/phase-source` | Reset the phase source to static |
| GET | `/parameter/by-id/{parameter-id}/phase-source` | Get the phase source of a parameter |
| PUT | `/parameter/by-id/{parameter-id}/phase-source` | Set the phase source of a parameter |
| POST | `/parameter/by-id/{parameter-id}/reset` | Reset a parameter |
| POST | `/parameter/by-id/{parameter-id}/trigger` | Trigger a parameter |

### `deck` — 17 operations

| Method | Path | Summary |
|---|---|---|
| POST | `/composition/decks/add` | Add a new deck to the composition |
| DELETE | `/composition/decks/by-id/{deck-id}` | Remove specified deck by id |
| GET | `/composition/decks/by-id/{deck-id}` | Retrieve deck properties by id |
| PUT | `/composition/decks/by-id/{deck-id}` | Update specific deck by id |
| POST | `/composition/decks/by-id/{deck-id}/close` | Close the given deck |
| POST | `/composition/decks/by-id/{deck-id}/duplicate` | Duplicate the given deck |
| POST | `/composition/decks/by-id/{deck-id}/open` | Re-open the given deck |
| POST | `/composition/decks/by-id/{deck-id}/select` | Select the deck by id |
| POST | `/composition/decks/by-id/{deck-id}/{parameter}/reset` | Reset a parameter in a deck to its default value. |
| DELETE | `/composition/decks/{deck-index}` | Remove a deck by index |
| GET | `/composition/decks/{deck-index}` | Retrieve deck properties by index |
| PUT | `/composition/decks/{deck-index}` | Update specific deck by index |
| POST | `/composition/decks/{deck-index}/close` | Close the given deck |
| POST | `/composition/decks/{deck-index}/duplicate` | Duplicate the given deck |
| POST | `/composition/decks/{deck-index}/open` | Re-open the given deck |
| POST | `/composition/decks/{deck-index}/select` | Select the deck by index |
| POST | `/composition/decks/{deck-index}/{parameter}/reset` | Reset a parameter in a deck to its default value. |

### `column` — 22 operations

| Method | Path | Summary |
|---|---|---|
| POST | `/composition/columns/add` | Add a new column to the composition |
| DELETE | `/composition/columns/by-id/{column-id}` | Remove specific layer by id |
| GET | `/composition/columns/by-id/{column-id}` | Retrieve column properties by id |
| PUT | `/composition/columns/by-id/{column-id}` | Update specific column by id |
| POST | `/composition/columns/by-id/{column-id}/connect` | Connect the column by id |
| POST | `/composition/columns/by-id/{column-id}/duplicate` | Duplicate the given column |
| POST | `/composition/columns/by-id/{column-id}/insert-copy` | Copy a column to this position by id |
| POST | `/composition/columns/by-id/{column-id}/insert-move` | Move a column to this position by id |
| POST | `/composition/columns/by-id/{column-id}/select` | Select the column by id |
| POST | `/composition/columns/by-id/{column-id}/{parameter}/reset` | Reset a parameter in a column to its default value. |
| POST | `/composition/columns/selected/insert-copy` | Copy a column to the selected column position |
| POST | `/composition/columns/selected/insert-move` | Move a column to the selected column position |
| POST | `/composition/columns/swap` | Swap columns |
| DELETE | `/composition/columns/{column-index}` | Remove a column by index |
| GET | `/composition/columns/{column-index}` | Retrieve column properties by index |
| PUT | `/composition/columns/{column-index}` | Update specific column by index |
| POST | `/composition/columns/{column-index}/connect` | Connect the column by index |
| POST | `/composition/columns/{column-index}/duplicate` | Duplicate the given column |
| POST | `/composition/columns/{column-index}/insert-copy` | Copy a column to this position |
| POST | `/composition/columns/{column-index}/insert-move` | Move a column to this position |
| POST | `/composition/columns/{column-index}/select` | Select the column by its position in the clip grid |
| POST | `/composition/columns/{column-index}/{parameter}/reset` | Reset a parameter in a column to its default value. |

### `layer` — 61 operations

| Method | Path | Summary |
|---|---|---|
| POST | `/composition/layergroups/by-id/{layergroup-id}/clear` | Disconnects any playing clips in the layer group by id |
| POST | `/composition/layers/add` | Add a new layer to the composition |
| DELETE | `/composition/layers/by-id/{layer-id}` | Remove specified layer by id |
| GET | `/composition/layers/by-id/{layer-id}` | Retrieve layer properties and clip info by id |
| PUT | `/composition/layers/by-id/{layer-id}` | Update specified layer and/or clips by id |
| POST | `/composition/layers/by-id/{layer-id}/clear` | Disconnects any playing clips in the layer by id |
| POST | `/composition/layers/by-id/{layer-id}/clearclips` | Clears all clips in the layer by id |
| POST | `/composition/layers/by-id/{layer-id}/copy-effects` | Copy effects from a source entity to this layer |
| POST | `/composition/layers/by-id/{layer-id}/duplicate` | Duplicate the given layer |
| POST | `/composition/layers/by-id/{layer-id}/effects/audio/add` | Add an audio effect to a layer by unique id |
| POST | `/composition/layers/by-id/{layer-id}/effects/audio/add/{offset}` | Add an audio effect to the layer with the given id, at the given offset |
| POST | `/composition/layers/by-id/{layer-id}/effects/audio/move` | Move an audio effect to the end of a layer |
| POST | `/composition/layers/by-id/{layer-id}/effects/audio/move/{offset}` | Move an audio effect to a specific offset inside the layer |
| DELETE | `/composition/layers/by-id/{layer-id}/effects/audio/{offset}` | Remove an audio effect from a layer |
| POST | `/composition/layers/by-id/{layer-id}/effects/video/add` | Add an effect to a layer by unique id |
| POST | `/composition/layers/by-id/{layer-id}/effects/video/add/{offset}` | Add an effect to the layer with the given id, at the given offset |
| POST | `/composition/layers/by-id/{layer-id}/effects/video/move` | Move an effect to the end of a layer |
| POST | `/composition/layers/by-id/{layer-id}/effects/video/move/{offset}` | Move an effect to a specific offset inside the layer |
| DELETE | `/composition/layers/by-id/{layer-id}/effects/video/{offset}` | Remove an effect from a layer |
| POST | `/composition/layers/by-id/{layer-id}/move` | Move a layer to a new position |
| POST | `/composition/layers/by-id/{layer-id}/remove-from-group` | Remove a layer from its group |
| POST | `/composition/layers/by-id/{layer-id}/select` | Select the layer by id |
| POST | `/composition/layers/by-id/{layer-id}/{parameter}/reset` | Reset a parameter in a layer to its default value. |
| GET | `/composition/layers/selected` | Retrieve layer properties and clip info for the selected layers |
| PUT | `/composition/layers/selected` | Update selected layer and/or clips |
| POST | `/composition/layers/selected/clear` | Disconnects any playing clips in the selected layer |
| POST | `/composition/layers/selected/clearclips` | Clears all clips in the selected layer |
| POST | `/composition/layers/selected/copy-effects` | Copy effects from a source entity to the selected layer |
| POST | `/composition/layers/selected/duplicate` | Duplicate the selected layer |
| POST | `/composition/layers/selected/effects/audio/add` | Add an audio effect to the selected layer |
| POST | `/composition/layers/selected/effects/audio/add/{offset}` | Add an audio effect at the given offset to the selected layer |
| DELETE | `/composition/layers/selected/effects/audio/{offset}` | Remove an audio effect from a layer |
| POST | `/composition/layers/selected/effects/video/add` | Add an effect to the selected layer |
| POST | `/composition/layers/selected/effects/video/add/{offset}` | Add an effect at the given offset to the selected layer |
| DELETE | `/composition/layers/selected/effects/video/{offset}` | Remove an effect from a layer |
| POST | `/composition/layers/selected/move` | Move the selected layer to a new position |
| POST | `/composition/layers/selected/remove-from-group` | Remove the selected layer from its group |
| POST | `/composition/layers/selected/{parameter}/reset` | Reset a parameter in the selected layer to its default value. |
| DELETE | `/composition/layers/{layer-index}` | Remove a layer by index |
| GET | `/composition/layers/{layer-index}` | Retrieve layer properties and clip info by index |
| PUT | `/composition/layers/{layer-index}` | Update specified layer and/or clips by index |
| POST | `/composition/layers/{layer-index}/clear` | Disconnects any playing clips in the layer by index |
| POST | `/composition/layers/{layer-index}/clearclips` | Clears all clips in the layer by index |
| POST | `/composition/layers/{layer-index}/copy-effects` | Copy effects from a source entity to this layer |
| POST | `/composition/layers/{layer-index}/duplicate` | Duplicate the given layer |
| POST | `/composition/layers/{layer-index}/effects/audio/add` | Add an audio effect to a layer by index |
| POST | `/composition/layers/{layer-index}/effects/audio/add/{offset}` | Add an audio effect to a layer by index, at the given offset |
| POST | `/composition/layers/{layer-index}/effects/audio/move` | Move an audio effect to the end of the layer |
| POST | `/composition/layers/{layer-index}/effects/audio/move/{offset}` | Move an audio effect to the given offset in the layer |
| POST | `/composition/layers/{layer-index}/effects/audio/{effect-index}/set-display-name` | Change the display name of an audio effect |
| DELETE | `/composition/layers/{layer-index}/effects/audio/{offset}` | Remove an audio effect from a layer |
| POST | `/composition/layers/{layer-index}/effects/video/add` | Add an effect to a layer by index |
| POST | `/composition/layers/{layer-index}/effects/video/add/{offset}` | Add an effect to a layer by index, at the given offset |
| POST | `/composition/layers/{layer-index}/effects/video/move` | Move an effect to the end of the layer |
| POST | `/composition/layers/{layer-index}/effects/video/move/{offset}` | Move an effect to the end of the layer |
| POST | `/composition/layers/{layer-index}/effects/video/{effect-index}/set-display-name` | Change the display name of an effect |
| DELETE | `/composition/layers/{layer-index}/effects/video/{offset}` | Remove an effect from a layer |
| POST | `/composition/layers/{layer-index}/move` | Move a layer to a new position |
| POST | `/composition/layers/{layer-index}/remove-from-group` | Remove a layer from its group |
| POST | `/composition/layers/{layer-index}/select` | Select the layer by index |
| POST | `/composition/layers/{layer-index}/{parameter}/reset` | Reset a parameter in a layer to its default value. |

### `layergroup` — 64 operations

| Method | Path | Summary |
|---|---|---|
| POST | `/composition/layergroups/add` | Add a new layer group to the composition |
| DELETE | `/composition/layergroups/by-id/{layergroup-id}` | Remove specified layer group by id |
| GET | `/composition/layergroups/by-id/{layergroup-id}` | Retrieve layer group properties and layer info by id |
| PUT | `/composition/layergroups/by-id/{layergroup-id}` | Update specified layer and/or clips by id |
| POST | `/composition/layergroups/by-id/{layergroup-id}/add-layer` | Add new layer to an existing layer group |
| POST | `/composition/layergroups/by-id/{layergroup-id}/copy-effects` | Copy effects from a source entity to this layer group |
| POST | `/composition/layergroups/by-id/{layergroup-id}/duplicate` | Duplicate the given layer group |
| POST | `/composition/layergroups/by-id/{layergroup-id}/effects/audio/add` | Add an audio effect to a layer group by unique id |
| POST | `/composition/layergroups/by-id/{layergroup-id}/effects/audio/add/{offset}` | Add an audio effect to a layer group by unique id |
| POST | `/composition/layergroups/by-id/{layergroup-id}/effects/audio/move` | Move an audio effect to the end of the layer group |
| POST | `/composition/layergroups/by-id/{layergroup-id}/effects/audio/move/{offset}` | Move an audio effect to the given offset in the layer group |
| DELETE | `/composition/layergroups/by-id/{layergroup-id}/effects/audio/{offset}` | Remove an audio effect from a layer group |
| POST | `/composition/layergroups/by-id/{layergroup-id}/effects/video/add` | Add an effect to a layer group by unique id |
| POST | `/composition/layergroups/by-id/{layergroup-id}/effects/video/add/{offset}` | Add an effect to a layer group by unique id |
| POST | `/composition/layergroups/by-id/{layergroup-id}/effects/video/move` | Move an effect to the end of the layer group |
| POST | `/composition/layergroups/by-id/{layergroup-id}/effects/video/move/{offset}` | Move an effect to the given offset in the layer group |
| DELETE | `/composition/layergroups/by-id/{layergroup-id}/effects/video/{offset}` | Remove an effect from a layer group |
| POST | `/composition/layergroups/by-id/{layergroup-id}/move` | Move a layer group to a new position |
| POST | `/composition/layergroups/by-id/{layergroup-id}/move-layer` | Add an existing layer to an existing layer group |
| POST | `/composition/layergroups/by-id/{layergroup-id}/select` | Select the layer group by id |
| POST | `/composition/layergroups/by-id/{layergroup-id}/{parameter}/reset` | Reset a parameter in a layer group to its default value. |
| DELETE | `/composition/layergroups/selected` | Remove the selected layer group |
| GET | `/composition/layergroups/selected` | Retrieve selected layer group properties and layer info |
| PUT | `/composition/layergroups/selected` | Update selected layer group and/or layers |
| POST | `/composition/layergroups/selected/add-layer` | Add new layer to the selected layer group |
| POST | `/composition/layergroups/selected/clear` | Disconnects any playing clips in the selected layer group |
| POST | `/composition/layergroups/selected/copy-effects` | Copy effects from a source entity to the selected layer group |
| POST | `/composition/layergroups/selected/duplicate` | Duplicate the selected layer group |
| POST | `/composition/layergroups/selected/effects/audio/add` | Add an audio effect to the selected layer group |
| POST | `/composition/layergroups/selected/effects/audio/add/{offset}` | Add an audio effect to the selected layer group |
| DELETE | `/composition/layergroups/selected/effects/audio/{offset}` | Remove an audio effect from a layer group |
| POST | `/composition/layergroups/selected/effects/video/add` | Add an effect to the selected layer group |
| POST | `/composition/layergroups/selected/effects/video/add/{offset}` | Add an effect to the selected layer group |
| DELETE | `/composition/layergroups/selected/effects/video/{offset}` | Remove an effect from a layer group |
| POST | `/composition/layergroups/selected/move` | Move the selected layer group to a new position |
| POST | `/composition/layergroups/selected/move-layer` | Add an existing layer to the selected layer group |
| POST | `/composition/layergroups/selected/{parameter}/reset` | Reset a parameter in the selected layer group to its default value. |
| DELETE | `/composition/layergroups/{layergroup-index}` | Remove a layer group by index |
| GET | `/composition/layergroups/{layergroup-index}` | Retrieve layer group properties and layer info by index |
| PUT | `/composition/layergroups/{layergroup-index}` | Update specified layer group and/or layers by index |
| POST | `/composition/layergroups/{layergroup-index}/add-layer` | Add a new layer to an existing layer group |
| POST | `/composition/layergroups/{layergroup-index}/clear` | Disconnects any playing clips in the layer group by index |
| GET | `/composition/layergroups/{layergroup-index}/columns/{column-index}` | Retrieve the column inside the layer group |
| PUT | `/composition/layergroups/{layergroup-index}/columns/{column-index}` | Update layer group column |
| POST | `/composition/layergroups/{layergroup-index}/columns/{column-index}/connect` | Connect the column in the layergroup by index |
| POST | `/composition/layergroups/{layergroup-index}/columns/{column-index}/select` | Select the column in the layergroup by index |
| POST | `/composition/layergroups/{layergroup-index}/copy-effects` | Copy effects from a source entity to this layer group |
| POST | `/composition/layergroups/{layergroup-index}/duplicate` | Duplicate the given layer group |
| POST | `/composition/layergroups/{layergroup-index}/effects/audio/add` | Add an audio effect to a layer group by index |
| POST | `/composition/layergroups/{layergroup-index}/effects/audio/add/{offset}` | Add an audio effect to a layer group by index |
| POST | `/composition/layergroups/{layergroup-index}/effects/audio/move` | Move an audio effect to the end of the layer group |
| POST | `/composition/layergroups/{layergroup-index}/effects/audio/move/{offset}` | Move an audio effect to the given offset in the layer group |
| POST | `/composition/layergroups/{layergroup-index}/effects/audio/{effect-index}/set-display-name` | Change the display name of an audio effect |
| DELETE | `/composition/layergroups/{layergroup-index}/effects/audio/{offset}` | Remove an audio effect from a layer group |
| POST | `/composition/layergroups/{layergroup-index}/effects/video/add` | Add an effect to a layer group by index |
| POST | `/composition/layergroups/{layergroup-index}/effects/video/add/{offset}` | Add an effect to a layer group by index |
| POST | `/composition/layergroups/{layergroup-index}/effects/video/move` | Move an effect to the end of the layer group |
| POST | `/composition/layergroups/{layergroup-index}/effects/video/move/{offset}` | Move an effect to the given offset in the layer group |
| POST | `/composition/layergroups/{layergroup-index}/effects/video/{effect-index}/set-display-name` | Change the display name of an effect |
| DELETE | `/composition/layergroups/{layergroup-index}/effects/video/{offset}` | Remove an effect from a layer group |
| POST | `/composition/layergroups/{layergroup-index}/move` | Move a layer group to a new position |
| POST | `/composition/layergroups/{layergroup-index}/move-layer` | Add an existing layer to an existing layer group |
| POST | `/composition/layergroups/{layergroup-index}/select` | Select the layer group by index |
| POST | `/composition/layergroups/{layergroup-index}/{parameter}/reset` | Reset a parameter in a layer group to its default value. |

### `clip` — 92 operations

| Method | Path | Summary |
|---|---|---|
| GET | `/composition/clips/by-id/{clip-id}` | Retrieve a clip by id |
| PUT | `/composition/clips/by-id/{clip-id}` | Update clip and/or its effects by id |
| POST | `/composition/clips/by-id/{clip-id}/clear` | Clears the clip with the given unique id |
| POST | `/composition/clips/by-id/{clip-id}/connect` | Connect the clip by id |
| POST | `/composition/clips/by-id/{clip-id}/copy-effects` | Copy effects from a source entity to this clip |
| POST | `/composition/clips/by-id/{clip-id}/effects/audio/add` | Add an audio effect to a clip by its unique identifier |
| POST | `/composition/clips/by-id/{clip-id}/effects/audio/add/{offset}` | Add an audio effect to a clip by its unique identifier |
| POST | `/composition/clips/by-id/{clip-id}/effects/audio/move` | Move an audio effect to the end of the clip |
| POST | `/composition/clips/by-id/{clip-id}/effects/audio/move/{offset}` | Move an audio effect to the given offset in the clip |
| DELETE | `/composition/clips/by-id/{clip-id}/effects/audio/{offset}` | Remove an audio effect from a clip |
| POST | `/composition/clips/by-id/{clip-id}/effects/video/add` | Add an effect to a clip by its unique identifier |
| POST | `/composition/clips/by-id/{clip-id}/effects/video/add/{offset}` | Add an effect to a clip by its unique identifier |
| POST | `/composition/clips/by-id/{clip-id}/effects/video/move` | Move an effect to the end of the clip |
| POST | `/composition/clips/by-id/{clip-id}/effects/video/move/{offset}` | Move an effect to the given offset in the clip |
| DELETE | `/composition/clips/by-id/{clip-id}/effects/video/{offset}` | Remove an effect from a clip |
| POST | `/composition/clips/by-id/{clip-id}/insert` | Inserts one or more sources and/or files, or copies of existing clips into the grid |
| POST | `/composition/clips/by-id/{clip-id}/open` | Loads a file or opens a source into the selected clip |
| POST | `/composition/clips/by-id/{clip-id}/openfile` | Loads file into clip with the given unique identifier |
| POST | `/composition/clips/by-id/{clip-id}/remove-audio-track` | Remove the audio track from a clip by its unique id |
| POST | `/composition/clips/by-id/{clip-id}/remove-video-track` | Remove the video track from a clip by its unique id |
| POST | `/composition/clips/by-id/{clip-id}/select` | Select the clip by id |
| DELETE | `/composition/clips/by-id/{clip-id}/thumbnail` | Revert thumbnail to default for the clip by id |
| GET | `/composition/clips/by-id/{clip-id}/thumbnail` | Retrieve the latest thumbnail belonging to the specified clip |
| POST | `/composition/clips/by-id/{clip-id}/thumbnail` | Set a custom thumbnail for the clip by id |
| POST | `/composition/clips/by-id/{clip-id}/thumbnail/update` | Update the clip thumbnail with the clip frame |
| GET | `/composition/clips/by-id/{clip-id}/thumbnail/{last-updated}` | Retrieve the latest thumbnail belonging to the specified clip |
| POST | `/composition/clips/by-id/{clip-id}/{parameter}/reset` | Reset a parameter in a clip to its default value. |
| POST | `/composition/clips/open` | Load one or more files and/or sources anywhere in the clip grid |
| GET | `/composition/clips/selected` | Retrieve the selected clip |
| PUT | `/composition/clips/selected` | Update selected clip and/or its effects |
| POST | `/composition/clips/selected/clear` | Clears the selected clip |
| POST | `/composition/clips/selected/connect` | Connect the selected clip |
| POST | `/composition/clips/selected/copy-effects` | Copy effects from a source entity to the selected clip |
| POST | `/composition/clips/selected/effects/audio/add` | Add an audio effect to the selected clip |
| POST | `/composition/clips/selected/effects/audio/add/{offset}` | Add an audio effect to the selected clip |
| DELETE | `/composition/clips/selected/effects/audio/{offset}` | Remove an audio effect from a clip |
| POST | `/composition/clips/selected/effects/video/add` | Add an effect to the selected clip |
| POST | `/composition/clips/selected/effects/video/add/{offset}` | Add an effect to the selected clip |
| DELETE | `/composition/clips/selected/effects/video/{offset}` | Remove an effect from a clip |
| POST | `/composition/clips/selected/insert` | Inserts one or more sources and/or files, or copies of existing clips into the grid |
| POST | `/composition/clips/selected/merge` | Merge another clip's tracks into the selected clip |
| POST | `/composition/clips/selected/open` | Loads a file or opens a source into the selected clip |
| POST | `/composition/clips/selected/openfile` | Loads file into the selected clip |
| POST | `/composition/clips/selected/remove-audio-track` | Remove the audio track from the selected clip |
| POST | `/composition/clips/selected/remove-video-track` | Remove the video track from the selected clip |
| DELETE | `/composition/clips/selected/thumbnail` | Revert thumbnail to default for the selected clip |
| GET | `/composition/clips/selected/thumbnail` | Retrieve the latest thumbnail belonging to the selected clip |
| POST | `/composition/clips/selected/thumbnail` | Set a custom thumbnail for the selected clip |
| POST | `/composition/clips/selected/thumbnail/update` | Update the clip thumbnail with the clip frame |
| GET | `/composition/clips/selected/thumbnail/{last-updated}` | Retrieve the latest thumbnail belonging to the selected clip |
| POST | `/composition/clips/selected/{parameter}/reset` | Reset a parameter in the selected clip to its default value. |
| POST | `/composition/clips/swap` | Swap two clips |
| GET | `/composition/effects/by-id/{effect-id}` | Retrieve effect properties given their unique identifier |
| PUT | `/composition/effects/by-id/{effect-id}` | Update effect by id |
| GET | `/composition/layers/by-id/{layer-id}/clips/active` | Retrieve a layer by id and get the active clip in it |
| PUT | `/composition/layers/by-id/{layer-id}/clips/active` | Retrieve a layer by id and update the active clip in |
| POST | `/composition/layers/by-id/{layer-id}/clips/by-id/{clip-id}/merge` | Merge another clip's tracks into a clip by id |
| GET | `/composition/layers/selected/clips/active` | Retrieve the active clip the currently selected layer |
| POST | `/composition/layers/selected/clips/active` | Update the active clip in the currently selected layer |
| GET | `/composition/layers/{layer-index}/clips/active` | Retrieve the active clip from a layer |
| POST | `/composition/layers/{layer-index}/clips/active` | Update the active clip in a layer |
| GET | `/composition/layers/{layer-index}/clips/{clip-index}` | Retrieve a clip by its position in the clip grid |
| PUT | `/composition/layers/{layer-index}/clips/{clip-index}` | Update clip and/or its effects by position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/clear` | Clears the clip by its position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/connect` | Connect the clip by its position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/copy-effects` | Copy effects from a source entity to this clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/audio/add` | Add an audio effect to a clip by its position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/audio/add/{offset}` | Add an audio effect to a clip by its position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/audio/move` | Move an audio effect to the end of the clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/audio/move/{offset}` | Move an audio effect to the given index in the clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/audio/{effect-index}/set-display-name` | Change the display name of an audio effect |
| DELETE | `/composition/layers/{layer-index}/clips/{clip-index}/effects/audio/{offset}` | Remove an audio effect from a clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/video/add` | Add an effect to a clip by its position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/video/add/{offset}` | Add an effect to a clip by its position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/video/move` | Move an effect to the end of the clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/video/move/{offset}` | Move an effect to the given index in the clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/effects/video/{effect-index}/set-display-name` | Change the display name of an effect |
| DELETE | `/composition/layers/{layer-index}/clips/{clip-index}/effects/video/{offset}` | Remove an effect from a clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/insert` | Inserts one or more sources and/or files, or copies of existing clips into the grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/merge` | Merge another clip's tracks into this clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/open` | Loads a file or opens a source into a clip by its position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/openfile` | Loads file into clip by its position in the clip grid |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/remove-audio-track` | Remove the audio track from a clip by its position |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/remove-video-track` | Remove the video track from a clip by its position |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/select` | Select the clip by its position in the clip grid |
| DELETE | `/composition/layers/{layer-index}/clips/{clip-index}/thumbnail` | Revert thumbnail to default for the specified clip |
| GET | `/composition/layers/{layer-index}/clips/{clip-index}/thumbnail` | Retrieve the latest thumbnail belonging to the specified clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/thumbnail` | Set a custom thumbnail for the specified clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/thumbnail/update` | Update the clip thumbnail with the clip frame |
| GET | `/composition/layers/{layer-index}/clips/{clip-index}/thumbnail/{last-updated}` | Retrieve the latest thumbnail belonging to the specified clip |
| POST | `/composition/layers/{layer-index}/clips/{clip-index}/{parameter}/reset` | Reset a parameter in a clip to its default value. |
| GET | `/composition/thumbnail/dummy` | Explicitly retrieve the dummy thumbnails used for clips without a thumbnail |

### `monitors` — 4 operations

| Method | Path | Summary |
|---|---|---|
| GET | `/composition/monitors` | List available render targets |
| GET | `/composition/monitors/{monitor-id}/snapshot` | Capture a PNG snapshot of a render target |
| GET | `/composition/monitors/{monitor-id}/snapshot.jpg` | Capture a JPEG snapshot of a render target |
| GET | `/composition/monitors/{monitor-id}/snapshot.png` | Capture a PNG snapshot of a render target |

---

## 6. Appendix B — OSC address shape

There is no static master list; the space is composition-dependent. Structure observed in the docs:

```
/composition/...                                  composition-level
/composition/layers/{n}/...                       layer by index
/composition/selectedlayer/...                    relative to selection
/composition/layers/{n}/video/opacity             e.g. layer opacity
/composition/layers/{n}/clips/{m}/...             clip by index
/composition/layers/{n}/clips/{m}/transport/position
/composition/layers/{n}/video/mixer/blendmode     Int 0-50
/composition/video/effects/transform/scale        Float 0.0-1.0 → 0-1000%
/composition/video/effects/transform/rotationz    Float 0.0-1.0 → -180..180
/composition/layers/{n}/clips/{m}/video/effects/{effect}/{param}
```

Argument forms:
```
<address> <float>                    normalised 0.0-1.0
<address> <int>                      for Int type tags
<address> "<name>"                   e.g. blendmode "Alpha"
<address> "a" <value>                absolute real-world units
<address> "+" | "-" | "*" <value>    relative math
<address> "?"                        poll; replies on same address
```

Sample list for a minimal composition: `resolume.com/download/Manual/OSC/OSC list.txt`.

---

## 7. Open items — not established this session

- The Dashboard contradiction in §3.1 (spec exposes `dashboard`, MCP page says REST can't reach dials).
- Whether OSC reaches clip cue points and parameter envelopes — REST demonstrably cannot; OSC is untested here.
- Pro DJ Link and StageLinQ specifics — listed, not read.
- Whether the supplied `swagger.yaml` matches the user's installed Arena build. `info.version` is `0.0.1` and carries no product version; the doc pages range 7.0.4–7.26.0.
- Exact REST/WebSocket behaviour for `selected` addressing when nothing is selected beyond the documented 404.
- Whether the `connect` deck-switch `0` emission is documented behavior or an acknowledged bug (carried from the earlier revision of this file).
- Full default OSC namespace under 7.20+ read from an official source rather than a third-party doc set (carried forward — partially addressed by §6 but still not an official complete list, which Resolume declines to publish).
