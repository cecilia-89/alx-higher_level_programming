#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix:

        for lst in matrix:

            for count, idx in enumerate(lst):

                if count != 3:

                    print("{:d}".format(idx), end=' ')

            print()
