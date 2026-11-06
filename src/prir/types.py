"""Shared dataclasses and enums (freeze in Phase 0)."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class TimingMode(str, Enum):
    TRANSFER = "transfer"
    RESIDENT = "resident"


@dataclass(frozen=True)
class Job:
    op: str
    n: int
    mode: str = "cpu"
    threads: int | None = None
    timing_mode: TimingMode = TimingMode.TRANSFER
    seed: int = 0
    params: dict[str, Any] | None = None


@dataclass
class Result:
    op: str
    n: int
    backend: str
    threads: int | None
    timing_mode: TimingMode
    time_ms: float
    correct: bool
    selector: str | None = None
    chosen: str | None = None
    predicted: str | None = None
    calib_phase: str | None = None
    rank: int = 0
    world_size: int = 1
    output: Any = None


# CSV schema — exact column order (Phase 0 contract)
CSV_COLUMNS: tuple[str, ...] = (
    "timestamp",
    "op",
    "n",
    "backend",
    "threads",
    "timing_mode",
    "time_ms",
    "correct",
    "selector",
    "chosen",
    "predicted",
    "calib_phase",
    "rank",
    "world_size",
)

DEFAULT_DTYPE = "float64"
REDUCE_RTOL = 1e-5
