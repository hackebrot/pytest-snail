def test_cli_option(testdir):
    testdir.makepyfile(
        """
        import pytest

        @pytest.fixture(name="friends")
        def fixture_friends():
            return "🐸🐼🦊🦁🐨🐯🦊🦊🐻🐻🐻"

        def test_friends(friends):
            assert f"Hello {friends}" == "Hello 🐸🐼🦊🦁🐨🐯🦊🦊🐻🐻🐻"
        """
    )

    result = testdir.runpytest("-v", "--turtle", "2.0")
    result.stdout.fnmatch_lines(["*::test_friends*PASSED*"])
    assert result.ret == 0


def test_marker(testdir):
    testdir.makepyfile(
        """
        import time
        import pytest

        @pytest.fixture(name="friends")
        def fixture_friends():
            return "🐸🐼🦊🦁🐨🐯🦊🦊🐻🐻🐻"

        def test_slow(friends):
            time.sleep(1.0)
            assert f"Hello {friends}" == "Hello 🐸🐼🦊🦁🐨🐯🦊🦊🐻🐻🐻"
        """
    )
    result1 = testdir.runpytest("-v")
    result1.stdout.fnmatch_lines(["*::test_slow*PASSED*"])
    assert result1.ret == 0

    testdir.makeconftest(
        """
        def pytest_collection_modifyitems(items, config):
            for item in items:
                if item.get_closest_marker("turtle"):
                    print(f"Found turtle marker on {item.name}")
        """
    )

    result2 = testdir.runpytest("-v", "--turtle", "0.5")
    result2.stdout.fnmatch_lines(["*Found turtle marker on test_slow*"])
    assert result2.ret == 0
