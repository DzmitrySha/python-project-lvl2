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


def format_plain(node, root_node=""):
    children = node.get('children')
    result = []

    for child in children:
        if root_node:
            path = root_node + f".{child['key']}"
        else:
            path = f"{child['key']}"

        if child['type'] == 'nested':
            result.append(format_plain(child, path))

        elif child['type'] == 'removed':
            phrase = make_phrase("removed", to_string(path))
            result.append(phrase)

        elif child['type'] == 'added':
            added_value = to_string(child["value"])
            phrase = make_phrase("added", to_string(path), value2=added_value)
            result.append(phrase)

        elif child['type'] == 'changed':
            old_value = to_string(child["old_value"])
            new_value = to_string(child["new_value"])
            phrase = make_phrase("updated", to_string(path),
                                 value1=old_value, value2=new_value)
            result.append(phrase)

    return "\n".join(result)
