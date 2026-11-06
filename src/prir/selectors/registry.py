"""Selector registry / factory — Phase 0."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from prir.selectors.base import DeviceSelector


class SelectorRegistry:
    _registry: dict[str, type] = {}

    @classmethod
    def register(cls, name: str, selector_cls: type) -> None:
        cls._registry[name] = selector_cls

    @classmethod
    def create(cls, name: str, **kwargs) -> DeviceSelector:
        if name not in cls._registry:
            raise KeyError(f"Unknown selector: {name!r}. Known: {sorted(cls._registry)}")
        return cls._registry[name](**kwargs)

    @classmethod
    def names(cls) -> list[str]:
        return sorted(cls._registry)

    @classmethod
    def clear(cls) -> None:
        cls._registry.clear()


def register_defaults() -> None:
    """Wire forced (Phase 0); threshold (P1); ml (P2)."""
    raise NotImplementedError("Phase 0: register default selectors")
