"""Sequential CPU backend stub — Phase 0 (shared)."""

from __future__ import annotations

from typing import Any

from prir.backends.base import ComputeBackend


class SequentialBackend(ComputeBackend):
    @property
    def name(self) -> str:
        return "cpu"

    def map(self, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement SequentialBackend.map")

    def reduce(self, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement SequentialBackend.reduce")

    def filter(self, data: Any, threshold: float) -> Any:
        raise NotImplementedError("Phase 0: implement SequentialBackend.filter")
