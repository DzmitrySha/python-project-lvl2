# build internal tree module

def make_tree(dict_1, dict_2) -> list:
    cross_dicts_keys = dict_1.keys() & dict_2.keys()
    dict1_unique_keys = dict_1.keys() - dict_2.keys()
    dict2_unique_keys = dict_2.keys() - dict_1.keys()

    result = []
    for key in cross_dicts_keys:
        child_1 = dict_1.get(key)
        child_2 = dict_2.get(key)

        if child_1 == child_2:
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': child_1,
            })
        elif isinstance(child_1, dict) and isinstance(child_2, dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': make_tree(child_1, child_2),
            })
        else:
            result.append({
                'key': key,
                'type': 'changed',
                'old_value': child_1,
                'new_value': child_2,
            })

    for key in dict1_unique_keys:
        result.append({
            'key': key,
            'type': 'removed',
            'value': child_1
        })

    for key in dict2_unique_keys:
        result.append({
            'key': key,
            'type': 'added',
            'value': child_2
        })
    result = sorted(result, key=lambda node: node['key'])
    return result


def build_tree(dict1, dict2):
    return {
        'type': 'root',
        'children': make_tree(dict1, dict2)
    }
