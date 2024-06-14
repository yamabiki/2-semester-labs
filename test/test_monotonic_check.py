import unittest

from src.monotonic_check import is_monotonic


class TestIsMonotonic(unittest.TestCase):
    def test_is_monotonic(self):
        self.assertTrue(is_monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(is_monotonic([5, 4, 3, 2, 1]))
        self.assertFalse(is_monotonic([1, 2, 2, 3, 2, 4]))


if __name__ == '__main__':
    unittest.main()
