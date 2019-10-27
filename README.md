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

## Community

Please check out the [good first issue][good first issue] label for tasks,
that are good candidates for your first contribution to
**pytest-snail**. Your contributions are greatly
appreciated! Every little bit helps, and credit will always be given!

You can also support the development of this project by volunteering to
become a maintainer, which means you will be able to triage issues, merge
pull-requests, and publish new releases. If you're interested, please submit
a pull-request to add yourself to the list of [maintainers][community] and
we'll get you started! 🚀

Please note that **pytest-snail** is released with a [Contributor Code of
Conduct][code-of-conduct]. By participating in this project you agree to
abide by its terms.

[good first issue]: https://github.com/hackebrot/pytest-snail/labels/good%20first%20issue
[code-of-conduct]: https://github.com/hackebrot/pytest-snail/blob/master/CODE_OF_CONDUCT.md
[community]: https://github.com/hackebrot/pytest-snail/blob/master/COMMUNITY.md

## License

Distributed under the terms of the MIT license, **pytest-snail** is free and
open source software.
