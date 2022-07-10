#!/usr/bin/python3

"""
Module: 3-is_kind_of_class
Function: is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):

    """
    returns true if obj is an instance of a
    class or an instance of a class that inherited
    from another class else returns false
    """

    if isinstance(obj, a_class):

        return True

    return False
