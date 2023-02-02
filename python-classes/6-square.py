#!/usr/bin/python3


class Square:
    #this initializes the square
    """ a square with defined size """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    
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
    
    @property
    def position(self):
        return (self.__position)
    @position.setter
    def position(self, value):
        if not isinstance(value, tulpe):
            raise TypeError("position must be a tuple of 2 positive integers")
    
    """ The area method returns the area """
    def area(self):
        return self.__size ** 2
    
    """ This prints the square """
    def my_print(self):
        if self.__size > 0:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for n in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
