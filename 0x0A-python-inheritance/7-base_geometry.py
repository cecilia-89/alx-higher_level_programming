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
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
