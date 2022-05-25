# make stylish module
from gendiff.constants import ADDED, REMOVED, UNCHANGED


def get_indent(depth, node_type='root'):
    indent = "    "
    if node_type == 'changed' or node_type == 'removed' or node_type == 'added':
        return (depth * indent)[:-2]
    return depth * indent


def to_string(value, depth):
    indent = get_indent(depth)
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}{UNCHANGED}{k}: {to_string(v, depth + 1)}")
        result = "\n".join(lines)
        return f'{{\n{result}\n{indent}}}'

    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return "null"
    return value


def format_stylish(node, depth=0):
    children = node.get('children')
    indent = get_indent(depth, node['type'])
    formatted_value = to_string(node.get('value'), depth)
    formatted_value1 = to_string(node.get('old_value'), depth)
    formatted_value2 = to_string(node.get('new_value'), depth)

    if node['type'] == 'root':
        lines = map(lambda child: format_stylish(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    if node['type'] == 'nested':
        lines = map(lambda child: format_stylish(child, depth + 1), children)
        result = '\n'.join(lines)
        return f"{indent}{node['key']}: {{\n{result}\n{indent}}}"

    if node['type'] == 'changed':
        line1 = f"{indent}{REMOVED}{node['key']}: {formatted_value1}\n"
        line2 = f"{indent}{ADDED}{node['key']}: {formatted_value2}"
        result = line1 + line2
        return result

    if node['type'] == 'unchanged':
        return f"{indent}{node['key']}: {formatted_value}"

    if node['type'] == 'removed':
        return f"{indent}{REMOVED}{node['key']}: {formatted_value}"

    if node['type'] == 'added':
        return f"{indent}{ADDED}{node['key']}: {formatted_value}"
