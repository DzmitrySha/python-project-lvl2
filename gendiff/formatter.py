# make diff result module

from gendiff.formatters import format_stylish, format_plain, format_json


CHOOSE_FORMAT = {
    "stylish": format_stylish,
    "plain": format_plain,
    "json": format_json,
}


def format_(format_name, tree):
    if format_name in CHOOSE_FORMAT:
        diff_result = CHOOSE_FORMAT[format_name](tree)
        return diff_result
    else:
        return "ERROR: Incorrect format name. " \
               "Please check that the format name is correct."
