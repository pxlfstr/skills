# Behringer X-Touch Compact

USB/MIDI control surface. Device facts, complete factory MIDI maps, and the receive-side (feedback) map.

**Primary source:** *X-Touch Compact Quick Start Guide, V 6.0* (Music Tribe, 2024) `[Official]` — read directly. Everything in §1–§5 is **Verified** from that document unless tagged otherwise.

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

> ⚠️ **Open item — unverified.** The RX button-LED table is printed as fixed notes 0–38 on the global channel, with no per-layer variant shown. In Layer A those numbers coincide with the transmit map; in Layer B the transmit notes are 71+ while the RX table still reads 0–38. The manual does not state whether RX feedback re-numbers per layer. **Bench-test before relying on Layer B LED feedback.**

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

**Tier: Lead.** A 723-byte `LayerA.bin` export was parsed as 91 fixed-width records in 7 blocks: 9 fader CCs; 16 encoder CCs across two rows (mode bytes `0x01` and `0x04`); 55 notes for buttons and encoder pushes; 2 CCs for the foot jacks; and 9 CCs carrying an anomalous `0x12` prefix of unknown purpose.

Two things the file did **not** reveal:
- **Per-control MIDI channel.** No field varies in a way that encodes it — likely a global device setting stored elsewhere.
- **Control→record identity.** Inferred from count arithmetic, not from a format spec.

This is a reverse-engineered read of an undocumented format. Verify empirically before trusting it.

---

## Open items

- RX button-LED numbering under Layer B (§5).
- Purpose of the `0x12` prefix block in the Layer A preset file (§7).
- Where per-control MIDI channel is actually stored.
- Whether the Speed-fader feedback gap is a Resolume bug or a mapping error (§6).
