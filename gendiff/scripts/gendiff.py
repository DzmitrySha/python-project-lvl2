#!/usr/bin/env python
"""Difference Generator."""

import argparse
from gendiff import generate_diff


def main():
    """Get start here."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description="Compares two configuration files "
                    "and shows a difference.")
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        choices=["stylish", "plain"],
                        default="stylish",
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
