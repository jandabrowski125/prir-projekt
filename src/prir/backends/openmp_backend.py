"""OpenMP (Numba prange) backend stub — Person 1, Track A."""

from __future__ import annotations

from typing import Any

from prir.backends.base import BackendNotReady, ComputeBackend


class OpenMPBackend(ComputeBackend):
    def __init__(self, threads: int | None = None) -> None:
        self.threads = threads

    @property
    def name(self) -> str:
        return "omp"

    def map(self, data: Any) -> Any:
        raise BackendNotReady("Person 1: implement OpenMPBackend.map")

    def reduce(self, data: Any) -> Any:
        raise BackendNotReady("Person 1: implement OpenMPBackend.reduce")

    def filter(self, data: Any, threshold: float) -> Any:
        raise BackendNotReady("Person 1: implement OpenMPBackend.filter")
