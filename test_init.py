import os
import json


def json_init():
    # Define the structure of the JSON object
    data = {
        "setup_get_tokens_info": [],
        "test_1": [],
        "test_2": []
    }
    # Ensure the directory exists
    os.makedirs('data', exist_ok=True)

    # Specify the file path
    file_path = 'data/test_suite_outputs.json'

    # Create and write the JSON data to the file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    json_init()