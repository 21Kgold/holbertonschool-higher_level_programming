#!/usr/bin/python3
"""
Class Base module
"""


import json
import os.path
import csv
import turtle


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
            empty_list = "[]"
            return empty_list
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that updates a list to asign values to keys of an object of
        Rectangle or Square class, then converts it into a json string and
        write it into a json file using it's class as a filename:
        <class.json>; Overwrites the file if already exists
        """
        key_value_list = []
        if list_objs is not None:
            for element in list_objs:
                key_value_list.append(cls.to_dictionary(element))

        filename = cls.__name__ + ".json"

        with open(filename, mode='w') as file:
            file.write(cls.to_json_string(key_value_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Function that returns a python object (list) of the JSON string
        representation
        """
        if json_string is None:
            empty_list = []
            return empty_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Function that creates an instance with all the attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(100, 100)

        elif cls.__name__ == "Square":
            dummy = cls(100)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """

        filename = cls.__name__ + ".json"

        if os.path.exists(filename):
            object_python_list = []
            with open(filename) as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)

                for i in json_list:
                    object_python_list.append(cls.create(**i))
            return object_python_list

        else:
            empty_list = []
            return empty_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Function that updates a list to asign values to keys of an object of
        Rectangle or Square class, then converts it into a csv string (first
        line contains name/key of each column, separated by a comma, and the
        rest of the lines contains the data asociated with that keys) and
        write it into a csv file using it's class as a filename:
        <class.csv>; Overwrites the file if already exists

        csv.DictWriter(filename, fieldnames) takes the name of the CSV file
        and a list of columns names or keys (fieldnames: represents the
        sequence of key that recognise the order in which values in
        dictionary are passed to the writerow() method) as an argument.

        The writeheader() method writes the first row of the columns names
        (or keys) in the CSV file that are the header row.

        The writerow() method is used to write the single row at a time and
        map the dictionary into CSV rows.
        """

        filename = cls.__name__ + ".csv"
        key_value_list = []

        if cls.__name__ == "Rectangle":
            keys_list = ["id", "width", "height", "x", "y"]

        elif cls.__name__ == "Square":
            keys_list = ["id", "size", "x", "y"]

        for element in list_objs:
            key_value_list.append(cls.to_dictionary(element))

        with open(filename, "w") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=keys_list)
            csv_writer.writeheader()
            csv_writer.writerows(key_value_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances
        """

        filename = cls.__name__ + ".csv"

        if os.path.exists(filename):
            object_python_list = []
            with open(filename) as csv_file:

                # csv.DictReader takes the keys from the first row in the
                # csv file and creates one dictionary for each of the
                # remaining lines using that keys; wich means it creates
                # a diccionary per object

                dict_matrix = csv.DictReader(csv_file)
                for row in dict_matrix:
                    # Cast "value" from string to int
                    cast_row = {key: int(value) for key, value in row.items()}
                    object_python_list.append(cls.create(**cast_row))
            return object_python_list
        else:
            empty_list = []
            return empty_list
