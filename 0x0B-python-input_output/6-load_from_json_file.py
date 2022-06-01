#!/usr/bin/python3
"""
Function that creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Function creates a Python dictionary from a JSON file
    """
    with open(filename) as file:
        python_dictionary = json.load(file)
        return python_dictionary
