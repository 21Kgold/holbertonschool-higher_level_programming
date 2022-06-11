#!/usr/bin/python3
"""
Class Square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        Get size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set size
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
        Returns ready to print the string, with the updated values:
        [Square] (<id>) <x>/<y> - <width>
        """
        a = f"({self.id})"
        b = f"{self.x}/{self.y}"
        c = f"{self.width}"
        return f"[Square] {a} {b} - {c}"

    def update(self, *args, **kwargs):
        """
        Update attribute values of a square
        using built in function: setattr(object, attribute, value)
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        attribute_list = ["id", "size", "x", "y"]
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, attribute_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """
        square_diccionary = {}
        square_diccionary["id"] = self.id
        square_diccionary["size"] = self.size
        square_diccionary["x"] = self.x
        square_diccionary["y"] = self.y
        return square_diccionary
