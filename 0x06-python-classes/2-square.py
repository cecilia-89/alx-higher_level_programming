#!/usr/bin/python3

"""Define a class Square"""


class Square:

    """class Square with an instance attribute"""

    def __init__(self, size=0):

        """creates an private instance attribute"""

        self.__size = size

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        if size < 0:

            raise ValueError("size must be >= 0")
