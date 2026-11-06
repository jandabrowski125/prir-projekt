"""ComputeBackend ABC — implement contract in Phase 0."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable

from prir.types import TimingMode


class BackendNotReady(RuntimeError):
    """Raised when an optional backend (omp/cuda) is registered but not implemented yet."""


class ComputeBackend(ABC):
    """Strategy: map / reduce / filter on a device."""

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    def supports_resident(self) -> bool:
        return False

    @abstractmethod
    def map(self, data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def reduce(self, data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def filter(self, data: Any, threshold: float) -> Any:
        raise NotImplementedError

    def timed_call(
        self,
        fn: Callable[[], Any],
        timing_mode: TimingMode = TimingMode.TRANSFER,
    ) -> tuple[Any, float]:
        """Return (result, time_ms). Implement timing helper in Phase 0."""
        raise NotImplementedError("Phase 0: implement ComputeBackend.timed_call")
