# make format plain module


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


def iter_(node: dict, path="") -> str:
    if node['type'] == 'unchanged':
        return ''

    children = node.get('children')
    current_path = f"{path}{node.get('key')}"

    if node['type'] == 'root':
        lines = map(lambda child: iter_(child, path), children)
        result = "\n".join(lines)
        return result.replace('\n\n', '\n')

    if node['type'] == 'nested':
        lines = map(lambda child: iter_(child, f"{current_path}."), children)
        result = "\n".join(lines)
        return result

    if node['type'] == 'removed':
        return f"Property '{current_path}' was removed"

    if node['type'] == 'added':
        formatted_value = to_string(node.get('value'))
        return f"Property '{current_path}' was added " \
               f"with value: {formatted_value}"

    if node['type'] == 'changed':
        formatted_old_value = to_string(node.get('old_value'))
        formatted_new_value = to_string(node.get('new_value'))
        return f"Property '{current_path}' was updated. " \
               f"From {formatted_old_value} to {formatted_new_value}"

    raise TypeError(f"Unknown node type: '{node['type']}'")


def format_plain(node: dict):
    return iter_(node)
