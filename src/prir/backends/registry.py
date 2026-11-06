"""Backend registry / factory — Phase 0."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from prir.backends.base import ComputeBackend


class BackendRegistry:
    _registry: dict[str, type] = {}

    @classmethod
    def register(cls, name: str, backend_cls: type) -> None:
        cls._registry[name] = backend_cls

    @classmethod
    def create(cls, name: str, **kwargs) -> ComputeBackend:
        if name not in cls._registry:
            raise KeyError(f"Unknown backend: {name!r}. Known: {sorted(cls._registry)}")
        return cls._registry[name](**kwargs)

    @classmethod
    def names(cls) -> list[str]:
        return sorted(cls._registry)

    @classmethod
    def clear(cls) -> None:
        cls._registry.clear()


def register_defaults() -> None:
    """Wire cpu / mock_* (Phase 0); omp / cuda (Person 1)."""
    raise NotImplementedError("Phase 0: register default backends")
