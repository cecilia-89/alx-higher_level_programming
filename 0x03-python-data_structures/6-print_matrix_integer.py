#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for lst in matrix:
        for idx in lst:
            print("{:d}".format(idx), end=' ')

        print()
