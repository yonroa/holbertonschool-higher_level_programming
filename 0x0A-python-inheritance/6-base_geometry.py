#!/usr/bin/python3
"""Module with a simple class"""


class BaseGeometry:
    """A simple class with one method"""

    def area(self):
        """function that raise an error"""
        raise Exception("area() is not implemented")
