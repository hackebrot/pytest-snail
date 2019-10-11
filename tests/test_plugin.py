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
