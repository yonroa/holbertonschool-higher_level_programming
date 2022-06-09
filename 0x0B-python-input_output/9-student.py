#!/usr/bin/python3
"""Module with the class Student"""


class Student:
    """A simple class with one method"""

    def __init__(self, first_name, last_name, age):
        """initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
