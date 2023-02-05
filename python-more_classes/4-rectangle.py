#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """A rectangle."""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.height * self.width
        return area
    def perimeter(self):
        if self.width == 0\
                or self.height == 0:
            return 0
        perimeter = 2 * (self.height + self.width)
        return perimeter

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end = "")
            if i != self.height - 1:
                print("")
        return ""

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")
