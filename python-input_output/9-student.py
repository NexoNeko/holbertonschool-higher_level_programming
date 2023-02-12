#!/usr/bin/python3
""" Defines the class student """

class Student:
    """ represents a student """

    def __init__(self, first_name, last_name, age):
        """ Initializes the student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dict repr of the student obj """
        return self.__dict__
