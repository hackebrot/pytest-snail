def test_cli_option(testdir):
    testdir.makepyfile(
        """
        import pytest

        @pytest.fixture(name="friends")
        def fixture_friends():
            return "🐸🐼🦊🦁🐨🐯🦊🦊🐻🐻🐻"

        def test_slow(friends):
            assert f"Hello {friends}" == "Hello 🐸🐼🦊🦁🐨🐯🦊🦊🐻🐻🐻"
        """
    )

    result = testdir.runpytest("-v", "--turtle", "2.0")
    result.stdout.fnmatch_lines(["*::test_slow*PASSED*"])
    assert result.ret == 0
