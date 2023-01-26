#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    modulos = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            modulos.append(True)
        else:
            modulos.append(False)

    return (modulos)
