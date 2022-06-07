#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for lst in matrix:

        for count, idx in enumerate(lst):

            if count == len(lst):
                print("{:d}".format(idx), end='')

            print("{:d}".format(idx), end=' ')

        print()
