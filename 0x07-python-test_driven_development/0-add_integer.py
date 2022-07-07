#!/usr/bin/python3#!/usr/bin/python3

"""
Module: 0-add_integer
Function: add_interger(), takes two positional
arguments a and b
"""

def add_integer(a, b=98):

    """Returns the sum of two numbers"""

    if type(a) != int and float:

        raise TypeError("a must be an integer")

    if type(b) != int and float:

        raise TypeError("b must be an integer")

    return int(a) + int(b)
