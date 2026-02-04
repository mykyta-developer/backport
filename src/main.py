#!/usr/bin/env python3
"""Main application module."""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers."""
    return a + b


def main():
    """Main entry point."""
    print(greet("World"))
    print(f"2 + 3 = {calculate_sum(2, 3)}")


if __name__ == "__main__":
    main()
