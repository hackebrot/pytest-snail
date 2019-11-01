def test_cli_option_default(testdir):
    testdir.makepyfile(
        """
        def test_snail(request):
            assert request.config.option.snail == 5.0
        """
    )
    result = testdir.runpytest("-v")
    result.stdout.fnmatch_lines(["*::test_snail*PASSED*"])
    assert result.ret == 0


def test_cli_option_custom(testdir):
    testdir.makepyfile(
        """
        def test_snail(request):
            assert request.config.option.snail == 2.0
        """
    )

    result = testdir.runpytest("-v", "--snail", "2.0")
    result.stdout.fnmatch_lines(["*::test_snail*PASSED*"])
    assert result.ret == 0
