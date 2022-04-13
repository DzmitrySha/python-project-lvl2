# make stylish module
from gendiff.constants import ADDED, REMOVED, CHANGED


def to_str(diff):
    result = "{\n" + "\n".join(diff).lower() + "\n}"
    return result


def to_str_dict(diff: dict):
    result = [f"{key}: {value}" for key, value in diff.items()]
    return "".join(result).lower()


def stylish_plain(diff: dict):
    result = []
    for key, value in diff.items():
        if value["status"] == CHANGED:
            result.append(REMOVED + to_str_dict(value["diff_rem"]))
            result.append(ADDED + to_str_dict(value["diff_add"]))
        else:
            result.append(value["status"] + to_str_dict(value["diff"]))
    return to_str(result)
