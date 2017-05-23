# Pyramid Cifar-10

## [Online Demo](https://pyramid-cifar-10.herokuapp.com/)

## How to Install

- Change directory into your newly created project.

    cd cifar_10

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
