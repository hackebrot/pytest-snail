import textwrap


def test_marker(testdir):
    """Test that the snail marker is applied to slow tests."""

    testdir.makepyfile(
        test_adventurers=textwrap.dedent(
            """
            import time
            import typing
            import attr
            import pytest


            @attr.s(auto_attribs=True, kw_only=True)
            class Adventurer:
                name: str
                profile: str = attr.ib(init=False)

                def eat(self, food) -> None:
                    print(f"{self.profile} {self.name} is eating. {food}")


            class Panda(Adventurer):
                profile: str = "🐼"


            class Bear(Adventurer):
                profile: str = "🐻"


            class Lion(Adventurer):
                profile: str = "🦁"


            @pytest.fixture(name="group")
            def fixture_group():
                return [
                    Panda(name="Dave"),
                    Lion(name="Julia"),
                    Lion(name="Jess"),
                    Bear(name="Audrey"),
                    Bear(name="Danny"),
                    Lion(name="Michael"),
                ]


            @pytest.fixture(name="morning_group")
            def fixture_morning_group(group):
                for adventurer in group:
                    adventurer.eat("🥐")
                time.sleep(0.25)

                yield group


            @pytest.fixture(name="evening_group")
            def fixture_evening_group(group):
                yield group

                for adventurer in group:
                    adventurer.eat("🍜")
                time.sleep(0.5)


            @pytest.fixture(name="hiking_group")
            def fixture_hiking_group(group):
                for adventurer in group:
                    adventurer.eat("🥐")
                time.sleep(0.25)

                yield group

                for adventurer in group:
                    adventurer.eat("🍜")
                time.sleep(0.5)


            def test_morning_walk(morning_group):
                print("Adventurers going for a walk. 🌳")
                # This will have a slow setup
                time.sleep(1)


            def test_evening_walk(evening_group):
                print("Adventurers going for a walk. 🌳")
                time.sleep(1)


            def test_day_hike(hiking_group):
                print("Adventurers hiking a mountain. ⛰")
                time.sleep(2)
            """
        )
    )

    testdir.makeconftest(
        """
        def pytest_collection_modifyitems(items, config):
            for item in items:
                if item.get_closest_marker("snail"):
                    print(f"Found snail marker on {item.name}")
                else:
                    print(f"Did not find snail marker on {item.name}")
        """
    )
    result1 = testdir.runpytest("-v")
    result1.stdout.fnmatch_lines(
        [
            "*Did not find snail marker on test_morning_walk*",
            "*Did not find snail marker on test_evening_walk*",
            "*Did not find snail marker on test_day_hike*",
            "*::test_morning_walk*PASSED*",
            "*::test_evening_walk*PASSED*",
            "*::test_day_hike*PASSED*",
        ]
    )
    assert result1.ret == 0

    result2 = testdir.runpytest("-v", "--snail", "2.0")
    result2.stdout.fnmatch_lines(
        [
            "*Did not find snail marker on test_morning_walk*",
            "*Did not find snail marker on test_evening_walk*",
            "*Found snail marker on test_day_hike*",
            "*::test_morning_walk*PASSED*",
            "*::test_evening_walk*PASSED*",
            "*::test_day_hike*PASSED*",
        ]
    )
    assert result2.ret == 0

    result3 = testdir.runpytest("-v", "--snail", "1.5")
    result3.stdout.fnmatch_lines(
        [
            "*Did not find snail marker on test_morning_walk*",
            "*Found snail marker on test_evening_walk*",
            "*Found snail marker on test_day_hike*",
            "*::test_morning_walk*PASSED*",
            "*::test_evening_walk*PASSED*",
            "*::test_day_hike*PASSED*",
        ]
    )
    assert result3.ret == 0
