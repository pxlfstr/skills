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

*First pass (§1, §5a/b, §7a, §11 Timer):*

- `WebSocket_DAT` (page edited 2025-11-27)
- `WebsocketDAT_Class` (⚠️ page edited **2018-05-25** — see §1)
- `Ableton_Link_CHOP` (page edited 2023-11-24)
- `Timer_CHOP` (page edited 2025-10-28)
- `MIDI_In_CHOP` (page edited 2026-03-10)
- `MIDI_Out_CHOP` (page edited 2026-03-10)

*Second pass, 2026-08-01 — promoted out of Tier B (§2, §3, §4, and three of §11):*

- `Web_Client_DAT` (page edited 2025-11-21)
- `Web_Server_DAT` (page edited 2026-06-04)
- `OSC_In_DAT` (page edited 2026-02-20)
- `OSC_Out_DAT` (⚠️ page edited **2022-05-21**)
- `OSC_In_CHOP` (⚠️ page edited **2022-07-19**, and internally inconsistent — see §4)
- `OSC_Out_CHOP` (page edited 2026-02-12)
- `Info_CHOP` (page edited 2023-12-18)
- `Perform_CHOP` (page edited 2025-06-04)
- `Trigger_CHOP` (page edited 2025-12-11)

*Third pass, 2026-08-01 — promoted out of Tier B and C:*

- `Clock_CHOP` (page edited 2026-01-21)
- `Timeline_CHOP` (page edited 2023-12-04)
- `Beat_CHOP` (page edited 2024-11-06)
- `Speed_CHOP` (page edited 2025-10-28)
- `Count_CHOP` (page edited 2026-01-23)
- `Event_CHOP` (⚠️ page edited **2021-11-16**, and self-contradictory on channel count — see §11)
- `Logic_CHOP` (⚠️ page edited **2021-11-16**; Derivative marks the operator superseded — see §11)
- `MIDI_In_DAT` (page edited 2026-03-10)
- `MIDI_In_Map_CHOP` (⚠️ page edited 2023-11-02 but carries an unresolved 2009 "needs updating"
  note — see §5e; treat as the weakest Tier A entry here)

**TIER B — everything not yet given a full page read.** Two kinds, and the difference matters:

*Snippet-sourced (some detail below, certainly incomplete):*
DMX_In_CHOP · DMX_Out_CHOP · LTC_In_CHOP · LTC_Out_CHOP · Timecode_CHOP · Sync_In_CHOP ·
Sync_Out_CHOP · Touch_Out_CHOP

*Not consulted at all (no detail below, listed so the gap is visible):*
Art-Net_DAT · Touch_In_CHOP

*Fourth pass, 2026-08-01 — cleared the outstanding item and opened a new category:*

- `MIDI_Event_DAT` (page edited 2026-03-10) — §5f
- `midiinDAT_Class` (⚠️ page edited **2018-05-25**) — §5g
- `midieventDAT_Class` (⚠️ page edited **2018-05-25**) — §5g

## ⚠️ PYTHON CLASS PAGES — a category that was silently skipped

Every operator page links to a Python class page carrying members, methods and **callback
signatures**. Through passes one to three these were **not read and not tracked**, so "Tier A —
full page read" in this file has meant *the operator page only*. That is now stated rather than
assumed.

**Class pages read:** `websocketDAT_Class` (pass 1) · `midiinDAT_Class` · `midieventDAT_Class` ·
`midioutCHOP_Class` · `timerCHOP_Class` (both 2024-08-15) · `oscoutDAT_Class` · `oscinDAT_Class` (both 2024-11-07) · `webclientDAT_Class` (⚠️ 2022-05-23) · `webserverDAT_Class` (⚠️ 2021-01-20) ·
`midiinCHOP_Class` (2023-12-19 — **read on both `docs` and the mirror; they match verbatim**, see §5i) ·
`midiinmapCHOP_Class` (⚠️ 2018-05-25 — empty, see §5j)

**Class pages NOT read, for operators that are otherwise Tier A:**

| Class page | Why it likely matters |
|---|---|
| `oscinCHOP_Class` / `oscoutCHOP_Class` | Likely thin, unverified |
| `abletonlinkCHOP_Class` | Unverified |
| `abletonlinkCHOP_Class` · `infoCHOP_Class` · `performCHOP_Class` · `triggerCHOP_Class` · `countCHOP_Class` · `eventCHOP_Class` · `logicCHOP_Class` · `speedCHOP_Class` · `beatCHOP_Class` · `clockCHOP_Class` · `timelineCHOP_Class` · `midiinmapCHOP_Class` | Most CHOP classes report no operator-specific members or methods; expected to be thin, **but that is an expectation, not a check** |

⚠️ Note the pattern: the three class pages read so far were all last edited **2018**, while their
operator pages are current. Class pages appear to be maintained on a much slower cycle. Weigh
accordingly.

Some Tier B snippets came from the `derivative.ca/UserGuide/` mirror rather than
`docs.derivative.ca`. Content appears to match, but that is an assumption, not a check.

*(Tier C has been folded into Tier B.)*

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
Network Port, Connection Timeout — and nothing else. That absence is from reading the full parameter
list, but "no documented parameter" is not the same as "no reconnect behaviour" — the operator may
reconnect internally without exposing it. **Untested.**

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

## 2. Web Client DAT — REST

Sends HTTP requests to a server and puts the response in the DAT. The right choice when the far end
is a REST API and you want to *see* failures: an HTTP call has a status code, unlike OSC. Successor
to the deprecated Web DAT.

For Resolume this covers the whole REST surface — structural changes, media loading, thumbnails,
monitor snapshots.

### Parameters — Web Client page

| Parameter | Name | Behaviour |
|---|---|---|
| Active | `active` | Toggles the operator on/off |
| Request Method | `reqmethod` | `get` / `post` / `put` / `delete` / `head` / `options` / `patch` |
| URL | `url` | Target URL. For a secure server it should begin with `https://` |
| Upload File | `uploadfile` | File contents sent to the server, **chunked if necessary** |
| Request | `request` | Pulse — sends the request |
| Stop | `stop` | Stops the stream of data from the server |
| Stream | `stream` | Enables streaming. Only needed if the server supports it |
| Verify Certificate (SSL) | `verifycert` | TLS certificate verification |
| Timeout | `timeout` | Milliseconds before giving up when no response arrives |
| Include Header in Output | `includeheader` | Puts the response header in the DAT output |

### Parameters — Authentication page

`authtype` offers **None / Basic / Digest / OAuth1 / OAuth2**. Digest is documented as base-64
username and password encrypted with a hashing function — a more secure Basic. Credentials go in
`username` / `pw`; OAuth1 uses `appkey`, `appsecret`, `oauthtoken`, `oauthsecret`; OAuth2 uses
`clientid` and `token`.

### Parameters — Output page

| Parameter | Name | Behaviour |
|---|---|---|
| Clear Output | `clear` | Clears the DAT |
| Clamp Output as Rows | `clamp` | Output becomes a **table instead of text**, clamped to Maximum Lines. **Should be on whenever streaming is on** |
| Maximum Lines | `maxlines` | Row cap when clamping |
| Callbacks DAT | `callbacks` | The callbacks DAT |

### Operator inputs

- **Input 0** — extra request headers. A **two-column table**, name/value pairs
  (e.g. `Content-Type` / `application/json`).
- **Input 1** — data/parameters. Two-column name/value table, or plain text sent as-is. If the
  method has no request body (GET, OPTIONS), a table input is **appended to the URL as query
  parameters**; non-table input is sent as request data.

### Info CHOP channels — the reason this operator supervises better than WebSocket DAT

`download_progress` · `downloaded_size` · `total_size` · **`connected`** · **`connection_error`** ·
**`communicating`**, plus `num_rows` / `num_cols` and the common operator channels.

**This is a real asymmetry and it matters for hub design:** the REST leg exposes connection state as
CHOP channels; the WebSocket leg does not (§10). If the hub needs a connection-health readout without
hand-built Python state, the REST leg can supply one and the WebSocket leg cannot.

### `webclientDAT_Class` — driving §2 from Python
*(Tier A — full page read, ⚠️ page edited **2022-05-23**)*

**Member:** `connections` → list **(read only)** — *"a list of active connection identifiers."*

**Methods:**

```python
request(url, method, header=None, data=None, pars=None,
        authType=None, username=None, password=None,
        appKey=None, appSecret=None, oauth1Token=None, oauth1Secret=None,
        oauth2Token=None, uploadFile=None, timeout=60000) -> int
closeConnection(id) -> None
```

- **`request()` returns a connection identifier.** Every keyword mirrors a parameter on the operator,
  so a single Web Client DAT can serve many differently-configured calls without touching its
  parameters — the useful property for a hub that talks to several endpoints.
- `method` must be one of `"GET"`, `"POST"`, `"PUT"`, `"DELETE"`, `"HEAD"`, `"OPTIONS"`, `"PATCH"` —
  **as a string**.
- `pars` are **URL-encoded and appended to the URL**; `data` goes in the body; `header` is a dict.
- ⚠️ **`uploadFile` is only valid with a PUT request method.**
- `timeout` defaults to **60000 ms** — a full minute. Far too long for a show cue that should fail
  fast; set it down explicitly.

**Callbacks:**

```python
def onConnect(webClientDAT): return
def onDisconnect(webClientDAT): return
def onResponse(webClientDAT, statusCode, headerDict, data): return
```

- `statusCode` is a **dict with two keys, `'code'` and `'message'`** — not a bare integer.
- `headerDict` is **only sent once when streaming.**

**⚠️ The page contradicts itself, and this one has consequences.** `request()` is documented as
returning an identifier that *"will correspond with the id passed to onResponse callbacks"* — but the
documented `onResponse` signature **has no `id` argument at all**. Taken literally there is no way to
correlate a response with the request that caused it, which is exactly what a hub firing several
concurrent REST calls needs. Either the signature is stale or the return-value description is
aspirational. **Check `onResponse`'s actual arguments in the running build before designing around
request/response correlation.** The page is from 2022; the operator page is from 2025.

