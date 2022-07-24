import pytest

from . import code


@pytest.mark.parametrize(
    "arg, expected",
    [
        (None, "a"),
        (True, "b"),
        (False, "c"),
    ],
)
def test_code(arg, expected):
    assert code.code(arg) == expected
