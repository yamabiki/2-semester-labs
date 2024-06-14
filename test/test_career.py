import unittest
from src.career import max_experience


class TestMaxExperience(unittest.TestCase):
    def test_max_experience_example_1(self):
        hierarchy = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        self.assertEqual(max_experience(hierarchy), 12)

    def test_max_experience_example_2(self):
        hierarchy = [
            [9999]
        ]
        self.assertEqual(max_experience(hierarchy), 9999)

    def test_max_experience_example_3(self):
        hierarchy = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        self.assertEqual(max_experience(hierarchy), 3)

if __name__ == "__main__":
    unittest.main()