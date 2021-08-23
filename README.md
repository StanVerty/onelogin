# onelogin

1) clone code from repo:
git clone {link to repo}

2) create docker image:
docker image build ./ -t {image name}

3) run the docker container:
docker container run -it {image name} /bin/bash

4) once inside container run (also use this command to run the program repeatedly):
python onelogin.py

5) Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
Operands and operators shall be separated by one or more spaces
Mixed numbers will be represented by whole_numerator/denominator. e.g. “3_1/4”
Improper fractions and whole numbers are also allowed as operands.

6) To run unit test:
6.1. Comment out the last line in onelogin.py (# fraction_trick())
6.2. Run command:
python -m unittest test_onelogin.py
