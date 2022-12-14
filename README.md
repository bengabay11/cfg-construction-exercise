[![Unit Tests](https://github.com/bengabay11/cfg-construction-exercise/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/bengabay11/cfg-construction-exercise/actions/workflows/unit-tests.yml)

# CFG Construction Exercise
This project reads from an invented assembly language and creates a Control Flow Graph From it

![asdsad](assets/even_number_example.jpg)
## Examples
To demonstrate the cfg construction, There are a few examples using the invented assembly language.

You can simply run each example inside [examples](examples) folder.
- Exponentiation
- Even Number
- Print if number is even or odd from zero to maximum number

## Dependencies
This project is using [pipenv](https://pipenv.pypa.io/en/latest/) for package management.

To create Python Virtual Environment and install all dependencies:
```
$ pipenv install
```
see [Pipfile](Pipfile) for more information

## Testing
This project is using [pytest](https://docs.pytest.org/en/7.1.x/#id1) for testing.
The tests are running automatically on every push to the repo.

To run the tests locally:
```
$ pipenv run unit-tests
```
For coverage report:
```
$ pipenv run unit-test-cov
```
## Lint
This project is using [pylint](https://pypi.org/project/pylint/) for linting.

To run lint check:
```
$ pipenv run lint
```
to change the linting configuration, see [.pylintrc](.pylintrc)

## License
This project is licensed under the terms of the MIT license.