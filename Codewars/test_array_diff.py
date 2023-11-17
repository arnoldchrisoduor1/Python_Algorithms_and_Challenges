import unittest
from array_diff import solution

class TestArrayDiff(unittest.TestCase):
    def test_one(self):
        result = solution([1,2,3,4], [1,2,3,4,5])
        self.assertEqual(result, [5])

    def test_two(self):
        result = solution([1,2,3,3,3,3,7,8], [1,2,3,7])
        self.assertEqual(result, [8])

    def test_null(self):
        result = solution([],[])
        self.assertEqual(result, [])

    def test_null(self):
        result = solution([1,2,3], [1,2,3])
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()