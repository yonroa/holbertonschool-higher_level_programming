#!/usr/bin/python3
"""Define an empty Reactangle Class"""


class Rectangle:
    """A simple class"""

    def __init__(self, width=0, height=0):
        """Instantiation safe of an rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
