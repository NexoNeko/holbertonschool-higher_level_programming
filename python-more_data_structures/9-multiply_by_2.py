#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    new_dictionary.update((x, y*2) for x, y in new_dictionary.items())
    return(new_dictionary)
