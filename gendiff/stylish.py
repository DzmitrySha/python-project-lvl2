def formatter(source, prefix='    '):
    pass


# def stringify(source, prefix=' ', prefix_count=1):
#
#     def add_prefix(tree, depth):
#         if not isinstance(tree, dict):
#             return str(tree)
#
#         next_depth_size = depth + prefix_count
#         previous_prefix = prefix * (depth - prefix_count)
#         current_prefix = prefix * depth
#         result = []
#         for key, tree in tree.items():
#             new_key = current_prefix + str(key)
#             new_value = add_prefix(tree, next_depth_size)
#             result.append(f'{new_key}: {new_value}')
#         result.append(previous_prefix)
#         return '{\n' + "\n".join(result) + '}'
#
#     return add_prefix(source, 1)
