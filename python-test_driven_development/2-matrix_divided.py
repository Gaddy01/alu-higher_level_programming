#!/usr/bin/python3
"""
This module writes a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """this function divides all elements of a matrix with a number"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_divided_matrix = []
    for row in matrix:
        if row == matrix[0]:
            row_len = len(row)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        new_dived_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix of integers/floats")
            new_dived_element = round(element/div, 2)
            new_dived_row.append(new_dived_element)
        new_divided_matrix.append(new_dived_row)

    return  new_divided_matrix
