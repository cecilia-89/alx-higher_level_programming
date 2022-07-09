import unittest

max_integer = __import__("6-max_integer").max_integer

class MaxIntTest(unittest.TestCase):

    def test_max(self):
        #Test when argument is a valid iterable

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("Hi"), 'i')

    def test_params(self):
        #Test when argument isn't valid

        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(89)

        with self.assertRaises(KeyError):
            max_integer({'key':6, 'we':'cat'})



