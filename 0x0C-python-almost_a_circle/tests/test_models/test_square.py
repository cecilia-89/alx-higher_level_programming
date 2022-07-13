import unittest

from models.square import Square

s1 = Square()
s2 = Square(10)
s3 = Square()

class BaseTest(unittest.TestCase):

    def test_square(self):
        pass

    def test_args(self):
        pass
