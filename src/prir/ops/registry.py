"""Operation registry / factory — Phase 0."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from prir.ops.base import Operation


class OperationRegistry:
    _registry: dict[str, type] = {}

    @classmethod
    def register(cls, name: str, op_cls: type) -> None:
        cls._registry[name] = op_cls

    @classmethod
    def create(cls, name: str, **kwargs) -> Operation:
        if name not in cls._registry:
            raise KeyError(f"Unknown operation: {name!r}. Known: {sorted(cls._registry)}")
        return cls._registry[name](**kwargs)

    @classmethod
    def names(cls) -> list[str]:
        return sorted(cls._registry)

    @classmethod
    def clear(cls) -> None:
        cls._registry.clear()


def register_defaults() -> None:
    """Wire MapOp / ReduceOp / FilterOp — call from package init in Phase 0."""
    raise NotImplementedError("Phase 0: register default operations")
