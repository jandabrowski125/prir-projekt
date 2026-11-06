"""Threshold selector stub — Person 1, Track A."""

from __future__ import annotations

from typing import Any

from prir.selectors.base import DeviceSelector


class ThresholdSelector(DeviceSelector):
    """Per-op size thresholds from calibration CSV."""

    @property
    def name(self) -> str:
        return "threshold"

    def choose(self, op: str, n: int, context: dict[str, Any] | None = None) -> str:
        raise NotImplementedError("Person 1: implement ThresholdSelector.choose")

    def fit_from_csv(self, path: str) -> None:
        raise NotImplementedError("Person 1: implement ThresholdSelector.fit_from_csv")
