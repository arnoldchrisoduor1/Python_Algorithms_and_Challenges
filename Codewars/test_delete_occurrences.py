import unittest
from delete_occurences import fun_occurrences

class TestDeleteOcuurences(unittest.TestCase):
    def test_for_occurence(self):
        result = fun_occurrences([3,4,5,6,6,7,8,8,8,8], 2)
        self.assertEqual(result, [3, 4, 5,6,6, 7,8, 8])

    def new_test(self):
        result = fun_occurrences([], 2)
        self.assertEqual(result, [])

    def test_3(self):
        result = fun_occurrences([1,2,3,4], 2)
        self.assertEqual(result, [1,2,3,4])

if __name__ == "__main__":
    unittest.main()