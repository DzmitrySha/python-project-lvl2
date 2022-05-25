# make format plain module


def make_phrase(phrase_type, path="", value1="", value2=""):
    phrases = {
        "removed": f"Property {path} was removed",
        "added": f"Property {path} was added with value: {value2}",
        "updated": f"Property {path} was updated. From {value1} to {value2}",
    }
    return phrases[phrase_type]


def to_string(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return value
    if value is None:
        return "null"
    return f"'{value}'"


def format_plain(node, n=""):
    children = node.get('children')
    result = []

    for child in children:
        if n:
            path = n + f".{child['key']}"
        else:
            path = f"{child['key']}"

        if child['type'] == 'nested':
            result.append(format_plain(child, path))

        elif child['type'] == 'added':
            value2 = to_string(child["value"])
            phrase = make_phrase("added", to_string(path), value2=value2)
            result.append(phrase)

        elif child['type'] == 'removed':
            value2 = to_string(child["value"])
            phrase = make_phrase("removed", to_string(path), value2=value2)
            result.append(phrase)

        elif child['type'] == 'changed':
            value1 = to_string(child["old_value"])
            value2 = to_string(child["new_value"])
            phrase = make_phrase("updated", to_string(path),
                                 value1=value1, value2=value2)
            result.append(phrase)

    return "\n".join(result)
