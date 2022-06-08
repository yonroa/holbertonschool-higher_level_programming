#!/usr/bin/python3
"""Module to define the child class MyList"""


class MyList(list):
    """Class MyList, just have a function"""

    def print_sorted(self):
        print(sorted(self))
