# PRiR O08 — Automatic CPU / GPU Selection

Python project stub for automatic backend selection (map / reduce / filter) across sequential CPU, OpenMP (Numba), CUDA (Numba), and MPI job suites, with threshold and ML selectors.

See [PROJECT_DESCRIPTION.txt](PROJECT_DESCRIPTION.txt) for course requirements and [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for the full plan.

## Status

**Stub only** — directory layout and module placeholders. Next step: **Phase 0 Contract Freeze** (shared ABCs, registries, CLI, CSV schema, `SequentialBackend`, `MockBackend`, `JobExecutor`).

## Team split

| Person 1 | Person 2 |
|----------|----------|
| `OpenMPBackend`, `CudaBackend`, `ThresholdSelector` | `MpiJobRunner`, suites, `MLSelector`, `ml/` |

After Phase 0, both tracks proceed in parallel against the frozen contract.

## Layout

```
src/prir/     package (ops, backends, selectors, runtime, mpi, cli)
ml/           train / metrics (Person 2)
suites/       JSON job suites
scripts/      calibration / report helpers
results/      run logs (gitignored)
docs/         report
tests/        pytest
```

## Setup (after Phase 0)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Intended CLI (contract — implement in Phase 0)

```text
python -m prir.cli --op map|reduce|filter --n N --mode cpu|omp|cuda|auto|auto-ml|mock_gpu
                  [--threads K] [--timing transfer|resident] [--log results/run.csv]
mpirun -n P python -m prir.mpi.runner --suite suites/test.json --log results/mpi.csv
```
