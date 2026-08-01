# TouchDesigner — Operators for Resolume Control Protocols

Which TouchDesigner operators speak each protocol Resolume exposes, and what they can and cannot do.
Pairs with `resolume-control-interfaces.md`, which covers the Resolume side of the same protocols.

**Target build:** TouchDesigner **2025.33070** (user-stated). ⚠️ The Derivative wiki does **not**
version its operator pages per build — pages carry a "TouchDesigner Build: Latest" marker and an
edit date, not a build number. Nothing below is confirmed *specifically* against 2025.33070; the
pages read were current as of the dates noted. Re-verify anything load-bearing against the running
build's own Python help.

## ⚠️ PROVENANCE — READ FIRST

This document has **two tiers of sourcing** and they are not equal.

**TIER A — full page read from docs.derivative.ca.** Complete parameter lists, methods and callbacks
as published. Trustworthy to the limits noted per section.

- `WebSocket_DAT` (page edited 2025-11-27)
- `WebsocketDAT_Class` (⚠️ page edited **2018-05-25** — see §1)
- `Ableton_Link_CHOP` (page edited 2023-11-24)
- `Timer_CHOP` (page edited 2025-10-28)
- `MIDI_In_CHOP` (page edited 2026-03-10)
- `MIDI_Out_CHOP` (page edited 2026-03-10)

**TIER B — assembled from search-result snippets, NOT full page reads.** Snippets are truncated
excerpts. **Parameters are certainly missing, and nothing here should be treated as a complete
list.** Verify against the page itself before building on any of it:

Web_Server_DAT · SocketIO_DAT · Web_Client_DAT · DMX_In_CHOP · DMX_Out_CHOP · LTC_In_CHOP ·
LTC_Out_CHOP · Timecode_CHOP · Info_CHOP · Perform_CHOP · Beat_CHOP · Speed_CHOP · Trigger_CHOP ·
Count_CHOP · Event_CHOP · Logic_CHOP · Sync_In_CHOP · Sync_Out_CHOP · Touch_Out_CHOP ·
MIDI_In_Map_CHOP · OSC operators

Some Tier B snippets came from the `derivative.ca/UserGuide/` mirror rather than
`docs.derivative.ca`. Content appears to match, but that is an assumption, not a check.

**TIER C — not consulted at all.** Clock_CHOP, Timeline_CHOP, Art-Net_DAT, MIDI_Event_DAT,
MIDI_In_DAT, MIDI_In_Map_CHOP, Touch_In_CHOP, OSC_In_DAT, OSC_Out_DAT.

**Every Tier B section below is marked inline.** Tier A sections are unmarked.

**Target build:** TouchDesigner **2025.33070** (user-stated). The Derivative wiki does **not**
version operator pages per build — pages carry a "TouchDesigner Build: Latest" marker and an edit
date only. Nothing here is confirmed specifically against 2025.33070.

---

## 0. Protocol → operator map

| Resolume protocol | Direction | TouchDesigner operator | Notes |
|---|---|---|---|
| **WebSocket API** | Bidirectional | **WebSocket DAT** | TD as *client*. The right operator for a Resolume control hub |
| REST API | TD → Resolume | **Web Client DAT** | Outbound HTTP incl. digest auth |
| REST/WS (TD as server) | Browser → TD | **Web Server DAT** | For TD's *own* browser UI, not for talking to Resolume |
| OSC | TD → Resolume | **OSC Out CHOP** / **OSC Out DAT** | CHOP for continuous, DAT for addressed/string |
| OSC | Resolume → TD | **OSC In CHOP** / **OSC In DAT** | |
| MIDI | Surface → TD | **MIDI In CHOP** / **MIDI In DAT** / **MIDI In Map CHOP** / **MIDI Event DAT** | |
| MIDI | TD → surface | **MIDI Out CHOP** | LED/motor feedback |
| Art-Net / DMX in | Console → TD | **DMX In CHOP** | Also sACN, KiNET, FTDI |
| Art-Net / DMX out | TD → fixtures | **DMX Out CHOP** (or **DMX Out POP** + **DMX Fixture POP**) | |
| SMPTE LTC | Audio → TD | **Audio Device In CHOP** → **LTC In CHOP** | Two-operator chain |
| SMPTE LTC | TD → audio | **LTC Out CHOP** → **Audio Device Out CHOP** | TD can *generate* LTC; Resolume cannot |
| Timecode handling | Internal | **Timecode CHOP**, `tdu.Timecode` | |
| Ableton Link | — | **Not established** — see §7 |
| Resolume MCP | — | Not a TD-facing protocol; AI desktop app only |

---

## 1. WebSocket DAT — the operator for a Resolume control hub

Receives and parses WebSocket messages, appending each as a row in the DAT's table. The table is
**FIFO** and limited to a parameter-set number of lines. An optional script runs per packet. Secure
(TLS) servers supported, and connections to different WebSocket sites work without manual header
setup.

**This is TD acting as a client** — the correct operator for connecting out to Resolume's
`ws://address:8080/api/v1`. Distinct from Web Server DAT, which is TD acting as a server.

### Parameters — Connect page

