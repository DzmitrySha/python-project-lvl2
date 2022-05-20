# make diff module

from constants import UNCHANGED, CHANGED, DICT, REMOVED, ADDED


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
