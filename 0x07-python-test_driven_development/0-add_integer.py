#!/usr/bin/python3
""" 
The "add_integer" module

This module supplies one function, add_integer(). For example.,

>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """Return a + b.

    Works whit integers and floats:

    >>> add_integer(8, -3)
    5

    >>> add_integer(37.5, -7.3)
    30

    a and b must be numbers:

    >>> add_integer(4, "hello")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer

    >>> add_integer(True, -8)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
