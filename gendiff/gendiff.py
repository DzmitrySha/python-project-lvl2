from gendiff.enter_parser import parser


def generate_diff(file_path1, file_path2):
    first_dict, second_dict = parser(file_path1, file_path2)

    cross_files_keys = sorted(first_dict.keys() & second_dict.keys())
    file1_unique_keys = sorted(first_dict.keys() - second_dict.keys())
    file2_unique_keys = sorted(second_dict.keys() - first_dict.keys())

    def make_plain_diff(first_dict, second_dict):
        diff = ''
        for key in cross_files_keys:
            if first_dict[key] == second_dict[key]:
                diff += f"  {key}: {first_dict[key]}\n"
            else:
                diff += f"- {key}: {first_dict[key]}\n"
                diff += f"+ {key}: {second_dict[key]}\n"
        for key in file1_unique_keys:
            diff += f"- {key}: {first_dict[key]}\n"
        for key in file2_unique_keys:
            diff += f"+ {key}: {second_dict[key]}\n"

        return "{\n" + diff.lower() + "}"

    return make_plain_diff(first_dict, second_dict)
