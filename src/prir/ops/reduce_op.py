"""Reduce (sum) operation stub — Phase 0."""

from __future__ import annotations

from typing import Any

from prir.ops.base import Operation


class ReduceOp(Operation):
    @property
    def name(self) -> str:
        return "reduce"

    def prepare_input(self, n: int, params: dict[str, Any] | None = None) -> Any:
        raise NotImplementedError("Phase 0: implement ReduceOp.prepare_input")

    def run(self, backend: Any, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement ReduceOp.run")

    def reference(self, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement ReduceOp.reference")

    def verify(self, actual: Any, expected: Any) -> bool:
        raise NotImplementedError("Phase 0: implement ReduceOp.verify")