**This also bears on the §10 supervision question.** The existence of `connections` (plural, a list)
and `closeConnection(id)` shows the operator tracks **multiple concurrent connections by id** — which
makes it likely that the `connected` Info CHOP channel is an aggregate rather than a per-request
flag. Likely, not stated. Still worth confirming before treating it as a health signal.

---

## 3. Web Server DAT — TD as server (not a Resolume path)

TD acting as a web server so clients (browsers) connect *to* TouchDesigner. Supports HTTP,
WebSockets, and binary send/receive including image upload/download. Built with **POCO v1.13.3**.
**Most functionality passes through the Callbacks DAT** — the docs say so explicitly.

### Parameters — Web Server page

| Parameter | Name | Behaviour |
|---|---|---|
| Active | `active` | Starts and stops the server |
| Restart | `restart` | Pulse — restarts the server while active |
| Port | `port` | Connection port, e.g. `9980` → `localhost:9980` |
| Local Address | `localaddress` | Pick a NIC. **Blank means listen on all interfaces** |
| Callbacks DAT | `callbacks` | Where the behaviour actually lives |

### Callbacks

`onHTTPRequest` — receives `request` (a dict of HTTP headers) and a `response` dict (status, reason).
Extra key/value pairs added to `response` **become headers in the HTTP response**, and the response
**must be returned** from the callback.

`onWebSocketOpen(client address)` · `onWebSocketClose(client address)` · `onWebSocketReceiveText` ·
`onWebSocketReceiveBinary` · `onServerStart` · `onServerStop`.

### Parameters — Secure page

| Parameter | Name | Behaviour |
|---|---|---|
| Secure (TLS) | `secure` | Server runs HTTPS instead of HTTP |
| Private Key File Path | `privatekey` | TLS private key |
| Certificate File Path | `certificate` | TLS certificate |
| Certificate Password | `password` | ⚠️ **Only visually hidden — still readable via Python.** To encrypt it on save, put the Web Server DAT inside a private component |
| Verify Client | — | Enables **mTLS**: client certificate must verify to complete the handshake |
| Minimum TLS Protocol | `minprotocol` | `tlsv10` / `tlsv11` / `tlsv12` / `tlsv13` |

Authentication is **Basic only**, via `authenticateBasic` in `webserverDAT_Class`; the credentials
arrive under the `Authorization` key of the request dict. The docs state plainly that security is
entirely the user's responsibility.

### Info CHOP channels

**`server_running`** · **`websocket_connections`**, plus `num_rows` / `num_cols` and the common
operator channels. Unlike WebSocket DAT, the *server* side does expose a live connection count.

### `webserverDAT_Class` *(Tier A — full page read, ⚠️ page edited **2021-01-20**, oldest class page here)*

**Member:** `webSocketConnections` (read only) — *"a string list of all the Web Socket connections in
the server."* Note this is a **list of client addresses**, while the Info CHOP only gives a count
(`websocket_connections`). The list is what you'd use to broadcast.

**Methods — all keyed by client address:**

```python
authenticateBasic(token, userPasswords) -> bool
webSocketSendText(client, data) -> None
webSocketSendBinary(client, data) -> None
webSocketSendPing(client, data=None) -> None
webSocketSendPong(client, data=None) -> None
webSocketClose(client) -> None
```

- **`authenticateBasic`** takes the token from an HTTP Basic Authorization header plus a
  **dictionary of accepted username/passwords**, and returns True/False. That's the whole auth story
  — a dict of credentials living in the network (see the §3 warning about putting the Web Server DAT
  in a private component).
- **Every send is per-client.** There is no broadcast method — iterate `webSocketConnections`.

**⚠️ The callback signatures here contradict the operator page (§3 above).** The operator page lists
`onWebSocketOpen(client address)`; the class page gives **`onWebSocketOpen(dat, client, uri)`** — with
a `uri` argument the operator page never mentions. The class page's callbacks are fully type-annotated
and clearly newer in style despite being the older page:

```python
def onHTTPRequest(dat, request: Dict, response: Dict) -> Dict
def onWebSocketOpen(dat, client: str, uri: str)
def onWebSocketClose(dat, client: str)
def onWebSocketReceiveText(dat, client: str, data: str)
def onWebSocketReceiveBinary(dat, client: str, data: bytes)
def onWebSocketReceivePing(dat, client: str, data: bytes)
def onWebSocketReceivePong(dat, client: str, data: bytes)
def onServerStart(dat)
def onServerStop(dat)
```

**`onWebSocketReceivePing` and `onWebSocketReceivePong` are not on the operator page at all** — §3's
callback list was incomplete. The documented default for the ping handler auto-replies:
`dat.webSocketSendPong(client, data=data)`.

**The `request` dict is documented in full**, and this is the useful part:

| Key | Contents |
|---|---|
| `'method'` | HTTP method — `'GET'`, `'PUT'`, … |
| `'uri'` | Requested URI path. **Query parameters are stripped out into `'pars'`, not left in the URI** |
| `'pars'` | The query parameters |
| `'clientAddress'` / `'serverAddress'` | Both ends of the connection |
| `'data'` | The request body |

**The `response` dict:** `'statusCode'` (integer — **default is 404**, so an un-filled response is a
Not Found), `'statusReason'`, `'data'`. **Arbitrary extra keys become response headers** —
`response['content-type'] = 'application/json'` is the documented example. The response dict must be
returned from the callback.

⚠️ **`statusCode` defaulting to 404** is worth designing around: any request path your callback
doesn't explicitly handle silently returns Not Found rather than erroring visibly.

**This is what the Arena Sequencer used** — for its phone/browser UI, not for talking to Resolume.
Don't reach for it to connect *to* Resolume; that's WebSocket DAT.

---

## 4. OSC operators

Four operators: **OSC In/Out CHOP** for channels, **OSC In/Out DAT** for messages handled in Python.

Choose by data shape: continuous streams of numbers → CHOP; sparse, addressed, string-carrying, or
needing dispatch logic → DAT. Resolume's `"a"` / `"+"` / `"-"` / `"*"` / `"?"` argument forms are
string-tagged and multi-argument, so **OSC Out DAT is the operator for those** — a CHOP can't
express them.

**Transport is not the same across the four.** The DATs offer Messaging (UDP), Multi-Cast Messaging
(UDP), **and Reliable Messaging (UDT library)**. OSC In CHOP offers only UDP and multicast. OSC Out
CHOP lists all three. So a reliable-transport OSC leg is a DAT job, not an In-CHOP job — and both
CHOP pages state flatly that OSC CHOPs use UDP.

⚠️ **Windows note, on all four pages:** if connections misbehave, the docs say to check Windows
Firewall.

### 4a. OSC In DAT *(page edited 2026-02-20)*

Receives and parses full OSC packets, one row per packet — either a single message or a whole
bundle. FIFO table, line-limited. Arguments are rendered as readable ASCII; multi-vector arguments
(blob, midi, rgb) come through **quoted**, and unknown types arrive as a quoted list of decimal
bytes.

Supported argument tags: `i` int32 · `f` float32 · `s` string · `b` blob · `h` int64 · `t` timetag ·
`d` double · `S` alt-string · `c` char · `r` RGBA · `m` 4-byte MIDI · `T` True · `F` False · `N` Nil ·
`I` Infinitum · `[` `]` array bounds.

| Parameter | Name | Behaviour |
|---|---|---|
| Active | `active` | **While off, data sent to the port is lost** |
| Protocol | `protocol` | `msging` / `multicastmsging` / `reliablemsging` (UDT) |
| Network Address | `address` | Multicast address to listen for, or the UDT server IP |
| Port | `port` | Listening port |
| Local Address | `localaddress` | Pick a NIC |
| Shared Connection | `shared` | Share one connection with other networking DATs on the same protocol |
| OSC Address Scope | `addscope` | Include/exclude by address pattern, e.g. `^*accel*` |
| Include Type Tag | `typetag` | Adds the argument type tag to each message |
| Split Bundle into Messages | `splitbundle` | One row per message inside a bundle |
| Split Message into Columns | `splitmessage` | Address and arguments get their own columns |
| Bundle Timestamp Column | `bundletimestamp` | Adds the bundle timestamp |
| Callbacks DAT | `callbacks` | Runs once per message received |
| Clamp / Maximum Lines / Clear / Bytes | `clamp` `maxlines` `clear` `bytes` | Same shape as WebSocket DAT: 100-message default, oldest dropped first, `.par.clear.pulse()` to clear |

Info CHOP: **`messages_pending`**.

`splitmessage` is worth knowing about — with it on, dispatch can read a column instead of parsing a
string.

#### `oscinDAT_Class` *(Tier A — full page read, page edited 2024-11-07)*

**⚠️ Confirmed: the OSC *In* DAT can also send.** The lead from the previous pass is right. This class
carries **exactly the same `sendOSC()`, `sendBytes()` and `send()` methods as `oscoutDAT_Class`** —
same signatures, same defaults, same type-conversion rules (see §4b; not repeated here).

**One operator can therefore serve a full bidirectional OSC leg** — receive on its port, reply from
the same socket, no separate OSC Out DAT. Whether replies go back to the sender's address or to
something configured is not stated on this page; the `peer` object below is the obvious route.

**Callback — 8 positional arguments:**

```python
def onReceiveOSC(dat, rowIndex, message, bytes, timeStamp, address, args, peer):
    return
```

| Argument | Documented meaning |
|---|---|
| `message` | **ASCII representation only.** ⚠️ **Unprintable and unicode characters are not preserved** — the docs say to use `bytes` for the raw data |
| `bytes` | Byte array of the message |
| `timeStamp` | The arrival time component of the OSC message |
| `address` | The address component, **already split out** |
| `args` | The values, **already a list** |
| `peer` | A Peer object describing the sender |

