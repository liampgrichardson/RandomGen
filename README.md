# nextNum
repo for nextNum

Prerequisites:
Requires python 3.10

How to use:
- create venv or .venv
- Clone this repo and run main.py for a working example implementation of nextNum

How to run tests:
- create venv or .venv
- pip install -r dev-requirements.txt
- python -m unittest discover

How to run coverage and view report then html:
- create venv or .venv
- pip install -r dev-requirements.txt
- coverage run python -m unittest discover
- coverage report
- coverage html
- go to finder and open htmlcov/index.html in browser

How to run linting:
- create venv or .venv
- pip install -r dev-requirements.txt
- pylint src/ tests/