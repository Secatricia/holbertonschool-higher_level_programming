#!/usr/bin/python3
"""Function that adds 2 integers."""


def matrix_divided(matrix, div):
    """Function that adds 2 integers"""
    new_matrix = []
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for column in matrix:
        if len(column) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for row in column:
            if not (isinstance(row, (int, float))):
                raise TypeError("matrix must be a matrix (list of lists) of in\
tegers/floats")
        new_matrix.append(list(map(lambda x: round(x/div, 2), column)))
    return (new_matrix)
