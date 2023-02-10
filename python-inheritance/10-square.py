#!/usr/bin/python3
""" Defines the Square class, subclass of Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Imports BaseGeometry class"""


class Square(Rectangle):
    """ Square subclass accepts width and height ints """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[Rectangle] " + str(self.__size) + "/" + str(self.__size))
