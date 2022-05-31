#!/usr/bin/python3
"""
Module Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry class
    """
    def __init__(self, width, height):
        """
        Initialization of a rectangle from BaseGeometry
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
