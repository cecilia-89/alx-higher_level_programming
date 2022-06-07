#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for lst in matrix:

        for count, idx in enumerate(lst):

            result = count == len(lst) - 1

            print("{:d}".format(idx), end='' if result else ' ')

        print()
