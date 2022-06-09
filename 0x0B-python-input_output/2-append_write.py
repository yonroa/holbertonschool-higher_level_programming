#!/usr/bin/python3
"""Module with the function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a') as file:
        n_lines = file.write(text)
        return n_lines
