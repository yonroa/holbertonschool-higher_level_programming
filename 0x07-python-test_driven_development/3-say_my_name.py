#!/usr/bin/python3
"""
The "3-say_my_name.py" module

This module supplies one function, say_my_name(). For example,

>>> say_my_name(Yon, Roa)
My name is Yon Roa
"""


def say_my_name(first_name, last_name=""):
    """Print the string "My name is" with a name and a last name
    Print some error if something is wrong
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
