import json


def generate_diff(file_path1, file_path2):
    diff_list = ''
    first_file = dict(json.load(open(file_path1)))
    second_file = dict(json.load(open(file_path2)))

    cross_files_keys = first_file.keys() & second_file.keys()
    file1_unique_keys = first_file.keys() - second_file.keys()
    file2_unique_keys = second_file.keys() - first_file.keys()

    # print(cross_files_keys)
    # print(file1_unique_keys)
    # print(file2_unique_keys)

    # Рабочий вариант 1
    for key in cross_files_keys:
        if first_file[key] == second_file[key]:
            diff_list += f"  {key}: {first_file[key]}\n"
        else:
            diff_list += f"- {key}: {first_file[key]}\n"
            diff_list += f"+ {key}: {second_file[key]}\n"
    for key in file1_unique_keys:
        diff_list += f"- {key}: {first_file[key]}\n"
    for key in file2_unique_keys:
        diff_list += f"+ {key}: {second_file[key]}\n"

    # Рабочий вариант 2
    # for key1, value1 in first_file.items():
    #     for key2, value2 in second_file.items():
    #         if key1 == key2 and value1 == value2:
    #             diff_list += f"  {key1}: {value1}\n"
    #         elif key1 == key2 and value1 != value2:
    #             diff_list += f"- {key1}: {value1}\n"
    #             diff_list += f"+ {key2}: {value2}\n"
    # for key1 in file1_unique_keys:
    #     diff_list += f"- {key1}: {first_file[key1]}\n"
    # for key2 in file2_unique_keys:
    #     diff_list += f"+ {key2}: {second_file[key2]}\n"

    return "{\n" + diff_list.lower() + "}"


# print(generate_diff('/home/dzmitry/python-project-lvl2/'
#                     'tests/fixtures/file1.json',
#                     '/home/dzmitry/python-project-lvl2/'
#                     'tests/fixtures/file2.json'))
