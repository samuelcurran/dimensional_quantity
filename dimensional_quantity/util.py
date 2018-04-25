import itertools
from operator import eq
from typing import Sequence, Iterable, Callable, Any


def seq_equal(s1: Sequence, s2: Sequence) -> bool:
    """
    Returns True is all elements of two sequences are equal.
    """
    return all(itertools.starmap(eq, itertools.zip_longest(s1, s2)))


def zipmap(func: Callable[Any], *sequences: Sequence) -> Iterable:
    """
    Zips sequences together and maps a function to them.
    """
    return itertools.starmap(func, itertools.zip_longest(*sequences))
