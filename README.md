# CFG Construction Exercise
This project reads from an invented assembly language and create a Control Flow Graph From it

## Examples
- Exponentiation
- Even Number
- Print List of Numbers

## Usage
```commandline
$ python examples/exponentiation.py
```

## Dependencies
This project is using [pipenv](https://pipenv.pypa.io/en/latest/) for package management.

To create Python Virtual Environment and install all dependencies:
```commandline
$ pipenv install
```
see [Pipfile](Pipfile) for more information

## Lint
This project is using [pylint](https://pypi.org/project/pylint/) for linting

To run lint check:
```commandline
$ pipenv run lint
```
to change the linting configuration, see [.pylintrc](.pylintrc)

## License
This project is licensed under the terms of the MIT license.