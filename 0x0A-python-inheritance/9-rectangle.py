#!/usr/bin/python3
"""Module with the child class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize a rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return a description of the rectangle"""
        return str(f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height
