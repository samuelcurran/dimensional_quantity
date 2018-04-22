from hypothesis.strategies import floats
from hypothesis import assume, given


@given(
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False))
def test_addition(a, b, c):
    assert (a + b) == (b + a)
    assert ((a + b) + c) == (a + (b + c))
    assert (a + 0.0) == a
    assert (a * (b + c)) == ((a * b) + (a * c))


@given(
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False),
    floats(allow_nan=False, allow_infinity=False))
def test_multiplication(a, b, c):
    assert (a * b) == (b * a)
    assert ((a * b) * c) == (a * (b * c))
    assert (a * 1.0) == a
    assert (a * (b + c)) == ((a * b) + (a * c))
