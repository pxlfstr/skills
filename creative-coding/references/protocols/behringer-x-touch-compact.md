# Behringer X-Touch Compact

USB/MIDI control surface. Device facts, complete factory MIDI maps, and the receive-side (feedback) map.

**Primary source:** *X-Touch Compact Quick Start Guide, V 6.0* (Music Tribe, 2024) `[Official]` — read directly. Everything in §1–§5 is **Verified** from that document unless tagged otherwise.

---

## Provenance

**Primary source:** *X-Touch Compact Quick Start Guide, V 6.0* (Music Tribe, 2024) `[Official]` — read directly. §1–§5 are **Verified** from that document.

**§7 `.bin` preset format decode is `[Lead]`** — reverse-engineered from a 723-byte export with no format specification. Field meanings for channel, message type, index, min and max are unambiguous from comparing two exports; trailing bytes remain unexplained.

**Not read:** no firmware release notes, no X-Touch Editor documentation beyond the Quick Start Guide, no MIDI Implementation Chart (Behringer does not publish one for this device as far as this session established).

**Open items, left in place:**
- The RX button-LED table is printed as fixed notes 0–38 on the global channel with no per-layer variant shown. **Unverified** whether that holds in Layer B.
- The layer Speed fader does not receive feedback on clip change. Suspected bug; **unconfirmed.**

**§5a added 2026-08-04 — Tier: bench-observed.** Measured on the unit, not read from any documentation. Several items contradict or extend the manual and say so in place. Nothing in §5a carries a page date or revision, because no page states it. No Behringer documentation covers local ring rendering, the Momentary/Toggle channel interference, or the absence of a query command — their absence from the manual is itself part of the finding.

**Stored 2026-07-20, extended 2026-08-04.** See `xtouch-compact-midi-map.md` for the user's own decoded map, which supersedes the factory maps here for their rig.

---

## 1. Hardware

| Item | Spec |
|---|---|
| Rotary/push encoders | 16, endless, detent + push, 13-segment amber LED ring, push not illuminated |
| Buttons (LED backlit) | 39 |
| Faders | 9 motorized, 100 mm, touch-sensitive (8 channel + 1 master) |
| Foot control — expression | 1/4" TS |
| Foot control — switch (sustain) | 1/4" TS |
| MIDI in / out | 5-pin DIN |
| Computer connection | USB 2.0 type B |
| USB hub | Multi-TT USB 2.0, 2 × type A, 5 V |
| Power | 100–240 VAC, 50/60 Hz, 25 W, IEC, fuse T 1A H 250V |
| Dimensions (H×W×D) | 100 × 391 × 301 mm |
| Weight | 3.7 kg |

USB class-compliant — no driver. The **X-Touch Editor** (free, behringer.com) is the only way to edit MIDI assignments or update firmware.

**Presets:** Layer A (user-programmable), Layer B (user-programmable), MC mode.

