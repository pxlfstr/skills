# TouchDesigner — POPs for Depth-Derived 3D Geometry

## Provenance

Mixed tiers, kept distinct below and per-operator in the reference section. `[Official]` lines are read from the current Derivative wiki (docs.derivative.ca), each cited with its own last-edited date. `Bench-verified` lines are the user's own direct observations this session, built on TouchDesigner 2025.33070 (July 16, 2026 release). `Designed`/reasoned lines are explicitly marked — several early conclusions in this session were revised or reversed once the user checked their actual node graph against a third-party example, and those corrections are preserved here rather than silently replaced, per the additive/non-lossy rule. **Full pages read this session:** TOP to POP, Neighbor POP, Ray POP, Proximity POP. **Not read — every other POP named this session is marked `# UNVERIFIED` in the per-operator reference section below**, including Connectivity, Normal, Math Combine, Math Mix, Lookup Attribute (snippet only), Trail, Feedback, Copy, Quantize, Force Radial, Script (covered only via a third-party build-changelog article, not its own doc page), Sprinkle, and Point Generator. Python class references for any POP were never read. The example patch's actual `.toe` file was described verbally by the user, not opened by Claude. Open contradiction preserved: whether Connectivity POP can build usable triangle/quad structure from Proximity's line output was asserted true by the user (correcting an earlier wrong claim by Claude) but never independently confirmed against documentation — flagged in place in the per-operator section.

**Depends on:** `patterns/touchdesigner-TDDepthAnything.md` for the depth TOP this whole chain consumes; not restated here.

---

## Per-operator reference

Every POP named this session, with its confirmation status. `[Official, read]` = the operator's own docs.derivative.ca page was opened and is cited. `# UNVERIFIED` = discussed or named this session from memory/inference only — page never opened, per Rule 5 do not treat as confirmed.

### TOP to POP `[Official, read]`
See dedicated section above.

### Neighbor POP `[Official, read]`
See dedicated section above (Bench-verified tuning) plus doc citation there.

### Ray POP `[Official, read]`
See dedicated section above.

### Proximity POP `[Official, read]`
Source: docs.derivative.ca/Proximity_POP, last edited 2025-10-28, oldid=36620.

Connects points to nearby points in its **own** first input, within a Min/Max Distance window — this is the key difference from Neighbor POP: Proximity does its own independent spatial search (own `Num Hash Buckets`, same "close to point count" heuristic), it does not consume Neighbor's `Nebr` output. If a second input is connected, it instead connects first-input points to in-range second-input points (cross-set proximity, not self-proximity).

**Output** menu: `Lines (Shared Points)` outputs actual 2-point line primitives (not line strips) between qualifying points — this is the operator for a visible connective-web look. `Point Prims` outputs just the qualifying points themselves, no connecting geometry.

Other parameters: **Max Lines per Point** caps connections per point (cost and visual density control); **Uniform Distribution** spreads selection more evenly among candidates rather than always picking the first found; **Duplicate Lines** (`Do Nothing` / `Avoid` / `Delete`) controls whether a pair of points can get more than one line between them; **Line Direction** / **Line Length** are optional output attributes on the line primitives; **End Point Attributes** (two-input mode only) copies the matched second-input point's own attributes onto the output as `EndP`/`EndN`/`EndTex` etc.

⚠️ **This session concluded Proximity POP alone outputs lines, not triangles/quads** — a separate step (Connectivity POP, `# UNVERIFIED` below) is needed to turn Proximity's line output into Ray-POP-compatible mesh primitives. Confirmed by this page: nothing on the Proximity page itself builds triangle/quad primitives.

### Connectivity POP `# UNVERIFIED`
Named and discussed this session; **its own docs page was never opened.** What's recorded here is inference plus the user's direct correction of an earlier wrong guess by Claude, not a doc citation:

- Claude's first guess (wrong, per the user): Connectivity POP only works on pre-structured grid data (e.g. Grid POP output) to decide row/column wiring into primitives.
- User's correction, asserted but not independently verified: Connectivity POP **can** take Proximity's line-connected point output and build triangle/quad primitives from it — used successfully this session as the step between Proximity and Normal POP in the Ray-collision chain.
- **Genuinely unknown:** whether the resulting mesh from proximity-derived connections is well-formed (consistent winding, non-degenerate) the way a true grid-based mesh would be. Flagged as a possible source of Ray POP artifacts (inconsistent hit directions, odd normals) — never checked.

