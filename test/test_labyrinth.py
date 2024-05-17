import unittest

from src.labyrinth import shortest_path, read_input_file, write_output_file


class TestShortestPath(unittest.TestCase):

    def test_write_output_file(self):
        outputfile = 'test_output_1.txt'
        inputfile = 'test_input_2.txt'
        start, end, matrix = read_input_file(inputfile)
        shortest_distance = shortest_path(matrix, start, end)
        write_output_file(outputfile, shortest_distance)
        with open(outputfile, 'r') as file:
            output_data = int(file.read().strip())
        self.assertEqual(output_data, 12)

    def test_no_path(self):
        outputfile = 'test_output_2.txt'
        inputfile = 'test_input.txt'
        start, end, matrix = read_input_file(inputfile)
        shortest_distance = shortest_path(matrix, start, end)
        write_output_file(outputfile, shortest_distance)
        with open(outputfile, 'r') as file:
            output_data = int(file.read().strip())
        self.assertEqual(output_data, -1)



if __name__ == '__main__':
    test.main()