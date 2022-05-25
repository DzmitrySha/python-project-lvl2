# make diff result module

from gendiff.formatters import format_stylish, format_plain, format_json


FORMATS = {
    "stylish": format_stylish,
    "plain": format_plain,
    "json": format_json,
}


def format_(tree, format_name="stylish"):
    if format_name in FORMATS:
        return FORMATS[format_name](tree)
    return "ERROR: Incorrect format name. " \
           "Please check that the format name is correct."
