#!/usr/bin/python3
"""
This module defines the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Matrix divided by a divisor
    :param matrix: The matrix to divide
    :param div: Divisor
    :return: Divided matrix
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
