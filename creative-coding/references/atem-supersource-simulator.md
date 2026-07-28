# ATEM SuperSource Simulator — a single-file compositing planner

A standalone HTML tool that reproduces the ATEM SuperSource palette and renders
what the composite will actually look like, so a layout can be built and its
numbers read off before anyone is in front of the switcher.

**All vendor facts are cited across to
`digital-video/references/atem-supersource.md` and are not restated here.** That
document owns the unit space, the parameter names, the XML schema and the list of
what Blackmagic does and does not document. This one owns how we built the thing
and what we learned doing it.

---

## Confidence

| Component | Tier | Note |
|---|---|---|
| Position and size rendering | **Bench-verified** | Geometry probed numerically in headless Chrome; matches the one verified preset in the digital-video doc |
| Border ring rendering | **Bench-verified** | Ring bounds probed on all four sides |
| Foreground art keying | **Bench-verified** | Composites and suppresses correctly; the *curve* is Designed, see below |
| XML import / export | **Bench-verified** | Round-tripped against a real switcher's saved state; export matches the source schema attribute for attribute |
| Pixel-domain editing | **Bench-verified** | Typed values land exactly where reachable, and snap predictably where not; checked at 1080p, 720p, UHD, DCI 2K/4K, 8K and a custom raster |
| ATEM-step quantisation | **Bench-verified** as behaviour, **Designed** as a premise | Rounds to the palette's two decimals. That the switcher accepts nothing finer is an assumption |
| **Crop model** | **Designed** | Our assumption about what crop means. Never tested against a switcher |
| **Clip/gain key curve** | **Designed** | A soft threshold we invented. Not ATEM's math |
| **Control ranges** (`RANGES`) | **Designed** | Invented end-stops; the vendor documents none |
| Whole tool vs. a real SuperSource output | **Not tested** | Nobody has put this side by side with a switcher yet |

The honest summary: the tool is verified to be *self-consistent and correct
against the one preset Blackmagic published*. It is not verified to match a
switcher. Until someone does that comparison, treat its output as a planning aid,
not as truth.

---

## Architecture

Single `.html` file, no dependencies, no build, opens from the filesystem.
Chosen because these tools get emailed to people and opened on show laptops that
will not have a toolchain.

- **One flat `state` object** — four box records, an art record, a border record,
  a selection index. **State is held in ATEM units, not pixels**, because units
  are what the switcher and the saved XML speak; keeping the file format's own
  representation canonical means no drift accumulates through repeated edits.
- **Pixels are the editing surface, units are the readout.** Every spatial
  control converts px → units on the way in and units → px on the way out, at
  the control rather than in the model. Raster origin top-left, and Position is
  the box's *top-left corner* — the corner that maps 1:1 onto the ATEM X/Y
  parameters — with the post-crop visible rectangle reported separately.
- **Render on change, not on a frame clock.** A compositor with no motion has no
  reason to run a `requestAnimationFrame` loop. Every mutation calls `render()`.
  This is what makes the per-pixel keying affordable.
- **`syncers` array.** Each control registers a closure that pushes state back
  into the DOM. `syncAll()` runs them all. Avoids the usual mess where dragging
  a box updates the canvas but not the number field beside it.
- **`bindPxSlider(range, number, get, set, bounds)`** pairs a range input with a
  text input over a *derived* pixel quantity. Bounds are a callback rather than a
  constant because they depend on the current raster and box size, and are
  recomputed on every sync.
- **Resizing anchors the top-left corner.** Type a width and the box grows to the
  right. ATEM's Size is centre-anchored, so the binder re-applies the stored
  top-left afterwards.
- **Canvas at output resolution** (1920 × 1080 internally), CSS-scaled to fit.
  Means the exported PNG is a real 1080p frame, not a screenshot of a widget.

### Rendering order

Art background → Box 4 → Box 3 → Box 2 → Box 1 → foreground art → overlays.
Back-to-front, matching the layer order recorded in the digital-video doc.

### Border ring

Drawn as **one path with two rectangles**: the outer rect wound normally, the
inner rect wound backwards by passing a negative width. Under the default
nonzero fill rule that punches the hole, giving the ring in a single `fill()`.
The box image is then drawn clipped to the inner rect, so the ring is never
overdrawn and the fill edge stays crisp.

Cheaper and cleaner than the obvious alternative of stroking four sides, which
gets fiddly once the six independent widths in the per-box border model are in
play.

### Foreground art keying

Offscreen canvas. Draw the fill, `getImageData`. Draw the key over it,
`getImageData` again. Walk the buffer writing the computed alpha into every
fourth byte, `putImageData`, then `drawImage` the result over the composite.

A full-raster pixel loop is roughly two million iterations — completely fine
because it only runs when something changes. If this ever needs to animate, it
becomes a shader.

### Quantisation, and admitting what is unreachable

ATEM's palette shows two decimals, so a "Quantize to ATEM steps" toggle rounds
every derived unit value to 0.01. At 1080p that is a **0.6 px grid for position
and a 19.2 × 10.8 px grid for size** — so a great many pixel values simply cannot
be reached, and a typed 137 comes back as 136.8.

