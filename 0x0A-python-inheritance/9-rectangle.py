#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
class: Rectangle that inherits from
BaseGeometry
"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):

        super().integer_validator("width", width)

        super().integer_validator("height", height)

        self.__width = width

        self.__height = height

    def area(self):

        area = self.__width * self.__height

        return area

    def __str__(self):

        return "[Rectangle] " + str(self.__width) + '/' + str(self.__height)
