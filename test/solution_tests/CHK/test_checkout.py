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
        ("E", 40),
        ("AA", 100),
        ("AAA", 130),
        ("AAAA", 180),
        ("AAAAA", 200),
        ("AAAAAA", 250),
        ("AAAAAAAA", 330),
        ("AAAAAAAAA", 380),
        ("BB", 45),
        ("BBB", 75),
        ("BBBB", 90),
        ("BABABCAA", 275),
        ("EEB", 80),
        ("EEBB", 110),
        ("EEEEBB", 160),
        ("EEEE", 160),
    ]
)
def test_checkout(skus, price):
    assert checkout(skus) == price


