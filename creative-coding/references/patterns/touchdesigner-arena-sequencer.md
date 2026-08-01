# Arena Sequencer — TouchDesigner column sequencer for Resolume Arena

Project: a column sequencer for Resolume Arena 7, running in TouchDesigner, with a browser/phone
UI. Built starting 2026-05-01.

> **Provenance of this document.** Reconstructed 2026-07-19 from session records, **not** from the
> source files. The original file set — `arena_sequencer.py`, `arena_web_callbacks.py`,
> `index.html`, `readme.txt` — was delivered as downloads and is not in hand. What survives is the
> design reasoning and the specific bugs we hit. Treat code fragments below as *descriptions of
> what the code did*, not as verified transcriptions. If the original files still exist locally,
> they supersede this entirely.
>
> Protocol facts about Resolume's API are deliberately **not** duplicated here — see
> `digital-video/references/` (Resolume API reference; see INDEX "depends on" note).

---

## 1. Architecture — three-tier split

**Tier: Bench-verified.** Ran end to end on the user's rig; no record of it running a show.

The split we settled on:

| Layer | Owns |
|---|---|
| TouchDesigner | Sequencer clock, playhead/cursor, Resolume triggers, state persistence, WebSocket broadcast to all connected browsers |
| Browser / phone | UI rendering, column trigger buttons, playlist editing, preset management — sends commands to TD, holds no authority |
| Resolume | Receives column connects. Nothing else. |

The browser is deliberately dumb. Every client sees the same state because TD broadcasts it, so
multiple phones stay in sync for free and there's no client-side merge problem.

**Components in TD:**

- **Web Server DAT** (`arena_web`) on port 9000, with a Callbacks DAT (`arena_web_callbacks`).
  Both HTTP *and* WebSocket must be enabled on it — HTTP alone serves the page but the UI won't update.
- **Execute DAT** with **Frame Start** toggled on, callback body calling `mod('arena_sequencer').tick()`.
  The clock is frame-driven, not a Timer CHOP.
- **Text DAT** holding `arena_sequencer` as a module, called via `mod()`.

**Startup order that worked:** Resolume running with its webserver enabled *first*, then open the
TD project. The console prints the LAN URL for phones to hit.

**Phone onboarding.** Print a QR of the LAN URL to the TD console. Requires installing `qrcode`
into TD's own Python:

```python
import subprocess
subprocess.run(['pip', 'install', 'qrcode', '--break-system-packages'])
```

**Tier: Bench-verified.** Note this installs into TouchDesigner's interpreter, not the system one,
and will not survive a TD reinstall.

**State persistence.** `arena-state.json` written beside the `.toe`, holding playlist, presets, and
Resolume connection config. Deleting it resets to blank. Connection settings are editable from the
web UI's settings panel and persist across TD sessions.

---

## 2. Column identity — key off `resId`, never index

**Tier: Shipped-quality reasoning, Bench-verified in practice.** This is the load-bearing decision
in the whole project.

Cue rows must reference columns by their stable id (`resId`), not by position. Column indices shift
whenever columns are reordered in Resolume, which silently repoints every saved cue.

### The trap: default column names

Storing the column's *display name* alongside `resId` seemed harmless and was not. Resolume's
default names are `Column 1`, `Column 2`, … and those **re-number on reorder**. A cue that stored
`colName = "Column 7"` would later render as the wrong label, or overwrite good data.

The fix, applied in two places:

- In the dropdown-refresh path: only write `colName` back onto a cue item if the column has a
  *custom* name — guard with `/^Column \d+$/`.
- In the column-select change handler: same guard, store `''` for default-named columns.

```javascript
// don't store default column names — they re-number when columns reorder
row.colName = (found?.name && !/^Column \d+$/.test(found.name)) ? found.name : '';
```

**Generalization, and it is ours not a documented rule:** in any Resolume integration, treat a
default-pattern name as *absence of a name*. Only user-assigned names are stable identifiers.

---

