# Behringer X-Touch Compact → Resolume (Avenue / Arena)

Device config and mapping protocol for using the X-Touch Compact as a
control surface for Resolume. Covers mode selection, X-Touch Editor
settings, Resolume-side MIDI setup, and known failure modes.

---

## 1. Operating mode — the decision that gates everything

Run the unit in **Standard MIDI mode**, not MC (Mackie Control) mode.

| Mode | What it emits | Resolume result |
|---|---|---|
| Standard | Plain Note + CC on MIDI ch 1 | Fully MIDI-learnable — use this |
| MC (Mackie Control) | Mackie/HUI control protocol | Not freely mappable — avoid |

**Setting it:** hold the **MC button (bottom-left corner)** while switching
the unit's power on. Hold until the MC MODE LED lights solid = now in MC.
Repeat the procedure to toggle back. **MC MODE LED off = Standard mode.**
Source: *X-TOUCH COMPACT Universal USB-MIDI Controller User Guide* [Official];
corroborated by *How do I change between Mackie Control and Standard Operating
mode on my Behringer X-Touch Compact?* (Sweetwater SweetCare) [Official].

**On-the-fly alternative:** send **CC127 on the global MIDI channel** to the
unit's MIDI In — value `0` = Standard mode (MC LED off), value `1` = MC mode
(MC LED on); values 2–127 are ignored. Useful for automated mode flips;
unnecessary for a fixed show setup. **Verified** against the RX MIDI DATA
table, *X-TOUCH COMPACT Quick Start Guide* p. 32 [Official], read first-hand.
(Previously carried as a Lead from a forum quote; the manual confirms it.)

⚠️ Do not confuse with the full-size **X-Touch** (non-Compact), which uses a
different procedure (hold Channel 1 SELECT while powering on, then encoder 1
selects HUI/MC, encoder 2 selects USB vs MIDI connection). The Compact does
not support HUI. Source: *How do I switch into Mackie Control mode on my
Behringer X-Touch* / *X-Touch Getting Started* (Sweetwater) [Official].

---

## 2. Native Standard-mode message layout

In Standard mode the factory presets are already what Resolume wants —
minimal re-authoring needed in the X-Touch Editor.

| Control | Message type |
|---|---|
| Fader movement | CC |
| Encoder rotation | CC |
| Fader touch (capacitive) | CC (separate from movement) |
| Foot switch / expression pedal | CC |
| Button press | Note |
| Encoder push | Note |

Both preset layers **A ("Mixer Control")** and **B ("Instrument Control")**
transmit on **MIDI channel 1**, using different note/CC numbers.
Source: *X-TOUCH COMPACT User Guide* [Official].

Hardware: 39 illuminated buttons, 16 rotary push-encoders, 9 touch-sensitive
motorized 100 mm faders. Class-compliant USB MIDI, no driver required.
Editor software is **Windows-only**. Source: *X-TOUCH COMPACT User Guide*
[Official]; Windows-only editor per *X-Touch Getting Started* (Sweetwater)
[Official].

### Why Notes for buttons, CC for faders

Not a preference — a type match.

- A **Note** is a discrete event with a clean press edge (note-on) and
  release edge (note-off / velocity 0). That is exactly a button's two
  states, and it is what Resolume reads as a trigger/toggle target.
- A **CC** is a continuous 0–127 stream — required for anything with a
  range (opacity, blur, speed, crossfade).

Resolume does offer a **Button** mode for CC shortcuts, for controllers that
emit CC on button press (e.g. Korg NanoKontrol series). Source: *Assigning
MIDI Shortcuts* (Resolume support docs) [Official]. It is a fallback for
hardware without Note output — not preferable here, because CC-as-button
depends on the controller sending both a press value and a release value,
whereas note-off is unambiguous.

Rule of thumb: **discrete → Note, continuous → CC.** Leave the X-Touch
transmit defaults alone.

⚠️ **Correction:** an earlier version of this document claimed button LED
feedback rides cleanly on Resolume echoing the note back. That is **wrong** —
see §4a. The LED map is separate from the transmit map and velocity-gated.

---

## 3. X-Touch Editor — the two edits worth making

Defaults are broadly correct. Change only these:

1. **Resolve the fader-touch CC collision.** Each motorized fader emits a
   *separate* CC when touched. During MIDI-learn, Resolume frequently latches
   onto the touch-CC rather than the movement-CC; the mapped parameter then
   jumps between extremes instead of sliding. Two fixes:
   - In the Editor, move each fader's **touch** CC to a channel/number range
     that will never be mapped, **or**
   - Map the fader while moving it with tape or a sleeve so the capacitive
     sensor never fires. (A third workaround: duplicate the Resolume shortcut
     onto the touch CC.)

   Source: *Resolume with Behringer XTouch Compact* (Resolume forum) [Forum].
   Behavioural lead, confirmed by multiple users; verify on the unit.

2. **Set buttons to Momentary**, and let Resolume drive the LED via MIDI
   feedback rather than a local hardware toggle. The LED then reflects
   Resolume's actual state, and stays correct when the same clip/parameter is
   triggered from elsewhere (mouse, Companion, timeline). Tier: **Memory /
   working practice** — not drawn from a manufacturer doc.

---

## 4. Resolume-side setup

- **Preferences → MIDI:** enable **both MIDI Input and MIDI Output** for the
  X-Touch Compact. MIDI Output is what drives the motor faders, encoder LED
  rings, and button LEDs. When Input Device and Output Device are the same
  device, Resolume sets the Output routing automatically.
  Source: *Assigning MIDI Shortcuts* (Resolume support docs) [Official].

- **Map CC shortcuts in Absolute mode.** Absolute maps the full travel of the
  fader/encoder to the full range of the parameter, and is the documented
  choice for standard (non-endless) controllers. Invert and Range options are
  available per shortcut. Other CC modes: Button, Relative, Fake Relative.
  Source: *Assigning MIDI Shortcuts* [Official].

- **Feedback routing:** a shortcut created on a given device defaults to
  sending feedback only to that device, so one controller's mapping does not
  disturb another's LEDs. The Output dropdown can be retargeted to a different
  device, to **All Devices**, or disabled entirely per shortcut — worth
  disabling when several shortcuts drive the same function.
  Source: *Assigning MIDI Shortcuts* [Official].

- **Shortcut targeting** (affects how feedback behaves on re-order):
  Layer Opacity and similar default to **By Position**, so fader 1 follows
  whatever layer sits first regardless of re-ordering. Other targets bind to a
  *specific* clip/layer/group (shortcut dies with the object) or to
  *selected*. Source: *Assigning MIDI Shortcuts* [Official].

---

## 4a. LED feedback — the RX MIDI map (why button LEDs don't respond)

Everything in this section is from the **RX MIDI DATA table, Quick Start Guide
p. 32** [Official] — read first-hand. This is the authoritative answer to
"Resolume feedback moves my faders but won't light my buttons."

Inbound LED/remote control is a **separate map from the transmit map**, and it
listens on the **GLOBAL channel** — not necessarily the layer's channel.

### Buttons LED Remote Control — velocity-gated

⚠️ **The manual's table does not match observed hardware.** Bench-tested via
TouchDesigner raw MIDI `send()` (exact bytes, no host-side rescaling):

| Velocity | Manual p.32 claims | **Observed on hardware** |
|---|---|---|
| 0 | LED off | not yet determined |
| 1 | LED on | **LED off** |
| 2 | LED blinking | **LED on** |
| 3 | ignored | **LED blinking** |
| 4–127 | ignored | presumed ignored, not yet confirmed |

The whole table is shifted up by one relative to the documentation. Use the
**observed** values. Cause not established — could be a documentation error,
a firmware revision difference, or a numbering-convention mismatch in how
Behringer wrote the table.

A conventional echo at velocity 127 is still discarded either way, so the
core point stands: naive note echo cannot drive these LEDs, and a host-side
velocity rewrite is mandatory.

**Epistemic note:** this table was previously recorded here as Verified
[Official], read first-hand from the manufacturer's manual, and it was still
wrong. Official documentation means *documented*, not *correct*. Bench
observation outranks it.

### Button LED note numbers ≠ button transmit note numbers

