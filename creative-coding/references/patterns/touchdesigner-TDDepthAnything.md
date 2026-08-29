# TouchDesigner — TDDepthAnythingRT

## Provenance

Bench-verified for setup, environment fixes, and one successful engine build/run this session. Repo: `jetXS/TDDepthAnythingRT` (fork of `olegchomp/TDDepthAnything`), README read in full via GitHub fetch this session — no oldid captured, page reflects the state at time of fetch (2026-08-29). Environment: TouchDesigner Build 2025.32820, Python 3.11.10, Windows, RTX A5500 Laptop GPU, driver 597.06 / CUDA 13.2. **Blur/Level pre-processing recommendations below are Designed only** — reasoned from TOP documentation and general video-noise principles, not yet tested against this pipeline's actual depth output. What was NOT read: the project's own Python source (`TDDepthAnythingRTExt`, `TDDepthAnythingRTAccelerate` DATs) beyond what appeared in error tracebacks; TDPyEnvManager's own documentation. No open contradictions.

**Depends on:**
- `patterns/touchdesigner-python-env-dependencies.md` for the general TDPyEnvManager/pip mechanics — not restated here.
- `protocols/nvidia-tensorrt-polygraphy.md` for the TensorRT FP16 version break and the 10.9.0.34 pin — not restated here.

---

## What the tool is

TouchDesigner implementation of Depth Anything V2 monocular depth estimation, accelerated via TensorRT, using TouchDesigner's own TDPyEnvManager (per-project isolated Python venv) and Thread Manager. Model source: HuggingFace (`depth-anything/Depth-Anything-V2-Small-hf` observed this session). Requires TouchDesigner 2025.32280+ per the README.

## requirements.txt — as shipped vs. working

**As shipped in the repo** (fetched this session):

```
tensorrt-cu12
--extra-index-url https://download.pytorch.org/whl/cu128
torch
torchaudio
torchvision
huggingface-hub
polygraphy
onnx
onnxscript
transformers
```

Every unpinned line above resolved to a broken or unwanted state this session — `tensorrt-cu12` to 11.2.1.2 (see `protocols/nvidia-tensorrt-polygraphy.md`), `torch` to a CPU-only build (see `patterns/touchdesigner-python-env-dependencies.md`), and `torchaudio` to a version that crashed on load (below). None of the three breakages were visible from the requirements.txt file itself — all surfaced only at runtime, in three separate steps of the install/build/run sequence.

**Working combination, bench-verified this session:**

```
tensorrt-cu12==10.9.0.34
--extra-index-url https://download.pytorch.org/whl/cu128
torch==2.11.0+cu128
torchvision==0.26.0+cu128
huggingface-hub
polygraphy
onnx
onnxscript
transformers
```

`torchaudio` removed entirely — see below.

## `torchaudio` is an unneeded transitive pull, and it crashes

`transformers`' `audio_utils.py` attempts `import torchaudio` as part of its own import chain, even though nothing in the depth-estimation pipeline uses audio. When `torchaudio`'s version doesn't match the installed `torch` build closely enough, its compiled `.pyd` extension fails to load:

```
FileNotFoundError: Could not find module '...\.venv\Lib\site-packages\torchaudio\lib\libtorchaudio.pyd' (or one of its dependencies).
...
OSError: Could not load this library: ...\torchaudio\lib\libtorchaudio.pyd
```

This surfaced as a **DAT compile error** on both `TDDepthAnythingRTAccelerate` and `TDDepthAnythingRTExt`, blocking the extension from loading at all — before any depth-estimation code ran.

**Fix — uninstall it, don't try to version-match it:**

```python
result = subprocess.run([r"<path-to-project>\.venv\Scripts\python.exe", "-m", "pip", "uninstall", "-y", "torchaudio"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
```

`transformers` degrades gracefully without it for this use case — no further error was observed after removal, for the parts of the pipeline exercised this session (Download Model, Accelerate).

**⚠️ Regresses on re-run of "Create from requirements.txt"** if the file still lists plain `torchaudio` — observed this session: closing/reopening the project reintroduced the identical crash, requiring the same uninstall again. The fix belongs in `requirements.txt` itself (remove the line), not just in the live venv.

## Resolution locks the compiled engine

The resolution set on the depth COMP **before** clicking Accelerate is baked into the TensorRT engine's fixed input profile and cannot be changed without rebuilding. Observed in the build log:

```
Profile 0:
    {input [min=(1, 3, 518, 518), opt=(1, 3, 518, 518), max=(1, 3, 518, 518)]}
```

518×518 is Depth-Anything V2's native training resolution — the README's implicit default and the safest choice for depth-map quality. Lower resolutions trade quality for speed/latency in a live-show context; the model was not trained above 518×518, so going higher costs compute without a corresponding accuracy gain. **Reasoned, not bench-compared** — no side-by-side test of depth quality at other resolutions was run this session.

## Setup sequence — one-time vs. per-launch

Per the README, confirmed accurate this session:

**One-time** (persists on disk once done — venv, downloaded weights, compiled `.engine` file all survive project close):
1. Open textport
2. TDPyEnvManager → "Create from requirements.txt"
3. TDDepthAnything COMP → Download Model
4. Accelerate (~5 min first build, this session: 312 s for Depth-Anything-V2-Small at 518×518 on an RTX A5500 Laptop GPU)

