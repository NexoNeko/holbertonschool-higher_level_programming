#!/usr/bin/python3
"""Defines the class square """


class Square:
    """This is a class Square."""
    def __init__(self, size=0):
        """ Initializes the square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ The area method returns the area """
        return self.__size ** 2
