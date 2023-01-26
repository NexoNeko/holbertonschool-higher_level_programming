#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    sqrt = []
    for i in matrix:
        sqrt.append(list(map(lambda x: x ** 2, i)))
    return(sqrt)
