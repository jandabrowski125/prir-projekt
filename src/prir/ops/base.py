"""Operation ABC — implement in Phase 0."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Operation(ABC):
    """Strategy: prepare input, run on a backend, reference result, verify."""

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def prepare_input(self, n: int, params: dict[str, Any] | None = None) -> Any:
        raise NotImplementedError

    @abstractmethod
    def run(self, backend: Any, data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def reference(self, data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def verify(self, actual: Any, expected: Any) -> bool:
        raise NotImplementedError
