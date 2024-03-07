import unittest
from lab2var2lvl2 import min_paint

class TestMinPaint(unittest.TestCase):
    def test_single_painter(self):
        lengths = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        k = 1
        t = 5
        self.assertEqual(min_paint(k, t, lengths), 700)

    def test_multiple_painters_equal_length(self):
        lengths = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        k = 10
        t = 5
        self.assertEqual(min_paint(k, t, lengths), 100)

    def test_multiple_painters_unequal_length(self):
        lengths = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        k = 5
        t = 5
        self.assertEqual(min_paint(k, t, lengths), 140)

if __name__ == '__main__':
    unittest.main()