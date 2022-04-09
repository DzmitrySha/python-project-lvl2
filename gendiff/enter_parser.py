# parsing module

import os
import json
import yaml


def parser(file_path1, file_path2):
    """Make dicts from paths."""
    file1_ext = os.path.splitext(file_path1)
    file2_ext = os.path.splitext(file_path2)

    if (file1_ext and file2_ext) == '.json':
        dict_1 = json.load(open(file_path1))
        dict_2 = json.load(open(file_path2))

    if (file1_ext and file2_ext) == '.yaml' or '.yml':
        dict_1 = yaml.safe_load(open(file_path1))
        dict_2 = yaml.safe_load(open(file_path2))

    return dict(dict_1), dict(dict_2)