**`address` and `args` arrive pre-split**, so a Python dispatcher never has to parse the message
string — the `splitmessage` parameter above is the table-side equivalent of the same thing.

**⚠️ The `message` argument is lossy.** Anything non-ASCII in an incoming address or string argument
will not survive into `message`. For a hub that might see unicode clip names coming back, `bytes` is
the trustworthy field.

**The `peer` object** — this is the `Peer Class` the open items list flagged as unread, documented
inline here:

| Member | Meaning |
|---|---|
| `peer.address` | Network address associated with the peer |
| `peer.port` | Network port associated with the peer |
| `peer.owner` | The operator the peer belongs to |
| `peer.close()` | Closes the connection |

That answers "how does a callback identify the sender" — the sender's address and port arrive with
every message. Multi-source OSC routing is possible without any extra plumbing.

### 4b. OSC Out DAT *(⚠️ page edited 2022-05-21 — oldest page in this section)*

Sending is done from Python, not from parameters: **`.sendOSC()`** on `oscoutDAT_Class`. It accepts a
**list of messages** and sends them as one bundle when called with `asBundle=True`. The docs frame
bundles as a performance optimization for real-time control of many parameters at once.

Parameters mirror OSC In DAT — `active`, `protocol` (UDP / multicast / **UDT reliable**), `address`,
`port`, `localaddress`, `shared`, `addscope`, `typetag`, `splitbundle`, `splitmessage`,
`bundletimestamp`, plus the same callbacks/clamp/maxlines/clear/bytes set. Info CHOP:
`messages_pending`.

⚠️ The page still labels its second parameter page "Received Messages" on an *output* operator, and
it has not been edited in four years. Treat parameter names here as the least current in the file.

#### `oscoutDAT_Class` — the actual send API *(Tier A — full page read, page edited 2024-11-07)*

**No operator-specific members.** Three send methods, all returning **the number of bytes sent**:

```python
sendOSC(address, *values, asBundle=False, useNonStandardTypes=True, use64BitPrecision=False) -> int
sendBytes(*messages) -> int          # raw bytes, no terminators, not OSC formatted
send(*messages, terminator='') -> int # strings, not OSC formatted
```

**⚠️ `useNonStandardTypes` defaults to True, and that is an interop hazard.** With the default, TD
sends Python types as *non-standard OSC types*: `True`/`False` become OSC **boolean T/F types**, and
`None` becomes the **OSC nil type** — not integers. A receiver expecting plain OSC 1.0 int 1/0 will
not see what you think you sent. **Pass `useNonStandardTypes=False` for a strict receiver.**

Documented conversion, which is worth having in full because nothing else states it:

| Python value | `useNonStandardTypes=True` (default) | `useNonStandardTypes=False` |
|---|---|---|
| int | 32- or 64-bit, **by magnitude** | 32-bit, or **an exception if too large** |
| float | 32-bit (64-bit only if `use64BitPrecision`) | 32-bit |
| `float("infinity")` | OSC **Infinitum** type | 32-bit float |
| `True` / `False` | OSC **boolean T / F** | 32-bit int 1 / 0 |
| `None` | OSC **nil** | 32-bit int 0 |
| str | OSC string | OSC string |
| bytes / bytearray | OSC blob | OSC blob |

- **`use64BitPrecision=True` requires `useNonStandardTypes=True` as well** — stated on this page.
- Both keywords are marked **available in 099.2018.21730 or later**.
- ⚠️ **Blob trap, documented:** a bytes/bytearray object **must be inside a list**. Passed directly to
  `sendOSC` it is treated as a list of individual integer values and does not go out as a blob.

Documented call shape, showing mixed types in one message:

```python
vals = [1, b'abc', 'apple', [6,7,8], True, None, float("infinity")]
n.sendOSC('/abc', vals)
```

⚠️ **`send()`'s terminator behaviour reads ambiguously.** The signature shows `terminator=''`, while
the description says a null character is appended automatically "if no append terminator is
specified" and that `terminator=''` means send no terminator. Those two readings of the default
conflict. Pass it explicitly.

*(A search snippet suggests `oscinDAT_Class` carries the same `sendOSC` / `send` methods — i.e. the
OSC **In** DAT can also transmit on its socket. `[Lead]` — not confirmed, that class page is still
unread. If true it matters: one operator could serve a bidirectional OSC leg.)*

### 4c. OSC In CHOP *(⚠️ page edited 2022-07-19, and internally inconsistent)*

Connectionless — accepts messages from any number of sources on one port simultaneously. The port
must be free before the CHOP takes it.

| Parameter | Name | Behaviour |
|---|---|---|
| Active | `active` | **While off, data sent to the port is lost** |
| Protocol | `protocol` | `msging` / `multicastmsging` — **no UDT option here** |
| Network Address / Network Port | `netaddress` `port` | Multicast address; listening port |
| Local Address | `localaddress` | Pick a NIC |
| OSC Address Scope | `oscaddressscope` | Pattern include/exclude, as on the DATs |
| Use Global Rate | `useglobalrate` | Sample at TD's global rate |
| Default Sample Rate | `samplerate` | Used when Use Global Rate is off |
| Queued | `queued` | Enables queuing to avoid lost messages |
| Queue Variance | `queuevariance` (+ `queuevarianceunit`) | Acceptable band around the target; inside it, no adjustment happens |
| Maximum Queue | `maxqueue` (+ `maxqueueunit`) | **Incoming samples are dropped once this is reached** |
| Queue Adjust Time | `adjusttime` (+ `adjusttimeunit`) | How often a sample is repeated/dropped to pull the queue back into range |
| Strip Prefix Segments | `stripsegments` | Drops N leading address segments — `/a/b/c/d/e` minus 3 → `d_e` |
| Reset Channels | `resetchannels` (+ `resetchannelspulse`) | Deletes all channels; while On, new channels are not added |
| Reset Values | `resetvalues` | Zeroes all channels; while On, values stop updating |

Info CHOP: `queue_length` · `time_queue_under_min_target` · `time_queue_over_max_target` ·
`queue_retarded_total` · `queue_advanced_total` · `total_bumped`. **`total_bumped` is the dropped-
message counter** — the channel to watch if OSC input is suspected of losing data.

⚠️ **The page contradicts itself.** The summary describes a "Min/Max Target size" range and a "Pulse
Mode toggle" (read one sample per incoming message, useful for beat sync) — **neither appears in the
current parameter list**, though the Info CHOP channel names still refer to min/max targets. Either
the summary or the parameter list is stale. Check the operator's own parameters in the running build
before relying on Pulse Mode.

### 4d. OSC Out CHOP *(page edited 2026-02-12)*

Sends all input channels to an address and port, channel name plus data together. TD timestamps
outgoing messages relative to system time at the first send.

| Parameter | Name | Behaviour |
|---|---|---|
| Active | `active` | When off, nothing is sent |
| Protocol | `protocol` | `msging` / `multicastmsging` / `reliablemsging` (UDT) |
| Network Address / Network Port | `netaddress` `port` | Target; `localhost` for same machine |
| Local Address | `localaddress` | Pick a NIC |
| Max Queue Size | `maxsize` (+ `maxsizeunit`) | Cap on messages sent at once |
| Cook Every Frame | `cookalways` | Cook regardless of whether upstream CHOPs cook |
| Numeric Format | `numericformat` | `int` 32 / `float` 32 / `double` 64 |
| Data Format | `format` | `sample` / `timeslice` / `transpose` / `transposename` |
| Max Message Bytes | `maxbytes` | Caps packet size and **splits the message** accordingly |
| Send Events Every Cook | `sendevents` | **On: send every channel every cook. Off: send only what changed** |

**`sendevents` off is the built-in send-rate reduction** — no throttle code needed for the
change-only case.

**Transpose By Name** groups channels sharing a root name (up to the first `/`) into one message,
values ordered as the input channels are: `A/Red B/Red A/Blue B/Blue` → `/A Red Blue` and
`/B Red Blue`.

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

### 5b. MIDI Out CHOP
*(Tier A — full page read. **Re-verified from `docs.derivative.ca` 2026-08-01**, page last edited
2026-03-10, oldid 37548. Everything below matched the earlier read; the additions are marked.)*

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

**14-bit output has a different constraint from 14-bit input.** The switch is **`controlformat`**
(Control page): `7bit` sends a single 7-bit controller message, `14bit` pairs two 7-bit messages.
In 14-bit mode controller indices must be in **0–31**, because **32–63 is reserved for the paired
messages and is not user-accessible**. Range **64–95 is always sent as a single 7-bit message.**

**Two Normalize parameters, on different pages, with different option sets** — this matters because
`midioutCHOP_Class` (§5h) cites them by different names:

| Page | Parameter | Options |
|---|---|---|
| Note | `notenorm` | None / 0 to 1 |
| Control | `controlnorm` | None / 0 to 1 / −1 to 1 / On-Off |

⚠️ **Doc slip on this page:** `volumeoff` and `volumeon` are both described as sending "All Notes
Off" / "All Notes On" messages, while the summary says these flags emit **Controller 7** events on
all 16 channels. The parameter descriptions and the summary disagree. Controller 7 is volume, so the
summary is the plausible one — **unresolved, don't rely on either wording.**

**Other parameters:** `active`; `destination` (Device or File, MIDI Mapper is the default);
`device` / `id`; **`onebased` — "make the index 1 based instead of the default 0 based"**;
`file` / `writefile` (capture a MIDI stream to a file);
`autonoteoff` (All Note Off at playback start, end, both, or none); `reset` (All Notes Off to all
channels); `volumeoff` / `volumeon` (emit Controller 7 events on all 16 channels); `startstop`
(send Start/Stop/Continue when the framebar starts or stops); **`sendmtc` — sends MIDI Timecode as
quarter-frame messages**, with `timecodeop` taking a CHOP with hour/minute/second/frame channels, a
DAT with a timecode string, or a Timecode Class object; `notenorm` (None or 0-to-1);
`controlnorm` (None / 0-to-1 / -1-to-1 / **On-Off**); `barname` + `barticks` for MIDI clock output
from a 0–1 bar ramp (**default 96 = 4 beats × 24 ticks per beat**).

