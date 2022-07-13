#!/usr/bin/python3
"""
Module: base.py
"""


class Base:
    """
    a class 'Base' with
    a class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantiates a new instance
        """

        if id:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
