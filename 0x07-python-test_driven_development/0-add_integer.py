#!/usr/bin/python3
""" 
The "add_integer" module

This module supplies one function, add_integer(). For example.,

>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """Return a + b."""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
