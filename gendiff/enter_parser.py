import os
import json
import yaml


def parser(file_path1, file_path2):
    file1_ext = os.path.splitext(file_path1)
    file2_ext = os.path.splitext(file_path2)

    if (file1_ext and file2_ext) == '.json':
        first_dict = json.load(open(file_path1))
        second_dict = json.load(open(file_path2))

    if (file1_ext and file2_ext) == '.yaml' or '.yml':
        first_dict = yaml.safe_load(open(file_path1))
        second_dict = yaml.safe_load(open(file_path2))

    return dict(first_dict), dict(second_dict)
