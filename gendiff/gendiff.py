from enter_parser import parser


def generate_diff(file_path1, file_path2):
    differences = ''
    first_file, second_file = parser(file_path1, file_path2)

    cross_files_keys = sorted(first_file.keys() & second_file.keys())
    file1_unique_keys = sorted(first_file.keys() - second_file.keys())
    file2_unique_keys = sorted(second_file.keys() - first_file.keys())

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
