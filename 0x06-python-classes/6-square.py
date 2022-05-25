#!/usr/bin/python3
"""Define a square class"""


class Square:
    """A simple class without methods or public attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation safe of an square"""
        self.size = size
        self.position = position

    @property
    def position(self):
        """int: Return the size of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the attribute attribute"""
        self.__position = value
        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """int: Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the attribute size"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """int: Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the char '#'"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for x in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
