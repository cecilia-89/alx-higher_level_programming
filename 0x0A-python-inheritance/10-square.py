#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""
Module: 10-square
"""


class Square(Rectangle):

    """A class 'Square' that inherits
    from Rectangle
    """

    def __init__(self, size):

        super().integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)
