# Control-surface authority — who owns a control's state

Patterns from building a bidirectional link between a Behringer X-Touch Compact and Resolume
Arena, in TouchDesigner. Generic: the surface and the target app are named only where a fact
about them is what makes the pattern necessary.

## Provenance

- **Tier: Bench-verified throughout** unless a section says otherwise. Every pattern here ran on
  hardware against live software on 2026-08-04. None has run a show.
- **Vendor facts are not restated.** Device behaviour is cited to
  `protocols/behringer-x-touch-compact.md` §5a, and the media server's message shapes to
  `protocols/resolume-control-interfaces.md` §3.2a. If a number appears wrong, those are the
  documents to correct.
- **Not read:** no literature on control-surface design was consulted. These are conclusions from
  one build against one surface, and the surface's particular limitations shaped several of them.
- **Open, unresolved:** whether the write-deduplication below can drift out of step with a device
  that changes state on its own; whether the settle interval for motor writes generalises past
  one operator's taste.

---

## 1. The surface is not a dumb terminal — decide who owns each control

**Tier: Bench-verified.**

The assumption that costs the most time is that a control surface displays what you tell it. A
capable surface renders its own controls locally: it lights its buttons while held, draws its own
encoder rings as you turn, and remembers positions across banks. It does this whether or not a
host is connected.

So for every control there are three possible owners, and the choice has consequences:

| Owner | Works well for | Costs |
|---|---|---|
| **Device** | Anything the device renders better than the host can | The host cannot reflect state that originates elsewhere |
| **Host** | Anything driven from software — a value changed in the target app, a preset recall | The host must write last, and may not be able to match the device's own fidelity |
| **Split** | Device owns the display while a hand is on it, host owns it otherwise | Two code paths, and a rule for which is active |

**The deciding question is not "who should own this" but "can the host actually render it".**
On this surface the encoder ring renders 25 states locally and accepts only 13 over MIDI
(`behringer-x-touch-compact.md` §5a). Host authority and smooth rendering are therefore mutually
exclusive for that control, and no amount of code changes it. Establish the ceiling before
designing around it.

**Where the host does own a control, it must write last, not first.** A device that lights its own
button on press and clears it on release will wipe a host write made at press time. The host has
to re-assert on the release event.

---

## 2. "Never seen" and "zero" are different, and conflating them moves motors

**Tier: Bench-verified — this one caused a visible fault.**

A host that stores control values in a table will typically return 0 for a control it has never
received. That is indistinguishable from a stored zero.

It stops being harmless the moment the host asserts state. On a bank change, a repaint drove every
fader the host had never learned to the bottom — over positions the device had correctly restored
from its own memory.

**The pattern:** track presence separately from value. Only assert a control the host has actually
learned; leave the rest to the device.

```
if not self.Has(control):
    return          # never learned in this bank — do not assert a zero
```

**Generalises past faders.** The same flaw affects any feedback, but only motorised controls make
it visible. Rings and LEDs fail silently in exactly the same way.

---

## 3. Trust the device's memory — deduplicate writes

**Tier: Bench-verified.**

A surface that remembers its own per-bank state does not need to be told what it already knows.
Re-asserting an unchanged value is at best pointless traffic and at worst overrides something the
device had right.

**The pattern:** record what was last actually sent, per control per bank, and skip the send when
the value has not moved.

```
seen = (control, bank)
if not force and self._written.get(seen) == value:
    return
self._written[seen] = value
```

⚠️ **Two traps, both hit during the build:**

- **Anything that deliberately re-sends an identical value breaks.** The re-assert on button
  release exists precisely to send an unchanged value again. It needs an explicit `force`. Audit
  every call site when adding deduplication — the failure is silent.
- **Drift has no automatic cure.** If the device and host ever disagree without the host's value
  changing, nothing corrects it. Keep a `Forget()` that clears the record, and wire it somewhere
  reachable.

---

## 4. Motorised faders: gate on the hand, settle before moving

