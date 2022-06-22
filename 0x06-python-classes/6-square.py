#!/usr/bin/python3

"""defines a class Square"""


class Square:

    """class Square defined with instance attributes"""

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size

        self.__position = position

    @property
    def position(self):
        """getter method which gets the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """setter method which sets the value"""

        for i in self.__position:

            if i < 0:

                raise TypeError("position must be a tuple\
                        of 2 positive integers")

        self.__position = value

    @property
    def size(self):
        """getter method which gets the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter method which sets the value"""

        if not isinstance(value, int):

            raise TypeError("size must be an integer")

        if value < 0:

            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns the square area"""

        return self.__size ** 2

    def my_print(self):
        """prints a sqaure of size"""

        if self.__size == 0:

            pass

        else:

            print("\n" * self.__position[1], end="")

            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size for rows
                             in range(self.__size)]))
