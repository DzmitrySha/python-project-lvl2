import os
import json
import yaml


def parser(file_path1, file_path2):
    file1_ext = os.path.splitext(file_path1)
    file2_ext = os.path.splitext(file_path2)
    if (file1_ext and file2_ext) == '.json':
        first_file = json.load(open(file_path1))
        second_file = json.load(open(file_path2))
    if (file1_ext and file2_ext) == '.yaml' or '.yml':
        first_file = yaml.safe_load(open(file_path1))
        second_file = yaml.safe_load(open(file_path2))
    return dict(first_file), dict(second_file)
