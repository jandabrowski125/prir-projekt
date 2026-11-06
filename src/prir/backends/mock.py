"""Mock backends with synthetic timings — Phase 0 (unblocks Person 2 ML).

mock_cpu / mock_gpu: correct NumPy results; t = alpha + beta * n (different coeffs).
"""

from __future__ import annotations

from typing import Any

from prir.backends.base import ComputeBackend


class MockBackend(ComputeBackend):
    def __init__(self, name: str = "mock_cpu", alpha: float = 1.0, beta: float = 1e-6) -> None:
        self._name = name
        self.alpha = alpha
        self.beta = beta

    @property
    def name(self) -> str:
        return self._name

    def map(self, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement MockBackend.map")

    def reduce(self, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement MockBackend.reduce")

    def filter(self, data: Any, threshold: float) -> Any:
        raise NotImplementedError("Phase 0: implement MockBackend.filter")

    def synthetic_time_ms(self, n: int) -> float:
        return self.alpha + self.beta * n
