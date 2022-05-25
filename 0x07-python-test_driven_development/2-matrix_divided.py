#!/usr/bin/python3
"""Module to divide a matrix by integer"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix by an integer or float"""

    new_matrix = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(error)

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(error)

        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        row_list = []
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error)
            row_list.append(round((element / div), 2))
        new_matrix.append(row_list)
    return new_matrix
