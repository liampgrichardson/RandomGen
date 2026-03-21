# What is RandomGen?

`RandomGen` is a Python class that generates random numbers from a user-defined list, where each number is chosen according to a specified discrete probability distribution. You provide a list of numbers and a corresponding list of probabilities (which must sum to 1), and `RandomGen` will return numbers based on those probabilities. This is useful for simulations, probabilistic algorithms, or any scenario where you need to sample values according to custom likelihoods.

Prerequisites:
Requires python 3.10

How to use:
- create venv or .venv
- Clone this repo and run main.py for a working example implementation of `next_num`

How to run unit tests:
- create venv or .venv
- pip install -r dev-requirements.txt
- python -m unittest discover

How to run coverage and view report then html:
- create venv or .venv
- pip install -r dev-requirements.txt
- coverage run -m unittest discover
- coverage report
- coverage html
- go to finder and open htmlcov/index.html in browser

How to run linting:
- create venv or .venv
- pip install -r dev-requirements.txt
- pylint src/ tests/