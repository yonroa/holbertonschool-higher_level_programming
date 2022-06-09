#!/usr/bin/python3
"""Module with the class Student"""


class Student:
    """A simple class with one method"""

    def __init__(self, first_name, last_name, age):
        """initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieves a dictionary
        representation of a Student instance
        """
        n_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for attributes in attrs:
                if attributes in self.__dict__:
                    n_dict.update({attributes: self.__dict__[attributes]})
            return n_dict
        return self.__dict__.copy()
