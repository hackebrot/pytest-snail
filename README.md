# pytest-snail

Plugin for adding a marker to slow running tests. 🐌

## Installation

You can install **pytest-snail** via [pip][pip] from [PyPI][PyPI]:

```text
pip install pytest-snail==0.1.0.dev1
```
[pip]: https://pypi.python.org/pypi/pip/
[PyPI]: https://pypi.org/project/pytest-snail/

## Usage

When you run your tests, **pytest-snail** keeps track of test durations for
each test item by test phase: setup, call, and teardown. ⏱

The next time you run your tests, **pytest-snail** adds a `snail` marker to
all test items with a recorded, accumulated duration that is equal or longer
than the value for the `--snail` CLI option (defaults to `5.0` seconds).

You can then use pytest's marker expressions to select or deselect tests.

### Examples

First run your tests to measure test durations:

```text
pytest
```

Then deselect all tests that take longer than `5.0` seconds to complete:

```text
pytest -m "not snail"
```

Select only tests that take longer than `10.0` seconds to complete:

```text
pytest --snail 10.0 -m snail
```

## License

Distributed under the terms of the MIT license, **pytest-snail** is free and
open source software.
