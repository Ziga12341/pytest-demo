#!/bin/bash

# Script to run various tests

echo "Starting tests..."

# Run python test on test_init.py
echo "Running python test on test_init.py"
python3 test_init.py

# Run pytest on demo_test_1.py
echo "Running pytest on demo_test_1.py"
pytest demo_test_1.py

# Run pytest on demo_test_2.py
echo "Running pytest on demo_test_2.py"
pytest demo_test_2.py

# Run python test on demo_test_teardown.py
echo "Running python test on demo_test_teardown.py"
python3 demo_test_teardown.py

echo "Tests completed."