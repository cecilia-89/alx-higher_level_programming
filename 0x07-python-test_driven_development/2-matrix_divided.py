#!/usr/bin/python3
"""
module: 2-matrix_divided
function: matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix with each
    elemeny divided by 'div'
    """

    length = len(matrix[0])

    new_list = []

    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")

    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for i, lst in enumerate(matrix):

        if len(lst) != length:
            raise TypeError("Each row of the matrix must have the same size")

        new_list.append([])

        for item in lst:

            if not isinstance(item, (int, float)):
                raise TypeError(msg)

            res = round(item/div, 2)
            new_list[i].append(res)

    return new_list