**Tier: Bench-verified.**

Two separate rules, often confused.

**A motor must never be driven while a hand is on the control.** A hold-off window, armed by touch
*and* by movement, and closed by a timeout or by an authoritative value from outside:

- **Movement opens the window**, because touch-on can lag the first movement message — roughly
  2–9 frames on this surface.
- **Touch keeps it open**, so a long adjustment never expires mid-move.
- **Release starts a short tail** rather than closing it immediately.
- **An authoritative value from outside outranks the hand** and closes the window at once.

**A motor should not chase a value that is still changing.** A fader following a slider drag in the
target app is noisy and pointless. Track the value as it arrives, write the state immediately so
nothing is lost, and move the motor once after the value has been still for a short interval —
15 frames worked.

---

## 5. Bank detection when the surface says nothing

**Tier: Bench-verified, with a documented limitation.**

A surface with hardware bank buttons that transmit nothing leaves the host unable to know which
bank is live. The device restores its own state silently, and there is no query command
(`behringer-x-touch-compact.md` §5a).

**What works:** derive the bank from the **channel** of any incoming message, and apply it before
anything else in the handler.

```
if control != PEDAL:                       # a control pinned to one channel
    live = 'b' if channel in (2, 4) else 'a'   # ... in both banks proves nothing
    if live != self.layer:
        self.layer = live
        self.RefreshAll()
```

⚠️ **Apply it first, ahead of every early return.** Several message paths return early — a button
whose state a listener owns, a note-off, a touch event — and a bank correction that only some
messages reach is worse than none. This was a real fault: only fader moves corrected the bank,
because everything else returned before reaching the check.

**A control deliberately pinned to one channel in both banks cannot be evidence of the bank.**
Exclude it explicitly.

**The residual limitation:** between a bank change and the next control message, the host's belief
is stale. Nothing fixes that from the host side. The alternative is for the host to own bank
switching outright — this surface accepts Program Change for it — at the cost of making the
hardware bank buttons off-limits.

---

## 6. Two components, one listener hook

**Tier: Bench-verified.**

Keep the surface component and the target-app component ignorant of each other. The surface
announces every control that moves; the target-app component listens and decides what it means.

```
def AddListener(self, comp): ...
def _notify(self, control, value, bank, channel, kind, num): ...
```

**Pass the message's own identity** — channel, type, number — not just a control name. A listener
that has to parse `fader_touch3` to find `fader3` is doing string surgery to recover an identity
the message already carried. Both mapping tables should key on the same thing.

**Pass the raw value, not the host's processed one.** A button bound to a selection wants the press
event, not the host's toggle state. A listener that wants the stored value can ask for it.

⚠️ **Re-attach on reconnect.** Reinitialising the surface component builds a fresh object with an
empty listener list, silently detaching everything. Attaching once at construction is not enough —
the symptom is a surface that lights its own buttons while nothing reaches the target app.

**Where a listener owns a control's state, let it claim the control**, so the surface does not
apply its own toggle first and latch the wrong state before the real answer arrives.

---

## 7. Subscribe rather than poll, where the target app allows it

**Tier: Bench-verified.**

Where the target app pushes on change, a control surface link needs no polling loop at all. The
pattern that worked:

1. On connect, take the app's structure dump and extract the parameter identifiers it names.
2. Subscribe to each.
3. Route incoming updates to the bound control.
4. Rebuild and re-subscribe whenever the structure changes — most apps re-send the dump.

**This covers changes made in the app's own interface for free**, which is usually the requirement
that rules out polling.

⚠️ **Do not assume the identifier you subscribe with is the one you get back.** On Resolume they
differ (`resolume-control-interfaces.md` §3.2a). Treat the subscription response as authoritative
for what later updates will carry.

⚠️ **A structure dump is a large message.** Parking it in a viewable text operator dropped the host
to 11 fps. Parse it, keep what is needed, and do not leave it rendering.
