#!/usr/bin/python3
"""
Class Rectangle module
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Get height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Get x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Get y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Set y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Calculate the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        for j in range(self.y):
            print()
        for i in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Returns ready to print the string, with the updated values:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        a = f"({self.id})"
        b = f"{self.__x}/{self.__y}"
        c = f"{self.__width}/{self.__height}"
        return f"[Rectangle] {a} {b} - {c}"

    def update(self, *args, **kwargs):
        """
        Update attribute values of a rectangle
        using built in function: setattr(object, attribute, value)
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if args is not None and len(args) != 0:
            attributes_list = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        rectangle_diccionary = {}
        rectangle_diccionary["id"] = self.id
        rectangle_diccionary["width"] = self.width
        rectangle_diccionary["height"] = self.height
        rectangle_diccionary["x"] = self.x
        rectangle_diccionary["y"] = self.y
        return rectangle_diccionary
