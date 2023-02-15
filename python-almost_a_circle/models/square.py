#!/usr/bin/python3
""" Defines the square class, inherits from rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class, represents a square"""
    def __init__(self, Size, x=0, y=0, id=None):
        super().__init__(Size, Size, x, y, id)
        self.Size = Size

    @property
    def size(self):
        return self.Size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        self.Size = value
