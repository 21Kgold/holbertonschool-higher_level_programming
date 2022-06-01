#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """
    Function that convert from JSON to Python
    json string and the result will be a Python dictionary
    """
    with open(filename, mode='r') as file:
        json_string = file.read()
        python_dictionary = json.dumps(json_string)
        return python_dictionary
