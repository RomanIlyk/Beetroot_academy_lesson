import unittest
import Homework13_3

class SquaresTestCase(unittest.TestCase):

    def test_squared(self):
        n = [1, 2, 3, 4, 5]
        result = Homework13_3.square_nums(n)
        self.assertEqual(result,  [1, 4, 9, 16, 25])

    def test_remove_negatives(self):
        n = [1, -2, 3, -4, 5]
        result = Homework13_3.remove_negatives(n)
        self.assertEqual(result,  [1, 3, 5])

unittest.main()