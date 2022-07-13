#!/usr/bin/python3
"""
Module: rectangle.py
"""

from models.base import Base


class Rectangle(Base):
    """class: Rectangle that
    inherits from 'Base'"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates new instances of a class
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value ofi height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """returns the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """returns the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """prints rectangle instance with '#'
        """
        [print() for i in range(self.__y)]

        print('\n'.join([' ' * self.__x + '#' *
              self.width for i in range(self.__height)]))

    def __str__(self):
        """returns string rep of
        class 'rectangle'
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
               .format(self.id, self.__x, self.__y, self.__width, self.height)

    def update(self, *args, **kwargs):
        """updates each instance attr
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:

            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dict representation
        of a class
        """
        return self.__dict__
