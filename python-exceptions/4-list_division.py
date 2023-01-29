#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for i in range(list_length):
        try:
            Res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            Res = 0
        except TypeError:
            print("wrong type")
            Res = 0
        except IndexError:
            print("out of range")
            Res = 0
        finally:
            my_list.append(Res)
    return my_list
