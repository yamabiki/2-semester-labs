import unittest

from src.minsquareN import find_square, check_capacity


class TestFindSquare(unittest.TestCase):

    def test_find_square(self):
        self.assertEqual(find_square(9, 2, 3), 9)
        self.assertEqual(find_square(2, 9999999, 9999999), 19999998)
        self.assertEqual(find_square(4, 5, 5), 10)

    def test_check_capacity(self):
        self.assertTrue(check_capacity(2, 3, 9, 9))
        self.assertTrue(check_capacity(9999999, 9999999, 2, 19999998))
        self.assertTrue(check_capacity(5, 5, 4, 10))


if __name__ == '__main__':
    unittest.main()