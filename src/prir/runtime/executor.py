"""JobExecutor — Template Method pipeline (CLI and MPI share this). Phase 0."""

from __future__ import annotations

from prir.types import Job, Result


class JobExecutor:
    """resolve op → select backend → run → verify → log."""

    def run(self, job: Job) -> Result:
        raise NotImplementedError("Phase 0: implement JobExecutor.run")
