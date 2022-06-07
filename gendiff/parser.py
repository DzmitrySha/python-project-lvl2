# Parser module

import json
import yaml


def parse(data, format_name):
    if format_name == '.json':
        return json.load(open(data))
    elif format_name in ('.yml', '.yaml'):
        return yaml.safe_load(open(data))
    else:
        raise OSError('Unknown file format')
