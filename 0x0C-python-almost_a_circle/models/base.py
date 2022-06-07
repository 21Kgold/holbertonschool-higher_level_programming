#!/usr/bin/python3
"""
Class Base module
"""


import json

class Base:
    """
    Class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Function that converts a Python object (list or dictionary)
        into a json string
        """

        if list_dictionaries is None:
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)
