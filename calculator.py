"""A tiny calculator used to practise the GitHub pull-request workflow."""

from __future__ import annotations

Number = int | float


def add(a: Number, b: Number) -> Number:
    """Return ``a + b``."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return ``a - b``."""
    return a - b


def divide(a: Number, b: Number) -> float:
    """Return ``a / b``.

    Raises:
        ValueError: If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
