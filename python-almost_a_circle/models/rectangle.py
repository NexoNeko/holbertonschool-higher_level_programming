#!/usr/bin/python3
""" Defines the rectangle class, inherits from base """
from models.base import Base


class Rectangle(Base):
    """ Defines the rectangle class
    The rectangle class represents a rectangle.
    It posseses the width, height, X and Y attributes
    as well as an unique ID that is heredated from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle instance """
        area = self.height * self.width
        return area

    def display(self):
        """ Prints the rectangle with # on the console """
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            for n in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            if i != self.height - 1:
                print("")
        print("")
        return ""

    def __str__(self):
        print(f"[Rectangle] ({self.id}) {self.x}/{self.y}"
              f" - {self.width}/{self.height}", end="")
        return ""

    def update(self, *args):
        """ Updates the values contained within rectangle.
        Each value updated depends on the index of args.
        0 = id, 1 = width, 2 = height, 3 = x, 4 = y """
        my_list = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            exec(f"self.{my_list[i]} = {args[i]}")
