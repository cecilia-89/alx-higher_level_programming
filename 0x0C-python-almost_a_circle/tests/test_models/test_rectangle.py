import unittest

from models.rectangle import Rectangle

r1 = Rectangle(10, 2)
r2 = Rectangle(10, 2, 0, 0, 12)
r3 = Rectangle(5, 8)
r4 = Rectangle(2, 3, 4, 5, 8)

class BaseTest(unittest.TestCase):

    def test_results(self):

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r4.id, 8)

    def test_values(self)::
        pass

    def test_area(self):
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r3.area(), 40)

    def test_display(self):
        pass

    def test_str(self):
        pass

    def test_update(self):
        pass
