#!/usr/bin/python3
"""
Class MyList that inherits from list
"""


class MyList(list):
    """ Class inheriting the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """
        Prints a sorted list without changing the original list
        """

        print(sorted(self))
