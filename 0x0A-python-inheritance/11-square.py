#!/usr/bin/python3

"""
Module: 11-square which defines a class 
Sqaure that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):

    """A class 'Square' that inherits
    from Rectangle
    """

    def __init__(self, size):
        """instantiates a new instance of
        class Square"""

        super().integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        """overrides string represantation of class
        Rectangle"""

        return "[Square] " + str(self.__size) + '/' + str(self.__size)
