# make format plain module
from gendiff.constants import ADDED, REMOVED, CHANGED, DICT, COMPLEX


def make_phrase(phrase_type, path="", value1="", value2=""):
    phrases = {
        "removed": f"Property {path} was removed",
        "added": f"Property {path} was added with value: {value2}",
        "updated": f"Property {path} was updated. From {value1} to {value2}",
    }
    return phrases[phrase_type]


def is_tree(dictionary):
    if isinstance(dictionary, dict):
        return any(isinstance(value, dict) for value in dictionary.values())
    return dictionary


def edit_value(value):
    if isinstance(value, int):
        return str(value).lower()
    elif value is None:
        return "null"
    return f"'{value}'"


def make_value(value, key):
    if is_tree(value):
        return COMPLEX
    return edit_value(value[key])


def format_plain(diff: dict, node=""):
    result = []
    for key, value in diff.items():
        status = value["status"]

        if node:
            path = node + f".{key}"
        else:
            path = f"{key}"

        if status == DICT:
            result.append(format_plain(value["diff"], path))
        elif status == ADDED:
            value2 = make_value(value["diff"], key)
            phrase = make_phrase("added", edit_value(path),
                                 value2=value2)
            result.append(phrase)
        elif status == REMOVED:
            value2 = make_value(value["diff"], key)
            phrase = make_phrase("removed", edit_value(path),
                                 value2=value2)
            result.append(phrase)
        elif status == CHANGED:
            value1 = make_value(value["diff_rem"], key)
            value2 = make_value(value["diff_add"], key)
            phrase = make_phrase("updated", edit_value(path),
                                 value1=value1, value2=value2)
            result.append(phrase)

    return "\n".join(result)
