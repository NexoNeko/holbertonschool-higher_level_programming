#!/usr/bin/python3
""" defines the is_same_class abstract class """


def is_same_class(obj, a_class):
    """ checks if a given object is exactly the given class"""
    if type(obj) == a_class:
        return True
    else:
        return False
