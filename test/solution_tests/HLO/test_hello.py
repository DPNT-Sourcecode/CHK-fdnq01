import pytest
from solutions.HLO import hello


@pytest.mark.parametrize(
    "friend_name,expected",
    [
        ("Craftsman", "Hello, World!"),
        ("Mr. X", "Hello, World!"),
    ]
)
def test_hello(friend_name, expected):
    assert hello(friend_name) == expected
