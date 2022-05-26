#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
    Rectangle class creation
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a object rectangle class
        """

        self.width = width
        self.height = height

    def width(self):
        """
        To get the width
        """

        return self.__width

    def width(self, value):
        """
        To set the width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """
        To get the height
        """

        return self.__height

    def height(self, value):
        """
        To set the height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
