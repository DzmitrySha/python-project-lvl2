# make format json module
import json


def format_json(diff):
    with open("data_file.json", "w") as write_file:
        json.dump(diff, write_file)
    return json.dumps(diff, indent=4)
