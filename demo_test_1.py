import pytest
import json
from demo_test_helper_functions import write_test_output_to_json

# mock api call to get token info from the API and write the output to json file
token_info_mock_data = [f"Mock token value output {i}" for i in range(100)]
write_test_output_to_json("setup_get_tokens_info", token_info_mock_data)


input_for_test_1_token_info = json.load(open("data/test_suite_outputs.json", "r"))["setup_get_tokens_info"]
@pytest.mark.parametrize("test_input_token_info", input_for_test_1_token_info)
def test_1(test_input_token_info):
    assert type(test_input_token_info) == str, f"""
------
Expected: {test_input_token_info}
------"""

    test_1_output = [f"Mock test 1 output of {test_input_token_info} {i}" for i in range(10)]

    write_test_output_to_json("test_1", test_1_output)