#!/bin/usr/python3

def square_matrix_simple(matrix=[]):

    if matrix:
        new_matrix = []

        for lst in matrix:
            index = []

            for idx in lst:
                index.append(idx**2)

            new_matrix.append(index)
        return new_matrix
