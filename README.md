# API End-to-End Testing Project with Dynamic Test Cases

## Introduction

This project is designed to address the unique challenges of testing API endpoints where the number of test cases can be dynamically determined based on the responses from the API itself. It leverages Python, pytest, and a custom setup to perform a series of dependent tests that validate the integrity and structure of the API responses. 

The tests are structured in a way that each subsequent test relies on the output of the previous one, starting with a set of predefined values to fetch initial data, which then serves as the foundation for more granular and detailed tests. This approach simulates a real-world scenario where API responses are interconnected, and the correctness of one part of the system can depend on the previous interactions.

## Description

The testing process begins with a preparation step that uses a fixed set of values to query the API and gather a list of new values. This is followed by three main tests: 

1. **Test 1**: Performs a get request for each value obtained during the preparation step and collects a list of codes returned by these calls.
2. **Test 2**: For each code collected in Test 1, it executes a request to fetch additional information about that code.
3. **Test 3**: Compiles codes that have additional information with the proper structure and performs further API calls for each combination of code and item obtained from Test 2.

The tests are designed to dynamically adjust the number of execution times based on the data received from the API, making the framework adaptable to various scenarios and data volumes. 

This project includes detailed instructions for setting up the testing environment, running tests, and adding new test cases. It also provides solutions for common issues such as permission denied errors when executing shell scripts.

By utilizing fixtures for common setup tasks, such as obtaining an API token, the project ensures that each test function is provided with the necessary context to execute correctly. This setup emphasizes the importance of dynamic testing in modern API development and provides a robust framework for validating complex interactions within an API.

## Key Features

- **Dynamic Test Execution**: Dynamically determines the number of tests to run based on API responses.
- **Dependent Tests**: Supports writing tests where the output of one test feeds into the next, mimicking real-world data flow.
- **Detailed Test Output**: Each test provides detailed feedback, including OK and FAIL statuses, with reasons for failures.
- **Fixture Support**: Utilizes pytest fixtures for common setup tasks, ensuring each test has the required context.
- **Customizable Test Suite**: Offers guidance on adding new test cases to the suite, allowing for easy expansion.

This project is ideal for developers and testers looking for a flexible and comprehensive approach to API testing, especially in scenarios where the data is dynamic and interconnected.


## INSTALL DEPENDENCIES

Create a virtual environment and install the dependencies from the requirements.txt file.
```bash
conda create -n pytest-demo
conda activate pytest-demo
```


```bash
pip install -r requirements.txt
```

## RUN TESTS
    
```bash
python test_init.py
pytest demo_test_1.py
pytest demo_test_2.py
python demo_test_teardown.py
```

## RUN TESTS FROM SHELL SCRIPT

```bash
./run_tests.sh
```

## PERMISSION DENIED ## 

if you get the following error:
`permission denied: ./run_tests.sh`

You need to give execution permission to the file:
```bash
chmod +x run_tests.sh
```

## ADDING NEW TEST CASES ##

First, you need to add the new test case in the test_init.py file.
After that, you need to create a new test file with the new test case.
Finally, you need to add the new test file in the run_tests.sh file.
