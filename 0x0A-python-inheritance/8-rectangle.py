#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
class: Rectangle that inherits from
BaseGeometry
"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):

        super().integer_validator("width", width)

        super().integer_validator("width", width)

        self.__width = width

        self.__height = height
