#!/usr/bin/python3
""" Defines the class student """


def pascal_triangle(n):
    """ prints the pascal triangle of n """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        maxz = triangle[-1]
        row = [1]
        for i in range(len(maxz) - 1):
            row.append(maxz[i] + maxz[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