### 5c. The MIDI family at a glance

| Operator | Use | Tier |
|---|---|---|
| MIDI In CHOP | Continuous values as channels — working input for a mapped surface | A (§5a) |
| MIDI Out CHOP | Feedback — motors, LED rings, button LEDs | A (§5b) |
| MIDI In DAT | Raw message inspection — the ground-truth capture tool | A (§5d) |
| MIDI In Map CHOP | Mapper-based indirection | A (§5e) |
| MIDI Event DAT | Logs **both directions**, all devices | A (§5f) |

### 5d. MIDI In DAT *(Tier A — full page read, page edited 2026-03-10)*

Logs every MIDI message from a device into a table: **message, type, channel, index, value**.

**⚠️ The line that matters most, quoted in substance:** the page states that the controller indices
the MIDI In DAT reports are **always converted to the 1-based range 1–128**.

That is the documented basis for the −1 correction we arrived at empirically on the X-Touch bench
test. The behaviour is documented, not a quirk of that device — which means the correction belongs
wherever MIDI In DAT indices are consumed, not just in the X-Touch path. The bench observation and
the doc now agree; previously we only had the observation.

*Connect page:*

| Parameter | Name | Behaviour |
|---|---|---|
| Active | `active` | Logs MIDI events when on |
| Device Table | `device` | Path to the MIDI device Table DAT |
| Device ID | `id` | Which device |
| 14 Bit Values | `value14` | Consolidates MSB/LSB pairs into a single 14-bit value |

**14-bit mode has a strict spec, and it silently does nothing if the device doesn't follow it:**

- MSB must be in controller range **0–31**; LSB in **32–63**, at **MSB index + 32** (MSB 12 → LSB 44)
- Index pairs **98/99** and **100/101** also work as MSB/LSB
- **If only an MSB arrives, nothing is output at all**
- If several LSBs arrive with no intervening MSB, the last MSB value is reused
- Controller range **64–95 is reserved for 7-bit** and passes through as 7-bit even in this mode
- **MIDI Event DAT differs here** — the page says it outputs both messages separately rather than
  consolidating

*Filter page — worth using instead of filtering in Python:*

`skipsense` (drop active-sense messages) · `skiptiming` (drop timing messages) · `filter` (enable the
rest) · `message` (e.g. "Control Change") · `channel` (1–16) · `index` (1–128) · `value` (0–127).

Dropping sense and timing at the operator keeps the FIFO table from filling with traffic that isn't
control data — relevant on any surface that sends active sensing.

*Received Messages page:* `callbacks` (runs once per row added, i.e. per event), `executeloc`,
`fromop`, `clamp` (100-message default), `maxlines`, `clear`, `bytes`. Info CHOP: `num_rows`,
`num_cols` and the common operator channels — **no MIDI-specific status channel.**

The page also notes that once MIDI is configured in the MIDI Device Mapper, Select CHOPs pointing at
`/local/maps/map1` (device 1) are the simpler general path.

### 5e. MIDI In Map CHOP *(Tier A — full page read, page edited 2023-11-02)*

Reads channels prepared by the **MIDI Device Mapper Dialog**, which names sliders `s1`, `s2`, … and
buttons `b1`, `b2`, …. The CHOP then selects from those.

| Parameter | Name | Behaviour |
|---|---|---|
| Device Table / Device ID | `device` `id` | Which device |
| Sliders | `sliders` | Pattern syntax, e.g. `s[1-16] s20 s[32-40]` |
| Buttons | `buttons` | e.g. `b[1-16] b20 b[32-40]` |
| Include Velocity in Buttons | `bvelocity` | Velocity on button inputs where available |
| Queue Slider Events | `squeue` | (no description on the page) |

*Channel page:* `rate`, `left` / `right` extend conditions (`hold` / `slope` / `cycle` / `mirror` /
`default`), `defval`.

**The trade-off the page states directly:** MIDI In CHOP addresses channel, note and controller
numbers *inside the CHOP*, so remapping means editing TouchDesigner. MIDI In Map CHOP pushes that
into the Device Mapper dialog, so a user can remap without touching the network. More portable,
one more layer of indirection.

⚠️ **This page carries its own staleness warning** — an editor's note dated **April 12, 2009** saying
the page needs updating from the release notes, still present on a page last edited 2023-11-02. The
`squeue` parameter has no description at all. Treat the parameter list here as the least trustworthy
Tier A entry in this file, and check the operator in the running build before relying on it.

### 5j. `midiinmapCHOP_Class` — empty
*(Tier A — full page read from `docs.derivative.ca`, page last edited **2018-05-25**, oldid 11415.)*

**No operator-specific members. No operator-specific methods. No callbacks.** Everything is inherited
CHOP Class and OP Class.

MIDI In Map CHOP has no Python surface of its own. All of its behaviour is in its parameters (§5e)
and in the MIDI Device Mapper dialog.

---

### 5i. `midiinCHOP_Class` — thin, but with one member that matters
*(Full page read from **`docs.derivative.ca`**, page last edited **2023-12-19**, oldid 30581.
Also read independently on the `derivative.ca/UserGuide/` mirror.)*

**✅ Docs and mirror agree, verbatim.** This entry was first written from the mirror because
`docs.derivative.ca/MidiinCHOP_Class` could not be fetched — the tool only accepts URLs surfaced by a
prior search or fetch, and two targeted searches failed to surface it. The user supplied the URL
directly, which made it fetchable. Both versions give the same single member, the same wording, the
same "no operator specific methods."

⚠️ **Two earlier notes in this file were wrong and are retracted:**

1. "The docs URL was not reachable this pass" — **inaccurate.** It was never attempted on the first
   try, and on the second it was *refused for lack of provenance*, which is not the same as
   unreachable. It is reachable.
2. The entry was marked "Tier A with an asterisk" pending a docs re-read. **The asterisk is now
   removed** — this is plain Tier A.

**This is the first direct docs-vs-mirror comparison in this file.** One page, matching. That is a
single data point, not a general clearance: the standing note in the provenance block — that mirror
content *appears* to match but that this is an assumption — still stands for every other
mirror-sourced item.

**Independently corroborated as well.** The **Release Notes for build 2023.10000 (experimental)** list
the member in the same terms — *"MidiinCHOP Class.timecode — a new getter that grabs the timecode
representation of the last set of quarter frame messages"* — added alongside
`AudiofileinCHOP Class.timecode`.

**Useful side effect: this dates the member.** It arrived in **2023.10000**, so it is comfortably
present in the target build — but it does not exist in anything older, which matters if this file is
ever consulted against an older install.

**No operator-specific methods.** Exactly **one** operator-specific member — and it is not nothing:

```python
timecode -> tdu.Timecode   # Read Only
```

*"Get a Timecode object representation of the last set of quarter frame messages."*

**MIDI In CHOP receives MTC.** Quarter-frame messages are how MIDI Timecode is carried, and the CHOP
assembles them into a `tdu.Timecode` object with no parsing on your side. That closes the loop with
**MIDI Out CHOP's `sendTimecode()`** (§5h) — TD can both send and receive MTC, and both ends use the
same Timecode Class object.

**⚠️ INFERRED — not documented. The send side is verified; the Timer side is not.** MIDI Out CHOP has a `sendmtc`
parameter — *"sends MIDI Timecode (MTC) as a stream of quarter frame messages"* — and a `timecodeop`
parameter documented as accepting **"a CHOP with channels 'hour', 'second', 'minute', 'frame', a DAT
with a timecode string in its first cell, or a Timecode Class object."** So MIDI Out explicitly takes
a Timecode object, and MIDI In explicitly produces one. That round trip is documented at both ends.

**⚠️ INFERRED, NOT DOCUMENTED, NOT TESTED:** that MIDI In's `.timecode` can drive a **Timer CHOP's
External Timecode** mode. §11 records that mode as accepting a "timecode CHOP/DAT/Object", but the
Timer's parameter name and its exact accepted types were never captured from the Timer's own page.
The shapes match and `timecodeop` is worded identically on Timeline CHOP and MIDI Out CHOP, which
suggests a shared convention — **that is a pattern, not a citation. Do not build on it without
testing.**

Everything else on the class is inherited CHOP Class and OP Class.

---

### 5h. `midioutCHOP_Class` — sending MIDI from Python
*(Tier A — full page read, page edited 2024-08-15. The most current class page in this file.)*

The documented way to send arbitrary MIDI to a device: call methods on an existing MIDI Out CHOP.
**No operator-specific members**; a large method set.

**The header line on the Methods section matters:** the event-generation methods **do not require any
CHOP inputs connected** to the MIDI Out CHOP. The node can exist purely as a Python send handle with
nothing wired into it.

#### The three that matter for a control surface

| Method | Signature | Notes |
|---|---|---|
| `sendNoteOn` | `(channel, index, value)` | channel 1–16. **index 0–127 *or* 1–128 depending on the One Based Index parameter.** `value` optional — **maximum when omitted** |
| `sendNoteOff` | `(channel, index, value)` | Same, but `value` is **minimum when omitted** |
| `sendControl` | `(channel, index, value)` | channel 1–16. index 0–127 or 1–128 per One Based Index. **`value` range set by the CHOP's Controller Normalize *and* Controller Format parameters** |

#### ⚠️ This narrows a stored bench finding — read before reusing it

Our note from the X-Touch session says raw `send()` **bypasses all normalize and index parameters
entirely.** The documentation supports that for `send()` specifically, and **contradicts it for the
named send methods**:

- **`send(*messages)`** takes raw bytes — nothing to normalize, nothing to index. Bypass is expected.
- **`sendNoteOn` / `sendNoteOff` / `sendControl` / `sendPolyKeyPressure` / `sendChannelPressure` /
  `sendProgram`** are each documented as honouring **One Based Index**, **Note Normalize**,
  **Controller Normalize** or **Controller Format**.

