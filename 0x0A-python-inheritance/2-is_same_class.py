#!/usr/bin/python3
"""
Module is_same_class
"""


def is_same_class(obj, a_class):
    """
        Check if the objects have the same class
    """
    if type(obj) is a_class:
        return True
    return False
