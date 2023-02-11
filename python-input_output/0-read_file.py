#!/usr/bin/python3
""" Defines the readfile function """


def read_file(filename=""):
    """Prints the contents of a file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
