## Pytest vs Nosetests

This is an example of how tests are written using two different test runners. We have two identical projects. The only difference is that one is using nosetest runner to run the tests, the other one is using pytest runner. 

### How to Install 

In order to run the tests, we need two virtual environments. Each project has it's own requirements.txt. After the virtual environemnt is created, the requirements must be installed.

### How to run

* testing-nosetests:
~~~~~~
./manage.py test
~~~~~~

* testing-pytest:
~~~~~
py.test
~~~~~
