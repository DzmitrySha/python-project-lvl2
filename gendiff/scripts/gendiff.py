#!/usr/bin/env python
"""Difference Generator."""

import argparse


def main():
    """Get start here."""
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description="Generate diff")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