**Every session after that:**
5. Upload Model to GPU
6. Turn on Active

## Completion signals — not documented by the README, observed this session

The README gives no explicit "how do I know it's done" signal for any step; the following was observed directly:

- **Download Model:** a `tqdm`-style progress bar (`Loading weights: 100%|...| 287/287`) reaching 100% and returning to the `python >>>` prompt with no traceback beneath it.
- **Accelerate:** the textport prints `[I] Finished engine building in <N> seconds` immediately followed by `[I] Saving engine to <path>.engine` — this is the definitive completion line. A quiet gap of several minutes between `[I] Building engine with configuration:` and this line is normal (see `protocols/nvidia-tensorrt-polygraphy.md` for what "still working" looks like in `nvidia-smi` during that gap) — total silence in the textport during this window is expected behavior, not a hang, provided GPU/CPU/disk signals still show activity.
- **Upload Model to GPU:** not confirmed to completion this session — the first attempt failed with `torch.cuda.Stream requires CUDA support` (CPU-only torch, fixed per `patterns/touchdesigner-python-env-dependencies.md`); re-attempt after the fix was not yet observed to a confirmed success line in this session.

**⚠️ A prior, unrelated failure mode:** `Acceleration reported success but the engine is missing or invalid` — observed once, when Accelerate was attempted while the `torchaudio` DAT-compile-error state above was still active (extension failed to load, so the accelerate call ran against a broken import state). Resolved by fixing `torchaudio` first, then reopening the project fresh, then re-running Accelerate. **Not confirmed whether this specific message can also occur for an unrelated reason** — only one cause was observed and fixed this session.

## Pre-processing for noisy live-camera input — Designed, not tested

**⚠️ Everything in this section is Designed only.** Reasoned from TOP documentation and general video-noise principles; none of it has been run against this pipeline's actual depth output or compared before/after.

**Problem:** bright, moving practical lights (LEDs, moving fixtures, strobes) in a live camera feed create sharp local contrast and motion-blur inconsistency frame to frame. Depth-Anything was not trained on this kind of input noise and can register it as false geometry — depth flicker correlated with lighting changes rather than actual scene movement.

**Proposed chain, source → model input:**

```
Camera source → Blur TOP → Level TOP → depth model input
```

Blur before Level: soften hotspots and motion-blur noise first, so Level's highlight compression operates on already-smoothed data rather than sharp-edged blown-out pixels.

**Blur TOP** (this build has no `Method` H/V dropdown — see below):
| Parameter | Suggested | Reasoning |
|---|---|---|
| Type | Gaussian | smooths hotspots without Catmull-Rom's edge-preservation bias, which fights the goal here |
| Extend | Hold | avoids wraparound bleed at frame edges |
| Pre-Shrink | 2 | cheaper blur cost; model already downscales input to 518×518, so little quality lost |
| Filter Size | 3–4, tune up if flicker persists | main tuning knob; higher = smoother but less real detail passed to the model |
| Filter Scale | 1, 1 | uniform (non-directional) blur — this build's stand-in for a Method dropdown, per §Build note below |
| Sample Step | 1, 1, 1 | leave default |
| Rotate Kernel | 0 | irrelevant with equal Filter Scale on both axes |
| Dither | On | cheap fix for potential 8-bit banding, no observed downside |

**⚠️ Build note:** the Blur TOP in TouchDesigner Build 2025.32820 has no `Method` (Horizontal/Vertical/Both) dropdown — this parameter appears in the current Derivative wiki page but not in this build's actual UI. Directional control here is via the two **Filter Scale** fields instead (equal values = uniform blur, unequal = directional). **Confirmed by user screenshot this session, not independently verified against release notes for which build introduced or removed the Method parameter.**

**Level TOP:**
| Parameter | Suggested | Reasoning |
|---|---|---|
| In High (Range page) | 0.85, lower toward 0.7 if still flickering | compresses blown-out highlights into the white point instead of leaving them clipped hard at 1.0 |
| Everything else | leave at this build's defaults | isolate the one control being tested before adding more |

**⚠️ Brightness 1's neutral/default value was not independently confirmed this session** — the Derivative wiki text did not state a numeric default, and the user's own build showed a default of 1 (not 0) in the live parameter field; the build's actual UI value should be trusted over the wiki text where they disagree. Not re-verified against release notes for which is correct across builds.

**Also proposed, not implemented or tested:** temporal smoothing via a Feedback TOP blending the current depth output with the previous frame(s) (e.g. 70/30 mix), targeting frame-to-frame depth flicker directly rather than only reducing what reaches the model. **Reasoned only — no network was built for this this session.**

---

## Open items

Upload Model to GPU has not been confirmed to a successful completion line after the torch/CUDA fix — only the pre-fix failure was directly observed. No confirmation yet that Active/live inference produces correct depth output, or that GPU-Util climbs during live inference (would confirm the pipeline isn't silently falling back to CPU somewhere downstream of the fixes in `patterns/touchdesigner-python-env-dependencies.md`). The Blur/Level pre-processing chain is entirely untested against this pipeline's actual output — no before/after comparison exists. Whether TDPyEnvManager re-triggers full environment recreation on every project reopen, or only on explicit "Create from requirements.txt" — see the matching open item in `patterns/touchdesigner-python-env-dependencies.md`.
