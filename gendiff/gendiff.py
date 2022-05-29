# generate diff module

from gendiff.cli import parser
from gendiff.tree import build_tree
from gendiff.formatters import format_


def generate_diff(file_path1: str,
                  file_path2: str,
                  format_name="stylish") -> str:
    dict_1, dict_2 = parser(file_path1, file_path2)
    tree = build_tree(dict_1, dict_2)
    diff = format_(tree, format_name)
    return diff
