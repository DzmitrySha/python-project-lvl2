# make difference module

from gendiff.enter_parser import parser
from gendiff.stylish import str_stylish


def make_diff(dict_1, dict_2):
    cross_dicts_keys = sorted(dict_1.keys() & dict_2.keys())
    dict1_unique_keys = sorted(dict_1.keys() - dict_2.keys())
    dict2_unique_keys = sorted(dict_2.keys() - dict_1.keys())

    diff = []

    for key in cross_dicts_keys:
        child_1 = dict_1[key]
        child_2 = dict_2[key]

        if child_1 == child_2:
            diff.append(f"  {key}: {child_1}")
        # elif isinstance(child_1, dict) and isinstance(child_2, dict):
        #     diff.append(key)
        #     diff.append(make_diff(child_1, child_2))
        else:
            diff.append(f"- {key}: {child_1}")
            diff.append(f"+ {key}: {child_2}")

    for key in dict1_unique_keys:
        diff.append(f"- {key}: {dict_1[key]}")
    for key in dict2_unique_keys:
        diff.append(f"+ {key}: {dict_2[key]}")
    return diff


def generate_diff(file_path1, file_path2):
    dict_1, dict_2 = parser(file_path1, file_path2)
    diff = make_diff(dict_1, dict_2)
    # print(diff)
    return str_stylish(diff)
