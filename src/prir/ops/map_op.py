"""Map operation stub — Phase 0: y[i] = x[i]*x[i] + 0.5*x[i]."""

from __future__ import annotations

from typing import Any

from prir.ops.base import Operation


class MapOp(Operation):
    @property
    def name(self) -> str:
        return "map"

    def prepare_input(self, n: int, params: dict[str, Any] | None = None) -> Any:
        raise NotImplementedError("Phase 0: implement MapOp.prepare_input")

    def run(self, backend: Any, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement MapOp.run")

    def reference(self, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement MapOp.reference")

    def verify(self, actual: Any, expected: Any) -> bool:
        raise NotImplementedError("Phase 0: implement MapOp.verify")
