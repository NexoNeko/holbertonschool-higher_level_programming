#!/usr/bin/python3
""" Defines the Rectangle class, subclass of BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Imports BaseGeometry class"""

class Rectangle(BaseGeometry):
    __width = 0
    __height = 0
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height == height
