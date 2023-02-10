#!/usr/bin/python3
""" Defines the MyList class """


class MyList(list):
    """ Prints a sorted list """
    def print_sorted(self):
        print(sorted(self))
