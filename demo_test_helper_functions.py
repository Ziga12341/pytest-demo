import os
import json


def write_test_output_to_json(test_name, output):
    # Path to the JSON file
    json_file_path = 'data/test_suite_outputs.json'

    # Initially assume the file does not exist and create an empty dictionary
    data = {}

    # If the file exists, load its current contents
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)

    # Check if the key exists, if not, set the default to an empty list
    if test_name in data:
        data[test_name].extend(output)
    else:
        data[test_name] = output

    # Write the updated dictionary back to the file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)