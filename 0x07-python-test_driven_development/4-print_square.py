#!/usr/bin/python3
"""
Module: 4-print_square
Function: def print_square()
"""


def print_square(size):

    if isinstance(size, float) and size < 0 or not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    [print('#' * size) for count in range(size)]
