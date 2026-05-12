"""Utility for adding two numbers from code or the command line."""

from __future__ import annotations

import argparse


def add_two_numbers(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def main() -> None:
    """Parse two numeric arguments and print their sum."""
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("first", type=float, help="The first number to add.")
    parser.add_argument("second", type=float, help="The second number to add.")
    args = parser.parse_args()

    print(add_two_numbers(args.first, args.second))


if __name__ == "__main__":
    main()
