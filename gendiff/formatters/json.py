# make format json module
import json


def format_json(tree: list) -> json:
    return json.dumps(tree, indent=4)
