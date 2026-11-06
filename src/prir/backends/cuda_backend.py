"""CUDA (Numba) backend stub — Person 1, Track A.

Timing modes: TRANSFER (H2D+kernel+D2H) and RESIDENT (kernel-only).
"""

from __future__ import annotations

from typing import Any

from prir.backends.base import BackendNotReady, ComputeBackend


class CudaBackend(ComputeBackend):
    @property
    def name(self) -> str:
        return "cuda"

    @property
    def supports_resident(self) -> bool:
        return True

    def map(self, data: Any) -> Any:
        raise BackendNotReady("Person 1: implement CudaBackend.map")

    def reduce(self, data: Any) -> Any:
        raise BackendNotReady("Person 1: implement CudaBackend.reduce")

    def filter(self, data: Any, threshold: float) -> Any:
        raise BackendNotReady("Person 1: implement CudaBackend.filter")
