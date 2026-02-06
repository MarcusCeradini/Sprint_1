# Steps to run on school laptop

1. Make sure Python and pip is installed:

`python --version` or `python3 --version`

`pip --version` or `pip3 --version`

2. Create a virtual environment

`python -m venv venv`


3. Activate the virtual environment

`venv\Scripts\Activate`

If this doesn't work, try running this first:

`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

If done right, you should see (venv) on the left side of your terminal's path

4. Install pygame

`pip install pygame` or `python -m pip install pygame-ce` for wake tech computers

Verify it is installed with: `pip show pygame`

5. Run program

`python game.py`