#!/usr/bin/python3
"""Module with the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or
    if the object is an instance of a class that inherited
    from, the specified class ; otherwise False
    """
    if type(obj) == a_class or isinstance(obj, a_class):
        return True
    return False