So the finding is correct *as scoped to `send()`* and over-general as written. **Which method the
bench test actually used decides whether this is a scoping fix or a real conflict between our
observation and the docs — that is not recorded, and it should be re-tested before the pattern is
reused.** Flagging rather than resolving: the docs are Verified, our observation is Bench-verified,
and they are not talking about the same call unless the test used a named method.

#### One Based Index — verified, and it defaults to 0-based

*(These parameters were first cited here second-hand, from `midioutCHOP_Class` merely referring to
them. **Both are now confirmed against the MIDI Out CHOP operator page itself**, oldid 37548, read
2026-08-01 — see §5b.)*

| Parameter | Page | Verified wording |
|---|---|---|
| `onebased` | Dest | *"Make the index 1 based instead of the **default 0 based**."* |
| `controlformat` | Control | `7bit` / `14bit` — it **is** the 7/14-bit switch |
| `notenorm` | Note | None / 0 to 1 |
| `controlnorm` | Control | None / 0 to 1 / −1 to 1 / On-Off |

**The asymmetry is real and now fully documented at both ends:**

- MIDI In DAT and MIDI Event DAT **always** convert to 1-based, with no parameter (§5d, §5f).
- MIDI Out CHOP is **0-based by default**, with `onebased` available to switch it.

So the in/out offset is not a fixed law of the operator pair — it is one setting on the output side.
**Check what `onebased` is set to on the rig before assuming the −1 correction is needed.** The forum
report of "MIDI In 1-based, MIDI Out 0-based" `[Forum]` matches the documented default exactly.

**A documented example shows the offset directly:** the page gives
`n.send(0xb0, 0x2f, 0x40)` and comments it as *Control Change : Channel 1, Index 48, Value 64*.
`0x2f` is 47 and `0x40` is 64 — so the value passes through raw while **the index is described one
higher than the byte on the wire**. That is the ±1 relationship, stated by Derivative, in an example.

#### Other methods worth knowing

- **`panic()`** — sends a volume-off for every channel and a note-off for every note. The show-shutdown
  and all-LEDs-dark call, already built.
- **`sendExclusive(*messages)`** — SysEx. **Start and end bytes are added automatically.** Accepts any
  mix of strings, byte arrays and single-byte numeric values.
- **`sendPitchBend(channel, value)`** — value range **0 to 16384**, i.e. the full 14-bit range, unlike
  everything else here.
- **`sendTimecode(timecode)`** — full MTC message. Requires a `tdu.Timecode` object, and the **rate must
  be 24, 25, 29.97 drop-frame, or 30**. Nothing else is accepted.
- **`sendAllNotesOff`**, **`sendResetAllControllers`**, **`sendLocalControl`** — the MIDI housekeeping
  messages, each `(channel, value)`.
- Indexed controller families: `sendEffectsDepth` (index 1–5), `sendSoundController` (1–10),
  `sendGeneralPurposeController` (1–8), `sendEffectControl` (1–2).
- The rest are one-per-CC-function conveniences — `sendModulationWheel`, `sendMainVolume`, `sendPan`,
  `sendBalance`, `sendBankSelect`, `sendBreathController`, `sendFootController`, `sendPortamento` and
  `sendPortamentoTime` and `sendPortamentoControl`, `sendDamperPedal`, `sendSoftPedal`, `sendSostenuto`,
  `sendHold2`, `sendLegatoFootswitch`, `sendDataIncrement` / `sendDataDecrement`, `sendMonoOn` /
  `sendPolyOn`, `sendOmniOn` / `sendOmniOff` — all `(channel, value)` in 0–127 unless indexed above.

⚠️ Two apparent doc slips on this page: `sendEffectControl` is described as "Sends a Main Volume
event," and `sendLegatoFootswitch`'s example passes `07`. Neither is load-bearing, but they suggest
the page was assembled by template.

---

### 5g. MIDI callback signatures — `midiinDAT_Class` and `midieventDAT_Class`
*(Tier A — full page reads. ⚠️ Both class pages edited **2018-05-25**.)*

**Both operators use the identical callback, same name and same 8 positional arguments:**

```python
def onReceiveMIDI(dat, rowIndex, message, channel, index, value, input, bytes):
    return
```

| Argument | Documented meaning |
|---|---|
| `dat` | The DAT that received the event |
| `rowIndex` | The row number that was added |
| `message` | A readable description of the event |
| `channel` | Numeric event channel |
| `index` | Numeric event index |
| `value` | Numeric event value |
| `input` | **True when the event was received** |
| `bytes` | Byte array of the event |

Documented example row: `Note On`, channel `1`, index `63`, value `127`, bytes `90 2f 127`.

**Two things this settles, and one it doesn't:**

- **Arity confirmed at 8.** That matches the bench observation from the X-Touch session exactly. What
  we established empirically is now documented — though note the doc pages predate that test by
  years, so this is confirmation, not a source we should have consulted instead.
- **The last argument is named `bytes` in the docs**, where our own notes call it `byteData`. Args
  are positional so nothing breaks, but the stored pattern should say which name is ours and which
  is Derivative's.
- **`input` is a direction flag, and it matters on MIDI Event DAT.** On MIDI In DAT everything is
  inbound, so it is always true and effectively dead. On MIDI Event DAT — which sees both directions
  (§5f) — it is how a callback tells an incoming control message from outgoing LED feedback, in
  Python rather than via the `dir` parameter.

Both classes report **no operator-specific members and no operator-specific methods** — everything
else is inherited DAT Class and OP Class.

---

### 5f. MIDI Event DAT *(Tier A — full page read, page edited 2026-03-10)*

Logs MIDI **coming into or out of** TouchDesigner, from **all** MIDI In/Out operators at once.
Columns: message, type, channel, index, value. FIFO, line-limited.

**Two properties make this the debug tool, not an input operator:**

1. **It has no device selection.** The Connect page contains only `active`. It taps whatever the
   existing MIDI operators are already doing.
2. **⚠️ It logs nothing if no MIDI In or Out operator is active.** It is a monitor on other
   operators' traffic, not an independent listener. If it looks dead, check that something else is
   actually running.

*Filter page* — same as MIDI In DAT (`skipsense`, `skiptiming`, `filter`, `message`, `channel`,
`index`, `value`) **plus one it doesn't have:**

| Parameter | Name | Behaviour |
|---|---|---|
| Dir | `dir` | Filter by direction — **"input" or "output"** |

**That is the operator to reach for on the X-Touch bridge.** It shows incoming control messages and
outgoing LED/motor feedback in one table, with `dir` to separate them. Neither MIDI In DAT nor MIDI
Out CHOP can show you the other half of the conversation.

**The 1-based index conversion applies here too** — the page states it in the same terms as MIDI In
DAT (§5d). Consistent across both DATs, so the −1 correction is not operator-specific.

⚠️ **14-bit differs from MIDI In DAT.** This operator has no `value14` parameter, and the MIDI In DAT
page states that MIDI Event DAT **outputs both MSB and LSB messages separately** rather than
consolidating them. If a device sends 14-bit CC, the two DATs will show different row counts for the
same physical move.

*Received Messages page:* `callbacks`, `executeloc`, `fromop`, `clamp`, `maxlines`, `clear`, `bytes`.
Info CHOP: `num_rows`, `num_cols`, common operator channels only.

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

**Confirmed by the second-pass reads, and it sharpens the point:** this is a WebSocket-DAT-specific
hole, not a TouchDesigner-wide one.

| Operator | Connection state as Info CHOP channels? |
|---|---|
| WebSocket DAT (TD as client) | **No** — nothing beyond `num_rows` / `num_cols` and the common cook and error channels |
| Web Client DAT (§2) | **Yes** — `connected`, `connection_error`, `communicating` |
| Web Server DAT (§3) | **Yes** — `server_running`, `websocket_connections` |
| OSC In DAT / OSC Out DAT (§4) | Partial — `messages_pending` |
| OSC In CHOP (§4c) | Partial — `queue_length`, `total_bumped` (dropped-message counter) |
| Ableton Link CHOP (§7a) | **Yes** — `linked`, `synced`, `numpeers` |

So the *one* leg that most needs supervision — the persistent WebSocket to Resolume — is the only one
without a channel-level readout. Whether that is deliberate or an oversight is not something the docs
say.

**Not read this session:** Clock CHOP, Timeline CHOP. Everything else listed is covered in §11.

---

## 11. Utility CHOPs for hub logic  ⚠️ MIXED TIER — marked per operator

Not protocol operators, but the pieces a control hub is actually assembled from.

**Tier A (full page read): Info CHOP, Perform CHOP, Timer CHOP, Trigger CHOP.**
⚠️ **Everything else in this section is still Tier B — snippet-sourced, parameter lists incomplete:**
Beat, Speed, Count, Event, Logic, Sync In/Out, Touch Out.

### Supervision and health

**Info CHOP** *(Tier A — full page read, page edited 2023-12-18)* — extra information about *any*
node, exposed as channels. Different node types carry different subsets. The operator-specific
attributes are **also available as Python members** of that operator, so the same data is reachable
either way.

| Parameter | Name | Behaviour |
|---|---|---|
| Operator | `op` | Path of the node being inspected; drag-and-drop works |
| Info Type | `infotype` | `all` / `general` / **`timecode`** — the Timecode entry **only appears if the target has a `.timecode` member**, and yields `hour`, `minute`, `second`, `frame` |
| Scope | `iscope` | Which attribute names to keep, by pattern |
| Values | `values` | `all` / `inside` / `outside` — select channels by whether their value is in Range |
| Range | `range` | `range1`, `range2` bounds for the above |
| **Passive** | `passive` | **Off: the Info CHOP forces the target to cook before reading it. On: it does not** |
| Children Cook Time | `childcooktime` | On a component, adds `children_cpu_cook_time` — sum of all children's cook times |

⚠️ **Two documented traps, both relevant to supervision:**

