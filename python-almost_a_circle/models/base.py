#!/usr/bin/python3
""" Defines the base class """


class Base:
    """ Base instance for future objects
    Manages IDs. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
