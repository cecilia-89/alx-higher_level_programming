#!/usr/bin/python3
from models.rectangle import Rectangle

"""
Module: models/square.py
"""


class Square(Rectangle):
    """
    class: Square which inherits from
    'Rectangle'
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates new instances
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size
        of square
        """
        return super().width

    @size.setter
    def size(self, value):
        """sets the size
        of square
        """
        super(Square, self.__class__).width.fset(self, value)

        self.height = value

    def __str__(self):
        """Returns the string representation
        of class Square"""

        return "[Square] ({}) {}/{} - {}"\
               .format(self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """updates the instance attributes
        """
        attr = ['id', 'size', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:

            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dict representation of
        a dict"""

        return self.__dict__