| Parameter | Name | Behaviour |
|---|---|---|
| Active | `active` | While on, the DAT receives. **While off, no updating occurs and data sent to the port is lost** |
| Network Address | `netaddress` | Hostname or IP. `localhost` for same machine |
| Network Port | `port` | **Port 443 implies a secure connection.** For a secure connection on any other port, a `wss://` prefix is required on Network Address |
| Connection Timeout | `timeout` | Milliseconds to wait when connecting. An **upper limit** — connection may fail sooner |

### Parameters — Received Messages page

| Parameter | Name | Behaviour |
|---|---|---|
| Callbacks DAT | `callbacks` | Executes once per incoming message |
| Execute from | `executeloc` | `current` / `callbacks` / `op` |
| From Operator | `fromop` | Used when Execute from is Specified Operator |
| Clamp Output | `clamp` | Default limit is 100 messages; can be set to anything including unlimited |
| Maximum Lines | `maxlines` | Oldest messages removed first |
| Clear Output | `clear` | Pulse. `op("opname").par.clear.pulse()` |
| Bytes Column | `bytes` | Outputs raw message bytes in a separate column |

### Methods (`websocketDAT_Class`)

All return `int` — bytes sent, or **negative on error**:

- `sendText(message)` — send a text frame. Multiple strings are joined **without spaces**
- `sendBinary(contents)` — binary frame; accepts strings, byte arrays, or single-byte numeric values
- `sendPing(contents)` — ping request
- `sendPong(contents)` — pong reply; contents should match the originating ping

For Resolume, every message must be valid JSON — build the dict and `json.dumps()` into `sendText()`.

### Callbacks

```python
def onConnect(dat): return
def onDisconnect(dat): return
def onReceiveText(dat, rowIndex, message): return   # text frames only
def onReceiveBinary(dat, contents): return          # binary frames only
def onReceivePing(dat, contents):
    dat.sendPong(contents)                          # documented default: reply with same message
    return
def onReceivePong(dat, contents): return
def onMonitorMessage(dat, message): return          # websocket status messages
```

⚠️ **Provenance warning:** the parameter pages above were edited 2025-11-27, but the
`WebsocketDAT_Class` page carrying these methods and callbacks was **last edited 2018-05-25**. The
signatures may lag the current build. **Verify against the running build's own Python help before
building on them** — the no-false-numbers rule applies with force here.

### Findings that matter for hub design

**No reconnect parameter exists on this operator.** The Connect page has Active, Network Address,
Network Port, Connection Timeout — and nothing else. By contrast the **SocketIO DAT** *does* expose
`reset` (disconnect then reconnect) and `delay` (Reconnect Delay in ms). The absence on WebSocket DAT
is from reading the full parameter list, but "no documented parameter" is not the same as "no
reconnect behaviour" — the operator may reconnect internally without exposing it. **Untested.**

Practical consequence either way: **reconnect logic has to be built, not assumed.** The available
hooks are `onDisconnect`, `onMonitorMessage`, and toggling `par.active` off/on. Given the
never-root-caused drop-after-subscribe in the Arena Sequencer, treat this as required work.

**Status and error messages go to the TouchDesigner text console, not the operator.** The text
console is off by default; enable with environment variable `TOUCH_TEXT_CONSOLE=1`, and it opens on
the next TouchDesigner launch. On Windows this is set via System Properties → Environment Variables.
`onMonitorMessage` is the in-network equivalent and is the better hook for programmatic health
checks.

**FIFO table is a debugging aid, not a data path.** With Resolume's `parameter_update` pushing on
every subscribed change, the table will churn constantly. Drive logic from `onReceiveText`; keep
`maxlines` low or use Clear Output to stop the table becoming a performance drag.

**SocketIO DAT is the wrong operator here** — Resolume speaks plain WebSocket, not socket.io.

---

## 2. Web Client DAT — REST  ⚠️ TIER B (snippets only)

Outbound HTTP requests including digest auth. The right choice when the far end is a REST API and
you want to *see* failures: an HTTP call has a status code, unlike OSC.

For Resolume this covers everything in the 295-operation REST surface — structural changes, media
loading, thumbnails, monitor snapshots. **Not read in full this session**; existing coverage is in
`creative-coding/references/touchdesigner-integration.md` §1.

---

## 3. Web Server DAT — TD as server (not a Resolume path)  ⚠️ TIER B (snippets only)

TD acting as a web server so clients (browsers) connect *to* TouchDesigner. Supports HTTP,
WebSockets, and binary send/receive including image upload/download. Built with **POCO v1.13.3**.

Key parameters: `active` (start/stop), `restart` (pulse to restart while active), `port`,
`localaddress` (choose a NIC; **blank means listen on all interfaces**), `secure` (TLS → HTTPS),
`privatekey`, `callbacks`.

WebSocket-side callbacks: `onWebSocketOpen(client address)`, `onWebSocketClose(client address)`,
`onWebSocketReceiveText`, `onWebSocketReceiveBinary`. HTTP callbacks receive a `request` and must
**return** a `response` dictionary — extra key/value pairs added to it become HTTP response headers.

**This is what the Arena Sequencer used** — for its phone/browser UI, not for talking to Resolume.
Don't reach for it to connect *to* Resolume; that's WebSocket DAT.

---

## 4. OSC operators  ⚠️ TIER B / C — not read this session

