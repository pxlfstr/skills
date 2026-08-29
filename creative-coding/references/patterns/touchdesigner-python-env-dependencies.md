# TouchDesigner Python Environment & Dependency Resolution

## Provenance

Bench-verified throughout. All of it ran on the user's machine this session: TouchDesigner Build 2025.32820, Python 3.11.10, Windows, NVIDIA RTX A5500 Laptop GPU, driver 597.06 / CUDA 13.2. No vendor documentation was read for this document — every claim below is a directly observed result of a command run in the user's textport, quoted or paraphrased from that session's actual output. What was NOT read: TDPyEnvManager's own source or official documentation; pip's dependency-resolver source. No open contradictions.

---

## The core trap: two Pythons, one textport

TDPyEnvManager creates an isolated `.venv` scoped to the project (e.g. `M:\IMAG\<project>\.venv\`), separate from TouchDesigner's own base Python interpreter. The textport's `python >>>` prompt runs in **TD's base interpreter**, not the project venv.

**Symptom:** `import subprocess; print(subprocess.run(["pip","list"],...).stdout)` in the textport returns a short, generic list (PySide6, colorama, etc.) — TD's own base packages — even when the project's venv has torch, transformers, tensorrt and more installed. This looks like "nothing installed" and is not.

**Fix — always target the venv's own interpreter explicitly:**

```python
result = subprocess.run([r"<path-to-project>\.venv\Scripts\python.exe", "-m", "pip", "list"], capture_output=True, text=True)
print(result.stdout)
```

Same pattern for any pip operation — install, uninstall, show — inside that project's venv. Never assume the bare `pip` or `python` in the textport reaches it.

## Verifying a package inside the venv

```python
result = subprocess.run([r"<path-to-project>\.venv\Scripts\python.exe", "-c", "import torch; print(torch.__version__); print(torch.version.cuda); print(torch.cuda.is_available())"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
```

This is the reliable way to confirm not just that a package imports, but what build it is (CPU vs. CUDA-tagged) and whether CUDA is actually reachable from it — see below, these are not the same question.

## CPU-only torch is a silent trap

Plain PyPI hosts a **CPU-only** build of `torch` by default. A `requirements.txt` line of bare `torch` (even with `--extra-index-url https://download.pytorch.org/whl/cu128` present) can still resolve to the CPU build if pip's resolver decides the PyPI wheel already satisfies the unversioned requirement — it does not compare CUDA-vs-CPU as a version difference.

**Symptom observed this session:** `torch.__version__` printed `2.13.0+cpu`; `torch.cuda.is_available()` returned `False`. Everything CUDA-adjacent that torch touches then fails downstream — in this case `torch.cuda.Stream requires CUDA support`, raised inside a worker thread when a tool tried to upload a model to GPU.

**Fix:**

```python
result = subprocess.run([r"<path-to-project>\.venv\Scripts\python.exe", "-m", "pip", "install", "--force-reinstall", "torch", "--index-url", "https://download.pytorch.org/whl/cu128"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
```

`--force-reinstall` is required — without it, pip reports "Requirement already satisfied" and does nothing, even though the installed build is wrong for the purpose.

## Matched-pair installs: torch + torchvision

`torchvision` declares an exact `torch==` pin as a dependency. Installing `torch` and `torchvision` separately, especially across two different pip invocations, risks pip resolving them against different points in each project's release history — pip's own resolver does not always catch this at install time.

**Symptom observed this session**, after fixing torch alone:

```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
torchvision 0.28.0 requires torch==2.13.0, but you have torch 2.11.0+cu128 which is incompatible.
```

**Fix — reinstall both from the same index in one pass**, letting pip resolve the pair together rather than patching one and leaving the other stale:

```python
result = subprocess.run([r"<path-to-project>\.venv\Scripts\python.exe", "-m", "pip", "install", "--force-reinstall", "torchvision", "--index-url", "https://download.pytorch.org/whl/cu128"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
```

This pulled `torchvision-0.26.0+cu128` as the pairing for the already-installed `torch-2.11.0+cu128`, with no resolver conflict — pip chose the compatible pair once both were sourced from the same cu128 index in the same operation.

## subprocess.run() blocks TouchDesigner's UI thread

`subprocess.run(...)` in the textport is a blocking call executed on TD's main thread. A large pip install (a multi-GB CUDA wheel, observed here at ~2.8 GB for one torch build) will freeze TouchDesigner's UI — spinning cursor, unresponsive — for the full download/install duration. This is expected, not a hang. Confirm liveness independently rather than assuming a frozen UI means a stuck process:

- `nvidia-smi` from a separate shell — GPU-Util/power-state changes indicate active work
- Task Manager → Details → the relevant `.exe`'s CPU% — near-zero *and* no disk I/O *and* no new console output over several minutes, together, is the actual stall signal; any one alone is not conclusive
- Disk I/O ticking (Resource Monitor) during a build/install is a "still alive" signal even when CPU and GPU both look idle

For future work: running long installs via TouchDesigner's Thread Manager DAT instead of directly in the textport would avoid the UI freeze. **Designed, not tried** — not run this session.

## requirements.txt: unpinned lines regress silently

An unpinned dependency line (`tensorrt-cu12` with no version) re-resolves to whatever is current on every fresh "Create from requirements.txt," which can silently reintroduce a previously-fixed incompatibility on the next environment rebuild — including simply reopening the project, if the manager re-triggers environment creation.

**Fix:** pin exact working versions once a known-good combination is confirmed, and remove any line for a package that turns out not to be needed at all (see `touchdesigner-TDDepthAnything.md` for the `torchaudio` case, which is tool-specific and cited there rather than restated here).

## Leftover temp directories after force-reinstall

`pip install --force-reinstall` on Windows sometimes leaves an orphaned temp folder it couldn't fully clean up, reported as a warning:

```
WARNING: Failed to remove contents in a temporary directory '...\.venv\Lib\site-packages\~orchvision'.
You can safely remove it manually.
```

Cosmetic. Safe to delete by hand; not referenced by anything once the real package folder exists alongside it.

---

## Open items

Whether Thread Manager DAT actually avoids the UI freeze for a subprocess-based pip install — reasoned as plausible, not tried. Whether TDPyEnvManager re-triggers full environment recreation on every project open or only on explicit "Create from requirements.txt" — observed behavior this session was consistent with the latter after the requirements.txt fix, but the manager's own trigger logic was not read from source or documentation.
