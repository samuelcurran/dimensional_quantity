import math
import pytest

from hypothesis import given, assume
import hypothesis.strategies as st

from dimnum import DimensionalQuantity as dq

dqs = st.builds(dq, st.integers(max_value=10000),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5),
                  st.integers(min_value=-5, max_value=5))

dqs_like_units = st.builds(dq, st.integers(max_value=100000))

@given(dqs_like_units)
def test_add_identity(a):
        zero = dq(0)
        assert (a + zero) == a

@given(dqs_like_units, dqs_like_units)
def test_add_communative(a, b):
        assert (a + b) == (b + a)

@given(dqs_like_units, dqs_like_units, dqs_like_units)
def test_add_associative(a, b, c):
    assert ((a + b) + c) == (a + (b + c))

@given(dqs)
def test_mul_identity(a):
    one = dq(1)
    assert (a * one) == a

@given(dqs, dqs)
def test_mul_communative(a, b):
    assert (a * b) == (b * a)

@given(dqs, dqs, dqs)
def test_mul_associative(a, b, c):
    assert ((a * b) * c) == (a * (b * c))

@given(dqs_like_units, dqs_like_units, dqs_like_units)
def test_distributive(a, b, c):
    assert (a * (b + c)) == ((a * b) + (a * c))
    