#!/usr/bin/python3
"""Module 1-my_list
define the child class MyList
"""


class MyList(list):
    """Class MyList, just have a function"""

    def print_sorted(self):
        """print the list in ascendig sort"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
