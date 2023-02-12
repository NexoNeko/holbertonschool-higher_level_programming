#!/usr/bin/python3
""" Defines the class student """


class Student:
    """ represents a student """

    def __init__(self, first_name, last_name, age):
        """ Initializes the student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dict repr of the student obj """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
