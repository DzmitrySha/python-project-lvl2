#!/usr/bin/env python
"""Difference Generator."""

from gendiff import generate_diff
from gendiff.cli import parse_args_


def main():
    """Get start here."""
    first_file, second_file, output_format = parse_args_()
    print(generate_diff(first_file, second_file, output_format))


if __name__ == '__main__':
    main()
