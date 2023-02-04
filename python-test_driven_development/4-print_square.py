#!/usr/bin/python3
"""Prints a square of <size> area"""


def print_square(size):
    """Prints a square of <size> area using char #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