1. **`passive` on has a side effect the docs call out**: if the Info CHOP and its target both cook
   that frame, the Info CHOP may cook *first*, so **its data is a frame late**. A monitoring readout
   that must not perturb the thing it watches is therefore also a readout that can lag by a frame.
2. **`childcooktime` costs performance on a large network** — every child cook time has to be
   summed. It is off by default for that reason.

This is the general health tool — but see §10: on WebSocket DAT it yields only `num_rows`,
`num_cols` and the common cook/error channels. **`errors` and `warnings` counts are the usable
supervision signal there**, alongside `num_rows` advancing. Contrast Web Client DAT (§2), which does
expose `connected` / `connection_error` / `communicating`.

**Perform CHOP** *(Tier A — full page read, page edited 2025-06-04)* — channels describing the state
of the TouchDesigner process itself. Every parameter on the Perform page **is** an output channel;
the parameter list and the channel list are the same thing.

| Channel | Name | Meaning |
|---|---|---|
| Frames per Second | `fps` | Frames rendered in the last second |
| Frame Time | `msec` | Milliseconds each frame takes to cook |
| Cook | `cook` | **1 when a frame cooked, 0 when it was skipped** |
| Dropped Frames | `droppedframes` | Frames dropped between last frame and this one |
| Movie Read Ahead Misses | `mvreadahead` | Times read-ahead failed to keep its frame count |
| GPU Mem Used / Total GPU Mem | `gpumemused` `totalgpumem` | Megabytes |
| CPU Mem Used | `cpumemused` | Megabytes |
| Total Active OPs | `activeops` | OPs actively cooking |
| Total Deactivated OP Calls | `deactivatedops` | Cook calls to components with the Cooking Flag off |
| Total OPs | `totalops` | Total OPs in the `.toe` |
| Cook State | `cookstate` | Which frames actually cooked |
| Cook Realtime | `cookrealtime` | State of the realtime flag |
| Cookrate | `cookrate` | **Target** rate (`root.time.rate`), typically 60 — actual fps may be lower |
| Time Slice Step | `timeslicestep` | Frames stepped this cook. **1 when a frame completes in `1000/rate` ms or less** (16.666 ms at 60) |
| Time Slice Milliseconds | `timeslicemsec` | Length of the current Time Slice |
| Perform Mode / Window Focus | `performmode` `performfocus` | Perform Mode state; whether the Perform window has focus |
| GPU Temperature | `gputemp` | ⚠️ Labelled **"(Slow)"** in the docs; **NVIDIA only** |
| AC Line / Battery | `aclinestatus` `batterycharging` `batterylife` `batterytime` | Laptop power state; `batterytime` only valid on battery |
| Active / Optimized / Cached Expressions | `activeexpressions` `optimizedexpression` `cachedexpressions` | Python expression counts |

**Documented tip:** feed `cook` (or `cookstate`) into a **Trail CHOP** to see which frames cooked and
which were skipped — the docs note `cookstate` looks permanently 1 in its own viewer because the
viewer only shows the current frame. This is the recommended way to find out whether a target frame
rate is actually being hit, and it is the readout to watch if the hub's message volume starts costing
frames.

⚠️ `gputemp` is explicitly flagged slow in the docs — don't leave it in a per-frame path.

### Timing and state

**Timer CHOP** *(Tier A — full page read)* — an engine for timed processes, explicitly documented as
able to **operate as a state machine**.

**Time Control** (`timecontrol`) has four modes, and two matter here: **Sequential**
(timeline-independent), **Lock To Timeline** (deterministic, non-deterministic features disabled),
**External CHOP Channel** (master time driven by a CHOP channel), and **External Timecode** (master
time driven by a timecode CHOP/DAT/Object). The External modes mean a Timer can be slaved to
incoming LTC.

**Callbacks — corrected and completed from `timerCHOP_Class`** *(class page edited 2024-08-15)*.
⚠️ **The pass-one list was wrong and incomplete.** There is no `onTimerActive()`; the actual name is
**`whileTimerActive()`**, and there are eleven callbacks, not seven:

```python
def onInitialize(timerOp, callCount): return 0
def onReady(timerOp): return
def onStart(timerOp): return
def onTimerPulse(timerOp, segment): return
def whileTimerActive(timerOp, segment, cycle, fraction): return
def onSegmentEnter(timerOp, segment, interrupt): return
def onSegmentExit(timerOp, segment, interrupt): return
def onCycleStart(timerOp, segment, cycle): return
def onCycleEndAlert(timerOp, segment, cycle, alertSegment, alertDone, interrupt): return
def onCycle(timerOp, segment, cycle): return
def onDone(timerOp, segment, interrupt): return
def onSubrangeStart(timerOp): return
```

**Three things in there worth building on:**

1. **`onInitialize()` can initialize asynchronously.** If it returns a value **greater than 0**, it is
   called again after that many frames. `callCount` increments per attempt, **starting at 1**. That is
   a documented retry loop — hold off Start until something external is ready (a connection, a media
   scan) without blocking a frame.
2. **`onTimerPulse()` fires when the timer starts counting up; `onSegmentEnter()` fires when the
   segment starts, which is when the *delay* starts.** Different moments when a segment has a delay.
   The docs call this out explicitly.
3. **`interrupt`** is passed to `onSegmentEnter`, `onSegmentExit`, `onCycleEndAlert` and `onDone` —
   **True if the user ended it prematurely, False on a normal timeout.** A clean way to tell a cue
   that finished from a cue that was cut.

**The `segment` object** casts to its index (`segment+3`, `segment==2` both work) and carries:
`index`, `owner`, `lengthSeconds/Samples/Frames`, `delaySeconds/Samples/Frames`,
`beginSeconds/Samples/Frames`, `speed`, `cycle`, `cycleLimit`, `maxCycles`,
`cycleEndAlertSeconds/Samples/Frames`, `row`, and **`custom` — a dictionary of every Segments DAT
column that doesn't map to a built-in feature.** That last one is the hook for arbitrary per-cue
metadata.

**Python control surface** *(`timerCHOP_Class`)*:

| Call | Behaviour |
|---|---|
| `goTo(segment=0, cycle=0, endOfCycle=?, seconds=0, frame=0, sample=0, fraction=0)` | Jump to a time index. **Only one time unit may be given** — passing both `seconds` and `frame` is an error. With a time unit alone it jumps to the *running* time index; add `segment` and/or `cycle` and it jumps to the *local* index. Fifteen valid argument combinations |
| `goToNextSegment()` / `goToPrevSegment()` | Same as pulsing the Segments page parameters |
| `goToCycleEnd()` | Same as pulsing Go to End of Cycle |
| `lastCycle()` | Makes the current cycle the last one — same as Exit at End of Cycle |

⚠️ **The page contradicts itself on `endOfCycle`:** the signature shows `endOfCycle=True`, the
argument description says "**False by default**." Don't rely on the default — pass it explicitly.
When True, `goTo()` is re-called at the end of the cycle so the jump happens only then.

**Time members, all settable except where noted** — `masterSeconds` is the main clock and can be set
directly (`OP.masterSeconds = val`), with `masterFrames`, `masterSamples`, `masterFraction` and
`masterTimecode` as equivalents. Read-only counterparts exist for cumulative, playing and running.
Every one has a `tdu.Timecode` form. `segment` and `cycle` are both get/set; `segments` returns the
list.

⚠️ A 2019 forum thread reports `goTo(seconds=)` breaking parallel timers — marked **FIXED** in that
thread. `[Forum]`, unverified, and old enough that it should not apply, but noted since parallel
timers plus `goTo()` is exactly the combination a cue system would use.

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

**Beat CHOP** *(Tier A — full page read, page edited 2024-11-06)* — ramps, pulses and counters timed
to the BPM and sync set by the **Beat Dialog**, which is where you manually tap tempo. The CHOP keeps
time after you stop tapping. Global tempo is settable from Python: `op('/local/time').tempo = 140`.

*Output page — each toggle is one output channel:* `ramp` (0–1 per period) · `pulse` · `sine` ·
`count` · `countramp` (continuously rising, equal to cycles since start) · `bar` · `beat` ·
`sixteenths` · `rampbar` · `rampbeat` · **`bpm`**.

The channel set is nearly identical to Ableton Link CHOP's, minus Link's status channels and with
`bpm` in place of `tempo` — so a hub can swap between local beat and network-synced Link with little
rewiring.

*Beat page — the parameters that matter for a hub:*

| Parameter | Name | Behaviour |
|---|---|---|
| Reference Operator | `op` | Which Time COMP defines the timing. **Blank = the Beat CHOP's own location**, default `/local/time` |
| Play Mode | `playmode` | `locked` (to local timeline — **resets when the timeline loops**) / `global` (follows the master Beat CHOP) / `local` (continuous, ignores timeline position) |
| Period | `period` | Beats per ramp cycle. Fractional values allowed — 3.33 beats per ramp works |
| Multiples | `multiples` | Number of channels to create |
| Shift Offset / Shift Step | `shiftoffset` `shiftstep` | Stagger the channels — Step 1 with Multiples 5 puts each channel 1/5 cycle after the last |
| Random Offset / Seed | `randoffset` `randseed` | Random time-shift per ramp |
| Reset Condition | `resetcondition` | `offtoon` / `on` / `ontooff` / `off` |
| Reset Bar Value | `resetbarvalue` | Which bar to jump to on reset; beat comes from the fractional part |
| Wait after Reset | `resetwait` | With **While On**, holds at zero until the next bar starts |
| Update Global | `updateglobal` | Makes this the master beat source |

⚠️ **Three things to know before wiring this into a show:**

1. **Play Mode `locked` resets when the local timeline loops.** For long improvised playing the docs
   point at **Local Sequential** instead. A hub running for hours wants `local`.
2. **`updateglobal` creates `/local/master_beat`** if it doesn't exist, and every other Beat CHOP set
   to `Locked to Global` follows it. The docs say plainly: **exactly one master Beat CHOP per `.toe`.**
   `$MASTER_BEAT` points at whichever one has the flag.
