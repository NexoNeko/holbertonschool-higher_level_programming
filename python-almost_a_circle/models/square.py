#!/usr/bin/python3
""" Defines the square class, inherits from rectangle """
from models.rectangle import Rectangle

class Square(Rectangle):
    """The square class, represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
