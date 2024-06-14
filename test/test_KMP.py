import unittest
from src.KMP import kmp_search, lps_exe


class TestKMP(unittest.TestCase):

    def test_single_occurrence(self):
        haystack = "abcxabcdabxabcdabcdabcy"
        needle = "abcdabcy"
        expected = [15]
        result = kmp_search(haystack, needle)
        self.assertEqual(result, expected, "Тест з одним входженням")

    def test_multiple_occurrences(self):
        haystack = "abcabydarkabcabythreeabcaby"
        needle = "abcaby"
        expected = [0, 10, 21]
        result = kmp_search(haystack, needle)
        self.assertEqual(result, expected, "Тест з кількома входженнями")

    def test_no_occurrence(self):
        haystack = "abcdefgh"
        needle = "xyz"
        result = kmp_search(haystack, needle)
        self.assertEqual(result, "Індекси Відсутні", "Тест без входження")

    def test_empty_needle(self):
        haystack = "abcdefgh"
        needle = ""
        result = kmp_search(haystack, needle)
        self.assertEqual(result, "needle порожній", "Тест з порожньою підстрічкою")

    def test_lps_computation(self):
        needle = "abcdabcy"
        expected_lps = [0, 0, 0, 0, 1, 2, 3, 0]
        lps = lps_exe(needle)
        self.assertEqual(lps, expected_lps, "Тест для таблиці LPS")

    def test_needle_longer_than_haystack(self):
        haystack = "abc"
        needle = "abcdef"
        result = kmp_search(haystack, needle)
        self.assertEqual(
            result,
            "needle довший ніж haystack",
            "Тест, коли підстрічка довша за головну стрічку",
        )


if __name__ == "__main__":
    unittest.main()

