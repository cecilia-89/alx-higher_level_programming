#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:

    """A class Rectangle"""

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):

        """A class method called when an instance is created"""

        self.width = width

        self.height = height

        type(self).number_of_instances += 1

    @property
    def width(self):

        """method to retrieve the width"""

        return self.width

    @width.setter
    def width(self, value):

        """method to set the width"""

        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):

        """method to retrieve the height"""

        return self.__height

    @height.setter
    def height(self, value):

        """method to set the height"""

        if not isinstance(self.__height, int):
            raise TypeError("heigth must be an integer")

        if self.__height < 0:
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

            return ''

        result = [str(self.print_symbol) *
                  self.__width for i in range(self.__height)]

        return "\n".join(result)

    def __repr__(self):

        """ returns string representation of rectangle"""

        return "Rectangle (" + str(self.__width)\
               + ", " + str(self.__height) + ")"

    def __del__(self):

        """ called when all references are deleted """

        print("Bye rectangle...")

        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """returns rec with biggest area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():

            return rect_1

        return rect2

    @classmethod
    def square(cls, size=0):
        """ returns new instance of a rec """

        width = height = size

        return cls(size, size)
