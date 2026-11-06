"""DeviceSelector ABC — Phase 0 contract."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DeviceSelector(ABC):
    """Strategy: choose backend name for (op, n)."""

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def choose(self, op: str, n: int, context: dict[str, Any] | None = None) -> str:
        raise NotImplementedError

    @property
    def calibration_cost_ms(self) -> float:
        return 0.0
