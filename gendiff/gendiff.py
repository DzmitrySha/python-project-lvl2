# generate diff module

from gendiff.cli import parser
from gendiff.tree import make_tree
from gendiff.formatters import format_


def generate_diff(file_path1: str, file_path2: str, format_name="stylish"):
    dict_1, dict_2 = parser(file_path1, file_path2)
    tree = make_tree(dict_1, dict_2)
    diff = format_(tree, format_name)
    return diff
