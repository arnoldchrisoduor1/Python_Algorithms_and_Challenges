import unittest
from ocurrences import solution

class TestDeleteNth(unittest.TestCase):

    def test_delete_nth_example_1(self):
        result = solution([1, 2, 3, 1, 2, 1, 2, 3], 2)
        self.assertEqual(result, [1, 2, 3, 1, 2, 3])

    def test_delete_nth_example_2(self):
        result = solution([20, 37, 20, 21], 1)
        self.assertEqual(result, [20, 37, 21])

    def test_delete_nth_repeated(self):
        result = solution([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 2)
        self.assertEqual(result, [1, 2, 2, 3, 3, 4, 4])

    def test_delete_nth_empty_list(self):
        result = solution([], 3)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()