Four operators: **OSC In/Out CHOP** for channels, **OSC In/Out DAT** for messages handled in Python.
All UDP.

Choose by data shape: continuous streams of numbers → CHOP; sparse, addressed, string-carrying, or
needing dispatch logic → DAT. Resolume's `"a"` / `"+"` / `"-"` / `"*"` / `"?"` argument forms are
string-tagged and multi-argument, so **OSC Out DAT is the operator for those** — a CHOP can't
express them.

OSC In CHOP is connectionless and accepts messages from any number of sources on one port
simultaneously. Fuller treatment in `creative-coding/references/touchdesigner-integration.md` §1.

---

## 5. MIDI operators

### 5a. MIDI In CHOP *(Tier A — full page read, page edited 2026-03-10)*

Reads Note events, Controller events, Program Change, System Exclusive and Timing events, from
devices **or MIDI files**. Supported events: Note On/Off, Polyphonic Aftertouch, Channel Pressure,
Program Change, Control Change, Pitch Wheel, Timer events including beat pulses, Bar Messages,
Start/Stop/Continue, Song Position Pointer, System Exclusive.

Any number of MIDI CHOPs can read from the same or different sources. TouchDesigner can be
configured so MIDI Start/Stop/Continue control the Timeline and Beat Dialog.

**Four findings that matter for this build:**

**1. `Channel Prefix` (`prefix`) is what makes the channel-per-layer scheme work.** With it blank,
input streams from multiple MIDI channels are **merged into one set of CHOP channels** — a "note 64
on" on channel 12 followed by "note 64 off" on channel 8 appears in the *same* note-64 CHOP channel
as a single note. Put a string like `ch` in this parameter and each MIDI channel splits into its own
CHOP channels. Given Layer A on ch1 and Layer B on ch2 sharing control numbers, **leaving this blank
would silently collapse both layers into one stream.** `MIDI Channels` (`channel`) accepts ranges
and multiple entries: `"1 4 6"`, `"1-7 12"`, `"1-5:2"`.

**2. `Preserve Pulses` (`preservepulses`)** — spaces quick value transitions across consecutive
output samples. Documented use: **when pulse frequencies approach or exceed the timeline rate,
otherwise they risk overlapping each other and being lost.** Button presses at 60 fps are exactly
this case.

**3. Sample rate can lose events outright.** From the page: if the sample rate is too low you may
miss MIDI events — a note event sets a sample to 1, and the next event less than 1/30 second later
sets it to 0 **on the same sample**, so the event is missed. Derivative's remedy: **raise the sample
rate, e.g. 600**, or guarantee a minimum separation between on/off events. There is also an
`Automatic High Frequency` mode capturing at **1000 samples/second** for events faster than the
timeline rate.

**4. The `.toe` restore trap is documented and called unavoidable.** MIDI input values are saved
into the `.toe` and restored on reload; the physical controllers may sit elsewhere, so values jump
when the controls are next moved. Derivative states plainly: *"This is unavoidable."* Confirms the
existing note in `creative-coding/references/touchdesigner-integration.md` §6 — and settles that
it's a design constraint, not a bug to chase. Mitigations are `Reset Channels` / `Reset Values`
(and their pulse variants) at startup.

**14-bit controller spec, in full** (`format` = `7bit` / `14bit`):
- MSB must be in controller range **0–31**; LSB in **32–63**, with **LSB index = MSB index + 32** (MSB 12 → LSB 44).
- Index pairs **98,99** and **100,101** may also be used as MSB/LSB.
- **A single message in range 0–63 outputs nothing** in 14-bit mode.
- Range **64–95 is always interpreted as 7-bit** and output as such.

**Other parameters worth knowing:**
- `1 Based Index` (`onebased`) — indices become 1–128 instead of 0–127. **Affects both Note and Controller indices.** This is the index-offset setting behind the bench-confirmed 1-based behaviour.
- `Simplified Output` (`simplified`) — auto-creates a channel per MIDI event type as it arrives; no name/channel/index patterns needed. **Turning this on disables the Record, Note, Control, Timer and Sys pages entirely.**
- `Normalize` — Controller page offers None (0–127, or 0–16383 for 14-bit), `0 to 1`, `-1 to 1`, and **On/Off (≥64 → 1, <64 → 0)**. Note page offers None or `0 to 1`. Pitch wheel is always −1 to +1.
- `Unwrap` — values don't jump between min and max but become continuous ramps. **Documented specifically for knob controllers** — relevant to encoders.
- `Note Output` — One Multiplexed Channel (value = most recent note number) vs Separate Channels (one CHOP channel per note).
- `Velocity` — Off / Note Amplitude (only valid with Separate Channels) / Separate Channels.
- `Record Method` — Single Frame (cooks only when MIDI arrives), Current Frame (recooks every frame), Current Time Slice, Full Length.
- `Controller Type` — By Index Only, or a named controller from a list; `Controller Index` accepts ranges like `"1-32 70-80:2"`.
- Timer page captures beat pulses, ramps, period, start, ticks-per-beat, bar ramp/period/start/message, song position.
- Info CHOP channels are the common CHOP and operator sets only — **no MIDI-specific info channels.**

