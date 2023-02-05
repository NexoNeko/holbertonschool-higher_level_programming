#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """A rectangle."""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return __width

    @width.setter
    def width(self, value):
        if value < 0:
            raise TypeError("width must be >= 0")
        if type(value) is not int:
            raise ValueError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return __height

    @height.setter
    def height(self, value):
        if value < 0:
            raise TypeError("height must be >= 0")
        if type(value) is not int:
            raise ValueError("height must be an integer")
        self.__height = value
