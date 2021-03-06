#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:

    """A class Rectangle"""

    def __init__(self, width=0, height=0):

        """A class method called when an instance is created"""

        self.__width = width

        self.__height = height

    @property
    def width(self):

        """method to retrieve the width"""

        return self.width

    @width.setter
    def width(self, value):

        """method to set the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):

        """method to retrieve the height"""

        return self.__height

    @height.setter
    def height(self, value):

        """method to set the height"""

        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        """returns rectangle area"""

        return self.__height * self.__width

    def perimeter(self):

        """returns rectangle perimeter"""

        if self.__height == 0 or self.__width == 0:

            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):

        """prints the rectangle with the character #"""

        if self.__height == 0 or self.__width == 0:

            return ""

        result = ["#" * self.__width for i in range(self.__height)]

        return "\n".join(result)