| Button block (of the 39 illuminated) | LED **RX** note | Layer A **TX** note | Layer B **TX** note |
|---|---|---|---|
| 3×8 top row (1–8) | 0–7 | 16–23 | 71–78 |
| 3×8 mid row (9–16) | 8–15 | 24–31 | 79–86 |
| 3×8 bottom row (17–24) | 16–23 | 32–39 | 87–94 |
| Lower row of 9 (25–33) | 24–32 | 40–48 | 95–103 |
| Right/transport area (34–39) | 33–38 | 49–54 | 104–109 |

Derived rule: **LED note = Layer A TX note − 16**, or **Layer B TX note − 71**.
Echoing a Layer A button at its own note lights a button 16 positions away;
echoing a Layer B button sends notes ≥71, entirely outside the 0–38 LED range.

The 39 illuminated buttons = 24 (3×8 block) + 9 (lower row) + 6 (transport).
Encoder pushes are **not illuminated** and have no LED map. The Layer A/B LEDs
are **not assignable** — exactly one of the two lights, per the selected layer.

### Why faders work and encoder rings don't

| Function | RX (inbound) | TX (outbound) | Straight echo works? |
|---|---|---|---|
| Fader position | CC1–CC9 | CC1–CC9 | **Yes** — symmetric |
| Button LED | Note 0–38, vel 2=on/3=blink (observed) | Note 16–54 (A), vel 127/0 | No |
| Encoder ring value | CC26–CC33 (enc 1–8), CC34–CC41 (enc 9–16) | CC10–CC25 (rotation) | No |

The fader map is the only symmetric one. This is the mechanism behind the
community-reported stale encoder-ring LEDs — it is a map mismatch, not a bug.

### Other inbound control (all GLOBAL CH)

| Function | Message | Values |
|---|---|---|
| Operation Mode Select | **CC127** | 0 = Standard (MC LED off), 1 = MC (MC LED on), 2–127 ignored |
| Preset Layer Change | **Program Change** | 0 = Layer A, 1 = Layer B, 2–127 ignored. **Standard mode only** |
| Fader movement | CC1–CC9 | 0–127 = position, bottom to top |
| LED ring **behaviour** | CC10–CC17 (enc 1–8), CC18–CC25 (enc 9–16) | 0 Single, 1 Pan, 2 Fan, 3 Spread, 4 Trim, 5–127 ignored |
| LED ring **value** | CC26–CC33, CC34–CC41 | 0 all off; 1–13 LEDs 1(left)–13(right) on; 14–26 same blinking; 27 all on; 28 all blinking; 29–127 ignored |
| Foot Switch LED | CC42 | 0–63 off, 64–127 on |
| Exp. Pedal LED | CC43 | on only during data transfer |

MC Mode / USB / MIDI I/O status LEDs are **not assignable**.

### Working around it

- **MIDI translator in the feedback path** (Bome, or a TouchDesigner /
  Companion middle layer between Resolume's MIDI out and the X-Touch's MIDI
  in): offset the note (−16 for Layer A, −71 for Layer B) and clamp velocity
  to 1 (on) / 0 (off). Solves both problems at once, covers both layers, and
  leaves the Resolume mappings untouched. Preferred.
- **Editor renumber**: reassign button TX notes to 0–38 so the echo lands on
  the correct button. Fixes numbering only — the velocity gate remains.
  Whether Resolume can be coaxed into emitting velocity 1 (via shortcut
  Range/Invert) is **untested**. Verify before relying on it.

**Bench test (30 seconds):** from any MIDI utility, send the X-Touch's MIDI
In note 0 velocity 1 on the global channel — top-left button should light.
The same note at velocity 127 should do nothing. Confirms both rules on the
actual unit.

---

## 5. Layer A / B banking

The A and B buttons are hardware preset layers on the controller, not
Resolume pages — effectively two controllers in one box. Map layer A in
Resolume, then map layer B; the different note/CC numbers keep them distinct.
Because the faders are motorized, **positions re-seat correctly on every A↔B
flip** — the main argument for this unit over a non-motorized fader box.

Suggested split for VJ use: **A** = layer opacities, master, crossfader;
**B** = effect parameters, clip/column triggers.

Source: *MIDI refresh shortcut* (Resolume forum) [Forum] — behaviour reported
by users, consistent with the manual's description of the A/B preset layers
[Official].

