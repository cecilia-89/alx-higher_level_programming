#!/usr/bin/python3

"""
is_same_class: returns true if 
an object belongs to a particular class
else returns false
"""


def is_same_class(obj, a_class):

    """
    determines if a particular object
    belongs to a certain class
    """

    if type(obj) == a_class:

        return True

    return False
