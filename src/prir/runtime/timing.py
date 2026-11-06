"""Wall-clock timing helpers — Phase 0."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator


@contextmanager
def timer_ms() -> Iterator[list[float]]:
    """Yield a one-element list that will hold elapsed milliseconds."""
    raise NotImplementedError("Phase 0: implement timer_ms")
