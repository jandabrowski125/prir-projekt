"""CLI entrypoint — Phase 0 contract.

Usage (intended):
  python -m prir.cli --op map|reduce|filter --n N --mode cpu|omp|cuda|auto|auto-ml|mock_gpu
                    [--threads K] [--timing transfer|resident] [--log results/run.csv]
"""

from __future__ import annotations


def main(argv: list[str] | None = None) -> int:
    raise NotImplementedError("Phase 0: implement CLI main")


if __name__ == "__main__":
    raise SystemExit(main())
