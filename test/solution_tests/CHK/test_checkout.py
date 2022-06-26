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
        ("AA", 100),
        ("AAA", 130),
        ("AAAA", 180),
        ("AAAAA", 230),
        ("AAAAAA", 260),
        ("BB", 45),
        ("BBB", 75),
        ("BBBB", 90),
        ("BABABCAA", 275),
    ]
)
def test_checkout(skus, price):
    assert checkout(skus) == price
