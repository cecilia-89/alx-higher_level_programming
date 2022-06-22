#!/usr/bin/python3

"""defines a class Square"""


class Square:

    """class Square with instances attributes"""

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        """getter method which returns the size
        of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter method which sets the value"""

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        if value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the area of the square"""

        return self.__size ** 2
