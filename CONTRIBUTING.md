# Contributing

Install Poetry and run `poetry install` to install dependencies. Then run `poetry shell` to activate the virtual environment.

Run `pre-commit install` to install the pre-commit hooks.

## Commit messages

type(scope/[subscope]): Title starting with uppercase and sentence ending with period.
More than 80 charactes use the body of the commit message.

Scope and subscopes are optional.

DO NOT use a bunch of different types: feat, fix, refactor should be more than enough.

## Running the Tests

You can run the tests using `pytest`:

```bash
pytest
```
