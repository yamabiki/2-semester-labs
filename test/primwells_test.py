import unittest

from src.primwells import min_cable_length


class TestCommunicationWells(unittest.TestCase):
    def test_based_testcase(self):
        file = "communication_wells.csv"
        out = "../test/result_communication_wells.txt"

        min_cable_length(file, out)
        # base test case
        with open(out) as output_file:
            output = output_file.read()

        expected = "1750"
        self.assertEqual(output, expected)


class TestCommunicationDisconnect(unittest.TestCase):
    def test_based_testcase(self):
        file = "../test/communication_wells_with_disconnection.csv"
        out = "../test/result_communication_wells_with_disconnection.txt"

        min_cable_length(file, out)

        with open(out) as output_file:
            output = output_file.read()
        # test case if no graph
        expected = "-1"
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()