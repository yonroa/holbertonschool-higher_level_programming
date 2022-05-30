#!/usr/bin/python3
"""
The "4-print_square" module

This module supplies one function, print_square(). For example,

>>> print_square(3)
###
###
###
"""


def print_square(size):
    """Print a square with the character '#'
    Print some error if something is wrong
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
