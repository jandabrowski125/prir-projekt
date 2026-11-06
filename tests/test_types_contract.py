"""Contract guards for shared types / CSV schema."""

from prir.types import CSV_COLUMNS, Job, TimingMode


def test_csv_columns_order():
    assert CSV_COLUMNS[0] == "timestamp"
    assert "time_ms" in CSV_COLUMNS
    assert CSV_COLUMNS[-1] == "world_size"
    assert len(CSV_COLUMNS) == 14


def test_job_defaults():
    job = Job(op="map", n=1024)
    assert job.mode == "cpu"
    assert job.timing_mode == TimingMode.TRANSFER