### 5b. MIDI Out CHOP *(Tier A — full page read, page edited 2026-03-10)*

Sends MIDI events **when its input channels change**, evaluated over the last time slice. The
Python `midioutCHOP Class` can send any event type through an existing MIDI Out CHOP without CHOP
inputs — which is the path behind the bench-confirmed raw-`send()`-bypasses-normalize finding.

**Channel naming IS the API** — events are mapped by channel name:
- `ch3n60` — MIDI channel 3, note 60. **Note On fires only when the value goes from 0 or less to greater than zero**; Note Off similarly. This is the semantics to write LED states against.
- `ch5n` — no trailing number, so the channel *value* is the note number, quantized to integer. Stepping 53 → 78 sends Note Off for 53 then Note On for 78.
- `ch14c7` — value sent to controller 7 on MIDI channel 14. By default 0–1 maps to MIDI 0–127.
- `pc` (program change) and `pw` (pitch wheel) need no trailing number — they go to the whole channel.
- Prefixes are configurable (`prefix`, `notename`, `controlname`, etc.), and channels can be renamed with a **Rename CHOP** before entering — the pattern already in your library.

**⚠️ `Cook Every Frame` (`cookalways`) — turn this ON.** Derivative's own wording: it should be on
"because the MIDI Out CHOP will otherwise only cook if the CHOP leads to a graphics display viewer."
For a headless feedback path with no viewer downstream, leaving this off means **feedback silently
never sends**. Likely the first thing to check if LEDs don't light.

**`events_sent` is a specific Info CHOP channel** on this operator. Notable given §10: the MIDI
feedback leg *does* expose a supervision signal, while the WebSocket leg exposes none.

**MIDI output runs in a separate thread**, so it slows TouchDesigner less.

**Time Slice mode works for note and controller events — but NOT for Program Change or Sysex.**

**14-bit output has a different constraint from 14-bit input:** controller indices must be in
**0–31**, because **32–63 is reserved for the paired messages and is not user-accessible** in this
mode. Range **64–95 is always sent as a single 7-bit message.**

**Other parameters:** `active`; `destination` (Device or File, MIDI Mapper is the default);
`device` / `id`; `onebased`; `file` / `writefile` (capture a MIDI stream to a file);
`autonoteoff` (All Note Off at playback start, end, both, or none); `reset` (All Notes Off to all
channels); `volumeoff` / `volumeon` (emit Controller 7 events on all 16 channels); `startstop`
(send Start/Stop/Continue when the framebar starts or stops); **`sendmtc` — sends MIDI Timecode as
quarter-frame messages**, with `timecodeop` taking a CHOP with hour/minute/second/frame channels, a
DAT with a timecode string, or a Timecode Class object; `notenorm` (None or 0-to-1);
`controlnorm` (None / 0-to-1 / -1-to-1 / **On-Off**); `barname` + `barticks` for MIDI clock output
from a 0–1 bar ramp (**default 96 = 4 beats × 24 ticks per beat**).

### 5c. Other MIDI operators  ⚠️ TIER B / C — not read this session

| Operator | Use |
|---|---|
| MIDI In CHOP | Continuous values as channels — working input for a mapped surface |
| MIDI In DAT | Raw message inspection — the ground-truth capture tool |
| MIDI In Map CHOP | Mapper-based indirection |
| MIDI Out CHOP | Feedback — motors, LED rings, button LEDs |
| MIDI Event DAT | Event-driven handling in Python |

Detail, plus the bench-confirmed 8-argument MIDI In DAT callback, the 1-based index offset, and the
raw-`send()`-bypasses-normalize finding, are in
`creative-coding/references/touchdesigner-integration.md` and
`behringer-xtouch-compact-resolume.md`. Not restated here.

---

## 6. DMX operators — Art-Net, sACN, KiNET, FTDI  ⚠️ TIER B (snippets only)

**DMX In CHOP** receives; **DMX Out CHOP** sends. Channel values are **0–255**.

Supported interfaces per the DMX overview page: **Art-Net** (DMX512-A over UDP), **sACN**
(DMX over IP via UDP), **KiNET** (Philips Color Kinetics), **FTDI** serial. Developed against ENTTEC
hardware but documented as working with many devices. DMX Out POP + DMX Fixture POP are the newer
POP-family path.

**DMX Out CHOP:**
- First input channel = first DMX address; channels map to consecutive DMX channels in order (12 channels in → DMX channels 1–12)
- `netaddress` — receiving device IP. **Default `255.255.255.255` broadcasts to all devices.** Art-Net Net/Subnet/Universe must match the receiver in all cases, broadcast included
- `localaddress` — pick the NIC by IP when the machine has several
- `localport` — default `-1` means OS-assigned
- `routingtable` — a docked Table DAT routing channels to universes by net/subnet/universe; available when using Packet Per Channel format for Art-Net or sACN

**DMX In CHOP:**
- ⚠️ **Input rate is limited to the DMX maximum refresh rate of 44 Hz**
- Filter Table DAT: rows per channel with net/subnet/universe, plus optional `srcaddress` and `destaddress` columns — only packets matching those IPs are accepted. Single IP per cell, **regex not supported**; blank accepts all. `srcaddress` is the documented remedy for DMX noise on the network. An `id` column gives a unique channel suffix alongside those
- Multicast builds the IP automatically from Net/Subnet/Universe, allowing receipt without knowing the sender's address
- `queuesize` — incoming packet queue; smooths data at the cost of latency

