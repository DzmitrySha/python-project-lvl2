# build internal tree module

def make_tree(dict_1, dict_2) -> list:
    cross_dicts_keys = sorted(dict_1.keys() & dict_2.keys())
    dict1_unique_keys = sorted(dict_1.keys() - dict_2.keys())
    dict2_unique_keys = sorted(dict_2.keys() - dict_1.keys())

    result = []
    for key in cross_dicts_keys:
        child_1 = dict_1.get(key)
        child_2 = dict_2.get(key)

        if child_1 == child_2:
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': dict_1[key],
            })
        elif isinstance(child_1, dict) and isinstance(child_2, dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': make_tree(dict_1[key], dict_2[key]),
            })
        else:
            result.append({
                'key': key,
                'type': 'changed',
                'old_value': dict_1[key],
                'new_value': dict_2[key],
            })

    for key in dict1_unique_keys:
        result.append({
            'key': key,
            'type': 'removed',
            'value': dict_1[key]
        })

    for key in dict2_unique_keys:
        result.append({
            'key': key,
            'type': 'added',
            'value': dict_2[key]
        })
    result = sorted(result, key=lambda child: child['key'])
    return result


def build_tree(dict1, dict2):
    return {
        'type': 'root',
        'children': make_tree(dict1, dict2)
    }
