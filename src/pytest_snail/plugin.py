"""Plugin for adding a marker to slow running tests."""

from collections import defaultdict

import pytest


class Snail:
    """Plugin for adding a marker to slow running tests."""

    def __init__(self, config):
        """Initialize the plugin and load test durations from the cache."""
        self.config = config
        self.durations = defaultdict(dict)
        self.durations.update(self.config.cache.get("cache/snail", defaultdict(dict)))

    def pytest_runtest_logreport(self, report):
        """Keep track of test durations for test items by test phase."""
        self.durations[report.nodeid][report.when] = report.duration

    @pytest.mark.tryfirst
    def pytest_collection_modifyitems(self, session, config, items):
        """Add the snail marker to slow running tests."""
        for item in items:
            duration = sum(self.durations[item.nodeid].values())
            if duration > self.config.option.snail:
                item.add_marker(pytest.mark.snail)

    def pytest_sessionfinish(self, session):
        """Write test durations to the cache."""
        cached_durations = self.config.cache.get("cache/snail", defaultdict(dict))
        cached_durations.update(self.durations)
        self.config.cache.set("cache/snail", cached_durations)

    def pytest_configure(self, config):
        """Register and document the snail marker."""
        config.addinivalue_line("markers", "snail: marker for slow running tests")


def pytest_addoption(parser):
    """Add the --snail CLI option."""
    group = parser.getgroup("snail")
    group.addoption(
        "--snail",
        action="store",
        type=float,
        default=5.0,
        metavar="DURATION",
        help="tests running longer than this value will be marked",
    )


def pytest_configure(config):
    """Hook implementation that registers the plugin."""
    config.pluginmanager.register(Snail(config), "snail_plugin")


def pytest_unconfigure(config):
    """Hook implementation that unregisters the plugin."""
    config.pluginmanager.unregister("snail_plugin")
