#!/usr/bin/python3
"""
Parse a valid JSON string and convert it into a Python Dictionary
"""

import json


def from_json_string(my_str):
    """
    Return:
        An object (Python data structure) represented by a JSON string
    Args:
        my_obj: it takes a string, bytes, or byte array instance which
        contains the JSON document as a parameter
    """

    return json.loads(my_str)
