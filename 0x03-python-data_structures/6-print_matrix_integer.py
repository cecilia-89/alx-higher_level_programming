#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix:

        for lst in matrix:

            if lst:
                for idx in lst:
                    print("{:d}".format(idx), end=' ')

                print()
