#!/usr/bin/python3
""" defines the is_same_class abstract class """


def is_kind_of_class(obj, a_class):
    """ checks if a given object is or inherits from a_class"""
    return isinstance(obj, a_class)