Note: the **X-Touch Mini** has the same A/B paging but non-motorized controls,
and users report Resolume does not re-push values on page change, so the
knob-ring LEDs go stale until touched. Workaround discussed: a Bomes patch
that nudges every value up and back down (~1 ms) to force a MIDI-out refresh.
Source: *MIDI refresh shortcut* (Resolume forum) [Forum].

---

## 6. Known limitations / gotchas

- **Layer Speed does not send feedback on clip change.** With a motorized
  fader mapped (Absolute) to a layer's Speed ("S") slider, triggering a new
  clip resets layer speed but sends no MIDI feedback — the fader stays at the
  old position until the UI control is nudged. Same for encoder ring LEDs.
  Play mode, trigger mode, play backwards/forwards, pause, and the timeline
  *do* send feedback on clip change. Reported as likely a bug.
  Source: *MIDI feedback for layer-mapped clip parameters* (Resolume forum)
  [Forum] — user-tested, longstanding; treat as Lead, retest on current build.

- **MC mode blocks the B layer.** In MC mode the A/B layer buttons do not
  provide the Standard-mode banking. Source: *Behringer X-Touch Compact CC
  control* (VI-Control) [Forum].

- **In Standard/MIDI mode the faders do not move under MC control** — motor
  movement comes from Resolume's MIDI Output feedback, not from Mackie
  protocol. Source: same [Forum]; consistent with Resolume docs [Official].

- **Firmware updates for the Compact are done via the Editor app, Windows
  only** (unlike the full-size X-Touch, which uses a SysEx file on PC or Mac).
  Firmware version displays briefly at power-on. Source: *X-Touch Getting
  Started* (Sweetwater) [Official].

---

## Verification status

| Claim class | Tier |
|---|---|
| Mode-switch procedure (MC button + power-on) | Verified [Official] |
| Standard-mode Note/CC layout, A/B layers, ch 1 | Verified [Official] |
| Hardware counts, class-compliant USB, Windows-only editor | Verified [Official] |
| Resolume MIDI In/Out, Absolute mode, feedback routing, shortcut targets | Verified [Official] |
| CC127 mode toggle | **Verified [Official]** — promoted from Lead by the manual's RX MIDI table |
| Full per-control TX maps, layers A and B and MC | **Verified [Official]** — manual pp. 29–31 |
| LED note map, ring CC map, PC layer change | **Verified [Official]** — manual p. 32, read first-hand |
| Button LED velocity values | **Bench-observed — CONTRADICTS the manual.** Real values are 1=off, 2=on, 3=blink |
| Raw `send()` bypasses TD MIDI Out CHOP normalize / one-based-index params | **Bench-observed** — changing those params had no effect on the wire |
| Button transmit velocity: 127 press, 0 release | **Bench-observed** |
| Layer A/B buttons transmit nothing (local-only) | **Bench-observed** — confirms the manual's diagram, which prints no number for them |
| Fader touch CC101–109, 127 on touch / 0 on release | **Bench-observed** — but touch-on LAGS first movement by ~2–9 frames |
| Fader-touch CC collision | Lead [Forum] — multi-user, behavioural |
| Layer Speed feedback gap | Lead [Forum] — user-tested, retest on current build |
| Whether Resolume can emit velocity 1 for LED-on | **Open** — untested, blocks the Editor-renumber workaround |
| Momentary button practice | Working practice, not doc-sourced |

**Corrected this pass:** the earlier claim that Resolume's note echo lights the
button LEDs. It does not — the LED map is separate from the transmit map and
gated to velocity 1/2. See §4a. The claim was a working assumption, not
doc-sourced, and should not have been stated as flatly as it was.

**Not yet verified — open items for next pass:** what velocity 0 does to a
button LED, and whether the ignored band is now 4–127; whether the same +1
shift affects the encoder ring value table (CC26–41) and the foot switch LED
(CC42); whether Resolume's shortcut Range/Invert can produce the required
velocity on feedback output; whether the Editor
exposes a direct disable for fader-touch CC output; the exact global-channel
default and where it is set in the Editor; current Resolume build behaviour on
the Speed feedback gap.
