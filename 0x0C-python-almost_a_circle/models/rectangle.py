#!/usr/bin/python3
"""Module with the class `Rectangle`"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return the attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return the attribute height"""

    @height.setter
    def height(self, value):
        """sets the attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return the attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #
        """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """return a string representation of the rectangle"""
        return str(f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " +
                   f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        new_dic = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return new_dic
