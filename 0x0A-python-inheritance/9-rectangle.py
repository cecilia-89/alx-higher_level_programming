#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Module: 9-rectangle.py which defines
a class Rectangle
"""


class Rectangle(BaseGeometry):
    """class Rectangle which inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """instantiates a new instance of
        class Rectangle"""

        super().integer_validator("width", width)

        super().integer_validator("height", height)

        self.__width = width

        self.__height = height

    def area(self):
        """ Returns the area of a rectangle"""

        area = self.__width * self.__height

        return area

    def __str__(self):
        """Retuens the string represenattion
        of class Rectangle"""

        return "[Rectangle] " + str(self.__width) + '/' + str(self.__height)
