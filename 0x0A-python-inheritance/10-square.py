#!/usr/bin/python3

"""
Module: 10-square which defines a class 
Square
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):

    """A class 'Square' that inherits
    from Rectangle
    """

    def __init__(self, size):
        """instantiates a new instance of class
        Square"""

        super().integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)
