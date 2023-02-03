#!/usr/bin/python3
"""defines a function that adds two integers"""


def add_integer(a, b=98):
    """ Returns the addition of a + b.
    Raises a type error if A or B are not ints
    Casts the values into int before adding"""

    if type(a) is not int\
            and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int\
            and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