## 3. External trigger detection — distinguishing us from a human

**Tier: Bench-verified.** Confirmed working end to end via console observation.

Requirement: if someone triggers a column directly in Resolume while the sequencer is running,
the sequencer should pause rather than fight them.

Two mechanisms were built, and both ended up useful.

### 3a. `selected` over WebSocket + a self-trigger timestamp

`selected` was the one parameter observed being pushed in real time. Everything else had to be polled.

The scheme:

- Every time TD triggers a column itself, stamp `_selfTrigCols[colIndex] = now`.
- When a `selected` event arrives, look up the stamp.
- Missing stamp, or stamp older than **1.5 s** → it was a human → pause immediately.

**The 1.5 s window is empirical.** It was chosen to cover observed WebSocket round-trip latency on
one machine on one LAN. It is not derived from anything and has no vendor basis. Re-check it on a
different network, and especially on anything routed or wireless — too tight causes false
"external" pauses on our own triggers, too loose misses fast human intervention.

### 3b. Composition poll + state diff (the fallback that proved itself)

Poll the composition at 1 s into a dict of column → connection state, and diff successive reads:

```python
mod('/project1/arena_sequencer')._prev_col_state
# {1: 'Disconnected', 2: 'Connected', 3: 'Disconnected', ... 23: 'Empty'}
```

Three observed states: `Connected`, `Disconnected`, `Empty`. Confirmed detecting an external
trigger correctly — column 19 flipped `Disconnected` → `Connected` and the diff fired.

**Gating gotcha:** detection only runs when `_playing or _paused` is true. Early testing looked
like the detection was broken when in fact the sequencer simply wasn't started. Check the gate
before debugging the detector.

**Known replacement path, not yet done.** Resolume pushes full composition state on WebSocket
connect and re-sends it on structural change. Folding that into the WS handler would let the 1 s
poll be dropped entirely. See `digital-video` for the API behavior; this refactor is **Designed**,
not attempted.

---

## 4. Bugs and dead ends

Kept deliberately — the record of what failed is worth as much as what worked.

### WebSocket closing immediately — **Abandoned / never root-caused**

Symptom: `Resolume WS closed — code: None msg: None` immediately after each successful subscribe,
in a loop. Close code `None` with no message.

- **Attempted fix:** adding an `Origin` header matching the Resolume host/port to the
  `WebSocketApp` constructor. Did not resolve it.
- **What we actually learned:** the connection *was* delivering data. Colour changes landed exactly
  when the socket reconnected and re-subscribed — meaning Resolume was sending the param update,
  and we were only seeing state on reconnect. So the subscription worked and the *connection
  lifetime* was the problem.
- **We never found out why it dropped.** Do not describe this as solved. If it resurfaces, that
  reconnect-timing observation is the thread to pull.

### `pause_toggle()` second-trigger bug — **Fixed**

A second external trigger resumed playback instead of staying paused. Fixed in the toggle logic.
Symptom is worth remembering because it masqueraded as broken external-trigger detection.

---

## 5. Debugging technique — introspect, don't instrument

**Tier: Shipped.** This is the single most useful habit from the project and generalizes past it.

Read live module state straight from the TD textport rather than adding prints and reloading:

```python
mod('/project1/arena_sequencer')._prev_col_state
mod('/project1/arena_sequencer')._playing, mod('/project1/arena_sequencer')._paused
```

Establishes what the system is *actually* doing in one line, with no edit-reload cycle. It found
both the gating gotcha and the confirmation that the composition poll was live — each of which had
been mistaken for a different bug.

**Corollary:** name internal state attributes so they're worth inspecting. `_prev_col_state` and
`_playing` were readable from the console at a glance; that was not an accident.

---

## Open items

- 1.5 s self-trigger window: never re-tested off the original network.
- 1 s composition poll: superseded in principle by the WS structural-change push; refactor untried.
- WebSocket drop: unexplained.
- Original source files: not in hand. Recover from local storage if they exist.
