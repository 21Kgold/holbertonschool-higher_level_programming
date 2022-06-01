#!/usr/bin/python3
"""
Write a string into a file, truncate:'write mode' (UTF8)
"""


def write_file(filename="", text=""):
    """
    Write a string into a file using 'with': create the file if doesn’t
    exist and overwrite the content of the file if it already exists
    Return the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
