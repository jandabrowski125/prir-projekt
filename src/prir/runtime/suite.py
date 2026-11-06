"""JobSuite loader from JSON — Phase 0 / Person 2 configs."""

from __future__ import annotations

from pathlib import Path

from prir.types import Job


class JobSuite:
    def __init__(self, jobs: list[Job]) -> None:
        self.jobs = jobs

    def __len__(self) -> int:
        return len(self.jobs)

    @classmethod
    def from_json(cls, path: str | Path) -> JobSuite:
        raise NotImplementedError("Phase 0 / Person 2: implement JobSuite.from_json")
