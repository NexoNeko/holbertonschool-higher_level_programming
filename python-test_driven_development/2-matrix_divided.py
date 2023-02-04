#!/usr/bin/python3
"""defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """ Returns a new matrix."""
    # div type error
    if type(div) is not int\
            and div is not float:
        raise TypeError("div must be a number")
    div = int(div)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # j type error
            if type(matrix[i][j]) is not int\
                    and type(matrix[i][j]) is not float:
                        raise TypeError\
                            ("matrix must be a matrix (list of lists) of integers/floats")
    # start of actual function
    matrix_new = []
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError\
                ("Each row of the matrix must have the same size")
        try:
            matrix_new.append(list(map(lambda x: round(x / div, 2), i)))
        except TypeError:
            raise TypeError\
                ("matrix must be a matrix (list of lists) of integers/floats")
    return matrix_new
