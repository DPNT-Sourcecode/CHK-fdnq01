import pytest
from solutions.CHK import checkout


@pytest.mark.parametrize(
    "skus,price",
    [
        ("A", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15),
        ("ABCD", 115),
        ("E", -1),
        ("AAA", 130),
        ("AAAA", 180),
        ("AAAAA", 230),
        ("AAAAAA", 260),
        ("BB", 45),
        ("BBB", 75),
        ("BBBB", 90),
    ]
)
def test_checkout(skus, price):
    assert checkout(skus) == price
