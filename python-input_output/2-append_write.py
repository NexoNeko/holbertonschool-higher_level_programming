#!/usr/bin/python3
""" Defines the append write file function """


def append_write(filename="", text=""):
    """appends a string to a text file
    and returns the number of characters written"""
    with open(filename, "a",  encoding="utf-8") as f:
        return f.write(text)
