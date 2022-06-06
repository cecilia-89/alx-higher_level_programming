#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix:

        for lst in matrix:

            for idx in lst:

                if idx:

                    print("{:d}".format(idx), end=' ')

            print()