3. **A "bar" is 4 beats** for this operator's purposes, and the "period" is whatever Period is set to —
   the two are not the same unit.

**Speed CHOP** *(Tier A — full page read, page edited 2025-10-28)* — integrates a rate into a
cumulative value (speed → distance); mathematically the area under the input curve. Feed it a
constant 1 and the output rises by 1 per second; negative values decrease it; 0 holds. Output is the
sum of input samples divided by the CHOP's sample rate (typically 60), starting at the Start index.
Time-sliced by default, so it accumulates every frame it cooks.

| Parameter | Name | Behaviour |
|---|---|---|
| Order | `order` | `first` / `second` / `third` — velocity→position, acceleration→position, etc. |
| Speed | `speed` | Generates values with no input connected; **disabled as soon as an input is wired** |
| First/Second/Third Constant | `constant1..3` | Added after each integration |
| Limit Type | `limittype` | `off` / `clamp` / `loop` / `zigzag`, bounded by `min` and `max` |
| Speed per Sample | `speedsamples` | Applies speed per sample rather than across the whole channel |
| Reset Condition | `resetcondition` | `offtoon` / `on` / `ontooff` / `off` |
| Reset Value | `resetvalue` | What the channel is set to on reset — **not necessarily 0** |
| Reset / Reset Pulse | `reset` `resetpulse` | Manual reset |
| Reset on Start | `resetonstart` | Reset every time the `.toe` restarts |

Reset also works from the **second input**: while that input is greater than 0, the value is reset
*and held* at the reset value.

⚠️ **The one that matters for a long-running install:** the docs warn that if the accumulated value
gets large enough, **the output starts stepping** as it hits the limit of CHOP numeric resolution.
`resetonstart` exists specifically for projects that run a long time. A seconds-since-last-message
counter that never resets will eventually go coarse — reset it on every message rather than letting
it climb.

Useful for time-since-last-event counters — e.g. seconds since the last `parameter_update`, which is
the inferred-health signal §10 calls for.

**Clock CHOP** *(Tier A — full page read, page edited 2026-01-21)* — wall-clock time as channels:
year, month, week, day, hour, minute, second, millisecond, plus moon phase and sun position.

| Parameter | Name | Behaviour |
|---|---|---|
| Output | `output` | `units` (integers — hour 0–23) / `fractions` (0–1 ramps) / **`countdown`** |
| Hour Format | `hourformat` | `12` or `24`; also affects the AM/PM channel |
| Hour Adjust | `houradjust` | Offsets the clock — **pretends the time is different from actual** |
| Start Reference | `startref` | `jan1` (since Jan 1 2000) or `program` (since the TD process started) |

Channel toggles: `msec` `sec` `min` `hour` `ampm` `wday` `day` `yday` `week` `month` `year`.
Solar page: `latitude` `longitude` (with N/S and E/W), `moonphase`, `sunphase`, `sunrise`, `sunset`,
`declination`. Latitude defaults to Toronto.

**Countdown mode is the show-relevant one.** First input carries channels named `year`, `month`,
`day`, `hour`, `min`, `sec`, `msec` for the target; missing values default to midnight January 1 of
the specified year; **year values are two-digit — 25 means 2025**. The second input is optional and
fills missing values from the current time. That is a countdown-to-doors or countdown-to-showtime
without any Python.

⚠️ Watch the conventions, they are not uniform: `wday` starts at **0 for Monday**, `yday` starts at
**0 for January 1**, but `month` starts at **1 for January**. And in Units mode `year` is relative
to Start Reference — 2009 reads as 9 by default, not 2009.

**Timeline CHOP** *(Tier A — full page read, page edited 2023-12-04)* — outputs the time state of a
component's Time COMP as channels. With no Reference Operator set it uses the time at its own
location (`me.time`).

| Parameter | Name | Behaviour |
|---|---|---|
| Reference Operator | `op` | Which node's time to read |
| Use Timecode | `usetimecode` | **Take time from a timecode reference instead of the Reference Operator** |
| Timecode Object/CHOP/DAT | `timecodeop` | A CHOP with `hour`/`minute`/`second`/`frame` channels, a DAT with a timecode string in its first cell, or a Timecode Class object |

Channel toggles: `frame` `rate` `start` `end` `rangestart` `rangeend` `signature1` `signature2`
`bpm` `play`.

**`usetimecode` is the interesting one for a timecode-driven show:** it lets the Timeline CHOP be
driven by incoming timecode while **still** taking bpm, time signature, start and end from the
Reference Operator. So the tempo grid and the transport can come from different places. The `play`
channel is a transport-state readout with no Python needed.

### Event detection

**Trigger CHOP** *(Tier A — full page read, page edited 2025-12-11)* — converts a threshold crossing
into a full ADSR envelope: delay, attack, peak, decay, sustain, release. A trigger point occurs when
the **first input's** channel rises across the trigger threshold; while the value stays above the
release threshold the envelope runs its sustain phase, and it releases once the input drops below.
Peak and sustain levels are set independently but **peak can never be less than sustain**. Works with
time-sliced or static inputs.

*Trigger page:*

| Parameter | Name | Behaviour |
|---|---|---|
| Release = Trigger Threshold | `threshold` | One threshold for both directions |
| Trigger / Release Threshold | `threshup` `threshdown` | Separate up and down thresholds |
| Re-Trigger Delay | `retrigger` (+ unit) | Time after a trigger before a new one may occur |
| Min Trigger Length | `mintrigger` (+ unit) | Minimum time the trigger stays active |
| Trigger On | `triggeron` | `increase` / `decrease` — release happens on the opposite slope |
| Multi Trigger | `multitrigger` | `ignore` (during attack) / `add` / `restart` |
| Clamp at Peak Level | `clamppeak` | Caps the additive effect of multi-triggers at Peak Level |
| Update Once per Cycle | `updateonce` | (no description on the page) |
| Complete Envelope | `complete` | On: every trigger produces a full envelope, un-interruptible by a release |
| Remainder | `remainder` | `crop` / `extend` (output runs longer if unfinished) / `mix` (fold remainder into the start) |
| Trigger / Release | `trigger` `release` | Pulse an envelope **regardless of input** |
| Reset / Reset Pulse | `reset` `resetpulse` | Reset the envelope and match output to input |

*Attack page:* `delay`, `attack`, `ashape`, `peak`, `peaklen`.
*Sustain page:* `decay`, `dshape`, `sustain`, `minsustain`, `release`, `rshape`.
Shapes are `linear` / `easein` / `easeout` / `halfcos` on all three ramps.
*Chan page:* `channame`, `specifyrate` + `rate`, `enableremaplength` + `remaplength` — remap rescales
**delay, attack, peak and release only; held sustain is not remapped**.

`retrigger` and `mintrigger` are the debounce primitives — relevant to the fader-touch lag and to
gating layer-switch replays. `minsustain` is the third one worth knowing: it guarantees a sustain
floor even when the input is only briefly held.

For jittery inputs, Derivative's own OP Snippet "trigger after a time threshold" pairs this with the
Count CHOP. ⚠️ To see the whole waveform, the page says to turn **off Time Slice** on the Common page
and leave the input disconnected.

**Count CHOP** *(Tier A — full page read, page edited 2026-01-23)* — counts threshold crossings, in
static or realtime ("Cook to Current Frame") mode. Default trigger value is 0: a count occurs when
input goes from ≤0 to >0.

*Trigger page:* `threshold` (release = trigger), `threshup`, `threshdown`, `retrigger` (+ unit),
`triggeron` (`increase` / `decrease`).

*Count page — four independent operation menus,* one per input state. **This is the part worth
knowing:** `offtoon`, `on` (while on), `ontooff`, and `off` (while off) each independently choose
from `none` / `inc` / `dec` / **`inctime`** / **`dectime`** / `reset`. So one Count CHOP can, for
example, increment on press and accumulate *time* while held.

| Parameter | Name | Behaviour |
|---|---|---|
| Limit | `output` | `off` / `loop` / `min` (clamp) / `lc` (loop min, clamp max) / `cl` / `zigzag` |
| Limit Minimum / Maximum | `limitmin` `limitmax` | Bounds for the above |
| Reset Condition | `resetcondition` | `offtoon` / `on` / `ontooff` / `off` |
| Reset Value | `resetvalue` | Value on reset |
| Reset / Reset Pulse | `reset` `resetpulse` | ⚠️ **While `reset` is On the CHOP does not count** — it only resumes when Reset goes Off |

**Three inputs, and the third is easy to miss:**

- Input 0 — the channels to count
- Input 1 — reset pulses. **Any non-zero value resets the count for *all* channels**
- Input 2 — **Increment Value.** Feed it a channel of 5 and it counts by fives, or by 5 per second in
  the time modes. Removes the need for a Math CHOP after the count

`inctime` / `dectime` work in the CHOP's own time-per-sample — at 100 samples/second each sample is
1/100 s. That, plus the loop/clamp limits, makes this a cleaner dwell-time counter than a Speed CHOP
for anything that needs bounds.

**Event CHOP** *(Tier A — full page read, ⚠️ page edited 2021-11-16)* — manages the birth and life of
**overlapping** events; the docs describe it as a simple particle system designed for MIDI keyboards.
One sample per off-to-on event, living until its ADSR completes, then disappearing like particle
death. Documented as lightweight even with an 88-key keyboard and heavy playing.

*Seven channels:*

| Channel | Meaning |
|---|---|
| `id` | Sequence number, from 0, +1 per event. **Unique per event** |
| `index` | Channel index of the incoming CHOP that caused it |
| `active` | 1 while the input is greater than 0 |
| `input` | **The input value at the moment of birth, preserved until the event ends** — velocity, typically |
| `time` | Seconds since the event started |
| `adsr` | Envelope value per the ADSR page |
| `state` | 0→1 attack, 1→2 repeating through sustain, 2→3 release. Fractional, for indexing movies |

