#!/usr/bin/python3
"""
Append a string into a file, 'append mode' (UTF8)
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and returns the number
    of characters added, using the 'with' statement
    If the file doesn’t exist, it should be created
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
