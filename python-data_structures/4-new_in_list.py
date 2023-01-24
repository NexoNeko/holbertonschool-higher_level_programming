#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list is not None:
        my_list_new = list(my_list)
        if idx < 0:
            return my_list_new
        if idx > len(my_list_new) - 1:
            return my_list_new
        my_list_new[idx] = element
        return my_list_new
