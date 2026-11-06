"""CSV logger using CSV_COLUMNS from prir.types — Phase 0."""

from __future__ import annotations

from pathlib import Path

from prir.types import CSV_COLUMNS, Result


class CsvLogger:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def write_header_if_needed(self) -> None:
        raise NotImplementedError("Phase 0: implement CsvLogger.write_header_if_needed")

    def append(self, result: Result) -> None:
        raise NotImplementedError("Phase 0: implement CsvLogger.append")

    @staticmethod
    def columns() -> tuple[str, ...]:
        return CSV_COLUMNS
