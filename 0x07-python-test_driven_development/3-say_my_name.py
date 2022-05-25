#!/usr/bin/python3
"""Module to add two strings"""


def say_my_name(first_name, last_name=""):
    """function that combine two strings with a whitespace in the middle"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