**Fader inversion:** value range can be inverted in the Editor (min = 127, max = 0) for drawbar-organ use. Drawbar footages (16', 5⅓', 8'…) are printed beside the fader numbers.

### USB mode vs. stand-alone

The unit detects whether a computer is present on the USB MIDI socket and switches automatically.

| | USB mode | Stand-alone |
|---|---|---|
| MIDI OUT carries | Only MIDI received from the host computer | X-Touch's own data, merged with MIDI IN |
| MIDI IN routes to | Host computer only | MIDI OUT (thru) **and** the X-Touch itself (parameter feedback) |
| USB hub | Active | Inactive |

The hub talks to the computer, **not** to the X-Touch. It is only live when the unit is powered on *and* in USB mode.

### Mode switching

Hold **MC** (bottom-left button) while switching on power. Keep holding until the MODE MC LED is steady = MC mode. Repeat and confirm the LED stays **off** to return to Standard mode. The mode persists across power cycles.

### Status LEDs

INTERFACE USB · MIDI IN · MIDI OUT · FOOT SW · FOOT EXP · MODE MC.

---

## 2. Preset Layer A — "Mixer Control" (MIDI channel 1)

Every **push** function (encoder push + button) is a **Note**. Every **continuous** function (encoder rotation, fader move, fader touch, foot control) is a **CC**.

| Control group | Message | Range |
|---|---|---|
| Encoders, top row (8) — turn | CC | CC10–CC17 |
| Encoders, top row (8) — push | Note | 0–7 |
| Encoders, right block (8) — turn | CC | CC18–CC25 |
| Encoders, right block (8) — push | Note | 8–15 |
| Button grid row 1 (8) | Note | 16–23 |
| Button grid row 2 (8) | Note | 24–31 |
| Button grid row 3 (8) | Note | 32–39 |
| Faders 1–8 + master — move | CC | CC1–CC9 (CC9 = master) |
| Faders 1–8 + master — touch | CC | CC101–CC109 |
| Lower button row (8) | Note | 40–47 |
| Lower button row, master position | Note | 48 |
| Transport / right area (6) | Note | 49, 50, 51, 52, 53, 54 |
| Expression pedal | CC | CC26 |
| Foot switch | CC | CC27 |

---

## 3. Preset Layer B — "Instrument Control" (MIDI channel 1)

Same physical layout, different numbers. Layer B does **not** simply offset Layer A — check the table.

| Control group | Message | Range |
|---|---|---|
| Encoders, top row — turn | CC | CC37–CC44 |
| Encoders, top row — push | Note | 55–62 |
| Encoders, right block — turn | CC | CC45–CC52 |
| Encoders, right block — push | Note | 63–70 |
| Button grid row 1 | Note | 71–78 |
| Button grid row 2 | Note | 79–86 |
| Button grid row 3 | Note | 87–94 |
| Faders 1–8 + master — move | CC | CC28–CC36 |
| Faders 1–8 + master — touch | CC | CC111–CC119 |
| Lower button row (8) | Note | 95–102 |
| Lower button row, master position | Note | 103 |
| Transport / right area (6) | Note | 104, 105, 106, 107, 108, 109 |
| Expression pedal | CC | CC63 |
| Foot switch | CC | CC64 |

**Note the gap:** Layer A fader-touch runs CC101–109, Layer B runs CC111–119. CC110 is unused in the factory maps.

---

## 4. MC (Mackie Control) mode

Fixed assignment, not user-editable from the layer maps.

- Faders 1–8 + Master; VPOT 1–8 (turn + push)
- Per-channel button rows: **SOLO / MUTE / SELECT / REC**
- **FLIP**, **MARKER**, **NUDGE**
- Encoders 9–14: **push = VPOT ASSIGN** (TRACK, SEND, PAN, PLUG-IN, EQ, INSTR); turn is **not** assigned
- Encoders 15, 16: **turn = Fader Bank / Channel select**; push is **not** assigned
- Foot switch = User Switch 1; expression pedal = External Control

---

## 5. Receive-side map (RX MIDI) — driving the surface

This is what makes the X-Touch a *feedback* surface rather than a one-way controller. All of it is received on the **global channel**, independent of the X-Touch Editor.

| Function | Message | Values |
|---|---|---|
| Operation mode select | CC127 | 0 = Standard, 1 = MC, 2–127 ignored |
| Preset layer change | Program Change | 0 = Layer A, 1 = Layer B, 2–127 ignored. **Standard mode only** |
| Fader movement (motors) | CC1–CC9 | 0–127 = position, bottom to top |
| LED ring **behavior** | Encoders 1–8: CC10–CC17<br>Encoders 9–16: CC18–CC25 | 0 = Single, 1 = Pan, 2 = Fan, 3 = Spread, 4 = Trim, 5–127 ignored |
| LED ring **value** | Encoders 1–8: CC26–CC33<br>Encoders 9–16: CC34–CC41 | 0 = all off; 1–13 = LED *n* (left→right) on; 14–26 = LED *n* blinking; 27 = all on; 28 = all blinking; 29–127 ignored |
| Button LEDs | Note on/off | Note off, or note on velocity 0 = off; velocity 1 = on; velocity 2 = blinking; velocity 3–127 ignored |
| Foot switch LED | CC42 | 0–63 off, 64–127 on |
| Expression pedal LED | CC43 | On only during data transfer (value change) |

**Button-LED note numbering (RX side):**

| Physical group | Notes |
|---|---|
| Upper top row 1–8 | 0–7 |
| Upper mid row 9–16 | 8–15 |
| Upper bottom row 17–24 | 16–23 |
| Lower row 25–33 | 24–32 |
| Right area 34–39 | 33–38 |

Layer A/B LEDs are **not assignable** — exactly one of the two lights, reflecting the selected layer.

**Bench-confirmed 2026-08-04**, one raw send per block: note 0 lights row 1 button 1, 8 lights row 2 button 1, 16 lights row 3 button 1, 24 lights row 4 button 1, 33 lights the rewind button. Numbering is raw throughout, not 1-based, and ascends left to right within each block. The whole table is now verified against hardware.

⚠️ **Button LED velocity contradicts the manual.** Bench-observed: **1 = off, 2 = on, 3 = blinking**, and velocity 0 also reads as off. The table above is the manual's, and it is wrong for `on` and `blink`. Working explanation: the firmware's enum is 1-based while the manual documents it 0-based, and velocity 0 lands on off separately through the standard note-on-velocity-0 convention. Values 4–127 untested.

⚠️ **Still open:** whether RX button-LED numbering re-numbers per layer. Confirmed only in Layer A.

---

## 5a. Bench findings, 2026-08-04

All measured on the unit, not read from documentation. Several contradict or extend the manual.

### The device drives its own controls

**In Momentary push behaviour the device lights and clears its own button LED** — lit while held, dark on release — regardless of what the host sends. A host write on the press is wiped by the device's clear on release.

**Consequence for any host that owns button state:** re-send on note-off, not only on note-on. Without that the LED goes dark on every release and only returns on the next periodic repaint, which reads as a multi-second delay to light and an instant response to turn off.

**The device also draws its own encoder rings** as you turn, and this cannot be switched off — none of the ring behaviour modes hands display to the host.

### Encoder ring: the device renders 25 states, the host can send 13

Measured with USB disconnected, so this is the device's own local rendering across its internal position:

| Value | Ring |
|---|---|
| 0 | all off |
| 1–6 | LED 1 |
| 7–11 | LEDs 1 & 2 |
| 12–16 | LED 2 |
| 17–21 | LEDs 2 & 3 |
| 22–27 | LED 3 |
| … | alternating single and adjacent pair |
| 64 | LED 7 |
| 122–126 | LEDs 12 & 13 |
| 127 | LED 13 |

Thirteen single LEDs plus twelve adjacent pairs — **25 states**. The RX table exposes only the thirteen singles.

⚠️ **So a host cannot reproduce what the device draws for itself.** Whenever the device is showing a pair, a host write lands on one of the two, which reads as a flicker on the neighbouring segment. No scaling formula fixes it; the resolutions differ. Host authority over the rings and smooth rendering are mutually exclusive on this hardware.

**Bench-confirmed:** raw sends of 30, 64 and 100 to a ring value CC produced no change, so **29–127 really are ignored** and the pair states are unreachable over MIDI. A send of 2 gave a single LED.

**Bench-confirmed:** the ring value table is **not** shifted the way the button LED velocity table is. Sending 13 gave the rightmost LED solid, 14 gave the leftmost blinking, exactly matching the documented 1–13 / 14–26 bands.

⚠️ **Value 0 is a real state — all LEDs off — not the bottom of the 1–13 range.** A host that clamps a zero up to 1 leaves one segment lit at zero.

### Bank changes are silent, and the device cannot be polled

**Switching banks on the surface produces no MIDI at all.** The device silently restores its own per-bank fader positions and LED states.

**The entire receive map is write-only.** There is no query, request or dump command — nothing asks the device for a control's position. So a bank change can never be detected after the fact, and the device's own memory is the only source of truth for anything the host has not been told.

Two consequences for host design:

- A host must not assert values it never learned. A "never seen" control and a stored zero are indistinguishable unless the host tracks them separately, and asserting an unlearned zero drives a motorised fader to the bottom over a position the device had correct.
- **Program Change is the way out** — `0 = Layer A, 1 = Layer B`, Standard mode only. A host that sets the bank always knows it. ⚠️ Documented, never bench-tested; and the hardware A/B buttons still transmit nothing, so a user pressing one desyncs it again.

### Fader touch interferes with the fader's own CC

⚠️ **Undocumented, mechanism unknown.** With fader touch assigned to the same MIDI channel as the fader's own move CC and set to **Momentary**, the move CC is corrupted — a fader alternated between 0 and 127 instead of sweeping, with the host sending nothing at all.

**Toggle** cleared the corruption but made touch useless as a gate: there is **no message on finger contact**, only one per release, alternating 127 then 0 on successive releases.

**The fix is neither setting — it is a separate channel.** With touch moved to its own MIDI channel it works properly on Momentary: 127 on contact, 0 on release, with the fader's own move messages arriving between the two, and no corruption.

⚠️ Touch-on lags the first movement message by roughly 2–9 frames, so touch is not usable as the *onset* signal for echo suppression. Arm on first movement and use touch for the release edge.

---

## 6. Integration notes — Resolume

**Tier: Lead / bench-derived.** These came out of a working session, not from a manufacturer document. Vendor-side facts for Resolume's control interfaces are in `resolume-control-interfaces.md`.

- **Boot in Standard mode**, not MC. Resolume expects plain Note/CC; MC mode speaks a different protocol entirely.
- **Leave the factory Note/CC layout alone.** It already matches what Resolume wants — Notes for discrete buttons, CC for continuous controls.
- **Two Editor edits are worth making:**
  1. Resolve the fader-touch CC so MIDI-learn doesn't grab the touch CC (CC101–109) instead of the move CC (CC1–9). Touching a fader before moving it is the normal gesture, so learn sees touch first.
  2. Set buttons to **Momentary**, so Resolume owns LED state and drives it back via feedback rather than the surface toggling locally.
- **Enable both MIDI Input and Output** in Resolume Preferences, or motors, encoder rings and button LEDs never re-seat.
- **Layer A/B as two control banks** — motors re-seat on each flip, which is the whole point of a motorized surface.
- **Why Notes for buttons rather than CC:** type matching. Notes model discrete press/release events; CC models continuous ranges. LED feedback rides more reliably on note echoes than on CC-as-button workarounds.
- ⚠️ **Known gap:** the layer Speed fader does not receive feedback on clip change. Suspected Resolume bug; unconfirmed.

---

## 7. Integration notes — TouchDesigner

**Tier: Lead / bench-derived.** TouchDesigner operator behavior is documented in `creative-coding/references/touchdesigner-integration.md`; only the X-Touch-specific consequences are here.

- **MIDI In DAT reports 1-based indices (1–128).** Raw CC *n* from the hardware appears as index *n+1*. This bites every time.
- **Prefer MIDI In CHOP over MIDI In Map CHOP** when the hardware assignments are already deliberate — the mapper's s1/b1 indirection creates a second mapping table to maintain.
- **Capture ground truth first.** MIDI In DAT with Bytes Column enabled, touch every control, record actual message/channel/index/value. Do not trust a decoded preset file or these tables alone for control→number identity.
- **Encoder mode matters** — relative vs. absolute changes how you integrate the value. Verify per encoder.
- **Feedback requires MIDI Out CHOP** for motors, rings and LEDs.

### Layer A `.bin` preset decode

**Superseded 2026-08-04.** A full decode from paired Layer A/B exports is in
`xtouch-compact-midi-map.md`, along with a working parser. It establishes the record layout,
that `0x12` in the channel byte means **channel Off** (which is what the prefix block below
actually was), that byte 3 carries encoder mode and byte 5 push behaviour. The reading below
predates it and is kept for history.

**Tier: Lead.** A 723-byte `LayerA.bin` export was parsed as 91 fixed-width records in 7 blocks: 9 fader CCs; 16 encoder CCs across two rows (mode bytes `0x01` and `0x04`); 55 notes for buttons and encoder pushes; 2 CCs for the foot jacks; and 9 CCs carrying an anomalous `0x12` prefix of unknown purpose.

Two things the file did **not** reveal:
- **Per-control MIDI channel.** No field varies in a way that encodes it — likely a global device setting stored elsewhere.
- **Control→record identity.** Inferred from count arithmetic, not from a format spec.

This is a reverse-engineered read of an undocumented format. Verify empirically before trusting it.

---

## Open items

- RX button-LED numbering under Layer B (§5) — Layer A confirmed 2026-08-04.
- Whether button LED velocities 4–127 are ignored (§5a).
- Whether Program Change bank switching works in practice (§5a) — documented, untested.
- Why fader touch on a shared channel corrupts the fader's own CC (§5a).
- What decides `.bin` record length, and where encoder ring mode is stored (§7).
- Whether the Speed-fader feedback gap is a Resolume bug or a mapping error (§6).
