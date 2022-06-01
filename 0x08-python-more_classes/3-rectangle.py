#!/usr/bin/python3
"""Define an empty Reactangle Class"""


class Rectangle:
    """A simple class"""

    def __init__(self, width=0, height=0):
        """Instantiation safe of an rectangle"""
        self.__width = width
        self.__height = height

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

    def area(self):
        """Method to return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Method to return the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Return a nice rectangle made with the char '#'"""
        if self.__height != 0 and self.__width != 0:
            rec_print = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rec_print += '#'
                rec_print += '\n'
            return rec_print[:-1]
        else:
            return ""
