#!/usr/bin/python3
"""Module with the function read_file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename) as file:
        r_text = file.read()
        print(r_text, end="")
