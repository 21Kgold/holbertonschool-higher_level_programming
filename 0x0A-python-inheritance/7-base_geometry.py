#!/usr/bin/python3
"""
Empty class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry empty class
    """
    def area(self):
        """
        Raise exception with message: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: that validates value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