### Normal POP `[Official, page not opened — only cross-referenced via POPs-vs-SOPs table and Learning About POPs]`
Confirmed via the POPs-vs-SOPs comparison table (docs.derivative.ca/Learning_About_POPs) as the POP-family replacement for SOPs' Attribute Create SOP / Facet SOP normal-generation role. **Its own dedicated parameter page was never opened this session** — the working understanding ("needs real triangle/quad structure to compute meaningful normals from, doesn't do anything useful on a bare point cloud") is inference from context and observed behavior (Ray Hit/Reflect failing without it), not read from Normal_POP's own page. Confirmed placement in the working chain: after mesh connectivity exists, before Ray POP's second input.

### Math Combine POP / Math Mix POP `# UNVERIFIED`
Named and discussed via the reference article's description (converting `RayHitNormal` → `P`, dividing Proximity/Noise `P` values → `color.rgb`) and via the build-2025.33070 changelog's confirmation that both POPs gained quaternion/rotation operations (`axisanglequat()`, quaternion×quaternion and quaternion×vector products, matrix multiplication) in the current build. **Neither operator's own parameter page was opened.** The article's specific attribute-conversion technique was never independently verified against documentation — only against the article's prose and the user's report of their own node's Ray Attribute being set to `P`.

### Lookup Attribute POP `[Official, page not opened — snippet only]`
A search-result snippet (not the full page) was read this session while trying to solve the `Nebr`-to-Ray-direction problem. Per that snippet: takes a **0–1 normalized value** as its lookup index into a second input's attributes (e.g. a Curve POP), or optionally a raw point-index if `Lookup Index Units` is set to `Point Index`. **This means it may actually be closer to a valid fit for resolving `Nebr` (integer point indices) than this session concluded** — the `Point Index Units` mode was never tested or even fully read before the session moved on to checking the reference patch directly. Left as a genuinely open alternative path, not ruled out.

