#!/usr/bin/python3


class Square:
    #this initializes the square
    def __init__(self, size=0):
        self.__size = size
    
    @property
    def size(self):
        return (self.__size)
    
    #this is now setting its value
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size > 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