*ADSR page:* `attacktime` `attacklevel` `decaytime` `sustaintime` `sustainmin` `sustainmax`
`releasetime` `releaselevel`, each time with its own Samples/Frames/Seconds unit, plus `speed` and
`globalspeed` to stretch or shorten an event's whole life.

*Three inputs:* triggers, reset, and an optional third that **samples values per event**.
`resetcondition` only becomes active when something is wired to the second input.

**`callbacks` is the part the earlier snippet-sourced entry missed:** the Event CHOP takes a
Callbacks DAT with **`onCreate()` and `onDestroy()` per event**. That makes it a per-event Python
dispatch, not just a channel generator — the closest thing in the CHOP family to per-control state
that survives concurrently.

⚠️ The page contradicts itself on channel count: the summary says "up to 8 channels," the Channels
page lists seven. Seven are named. And it hasn't been edited since 2021.

**Logic CHOP** *(Tier A — full page read, ⚠️ page edited 2021-11-16)* — converts all input channels to
binary (0/1) and then combines them. For arithmetic between channels use the **Math CHOP** instead.

⚠️ **Derivative's own page says this operator is superseded** by the CHOP Execute DAT or a Text DAT,
which run scripts when channel values change. Worth weighing before building logic trees out of it.

| Parameter | Name | Options |
|---|---|---|
| Convert Input | `convert` | `nonzero` (off when zero) / `pos` (off when ≤0) / `bound` (off outside Bounds) / **`valchange`** (on when the value changed) / `namechange` (on when the channel name changed) |
| Channel Pre OP | `preop` | `off` / `invert` / **`toggle`** / **`radio`** / `radio2` / **`rise`** / `fall` |
| Combine Channels | `chanop` | `off` / `and` / `or` / `xor` / `nand` / `nor` / `eqv` / `lowest` / `highest` |
| Combine CHOPs | `chopop` | Same set, applied across inputs rather than within one |
| Match by | `match` | `index` or `name` |
| Align | `align` | Nine options for inputs that don't start on the same frame |
| Bounds | `bound` | `boundmin` / `boundmax`, used by `bound` convert mode |

**The Pre OP menu is the useful part for a control surface:**

- **`toggle`** — each 0→1 transition flips a held state. Latching buttons without Python
- **`radio`** — only one channel on at a time; turning one on turns the previous one off. That is
  exclusive layer or bank selection, done in a CHOP
- **`radio2`** ("Last Two On") — keeps up to two on; the docs suggest following it with a Lag CHOP to
  blend between pairs
- **`rise`** / **`fall`** — on for exactly one sample at each edge. Edge detection without a Trigger CHOP

`lowest` / `highest` return the index of the lowest or highest channel that is on, **or −1 when none
are** — a ready-made "which button is selected" readout.

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

*Added on the second pass (2026-08-01):*

- Whether OSC In CHOP still has a **Pulse Mode** toggle and Min/Max Target parameters. The page's summary describes both; the page's own parameter list does not contain either, while the Info CHOP channel names still reference min/max targets. Unresolved from the docs alone — check the operator in the running build.
- Whether OSC Out DAT's parameter names are still accurate. The page has not been edited since 2022-05-21 and still labels an output operator's second page "Received Messages."
- Whether `total_bumped` on OSC In CHOP counts dropped messages or dropped samples. The page names the channel but does not define it; "Incoming samples will be dropped if the maximum queue is reached" is the nearest statement.
- Whether Web Client DAT's `connected` channel tracks a persistent connection or only the in-flight request. **Partly answered on the ninth pass:** `webclientDAT_Class` exposes a `connections` *list* and `closeConnection(id)`, so the operator tracks several concurrent connections by id — `connected` is therefore probably an aggregate. Still not stated outright. **This matters before treating the REST leg as a health signal** — see §10 and §2.
- ⚠️ **Whether `onResponse` actually receives a request id.** `webclientDAT_Class` says `request()` returns an id corresponding to "the id passed to onResponse callbacks", but the documented `onResponse` signature has no id argument (§2). Without one, concurrent REST calls cannot be correlated to their responses. Check the running build.
- Whether the Error DAT (§12) can catch WebSocket DAT disconnects, which would close the §10 gap without inference. Still unread.
- Sync In/Out CHOP, Touch Out CHOP, the DMX pair and the timecode group remain Tier B — snippet-sourced, parameter lists incomplete.

*Added on the eleventh pass (2026-08-01):*

- Whether a MIDI In CHOP's `.timecode` member can drive a Timer CHOP's **External Timecode** mode directly (§5i). The Timer's `timecodeop` accepts a Timecode Class object and this produces one, so it should — inference, untested.
- ~~`midiinCHOP_Class` was mirror-sourced~~ — **resolved.** Read from `docs.derivative.ca` (2023-12-19, oldid 30581) after the URL was supplied directly. **Docs and mirror match verbatim** — the first direct comparison of the two in this file. One matching page is not a general clearance for the mirror; the standing assumption in the provenance block stands for everything else.
- **Fetch-tool constraint worth recording for future passes:** URLs can only be fetched if they appeared in a prior search result, a prior fetch, or were supplied by the user. A `docs.derivative.ca` page that no search surfaces is not unreachable — it just needs the URL pasted in. Do not record such cases as "unreachable."
- Re-check whether other `docs` pages differ from their mirror counterparts. Only one pair has been compared.
- **`docs.derivative.ca/Timecode_Class` is now a known-good URL** (surfaced 2026-08-01). It is referenced by Info CHOP's Timecode info type, Timeline CHOP's `timecodeop`, MIDI Out CHOP's `sendTimecode()`, MIDI In CHOP's `.timecode` and Timer CHOP's timecode members — five operators in this file depend on it and it is still unread. **Highest-value unread supporting page.**
- Whether the Timer CHOP's External Timecode parameter accepts a `tdu.Timecode` object the way Timeline CHOP's and MIDI Out CHOP's `timecodeop` explicitly do (§5i). Timer's own parameter name was never captured.

*Added on the tenth pass (2026-08-01):*

- ⚠️ **§3's Web Server DAT callback list is incomplete and its signatures disagree with the class page.** The class page gives `onWebSocketOpen(dat, client, uri)` — the operator page omits `uri` — and adds `onWebSocketReceivePing` / `onWebSocketReceivePong`, which the operator page does not list at all. Verify against the running build.
- Whether an unhandled request path really returns 404 by default, as the `response['statusCode']` default implies (§3).

*Added on the seventh pass (2026-08-01):*

- ⚠️ **What `useNonStandardTypes` should be set to for each OSC receiver in the rig.** It defaults True, which sends booleans and None as OSC T/F/nil rather than ints (§4b). Resolume's tolerance for this is not established — worth a bench check on any OSC leg that sends booleans.
- Whether `send()`'s `terminator` default appends a null or nothing — the page states both (§4b).
- ~~Whether `oscinDAT_Class` really exposes `sendOSC`~~ — **resolved on the eighth pass: it does.** OSC In DAT is bidirectional (§4a). Still open: whether its replies go to the originating peer automatically or need `peer.address` / `peer.port` supplied explicitly.
- ⚠️ **`Peer Class` is now partly covered** — its four members are documented inline on `oscinDAT_Class` (§4a). The standalone page is still unread, so anything beyond `address`, `port`, `owner` and `close()` is unknown.

*Added on the sixth pass (2026-08-01):*

- ⚠️ **The pass-one Timer CHOP callback list in §11 was wrong** (`onTimerActive` does not exist; it is `whileTimerActive`) **and missed four callbacks**. Now corrected from the class page. Worth asking what else from pass one was taken from the operator page's prose rather than a callback listing.
- Whether `goTo()`'s `endOfCycle` actually defaults True or False — the class page states both (§11).

*Added on the fifth pass (2026-08-01):*

- ⚠️ **Which MIDI Out send method the X-Touch bench test used is not recorded.** The stored "raw `send()` bypasses normalize and index" pattern is correct for `send()` and contradicted by the docs for the named send methods (§5h). Re-test before reuse.
- **What One Based Index is set to on the rig.** It decides whether the −1 correction is needed on the output side at all (§5h).
- Whether MIDI Out CHOP's **Controller Format** parameter (referenced by `sendControl`) is the 7-bit/14-bit switch. The MIDI Out CHOP page was read in pass one but this parameter is not captured in §5b.

*Added on the fourth pass (2026-08-01) — supporting pages referenced by operators already read, none of them consulted:*

- **`Peer Class`** — linked from OSC In DAT. Presumably how a callback identifies the *sender* of a message. Relevant to any hub taking OSC from more than one source; unread.
- **`Network Protocols`** — linked from all four OSC operators. Defines what Messaging / Multi-Cast / Reliable (UDT) actually guarantee, and what **Shared Connection** does when several DATs share a port. §4 states the menu options without the semantics behind them.
- **`Pattern Matching`** — the syntax for every `addscope` / `oscaddressscope` / `scope` / `sliders` / `buttons` parameter in this file. Used throughout, never read.
- **`MIDI Device Mapper Dialog`** — MIDI In Map CHOP (§5e) is only meaningful in terms of this dialog, and MIDI In DAT points at it as the simpler setup path. Unread.
- **`Beat Dialog`** — Beat CHOP (§11) gets its BPM and sync from it. Unread.
- **`Timecode` page / `Timecode Class`** — referenced by Info CHOP's Timecode info type, Timeline CHOP's `timecodeop`, and MIDI Out CHOP's MTC output. Unread.
- **Common-page parameters were deliberately omitted** from every entry in this file (Time Slice, Scope, Sample Rate Match, Export Method, Rename). They are near-identical across the CHOP family. This is an editorial choice, not a gap — but it means "complete parameter list" in the Tier A definition excludes them.
- **`Experimental:` namespace pages exist for some operators** (an Experimental Timer CHOP page was seen in search results). Whether they carry newer information than the main pages is unknown; none were checked.


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
