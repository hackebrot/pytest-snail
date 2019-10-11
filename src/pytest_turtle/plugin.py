"""Plugin for adding markers to slow running tests."""

from collections import defaultdict

import pytest


class Turtle:
    """Plugin for adding markers to slow running tests."""

    def __init__(self, config):
        """Initialize the plugin and load test durations from the cache."""
        self.config = config
        self.durations = defaultdict(dict)
        self.durations.update(self.config.cache.get("cache/turtle", defaultdict(dict)))

    def pytest_runtest_logreport(self, report):
        """Keep track of test durations for test items by test phase."""
        self.durations[report.nodeid][report.when] = report.duration

    @pytest.mark.tryfirst
    def pytest_collection_modifyitems(self, session, config, items):
        """Add the turtle marker to slow running tests."""
        for item in items:
            duration = sum(self.durations[item.nodeid].values())
            if duration > self.config.option.turtle:
                item.add_marker(pytest.mark.turtle)

    def pytest_sessionfinish(self, session):
        """Write test durations to the cache."""
        cached_durations = self.config.cache.get("cache/turtle", defaultdict(dict))
        cached_durations.update(self.durations)
        self.config.cache.set("cache/turtle", cached_durations)

    def pytest_configure(self, config):
        """Register and document the turtle marker."""
        config.addinivalue_line("markers", "turtle: marker for slow running tests")


def pytest_addoption(parser):
    """Add the --turtle CLI option."""
    group = parser.getgroup("turtle")
    group.addoption(
        "--turtle",
        action="store",
        type=float,
        default=5.0,
        metavar="DURATION",
        help="tests running longer than this value will be marked",
    )


def pytest_configure(config):
    """Hook implementation that registers the plugin."""
    config.pluginmanager.register(Turtle(config), "turtle_plugin")


def pytest_unconfigure(config):
    """Hook implementation that unregisters the plugin."""
    config.pluginmanager.unregister("turtle_plugin")
