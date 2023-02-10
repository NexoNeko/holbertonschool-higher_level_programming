#!/usr/bin/python3
""" Defines the Square class, subclass of Rectangle """
Rectangle = __import__('9-rectangle').Rectangle
""" Imports Rectangle class """


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
