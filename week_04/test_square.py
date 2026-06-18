from unittest import TestCase
from week_04.square import square

class Test(TestCase):
    def test_positive_integer(self):
        expected = 4
        actual = square(2)
        self.assertEqual(expected, actual)

    def test_negative_integer(self):
        expected = 4
        actual = square(-2)
        self.assertEqual(expected, actual)

    def test_zero(self):
        expected = 0
        actual = square(0)
        self.assertEqual(expected, actual)

    def test_positive_float(self):
        expected = 2.25
        actual = square(1.5)
        self.assertEqual(expected, actual)

    def test_negative_float(self):
        expected = 2.25
        actual = square(-1.5)
        self.assertEqual(expected, actual)

