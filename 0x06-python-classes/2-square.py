#!/usr/bin/python3
"""Define a square class"""


class Square:
    """A simple class without methods or public attributes"""

    def __init__(self, size=0):
        """Instantiation safe of an square"""
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