### Trail POP `# UNVERIFIED`
Named twice this session — once as a technique for visualizing per-point motion history (time-history line strips per particle, per the "POPs vs SOPs" table's own description of it), once in the Notch-style effects brainstorm for a ghost/streaking look. **Page never opened.** Also noted (via the build-2025.33070 changelog, which *was* read) as having gained the ability to output tangent-normal-binormal frame orientation in that release — a real fact, but about a feature not used or tested this session.

### Feedback POP `# UNVERIFIED`
Named for two purposes this session: (1) general particle-motion integration (force → velocity → position accumulation over time, per the "POPs vs SOPs" table's own mention of it in that role) and (2) a proposed technique for depth-flicker temporal smoothing and for accumulating/decaying point history in a Notch-style disintegration effect. **Page never opened**, no parameters confirmed.

### Copy POP `# UNVERIFIED`
Named as an instancing option for a voxel/blocky look (small cube geometry copied to each depth point) and, separately, confirmed via the build-2025.33070 changelog (which was read) to have gained quaternion attribute support and a new "Template Rotate Attribute" parameter for quaternion-driven per-instance rotation. **Its core copy/instancing parameters were never read.**

### Quantize POP `# UNVERIFIED`
Named once, for snapping point positions to a grid as part of a voxel-block look. Never opened, never used.

### Force Radial POP `# UNVERIFIED`
Named once, for an outward-explosion particle effect from a center point (Notch-style disintegration brainstorm). Never opened, never used.

### Script POP `[Official, page not opened — covered via a build-changelog article, not the operator's own doc]`
Confirmed as a real, current operator via the build-2025.33070 changelog article (interactiveimmersive.io, read in full this session) — new in that release, allows Python-authored POP generation or filtering, can create points/any primitive type/any attribute type including arrays, and can set Dimension. The changelog's own example: copies input points, adds a new point on a Pulse triggered by a `timer1` CHOP's Done channel, clears added points via a `timer2` CHOP's Done channel. **Script_POP's own dedicated parameter page (docs.derivative.ca/Script_POP) was never opened.** Noted as a possible replacement for parts of the multi-operator Neighbor/Ray/Proximity/Connectivity chain via custom logic — not attempted.

### Sprinkle POP, Point Generator POP `# UNVERIFIED`
Both named only in passing (general point-cloud/particle-generation context, and Sprinkle POP's volume mode was mentioned once via the Hardware Ray Tracing page as another operator that supports acceleration structures alongside Ray POP). Neither used, neither page opened.

---

## `[Official]` TOP to POP — depth TOP → 3D points

Source: docs.derivative.ca/TOP_to_POP, last edited 2025-12-13, oldid=37076.

**First RGBA Contains → `Depth`** is the mode for converting a depth-map TOP into 3D point positions. TOP to POP does no depth estimation itself — it expects pixel values that are *already* depth data (that's Depth-Anything's job upstream) and does the reprojection math (2D pixel + depth value + camera FOV → XYZ position).

**Depth-mode parameters, all on the dedicated Depth page:**
- **Camera** — required; references a Camera COMP, defines the projection used to place points in 3D
- **Rerange from Low/High → Rerange to Low/High** — "from" is your depth TOP's actual input value range (Depth-Anything output observed this session: 0–1, normalized); "to" is the output range in real scene units. Leaving "to" at a small/default range compresses all depth into a thin Z-slice that can visually read as flat even when the data is real (Bench-verified as a live troubleshooting step this session, not yet confirmed as the actual cause of the "flat rectangle" issue below)
- **View Angle Method** — Horizontal FOV / Vertical FOV / Focal Lengths. Must match the actual optical FOV of the physical camera whose feed produced the depth TOP — this is a lens-and-sensor property, unrelated to whether the video signal path is analog-converted-to-digital or native digital
- **Delete Near/Far Points + Near/Far Depth** — built-in clipping for unreliable depth at range extremes

**Connectivity** (Detail page) sets primitive type directly from the depth TOP's inherent pixel grid — `None` / `Point Primitives` / `Lines` / `Line Strips` / `Triangles` / `Alternating Triangles` / `Quadrilaterals`. Setting `Quadrilaterals` here wires adjacent pixels into quads using row/column adjacency automatically — no downstream Proximity/Connectivity POP needed if grid-based mesh structure is all that's wanted. Tradeoff: a depth discontinuity between adjacent pixels (e.g. a hand in front of a torso) can produce a stretched connecting quad across the gap, since grid adjacency doesn't check actual 3D distance the way Proximity POP does.

**Channel Scope is greyed out in Depth mode** — Bench-verified this session. The operator already knows it wants one depth value per pixel in this mode, so manual RGBA channel selection isn't applicable. Not a bug.

## `[Official]` FOV estimation for a roaming performer camera, 5–20ft

No hard number exists without knowing the actual lens; FOV is a function of focal length **and** sensor size together, not focal length alone (shorter focal length or larger sensor → wider FOV; longer focal length or smaller sensor → narrower). For a broadcast/ENG-style zoom lens actively reframing full-body-to-mid-tight shots at 5–20ft, **30–50° horizontal FOV** is a reasonable estimate, landing near **40°** as a working default — reasoned from typical 24–50mm-equivalent zoom ranges for this kind of live coverage, not sourced from a spec sheet. **A single static FOV value will be wrong as the operator actually zooms** — the Camera COMP's FOV would need to be read live from lens/servo data and driven dynamically to stay correct through a zoom move. Not attempted this session.

**Cameras with different fixed focal lengths in the same rig need separate FOV values, not one shared estimate** — either per-camera Camera COMPs with matched FOV, or the active FOV driven dynamically by which camera is live (tally-derived), depending on whether cameras are switched or run simultaneously. User indicated they already have a plan for the tally-to-TouchDesigner path; not detailed in this session.

---

## `[Bench]` Point count and performance

Full 518×518 depth resolution ≈ 268,000 points — **too many for real-time Neighbor POP search**, observed as dropped frames this session. Fix: **Override Resolution on TOP to POP itself**, reduced to 256×256 (65,536 points) with **Filter: High Quality Resize** — resolved the frame drops. High Quality Resize gives better downsampling filtering than Nearest Pixel when cutting resolution this aggressively.

**Two point-count tiers emerged as a natural architecture**, not yet fully built out:
- Full/high resolution — for detail-preserving, per-point-independent effects (displacement, color-from-depth) that don't need relational search
- Low resolution (256×256 or below) — for relational/expensive effects (Neighbor, Ray-against-mesh, Proximity) with per-point search cost

⚠️ Whether 256×256 is a true ceiling or just the first value tried was left unresolved — user was advised to test scaling Num Hash Buckets proportionally with resolution to see if higher point counts become viable, not yet tried.

## `[Bench]` Neighbor POP tuning

Source for parameter definitions: docs.derivative.ca/Neighbor_POP, last edited 2026-08-07, oldid=38404.

- **Max Neighbors** default in this build observed as **5** — reasonable, was not the cause of frame drops
- **Num Hash Buckets** default in this build observed as **10000** against 65,536 points (~6-7 points/bucket) — reasonably close to the doc's own heuristic ("choose it to be close to the number of points"), also not the likely cause
- Conclusion: the frame-drop cause was most likely **raw point count alone** (268k+ at full resolution), not a misconfigured Neighbor parameter — both Max Neighbors and Hash Buckets were already near-sensible defaults before the resolution fix
- **Distribution** modes, by cost: `Default` (fastest, rare duplicates possible) → `Unique` (checks duplicates, still fast) → `Random` (unbiased sampling) → `Closest` (**slowest** — sorts all candidates by distance; avoid unless guaranteed-nearest is specifically required)

`Nebr` is an **array of integer point indices**, not a direction vector or a 0–1 normalized value — this distinction caused real confusion this session (see Ray POP section below).

## `[Official]` Ray POP — collision requirements, corrected understanding

Source: docs.derivative.ca/Ray_POP, last edited 2026-01-14, oldid=37146.

**Ray POP only accepts triangles/quads on its second input** — confirmed directly by the user against their own node ("Ray only supports triangles and quads"), matching the doc's own summary ("the set of triangles and quads that the rays are tested against"). **It cannot test rays against a raw point cloud or against other points via `Nebr` indices.** This closed a real wrong turn earlier in the session (see below).

**Ray Hit and Ray Reflect require surface normals on the collision geometry.** Without them, hit/reflect computation fails — the geometry has no defined surface orientation to compute against. **Normal POP** is the fix, but only produces meaningful output when the input already has real triangle/quad primitive structure — a raw point cloud (Point Primitives only) doesn't give Normal POP enough to compute from. Correct placement, confirmed working this session: **after** whatever step builds triangle/quad connectivity (Proximity → Connectivity, or TOP to POP's own `Quadrilaterals` Connectivity setting), **before** Ray POP's second input.

⚠️ Confirmed working chain, but with an unconfirmed detail: `TOP to POP → Proximity → Connectivity (builds triangles/quads) → Normal POP → Ray POP (input 2)`. **Whether Connectivity POP reliably produces clean, consistently-wound mesh structure from Proximity's distance-based line output — as opposed to a genuine row/column grid — was never verified.** The user asserted Connectivity POP does the triangle/quad conversion (correcting Claude's earlier wrong guess that it only worked on pre-structured grid data), but normal quality/consistency from a proximity-derived mesh was flagged as a possible source of artifacts (weird glints, inconsistent hit directions) and never actually checked.

## Real wrong turn this session, worth remembering: `Nebr` is not a Ray direction

Early in the session, Claude assumed `Nebr` (Neighbor POP's output — an array of neighbor point indices) could feed directly into Ray POP's **Ray Attribute** parameter, which expects a **direction vector**. This is a type mismatch: an index is not a direction. The presumed fix (some Lookup POP resolving index→direction) was never confirmed to exist for this specific case — Lookup Attribute POP's actual mechanism takes a **0–1 normalized value**, not a raw integer point-index array, so it doesn't obviously fit either.

**Resolved by checking the user's actual reference patch** (interactiveimmersive.io's "Creative Uses of POPs" example, https://interactiveimmersive.io/wp-content/uploads/2026/05/Creative-Uses-of-POPs-in-TouchDesigner.zip) rather than continuing to guess from documentation prose: in that patch, **Ray Attribute is set to `P`** (the point's own position), not anything derived from `Nebr`. `Nebr`/Proximity are a **separate branch** in that network, unrelated to what feeds Ray directly. **Neighbor and Ray are not a single linear pipeline** — this was an incorrect inference from the article's prose description, corrected once the user actually opened the patch.

**Lesson for next time a similar chain is being built from a tutorial's written description rather than its actual node graph: check the real wiring before assuming a prose-described sequence is a literal linear chain.** Article prose ("we connect X to Y to Z") can compress or omit parallel branches.

## `[Designed]` Composited-effect architecture, chosen this session

Given repeated difficulty getting a Ray/Noise-collision technique (built for texturing a static/generic shape) to preserve a *live depth-derived human silhouette*, the session concluded that technique is likely the wrong fit for this goal — texturing a generic sphere/grid is a different problem than stylizing a recognizable performer shape.

**Chosen alternative, not yet built:** split into two independent branches from the same depth TOP, composited back together in TOP-land rather than trying to preserve shape *inside* the POP chain:

```
Depth TOP ──┬──→ (clean silhouette path — original camera image, or a Threshold/Luma Key on the depth TOP as a matte)
            └──→ TOP to POP → [whatever POP effect, however extreme] → Render TOP
                                                    │
                                Composite TOP (Over / Screen / Add / Difference / Matte) → final output
```

This decouples "does the effect preserve shape" (no longer a constraint on the POP chain itself) from "does the final composite read as the performer" (handled entirely in 2D compositing afterward). Considered simpler and more flexible than in-POP-chain shape preservation via edge detection or weight-attribute masking, since it lets the POP effect branch be arbitrarily chaotic without needing to also behave.

**Simpler techniques identified as likely better first attempts than the Ray/Noise/collision chain, given today's difficulty:**
- Depth cloud → **Noise POP** or **Transform POP** directly on the cloud's own points (per-point displacement, no second geometry needed)
- Depth cloud → **Neighbor → Proximity** (Proximity's own line-output mode, not routed through Ray) for a connective-web look, without needing a collision mesh at all
- Depth cloud → **Trail POP** for motion-trail effects

None of these three were built or tested this session — Designed/reasoned only.

## `[Designed]` Troubleshooting a "flat wavy rectangle" result

Session ended mid-diagnosis. Confirmed: the wavy/noisy quality in the point cloud **is** real depth data (user confirmed directly), not a Noise POP artifact fighting the depth signal — this ruled out an earlier hypothesis. Left open: why the overall shape reads as a flat rectangle rather than a recognizable silhouette. Live hypotheses, none confirmed:
- Viewing the cloud face-on (down the same axis depth is pushed along) can visually compress real Z variation into looking flat — orbiting the viewport to a 3/4 or side angle was suggested as the fastest check
- Rerange to Low/High may be compressing real depth data into a Z range too small relative to the cloud's X/Y spread to read visually
- A person standing against a mostly-flat backdrop *will* produce a genuinely rectangular overall point cloud (person + background plane both contain valid depth) unless background depth is being masked out — the "rectangle" observation might be geometrically correct, not a bug

---

## Open items

Whether Connectivity POP produces clean/consistent normals-ready mesh structure from Proximity's proximity-based line output, as opposed to only working well on genuine grid-structured input — asserted by the user, never independently verified. Whether Num Hash Buckets scaling with resolution raises the real point-count ceiling for Neighbor POP past 256×256 — not tried. Whether the composited two-branch architecture (clean silhouette + separate POP effect layer) actually produces the intended look — not built this session. Root cause of the flat-rectangle appearance — left unresolved at session end, three hypotheses untested. Whether Script POP (new in build 2025.33070, confirmed present in the user's actual build) could replace some of this multi-operator chain with custom Python logic — noted as a possibility, never attempted. **Whether Lookup Attribute POP's `Point Index Units` mode is actually the correct way to resolve `Nebr`'s integer point indices into usable position/direction data** — surfaced late in this pass as a plausible alternative to the "Neighbor and Ray are unrelated branches" conclusion, never tested; the session's actual working chain (Ray Attribute = `P`) sidestepped the question rather than resolving it. Every operator marked `# UNVERIFIED` above needs its own doc page read before its parameters are used with confidence, per Rule 5 — none should be treated as more than named/discussed until then.
