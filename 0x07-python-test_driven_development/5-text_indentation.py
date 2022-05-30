#!/usr/bin/python3
"""
The "5-text_indentation" module

This module supplies one function, text_indentation(). For example,

>>> text_indentation("How are you? I am fine")
How are you?

I am fine
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :
    Print some error if something is wrong
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print(text, end="")
