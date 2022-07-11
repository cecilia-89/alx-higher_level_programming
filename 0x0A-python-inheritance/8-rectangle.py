#!/usr/bin/python3
"""
Module: 8-rectangle which defines
a class Rectanglie
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    class: Rectangle that inherits from
    BaseGeometry
    """

    def __init__(self, width, height):
        """instantiates an instance
        of class Rectangle"""

        super().integer_validator("width", width)

        super().integer_validator("width", width)

        self.__width = width

        self.__height = height
