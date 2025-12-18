
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 5, 4),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected



@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 2, 3),
        (2, 5, -3),
        (0, 7, -7),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 4, 12),
        (-2, 3, -6),
        (0, 999, 0),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (-10, 2, -5),
        (1, 3, 0.3333333333),  
    ],
)
def test_divide_valid(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)

def test_divide_by_zero_raises(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

@pytest.mark.parametrize(
    "n,expected",
    [
        (-10, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (97, True),
        (99, False),
    ],
)
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) is expected
