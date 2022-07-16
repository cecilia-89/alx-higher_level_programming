import unittest

from models.base import Base

b1 = Base()
b3 = Base(10)
b4 = Base()

class BaseTest(unittest.TestCase):

    def test_values(self):

        self.assertEqual(b1.id, 1)
        self.assertEqual(b3.id, 10)
        self.assertEqual(b4.id, 2)

if __name__ == '__main__':
    unittest.main()
