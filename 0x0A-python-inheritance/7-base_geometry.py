#!/usr/bin/python3
"""Module with a simple class"""


class BaseGeometry:
    """A simple class with one method"""

    def area(self):
        """method that raise an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates the value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
