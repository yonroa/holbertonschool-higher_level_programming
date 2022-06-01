#!/usr/bin/python3
"""Define an empty Reactangle Class"""


class Rectangle:
    """A simple class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation safe of an rectangle"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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
                    rec_print += str(self.print_symbol)
                rec_print += '\n'
            return rec_print[:-1]
        else:
            return ""

    def __repr__(self):
        """Return a string representation of the rectangle
        to be able to recreate a new instance
        """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Print a delete message when an instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size"""
        return cls(size, size)
