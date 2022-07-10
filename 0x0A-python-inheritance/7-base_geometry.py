#!/usr/bin/python3

"""
Module: 5-base_geometry
class: BaseGeometry
"""


class BaseGeometry:
    """
    An empty class Base geometry
    """
    def area(self):
        """
        Returns the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates 'value'
        """

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
