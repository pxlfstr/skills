# NVIDIA TensorRT + Polygraphy — Version Behavior

## Provenance

`[Bench]` — observed directly in a user's textport session this session, not sourced from NVIDIA documentation. Environment: `tensorrt-cu12` 11.2.1.2 then downgraded to 10.9.0.34, `polygraphy` 0.53.4, Windows, RTX A5500 Laptop GPU, driver 597.06, CUDA 13.2 (system), torch 2.11.0+cu128. No NVIDIA or Polygraphy release notes were read to confirm which exact TensorRT release introduced the breaking change described below — the finding here is empirical (it broke at 11.2.1.2, it worked at 10.9.0.34), not sourced from a changelog. This is a gap: the true boundary version between "breaks" and "works" is unknown, only that it falls somewhere between 10.9.0.34 and 11.2.1.2. What was NOT read: TensorRT 11.x release notes, Polygraphy's own changelog, NVIDIA's TensorRT-to-CUDA compatibility matrix. No open contradictions — single data point, not cross-checked against a second source.

---

## `polygraphy`'s FP16 `CreateConfig` breaks on TensorRT 11.2.1.2

**Observed failure**, building a TensorRT engine via `polygraphy.backend.trt`:

```
[!] fp16 in CreateConfig is not available on TensorRT version 11.2.1.2.
polygraphy.exception.exception.PolygraphyException: fp16 in CreateConfig is not available on TensorRT version 11.2.1.2.
```

Traceback origin: `polygraphy/backend/trt/config.py`, `_configure_flags` → `try_set_flag("FP16")` → `trt_util.fail_unavailable`. Polygraphy's own flag-setting call for FP16 precision does not find a matching mechanism on TensorRT 11.2.1.2's `CreateConfig` — the API this version of Polygraphy expects for setting the FP16 builder flag is not present, or has moved, in TensorRT 11.x as of this release.

**⚠️ Unresolved: whether this is a Polygraphy 0.53.4 problem, a TensorRT 11.x API change, or a version mismatch between the two** — not established this session. Only the empirical fact that the combination fails is confirmed.

## Working combination — Bench-verified

`[Bench]` **TensorRT 10.9.0.34** (`tensorrt-cu12==10.9.0.34`) with **Polygraphy 0.53.4** builds an FP16 engine successfully end to end — same script, same machine, same model, only the TensorRT version changed. Full build log for this combination on a Depth-Anything-V2-Small model at 518×518, single profile:

```
[I] Configuring with profiles:[
        Profile 0:
            {input [min=(1, 3, 518, 518), opt=(1, 3, 518, 518), max=(1, 3, 518, 518)]}
    ]
[W] profileSharing0806 is on by default in TensorRT 10.0. This flag is deprecated and has no effect.
[I] Building engine with configuration:
    Flags                  | [FP16]
    Engine Capability      | EngineCapability.STANDARD
    Memory Pools           | [WORKSPACE: 16383.50 MiB, TACTIC_DRAM: 16383.50 MiB, TACTIC_SHARED_MEMORY: 1024.00 MiB]
    Tactic Sources         | [EDGE_MASK_CONVOLUTIONS, JIT_CONVOLUTIONS]
    Profiling Verbosity    | ProfilingVerbosity.DETAILED
    Preview Features       | [PROFILE_SHARING_0806]
...
[I] Finished engine building in 312.247 seconds
[I] Saving engine to <path>.engine
```

312 seconds (~5.2 min) for a first-time build of this model size, on this GPU. No indication whether this scales linearly with model size — single data point.

**Downgrade command:**

```python
result = subprocess.run([r"<path-to-project>\.venv\Scripts\python.exe", "-m", "pip", "install", "tensorrt-cu12==10.9.0.34"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
```

pip correctly resolved and matched `tensorrt_cu12_libs==10.9.0.34` and `tensorrt_cu12_bindings==10.9.0.34` as sub-dependencies in the same operation — no separate pin needed for those.

## `CUDA is not available` warning during build — did not block the build

**Observed**, both before and after the version fix:

```
2026-08-29 11:23:30,508 - WARNING - ... - CUDA is not available; skipping TF32 enablement.
```

This fired even while TensorRT itself successfully built an engine using the GPU. **⚠️ Read this as a torch-level check, not a TensorRT-level one** — in this session it correlated with a CPU-only torch build being active in the same venv (see `patterns/touchdesigner-python-env-dependencies.md`), while TensorRT's own engine-building machinery, which manages its own CUDA context independent of torch, proceeded normally regardless. Do not treat this warning as evidence the TensorRT build itself is failing or running on CPU — it is not established that it means that, and in the one case observed it did not.

## `nvidia-smi` signal during a build

`[Bench]` During active tactic-search/engine-building, observed: GPU-Util 6–10%, power state P1 (up from idle P8), memory usage ~1.2–1.3 GB, all sustained over several minutes with the process legitimately still working. The build is bursty — CPU and GPU load both fluctuate, including stretches with near-zero visible activity on either, while Polygraphy benchmarks kernel tactics internally. A single low reading is not evidence of a stall; sustained zero activity across GPU, CPU, and disk I/O together, with no new console output, is the actual stall signal (see `patterns/touchdesigner-python-env-dependencies.md` for the general version of this check).

---

## Open items

The actual TensorRT version boundary between "FP16 CreateConfig works" and "breaks" — only two points are known (10.9.0.34 works, 11.2.1.2 breaks), nothing in between was tested. Whether the break is fixable by upgrading Polygraphy instead of downgrading TensorRT — not tried. Whether the same break reproduces on TensorRT 11.0.x or 11.1.x, or is specific to 11.2.1.2. Root cause of the `CreateConfig` API mismatch — not read from either project's source or release notes.
