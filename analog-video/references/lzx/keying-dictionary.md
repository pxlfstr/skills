# LZX Keying Dictionary

Source: LZX community "A Keying Dictionary" (Lars Larsen). Disambiguates "key" terminology across LZX's history and classifies each module's keying role. Pairs with `functional-map.md` (keying section) and `cadet-circuits.md` (LM361 comparator = hard key).

## Terms

- **Key** — any video signal used to control a transition between two+ other signals. *Any* signal patched to a key input becomes a key.
  - **Hard key** — a boolean logic signal that switches between sources.
  - **Soft key** — an analog voltage representing the mix ratio between two sources.
- **Key generator** — a module that conditions an input for keying.
  - **Hard key generator** — typically a differential analog **comparator**.
  - **Soft key generator** — typically a **high-gain differential amplifier with black/white level clipping**.
  - **Chroma key generator** — acts on chroma (Pb/Pr); keys on hue & saturation.
  - **Luma key generator** — acts on luma (Y); keys on brightness.
  - **Component key generator** — acts on one color channel but includes the whole colorspace (e.g. a red key fires where red appears without green/blue).
  - **Multi-level key generator** — many keys from one source; front-end for colorizers/sequencers.
  - **Window key generator** — dual thresholds, either Upper/Lower or Span/Center.
- **Fader / switcher** — performs the transition between two sources; usually a direct key input with little local key control.
- **Keyer** — has **both a key generator and a fader** (key-gen output drives the fader).
- **Linear colorizer / multi-level keyer** — multiple faders + a multi-level key generator → transition across more than two inputs. Static color offsets on the inputs = colorizer; video sources = sequencer/compositor.

Relations: a keyer = key generator + fader. Keying is always fading, but fading isn't always keying.

## Module classification (across series)

| Module (series) | Keying role |
|---|---|
| Triple Video Fader & Key Gen (Visionary) | triple hard key gen + triple fader; can act as a single RGB hard keyer |
| Cadet VIII Hard Key (Cadet) | single hard key generator |
| Keychain (Gen3) | triple hard key generator |
| Doorway (Expedition) | single **soft** keyer |
| FKG3 (Gen3) | single RGB/Luma **soft** keyer |
| Topogram (Expedition) | five-band **multi-level** key generator |
| Polar Fringe (Expedition) | soft **chroma** key generator |
| Visual Cortex (Expedition) | integrated single hard keyer / output encoder |
| Memory Palace (Orion) | discrete digital **soft window** keyer |

## Circuit notes (for DIY / understanding)

- **Soft key generator** (Lars's preferred topology): VCA block → multiple op-amp gain stages in series, ~4–5× each, a couple stages → ~25× total for a decently hard edge (this is roughly where Topogram sits). The **Cadet II RGB Encoder** is a good reference for a precision black/white clipping circuit.
- **Window key (Span/Center) math:** Upper Threshold = Center + (Span / 2); Lower Threshold = Center − (Span / 2).