**Relevance to a Resolume rig:** Resolume Arena's own Art-Net output is pixel data to fixtures, and
its Art-Net input is shortcut-mapped control. TD sitting alongside can either take console DMX in
(DMX In CHOP) and translate to WebSocket, or drive fixtures directly (DMX Out CHOP) — but note both
Resolume and TD sending Art-Net on the same universes will conflict. Also note Resolume's DMX
preference selects **one adapter governing both its input and output**.

---

## 7. Timecode operators  ⚠️ TIER B (snippets only)

**LTC In CHOP** reads SMPTE timecode encoded in an audio signal. **The audio must first come in via
an Audio Device In CHOP**, which then feeds the LTC In CHOP — a two-operator chain.
- `inputrate` — complete frame messages per second the signal encodes, usually 24–30
- `discrete` — adds `frame`, `second`, `minute`, `hour` channels
- `totalframes` — total elapsed LTC frames; **this value changes if up-sampling to timeline FPS**
- `totalsec` — total elapsed seconds

**LTC Out CHOP** *generates* LTC, output to an Audio Device Out CHOP. Notable because **Resolume
consumes timecode but cannot generate it** — TD can be the timecode master for a Resolume rig.
- `playmode` — `sequential` (counts forward) or `timecodeop` (driven by a reference)
- `timecodeop` — a CHOP with `hour`/`minute`/`second`/`frame` channels, a DAT with a timecode string in its first cell, or a `Timecode Class` object
- `play`, `cue`, `cuepulse`, `frame` — transport and initial value
- `duplicateframes`, `audiorate`
- `user1`–`user4` — LTC User Data bits, conventionally reel number and date, usable for anything

**Timecode CHOP** and `tdu.Timecode` handle timecode internally. The `smpte` flag, when enabled,
conforms to SMPTE — non-negative, loops at 24 hours. **Disabled, it allows negative timecode and a
maximum of 100 hours.** Worth knowing against Resolume Arena's documented acceptance of timecode up
to **35 hours** (past the SMPTE 24-hour limit) — the two non-conforming behaviours are not the same
and have not been tested together.

---

## 7a. Ableton Link CHOP — confirmed, and the model for status monitoring

**Ableton Link CHOP exists.** Retrieves timing from an Ableton Link network. (Full Ableton Live
integration is a separate thing — **TDAbleton**, a component set reaching Songs, Tracks, Chains,
Parameters and MIDI.)

**Ableton page:** `active` (output on/off), `enable` (initializes the Link session connection),
`startstopsync` (start/stop sync across the session, allowing start/stop sharing between subgroups
of peers), `signature1`/`signature2` (time signature), `callbacks` (DAT of per-event callbacks).

**Output page — each is a toggle adding channels:**

| Group | Channels |
|---|---|
| **Status** (`status`) | `numpeers` (Link devices/apps found), `linked` (connected to the Link network), `waiting` (waiting, not synced), `synced` (synced with the network) |
| Musical position | `bar`, `beat`, `sixteenths`, `beats` (total), `phase` (current phase in the bar) |
| Tempo | `tempo` (BPM) |
| Generated per-bar | `ramp` (0–1 each bar), `pulse`, `sine`, `count`, `countramp` |
| Per-beat | `rampbeat` (0–1 each beat); `rampbar` (0–1 each bar) |

**Info CHOP channels** add clock-health detail: `ableton_link_clock`, `ableton_td_clock`,
`ableton_clock_adjust_count`, `ableton_clock_diff`, `ableton_max_clock_diff`,
`ableton_clock_diff_to_adjust`, `ableton_time_behind_link`, `ableton_lost_time`,
`ableton_startstop_sync_enable`, `ableton_is_playing`, `ableton_tempo`.

⚠️ **Documented gotcha:** Ableton Link does not work with all sound drivers, **including DirectX**.
Derivative points at ASIO4All as a free virtual ASIO replacement. Relevant on Windows.

**Why this matters beyond tempo:** Resolume also speaks Link, so TD and Resolume can share a session
directly without the hub brokering tempo at all. And the `linked`/`synced`/`waiting`/`numpeers`
channels are a worked example of connection health exposed *as CHOP channels* — which is exactly
what WebSocket DAT does **not** provide (see §10).

---

## 8. What TouchDesigner does not obviously cover

- **Resolume MCP servers** — an AI-desktop-app integration, not a TD-facing protocol. No operator path.
- **Pro DJ Link / StageLinQ** — no TD operator identified in the CHOP or DAT family lists; not researched further.

---

## 10. CHOPs — often the easier path, and one important gap

The CHOP family was enumerated from the operator list on the Ableton Link CHOP page. Protocol-facing
CHOPs relevant here: **Ableton Link, Audio Device In/Out, DMX In/Out, LTC In/Out, MIDI In, MIDI In
Map, MIDI Out, OSC In, OSC Out, Timecode, Timeline, Timer, Serial, Sync In/Out, Script, Info**.

