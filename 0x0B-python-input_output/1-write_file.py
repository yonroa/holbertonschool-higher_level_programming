#!/usr/bin/python3
"""Module with the function write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w') as file:
        n_lines = file.write(text)
        return n_lines
