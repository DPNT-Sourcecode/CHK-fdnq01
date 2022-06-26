import pytest
from solutions.CHK import checkout


@pytest.mark.parametrize(
    "skus,price",
    [
        ("A", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15),
        ("E", 40),
        ("A", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15),
        ("E", 40),
        ("F", 10),
        ("G", 20),
        ("H", 10),
        ("I", 35),
        ("J", 60),
        ("K", 80),
        ("L", 90),
        ("M", 15),
        ("N", 40),
        ("O", 10),
        ("P", 50),
        ("Q", 30),
        ("R", 50),
        ("S", 30),
        ("T", 20),
        ("U", 40),
        ("V", 50),
        ("W", 20),
        ("X", 90),
        ("Y", 10),
        ("Z", 50),

        ("ABCD", 115),
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
        ("FF", 20),
        ("FFF", 20),

        ("H" * 5, 45),
        ("H" * 7, 65),
        ("H" * 10, 80),
        ("KK", 150),
        ("P" * 5, 200),
        ("QQQ", 80),
        ("U" * 4, 120),
        ("VV", 90),
        ("VVV", 130),
    ]
)
def test_checkout(skus, price):
    assert checkout(skus) == price




