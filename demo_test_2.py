import pytest
import json
from demo_test_helper_functions import write_test_output_to_json


input_for_test_2 = json.load(open("data/test_suite_outputs.json", "r"))["test_1"]
@pytest.mark.parametrize("test_input_token_info_and_test_1_output", input_for_test_2)
def test_2(test_input_token_info_and_test_1_output):
    assert type(test_input_token_info_and_test_1_output) == str, f"""
------
Expected: {test_input_token_info_and_test_1_output}
------"""

    test_2_output = [f"Mock test 2 output of {test_input_token_info_and_test_1_output} with additional data from api"]

    write_test_output_to_json("test_2", test_2_output)