**Where CHOPs beat DATs for this work:**
- **Continuous values** — fader positions, encoder values, DMX channel levels, opacity. Channels are numeric and exportable straight to parameters; no parsing, no callback.
- **Status as channels** — Ableton Link CHOP's `linked`/`synced`/`numpeers` can drive UI or logic by expression instead of Python state-keeping.
- **Info CHOP on any operator** — cook counts, error/warning counts, and operator-specific channels, readable as numbers. The general health-monitoring tool.
- **Export** rather than scripting: `exportmethod` (DAT Table by Index / by Name / Channel Name is Path:Parameter) wires channels to parameters directly.

**Where DATs remain necessary:**
- Anything **addressed and string-carrying** — Resolume's WebSocket JSON, and OSC's `"a"` / `"+"` / `"?"` argument forms. No CHOP can express these.
- Sparse events needing dispatch logic.

### ⚠️ The gap: WebSocket DAT has no connection-status channel

The WebSocket DAT's Info CHOP channels are **only** `num_rows`, `num_cols`, plus the common operator
channels (`total_cooks`, `cook_time`, `cook_frame`, `cook_abs_frame`, `cook_start_time`,
`cook_end_time`, `cooked_this_frame`, `warnings`, `errors`). **There is no `connected`, `linked`, or
equivalent channel** — unlike Ableton Link CHOP, which exposes exactly that.

Consequence for the hub: **connection health cannot be read as a CHOP channel.** It has to come from
the `onConnect` / `onDisconnect` / `onMonitorMessage` callbacks, or be inferred — e.g. watching
`num_rows` stop advancing, or timing since the last `onReceiveText`. Combined with the absent
reconnect parameter (§1), connection supervision on the Resolume leg is entirely hand-built.

**Not read this session:** Clock CHOP, Timeline CHOP. Everything else listed is covered in §11.

---

## 11. Utility CHOPs for hub logic  ⚠️ TIER B except Timer CHOP

Not protocol operators, but the pieces a control hub is actually assembled from.

⚠️ **Timer CHOP below is Tier A (full page read). Everything else in this section is Tier B —
snippet-sourced, parameter lists incomplete.**

### Supervision and health

**Info CHOP** — extra information about *any* node, exposed as channels. Different node types carry
different subsets. The operator-specific attributes are **also available as Python members** of that
operator, so the same data is reachable either way. Notably: any OP with a `.timecode` member also
gets a **Timecode Info Type**, viewing timecode as a set of channels. Parameter: `op` (path of the
node being inspected).

This is the general health tool — but see §10: on WebSocket DAT it yields only `num_rows`,
`num_cols` and the common cook/error channels. **`errors` and `warnings` counts are the usable
supervision signal there**, alongside `num_rows` advancing.

**Perform CHOP** — many channels describing the state of the TouchDesigner process itself:
frames-per-second, and the **cook time of the prior drawn frame**. Intended for real-time
self-tuning driven from within the network. Documented tip: feed it into a **Trail CHOP** to see
which frames cooked and which were skipped — the recommended way to find out whether a target frame
rate is actually being hit. Relevant if the hub's message volume starts costing frames.

### Timing and state

**Timer CHOP** *(Tier A — full page read)* — an engine for timed processes, explicitly documented as
able to **operate as a state machine**.

**Time Control** (`timecontrol`) has four modes, and two matter here: **Sequential**
(timeline-independent), **Lock To Timeline** (deterministic, non-deterministic features disabled),
**External CHOP Channel** (master time driven by a CHOP channel), and **External Timecode** (master
time driven by a timecode CHOP/DAT/Object). The External modes mean a Timer can be slaved to
incoming LTC.

**Callbacks:** `onInitialize()`, `onStart()`, `onTimerActive()` (every running frame with no delay
and Play on), `onCycleStart()`, `onCycleEndAlert()` (fires N units before a cycle/segment/done —
set by `cycleendalert`, so you can prepare the next step), `onSegmentEnter()` / `onSegmentExit()`
(when driven by a Segments DAT; the `segment` argument is an object carrying your custom columns —
`print(help(segment))` to inspect), `onDone()`. `.masterSeconds` in `onInitialize()` initializes at
a specific time.

**Segments DAT columns** (`segdat`): `delay` or `begin`, `length`, `cycle`, `cyclelimit`,
`maxcycles`, `cycleendalert` — these override the equivalent parameters. `begin` replaces `delay`
and means time from Start. **Serial Timers** plays segments back to back; **Parallel Timers** runs
them simultaneously, each with its own begin, length and full set of output channels. Custom columns
can be routed to extra channels (`channelcolumns`) with step/linear/ease interpolation, or to an
Info DAT (`infocolumns`).

**Four independent time counts, each behaving differently** — this is the part worth knowing:

| Count | Speed | Play off | Cycles | Go To / Cue | Delay between segments |
|---|---|---|---|---|---|
| Cumulative | slows if speed<1 | pauses | keeps counting | jumps | pauses |
| Playing | unaffected | pauses | keeps counting | keeps counting | keeps counting |
| Running | unaffected | unaffected | keeps counting | keeps counting | keeps counting |
| Master | slows if speed<1 | pauses | see note | jumps | keeps counting |

*Note: jumps back every cycle if Cycle Limit is off; keeps counting up if Cycle Limit is on.*

