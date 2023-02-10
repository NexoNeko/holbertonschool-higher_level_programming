#!/usr/bin/python3
"""defines the inherits from class"""


def inherits_from(obj, a_class):
    """ Returns true if  the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False."""
    if type(obj) == a_class:
        return False
    if issubclass(a_class, type(obj)):
        return True
    return isinstance(obj, a_class)
