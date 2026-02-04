"""Utility functions."""


def format_number(n: int) -> str:
    """Format a number with thousand separators."""
    return f"{n:,}"


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Check if a number is odd."""
    return n % 2 == 1
