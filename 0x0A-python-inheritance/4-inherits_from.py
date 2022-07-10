#!/usr/bin/python3

"""
Module: 4-inherits_from
Function: inherits_from()
"""


def inherits_from(obj, a_class):

    """
    returns true if obj is an instance of a
    class or an instance of a class that inherited
    from another class else returns false
    """

    if issubclass(a_class, obj):

        return True

    return False