Rather than hide that, fields turn amber when a value cannot land on a whole
pixel, and the toggle can be switched off to see ideal geometry instead of
reachable geometry. **That the switcher accepts nothing finer than 0.01 is an
assumption** — the displayed precision is all we have. If it turns out to accept
more, one constant in `RANGES` changes and the whole grid loosens.

The general point: when a tool sits on top of hardware with a coarser input
resolution than the units the user thinks in, showing the *requested* value is a
lie. Show what you will actually get, and mark it.

### The assumption surface

**The pattern worth reusing.** Every value we could not verify lives in one named
block at the top of the script — `RANGES` and `keyAlpha()` — with a comment
saying explicitly what is verified, what is assumed, and where the verified
material came from. Correcting the tool when the real numbers arrive is one edit
in one place, not an archaeology exercise through eight hundred lines.

The alternative — scattering plausible constants through the render code — is how
a guess quietly becomes a fact three months later. Given how much of this
parameter space Blackmagic leaves undocumented, the assumption surface *is* the
design.

---

## Verifying canvas output: probe it, don't look at it

The reusable method from this build.

Headless Chrome via Playwright, using the browser already on the box:

```python
b = pw.chromium.launch(executable_path='/opt/google/chrome/chrome',
                       args=['--no-sandbox'])
```

Then drive and interrogate the page in its own scope. Because the tool's internal
functions are top-level, `page.evaluate()` can call them directly:

```python
pg.evaluate("()=>{const b=state.boxes[0]; b.cropLeft=8; syncAll(); render();}")
pg.evaluate("()=>boxGeom(state.boxes[0])")          # geometry, not pixels
pg.evaluate("""()=>{const c=document.getElementById('cv'), g=c.getContext('2d');
  const at=(X,Y)=>{const x=(X+16)*(c.width/32), y=(9-Y)*(c.height/18);
    const d=g.getImageData(Math.round(x),Math.round(y),1,1).data;
    return [d[0],d[1],d[2]];};
  return at(-7.0, 0);}""")                           # sample in *unit* coords
```

Sampling in unit coordinates rather than pixels is what makes the assertions
readable — you probe "just outside the left edge of the box," not "pixel 246."

This caught real problems and, more importantly, produced numbers that could be
checked against the vendor values by hand. A screenshot cannot do that.

### The trap that cost three rounds

Three separate "bugs" that were all bad test isolation, not code:

1. **Sampled outside the canvas.** The box under test was flush to the frame
   edge, so the probe point sat at a negative coordinate. `getImageData` returns
   zeros there — read as "the border is missing."
2. **Sampled a point covered by a different box's border.** Adjacent boxes were
   still enabled. Read as "the border is bleeding across the frame."
3. **Tested the border with art in foreground**, where the border is *correctly*
   suppressed. Read as "the border stopped drawing."

**The rule that came out of it:** before probing a canvas, disable every other
element, move the object under test away from the raster edge, and write down the
expected value *before* sampling. A pixel probe with an unstated expectation is
just a number, and a number will happily confirm whatever you already believed.

Worth generalising past this project — it applies to any visual output being
checked programmatically.

---

## What the tool does

- Full palette: four preset layouts, per-box enable / source / X / Y / size /
  crop, art fill and key with background-or-foreground placement, pre-multiplied
  and clip/gain keying, invert, the per-box border model, box-to-box copy.
- Direct manipulation on the preview — drag to move, wheel to size, number keys
  to select, arrows to nudge, shift to snap to centre.
- **Pixel-first editing** against any output raster including custom: Position as
  Left/Top in pixels from the raster's top-left, Size as Width/Height in pixels,
  Crop in **source** pixels removed from the incoming feed. The ATEM values to
  type into the palette are the reference readout, with a copy button.
- **Drawn-rectangle readout** giving the post-crop rectangle, screen-space crop,
  border extents and any off-raster overhang.
- Loads a real ATEM saved-state XML: takes the source names and the SuperSource
  block. Exports a `<SuperSources>` block that can be pasted back.
- Exports the composite as a PNG at output resolution, and the whole state as
  JSON.
- Sources without an assigned image render as generated placeholder cards
  carrying the source name, so the tool is useful with no assets at all.

Implements the **flat per-box border model only**. The bevelled
whole-SuperSource model in the SDK is not implemented — see the digital-video
doc for the distinction.

---

## Open items

1. **Never compared against a switcher.** The one test that would move most of
   this from Designed to Verified: build a layout on a real SuperSource, save the
   XML, load it into the tool, and put the two outputs side by side.
2. **Crop model unconfirmed.** We treat crop as full-frame units taken off the
   source, scaling with box size. The digital-video doc carries the thirty-second
   switcher test that settles it.
3. **Key curve is invented.** `keyAlpha()` is a soft threshold, chosen because it
   behaves sensibly, not because it matches ATEM.
4. **`RANGES` are invented.** Every end-stop in the tool is a guess.
5. **Presets 1–3 are traced from a thumbnail.** Only the quad has real numbers.
6. **Stills only** — no video or NDI sources. Fine for layout, useless for
   judging motion or a moving key.
7. **One SuperSource.** Switchers with two are not represented.
8. **No bevel/softness border model.**
9. **The 0.01 quantisation step is assumed from displayed precision**, not from
   anything documented or measured. It sets the entire reachable grid.
