import pytest
from solutions.HLO import hello


@pytest.mark.parametrize(
    "friend_name,expected",
    [
        ("Craftsman", "Hello, Craftsman!"),
        ("Mr. X", "Hello, Mr. X!"),
        ("John", "Hello, John!"),
    ]
)
def test_hello(friend_name, expected):
    assert hello(friend_name) == expected
