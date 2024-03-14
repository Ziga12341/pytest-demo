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