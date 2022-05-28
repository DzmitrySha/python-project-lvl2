# make diff result module

from gendiff.formatters import format_stylish, format_plain, format_json


def format_(tree, format_name="stylish"):
    formats = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }
    if format_name in formats:
        return formats[format_name](tree)

    raise ValueError(f'Unknown format: {format_name}')
