#!/usr/bin/python3
"""Defines the class square """


class Square:
    """This is a class Square."""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the square """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ The area method returns the area """
        return self.__size ** 2

    def my_print(self):
        """ This prints the square """
        if self.__size > 0:
            for i in range(0, self.position[1]):
                print("")
            for i in range(0, self.__size):
                for n in range(0, self.position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
