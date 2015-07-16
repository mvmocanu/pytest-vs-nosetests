## Pytest vs Nosetests

This is an example of how tests are written using two different test runners. We have two identical projects. The only difference is that one is using nosetest runner to run the tests, the other one is using pytest runner. 

We can use a diff tool to see all the diferences between the two projects. For example `meld`:
~~~~
$ meld testing-nosetests testing-pytest
~~~~

### How to Install 

In order to run the tests, we need two virtual environments - one for each project. Each project has it's own requirements.txt. After the virtual environemnt is created, the requirements must be installed.

* testing-nosetests:
~~~~~~
$ pwd
testing-nosetests
$ virtualenv ve
$ source ve/bin/activate
$ pip install -r requirements.txt
~~~~~~
* testing-pytest:
~~~~~~
$ pwd
testing-pytest
$ virtualenv ve
$ source ve/bin/activate
$ pip install -r requirements.txt
~~~~~~

### How to run the tests

* testing-nosetests:
~~~~~~
$ ./manage.py test
~~~~~~

* testing-pytest:
~~~~~
$ py.test
~~~~~

### How to see how failing tests are looking
There is an example of failing tests and one can see the difference that the asserts outputs

* testing-nosetests:
~~~~~~
$ mv testing_project/fail testing_project/test_fail.py
$ ./manage.py test testing_project.test_fail
~~~~~~

* testing-pytest:
~~~~~
$ mv testing_project/fail testing_project/test_fail.py
$ py.test testing_project/test_fail.py
~~~~~
