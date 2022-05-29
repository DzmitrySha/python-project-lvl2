# make format plain module

def make_phrase(phrase_type: str, path="", old_value="", new_value="") -> str:
    phrases = {
        "removed": f"Property {path} was removed",
        "added": f"Property {path} was added with value: {new_value}",
        "updated": f"Property {path} was updated."
                   f" From {old_value} to {new_value}",
    }
    if phrase_type in phrases:
        return phrases[phrase_type]
    raise ValueError(f'Unknown phrase: {phrase_type}')


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


def format_plain(node: dict, path='') -> str:
    children = node.get('children')
    result = []

    for child in children:
        if path:
            current_path = path + f".{child['key']}"
        else:
            current_path = f"{child['key']}"

        if child['type'] == 'nested':
            result.append(format_plain(child, current_path))

        elif child['type'] == 'removed':
            phrase = make_phrase("removed", to_string(current_path))
            result.append(phrase)

        elif child['type'] == 'added':
            added_value = to_string(child["value"])
            phrase = make_phrase("added", to_string(current_path),
                                 new_value=added_value)
            result.append(phrase)

        elif child['type'] == 'changed':
            old_value = to_string(child["old_value"])
            new_value = to_string(child["new_value"])
            phrase = make_phrase("updated", to_string(current_path),
                                 old_value=old_value, new_value=new_value)
            result.append(phrase)

        elif child['type'] == 'unchanged':
            continue

        else:
            raise ValueError(f"Unknown child type: {child['type']}")

    return "\n".join(result)
