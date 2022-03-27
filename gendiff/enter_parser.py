import os
import json
import yaml


def parser(file_path1, file_path2):
    if os.path.splitext(file_path1) == '.json':
        first_file = dict(json.load(open(file_path1)))
        second_file = dict(json.load(open(file_path2)))
    elif os.path.splitext(file_path1) == '.yaml' or '.yml':
        first_file = dict(yaml.safe_load(open(file_path1)))
        second_file = dict(yaml.safe_load(open(file_path2)))
    return first_file, second_file
