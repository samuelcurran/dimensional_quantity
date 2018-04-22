import itertools


def seq_equal(seq1, seq2) -> bool:
    """
    Returns True is all elements of two equal-length sequences are equal using the == comaprison.
    """
    if len(seq1) != len(seq2):
        return False
    else:
        for a, b in zip(seq1, seq2):
            if a != b:
                return False

        return True


def zipmap(func, *sequences):
    """
    Zips sequences together and maps a function to them.
    """
    return itertools.starmap(func, zip(*sequences))
