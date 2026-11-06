"""Filter operation stub — Phase 0: keep x[i] > threshold."""

from __future__ import annotations

from typing import Any

from prir.ops.base import Operation


class FilterOp(Operation):
    @property
    def name(self) -> str:
        return "filter"

    def prepare_input(self, n: int, params: dict[str, Any] | None = None) -> Any:
        raise NotImplementedError("Phase 0: implement FilterOp.prepare_input")

    def run(self, backend: Any, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement FilterOp.run")

    def reference(self, data: Any) -> Any:
        raise NotImplementedError("Phase 0: implement FilterOp.reference")

    def verify(self, actual: Any, expected: Any) -> bool:
        raise NotImplementedError("Phase 0: implement FilterOp.verify")
