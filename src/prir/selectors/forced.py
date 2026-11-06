"""Forced selector stub — Phase 0 (always returns a fixed backend name)."""

from __future__ import annotations

from typing import Any

from prir.selectors.base import DeviceSelector


class ForcedSelector(DeviceSelector):
    def __init__(self, backend_name: str = "cpu") -> None:
        self.backend_name = backend_name

    @property
    def name(self) -> str:
        return "forced"

    def choose(self, op: str, n: int, context: dict[str, Any] | None = None) -> str:
        return self.backend_name
