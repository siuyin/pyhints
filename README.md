# PyHints is a series of experiments using python type hints

The package manager used is `uv`.

Experiments include:
* asyncio for python asynchronous io and coroutines
* dict to demonstrate python typed dictionaries
* fastapi showing a python typed web framework
* mypy a python type checker
* `pydantic_ai` an agent framework
* `typing_test` demonstrates pytype lenient type checking
* class show python classes and methods
* fastapi go comparison
* pydantic data model validation library

## Tooling
* `uvx ruff check --watch` to lint
* `uvx ruff format` to format python code within current folder
* `uvx pytype .` or `uvx mypy .` to type check python code within current folder

Note: pytype currently (2025-06-22) upto python 3.12


* `uv sync` to synchronize dependencies
* `uv run mypy_test.py` etc to run python code

