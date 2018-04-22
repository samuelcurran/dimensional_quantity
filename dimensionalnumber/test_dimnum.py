import dimnum

from hypothesis.strategies import integers
from hypothesis import assume, given


@given(integers(), integers(), integers())
def test_addition(a, b, c):
    assert (a + b) == (b + a)
    assert ((a + b) + c) == (a + (b + c))
    assert (a + 0) == a
    assert (a * (b + c)) == ((a * b) + (a * c))


@given(integers(), integers(), integers())
def test_multiplication(a, b, c):
    assert (a * b) == (b * a)
    assert ((a * b) * c) == (a * (b * c))
    assert (a * 1) == a
    assert (a * (b + c)) == ((a * b) + (a * c))
