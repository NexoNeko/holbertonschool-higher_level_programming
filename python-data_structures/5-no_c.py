#!/usr/bin/python3


def no_c(my_string):
    new_string = ''
    if len(my_string) == 0:
        return new_string
    for a in my_string:
        if a != 'C' and a != 'c':
            new_string += a
    return new_string
