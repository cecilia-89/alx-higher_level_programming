#!/usr/bin/python3

"""
is_kind_of_class: returns true if
an object is an instance of a class or
an instance of a class that inherited
from another class else returns false
"""


def is_kind_of_class(obj, a_class):

    """
    determines if a particular object
    belongs to a certain class
    """

    if isinstance(obj, a_class):

        return True

    return False
