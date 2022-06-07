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
        return self.__width

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
