#!/usr/bin/python3

"""Defines a class Square"""


class Square:

    """Creates an instance attribute"""

    def __init__(self, size=0):

        """creates a private instance with size"""

        self.__size = size

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        if size < 0:

            raise ValueError("size must be >= 0")

    def area(self):

        """creates another instance attribute
        which returns square of square"""

        return self.__size ** 2