**Running Time** is wall-clock since Start regardless of delays, speeds, cycles or premature
segment-end clicks, and stops at Done — the one to use for a reconnect watchdog. Python members:
`.cumulativeSeconds`, `.playingSeconds`, `.runningSeconds`, `.masterSeconds`.

**Output channels** (each toggled on the Outputs page): `timer_fraction`, `timer_seconds` /
`timer_frames` / `timer_samples`, `timer_active`, `timer_pulse`, `delay_fraction`, `initializing`,
`ready`, ready pulse, `running`, `done`, done pulse, `cycles`, cycle pulse, `cycle_plus_fraction`,
`segment`, `segment_pulse`, `segment_plus_fraction`, `length`, plus the four count families above.

**Other parameters worth knowing:** `active` (Never / Always / While Running / While Playing —
controls when the CHOP cooks at all), `deferpars` (parameter changes ignored until next Initialize,
avoiding mid-run state jumps), `lengthtype` Fixed or **Infinite**, `play`, `speed`, `cue` /
`cuepoint`, `cycle` / `cyclelimit` / `maxcycles`, `exitendcycle`, `gotoendcycle`, `gotodone`,
`ondone` (Do Nothing / Re-Initialize / Re-Start / Re-Start without Initializing). Sub Range page
limits output to a portion of the length with Pause or Loop at end. Default sample rate 60.

**Info CHOP channels:** `frames_timer`, `frames_segment`, `frames_cumulative`, `frames_running`. Outputs seconds, frames, samples, fraction and on-off states while counting,
including a `done` channel. Triggered by pulsing parameters or via its second input. Python
callbacks fire at timing events, from which you can set parameters, read/write DATs, CHOPs and
storage, restart itself, or trigger other nodes. Play/pause plus a speed control; can cycle
indefinitely and be signalled to stop immediately or at end of cycle.

- **Multiple segments in one Timer CHOP** — attach a Table DAT, one timer per row. Custom text strings per segment go in the Info DAT, and custom animated channels can be created.
- **Chaining** — export one Timer's `ready_pulse` channel to the next Timer's Initialize parameter. They must all be Initialized together.
- **Looping** — set the On Done menu to Re-Start.
- ⚠️ **Start-frame gotcha:** on the frame you press Start, `running` goes 0→1 and all `timer_` counters step forward by one frame. Set **Run Value to Zero** to hold the timers at 0 until the next frame — documented as mattering when cutting from black to a visible first frame.

This is the strongest candidate for the hub's reconnect backoff and for layer-switch replay timing.

**Beat CHOP** — ramps, pulses and counters timed to BPM. Channels: `ramp`, `pulse`, `sine`,
`count`, `countramp`, `bar`, `beat`, `sixteenths`, `rampbar`, `rampbeat`, and **`bpm`**. Note the
channel set is nearly identical to Ableton Link CHOP's, minus Link's status channels and with `bpm`
in place of `tempo` — so a hub can swap between local beat and network-synced Link with little
rewiring. `$MASTER_BEAT` is set to whichever Beat CHOP has that option enabled.

**Speed CHOP** — integrates a rate into a cumulative value (speed → distance). Feed it a constant 1
and the output rises by 1 per second; negative values decrease it; 0 holds. Resettable via the Reset
parameter or by sending a channel >0 into the second input. Useful for time-since-last-event
counters — e.g. seconds since the last `parameter_update`, which is the inferred-health signal §10
calls for.

### Event detection

**Trigger CHOP** — converts a threshold crossing into an envelope with independently settable peak
and sustain levels (**peak can never be less than sustain**). Works with time-sliced or static
inputs. Parameters: `threshold` (release = trigger threshold), `threshup`, `threshdown`,
`retrigger` (Re-Trigger Delay — time after a trigger before a new one may occur), `mintrigger`
(minimum time the trigger stays active). For jittery inputs, Derivative's own snippet
"trigger after a time threshold" pairs it with the Count CHOP.

`retrigger` and `mintrigger` are the debounce primitives — relevant to the fader-touch lag and to
gating layer-switch replays.

**Count CHOP** — counts threshold crossings, in static or realtime ("Cook to Current Frame") mode.
Default trigger value is 0: a count occurs when input goes from ≤0 to >0. Crossing the trigger level
upward is a *trigger event*; crossing the release level downward is a *release event*. On each event
the count can increment, decrement, add time, or reset to zero. Operations can also run while the
input stays above or below a level.

**Event CHOP** — outputs **seven channels** describing events, each with a unique `id` (sequence
number from 0) and `index` (the channel index of the incoming CHOP that caused it). First input is
event triggers, second resets them, third optionally samples values per event. Designed for
overlapping, individually-tracked events — worth considering if per-control state needs to survive
concurrently rather than as one global value.

**Logic CHOP** — logic operations on samples. With one input, inverts values; can also reduce N
channels to one via `or`/`and`/etc. With two or more inputs, combines channels across CHOPs,
reducing N CHOPs to 1. For arithmetic between channels use the **Math CHOP** instead.

### Multi-machine

**Sync In / Sync Out CHOP** — keeps timelines in two or more TouchDesigner *processes* within a
single frame of each other. One process holds Sync Out; the others hold Sync In.

