#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:

    """A class Rectangle"""

    def __init__(self, width=0, height=0):

        """A class method called when an instance is created"""

        self.__height = height

        self.__width = width

    @property
    def height(self):

        """method to retrieve the width"""

        return self.height

    @height.setter
    def height(self, value):

        """method to set the width"""

        if not isinstance(self.__height, int):
            raise TypeError("width must be an integer")

        if self.__height < 0:
            raise ValueError("width must be >= 0")

        self.__height = value

    @property
    def width(self):

        """method to retrieve the height"""

        return self.__width

    @width.setter
    def width(self, value):

        """method to set the height"""

        if not isinstance(self.__width, int):
            raise TypeError("heigth must be an integer")

        if self.__width < 0:
            raise ValueError("height must be >= 0")

        self.__width = value