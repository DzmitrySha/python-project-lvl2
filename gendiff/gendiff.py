# make difference module

from gendiff.enter_parser import parser
from gendiff.stylish import stylish
from gendiff.constants import ADDED, REMOVED, CHANGED, UNCHANGED, DICT


def make_diff(dict_1, dict_2) -> dict:
    cross_dicts_keys = dict_1.keys() & dict_2.keys()
    dict1_unique_keys = dict_1.keys() - dict_2.keys()
    dict2_unique_keys = dict_2.keys() - dict_1.keys()

    diff = {}
    for key in cross_dicts_keys:
        child_1 = dict_1.get(key)
        child_2 = dict_2.get(key)

        if child_1 == child_2:
            diff[key] = {
                "status": UNCHANGED,
                "diff": {key: child_1},
            }
        elif isinstance(child_1, dict) and isinstance(child_2, dict):
            diff[key] = {
                "status": DICT,
                "diff": make_diff(child_1, child_2),
            }
        else:
            diff[key] = {
                "status": CHANGED,
                "diff_rem": {key: child_1},
                "diff_add": {key: child_2},
            }
    for key in dict1_unique_keys:
        diff[key] = {
            "status": REMOVED,
            "diff": {key: dict_1[key]},
        }
    for key in dict2_unique_keys:
        diff[key] = {
            "status": ADDED,
            "diff": {key: dict_2[key]},
        }
    return dict(sorted(diff.items()))


def generate_diff(file_path1, file_path2):
    dict_1, dict_2 = parser(file_path1, file_path2)
    diff = make_diff(dict_1, dict_2)
    return stylish(diff)


# def make_diff(dict_1, dict_2):
#     cross_dicts_keys = sorted(dict_1.keys() & dict_2.keys())
#     dict1_unique_keys = sorted(dict_1.keys() - dict_2.keys())
#     dict2_unique_keys = sorted(dict_2.keys() - dict_1.keys())
#     diff = []
#
#     for key in cross_dicts_keys:
#         child_1 = dict_1[key]
#         child_2 = dict_2[key]
#
#         if child_1 == child_2:
#             diff.append(f"{UNCHANGED}{key}: {child_1}")
#         elif isinstance(child_1, dict) and isinstance(child_2, dict):
#             diff.append(key)
#             diff.append(make_diff(child_1, child_2))
#         else:
#             diff.append(f"{REMOVED}{key}: {child_1}")
#             diff.append(f"{ADDED}{key}: {child_2}")
#     for key in dict1_unique_keys:
#         diff.append(f"{REMOVED}{key}: {dict_1[key]}")
#     for key in dict2_unique_keys:
#         diff.append(f"{ADDED}{key}: {dict_2[key]}")
#
#     return diff
#
#
# def generate_diff(file_path1, file_path2):
#     dict_1, dict_2 = parser(file_path1, file_path2)
#     diff = make_diff(dict_1, dict_2)
#     return to_str(diff)