- Sync In processes should have their **Realtime flag off** — their frame rate is set by Sync Out.
- **All monitors, clients and server, must be set to the same rate.** Adding or removing monitors can silently change previously configured settings.
- They synchronise by pausing their own timeline until all Sync In/Out CHOPs have cooked; **Sync Out runs ahead of Sync In**.
- ⚠️ **If any CHOP fails to communicate, the others time out and all processes run slowly.** Clients may come and go; Sync Out adjusts by timing out and temporarily or permanently banning individual clients.
- Info channel `sync_serial` — last serial index sent from Sync Out, incrementing per message.

**Touch In / Touch Out CHOP** — TD-to-TD channel transport. `syncports` sends all data in a single
global pipe (internally port **10500**) when streams must stay frame-synced, rather than separate
ports per port number. Not read in full; noted because it is the TD-native alternative to using OSC
between two TouchDesigner machines.

---

## 9. Open items

- Whether WebSocket DAT reconnects internally without a documented parameter, and what `onDisconnect` fires on versus `onMonitorMessage`.
- Whether the `WebsocketDAT_Class` callback signatures (page dated 2018) still match build 2025.33070.
- Whether the Arena Sequencer's never-root-caused drop-after-subscribe was a Web Server DAT problem or follows to WebSocket DAT as a client.
- Whether build 2025.33070 is current; the wiki does not version operator pages per build.
- Clock CHOP and Timeline CHOP — still unread.
- Touch In/Out CHOP read only at summary level; the synced-ports behaviour is noted, not verified in detail.
- Whether Timer CHOP's callback-driven state machine or plain Python in the WebSocket callbacks is the better home for reconnect backoff. Untested either way.
- Whether TD and Resolume sharing an Ableton Link session directly is preferable to brokering tempo through the hub. Untested.
- Web Client DAT, OSC operators and MIDI operators were **cross-referenced, not re-read** this session — their detail lives in the creative-coding library and may itself predate this build.
- ⚠️ **Library split note:** `creative-coding/references/touchdesigner-integration.md` §1 currently holds an operator-selection table, which is a vendor fact and arguably belongs here in `digital-video`. Not moved — flagging so the split doesn't drift.


---

## 12. DATs not yet covered — candidates for this build

Enumerated from the complete DAT family list on the WebSocket DAT page (Tier A page content).
**None of these have been read** — listed so the gap is explicit rather than invisible.

**Likely to matter for a Resolume hub:**

| DAT | Why it's a candidate |
|---|---|
| **JSON DAT** | Resolume's WebSocket traffic is entirely JSON. May remove hand-rolled `json.loads()` from the callbacks. **Highest-value unread operator.** |
| **Error DAT** | Catches errors programmatically. Possible supervision path for the WebSocket-DAT-has-no-status-channel gap in §10 — worth checking before settling for inference. |
| **CHOP Execute DAT** | Fire Python on channel change. The natural bridge from MIDI In CHOP channels to hub routing logic. |
| **DAT Execute DAT** | Fire Python on DAT change — e.g. when the WebSocket DAT's table receives a row. |
| **Parameter Execute DAT** / **ParGroup Execute DAT** | Fire on parameter change. |
| **OP Execute DAT** | Fire on operator state change (flags, children, etc.). |
| **Execute DAT** | Frame/start/exit hooks — what the Arena Sequencer used for its clock. |
| **Table DAT** | The mapping table itself; also feeds Timer CHOP segments and DMX routing/filter tables. |
| **Info DAT** | Timer CHOP pairs with it for timecodes and per-segment custom columns. |
| **Examine DAT** | Inspects storage contents — fits the debug-by-observing-live-state method. |
| **Text DAT** / **Script DAT** | Module code and generated tables. |

**Transport alternatives, if a leg needs raw access:**
Art-Net DAT · MQTT Client DAT · TCP/IP DAT · UDP In DAT · UDP Out DAT · UDT In/Out DAT ·
Serial DAT · Touch In/Out DAT · WebRTC DAT · Web DAT

**Device and system enumeration:**
Monitors DAT · Audio Devices DAT · Serial Devices DAT · Video Devices DAT · Perform DAT ·
Media File Info DAT · NDI DAT

**Full DAT family, for completeness** (from the Tier A page): Art-Net, Audio Devices, CHOP Execute,
CHOP to, Clip, Convert, CPlusPlus, DAT, Execute (DAT Execute), DAT Export, Error, EtherDream,
Evaluate, Examine, Execute, FIFO, File In, File Out, Folder, In, Indices, Info, Insert, JSON,
Keyboard In, Lookup, Media File Info, Merge, MIDI Event, MIDI In, Monitors, MPCDI, MQTT Client,
Multi Touch In, NDI, Null, OP Execute, OP Find, OSC In, OSC Out, Out, Panel Execute, Parameter,
Parameter Execute, ParGroup Execute, Perform, POP to, Render Pick, Reorder, Script, Select, Serial,
Serial Devices, SocketIO, SOP to, Sort, Substitute, Switch, Table, TCP/IP, Text, Touch In, Touch
Out, Transpose, TUIO In, UDP In, UDP Out, UDT In, UDT Out, Video Devices, Web Client, Web, Web
Server, WebRTC, WebSocket, XML.
