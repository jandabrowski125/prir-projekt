"""ML selector stub — Person 2, Track B."""

from __future__ import annotations

from typing import Any

from prir.selectors.base import DeviceSelector


class MLSelector(DeviceSelector):
    """sklearn model loaded from joblib; fallback to threshold by name if missing."""

    def __init__(self, model_path: str | None = None) -> None:
        self.model_path = model_path

    @property
    def name(self) -> str:
        return "ml"

    def choose(self, op: str, n: int, context: dict[str, Any] | None = None) -> str:
        raise NotImplementedError("Person 2: implement MLSelector.choose")

    def load(self, path: str) -> None:
        raise NotImplementedError("Person 2: implement MLSelector.load")
