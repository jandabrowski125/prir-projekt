"""Compute backends (Strategy). Phase 0: sequential + mock; Track A: omp + cuda."""

from prir.backends.registry import BackendRegistry

__all__ = ["BackendRegistry"]
