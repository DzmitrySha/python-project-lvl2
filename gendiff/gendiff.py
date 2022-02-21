import json


def generate_diff(file_path1, file_path2):
    differences = ''
    first_file = dict(json.load(open(file_path1)))
    second_file = dict(json.load(open(file_path2)))

    cross_files_keys = first_file.keys() & second_file.keys()
    file1_unique_keys = first_file.keys() - second_file.keys()
    file2_unique_keys = second_file.keys() - first_file.keys()

    for key in cross_files_keys:
        if first_file[key] == second_file[key]:
            differences += f"  {key}: {first_file[key]}\n"
        else:
            differences += f"- {key}: {first_file[key]}\n"
            differences += f"+ {key}: {second_file[key]}\n"
    for key in file1_unique_keys:
        differences += f"- {key}: {first_file[key]}\n"
    for key in file2_unique_keys:
        differences += f"+ {key}: {second_file[key]}\n"

    return "{\n" + differences.lower() + "}"
