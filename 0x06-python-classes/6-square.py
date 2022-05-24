#!/usr/bin/python3
"""Define a square class"""


class Square:
    """A simple class without methods or public attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation safe of an square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: Return the size of the square"""
        return (self.__size)

    @property
    def position(self):
        """int: Return the position of the square"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """Sets the attribute size"""
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """Sets the attribute position"""
        if len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """int: Return the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the char '#'"""
        if self.__size != 0:
            for i in range(self.__size + self.__position[1]):
                for j in range(self.__size + self.__position[0]):
                    if j >= self.__position[0] and i >= self.__position[1]:
                        print("#", end="")
                    elif i >= self.__position[1]:
                        print(" ", end="")
                print("")
        else:
            print("")
