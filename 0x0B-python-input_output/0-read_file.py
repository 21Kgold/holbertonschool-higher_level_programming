#!/usr/bin/python3
"""
Reads a file, 'read mode' (UTF8) and print it to stdout
"""


def read_file(filename=""):
    """
    Reads a file using 'with'
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.readlines(), end="")
