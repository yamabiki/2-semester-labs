import unittest
from src.avl_priority_queue import AVLPriorityQueue

class TestAVLPriorityQueue(unittest.TestCase):
    def test_insert_and_remove_max(self):
        queue = AVLPriorityQueue()
        queue.insert(5, 2)
        queue.insert(7, 4)
        queue.insert(3, 1)
        queue.insert(9, 3)

        self.assertEqual(queue.remove_max(), 7)
        self.assertEqual(queue.remove_max(), 9)
        self.assertEqual(queue.remove_max(), 5)
        self.assertEqual(queue.remove_max(), 3)
        self.assertIsNone(queue.remove_max())

    def test_remove_max_from_empty_queue(self):
        queue = AVLPriorityQueue()
        self.assertIsNone(queue.remove_max())

    def test_insert_and_remove_max_alternate(self):
        queue = AVLPriorityQueue()
        queue.insert(5, 5)
        queue.insert(10, 10)
        queue.insert(2, 2)
        queue.insert(8, 8)
        queue.insert(1, 1)
        queue.insert(9, 9)
        queue.insert(4, 4)
        queue.insert(3, 3)

        self.assertEqual(queue.remove_max(), 10)
        self.assertEqual(queue.remove_max(), 9)
        self.assertEqual(queue.remove_max(), 8)
        self.assertEqual(queue.remove_max(), 5)
        self.assertEqual(queue.remove_max(), 4)
        self.assertEqual(queue.remove_max(), 3)
        self.assertEqual(queue.remove_max(), 2)
        self.assertEqual(queue.remove_max(), 1)
        self.assertIsNone(queue.remove_max())

if __name__ == '__main__':
    unittest.main()