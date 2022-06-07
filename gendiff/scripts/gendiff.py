#!/usr/bin/env python
"""Difference Generator."""

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    """Get start here."""
    args = parse_args()
    print(generate_diff(args))


if __name__ == '__main__':
    main()
