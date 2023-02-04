#!/usr/bin/python3
"""defines a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """ Prints first + last name
        Raises type error if names are not str"""
    if type(first_name) is not string:
        raise TypeError("first_name must be a string")
    if type(last_name) is not string:
    raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

