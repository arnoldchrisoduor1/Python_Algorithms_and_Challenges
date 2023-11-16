import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_found(self):
        sorted_list = [1, 3, 5, 7, 9]
        target_element = 5
        result = binary_search(sorted_list, target_element)
        self.assertEqual(result, 2)

    def test_binary_search_not_found(self):
        sorted_list = [1, 3, 5, 7, 9]
        target_element = 4
        result = binary_search(sorted_list, target_element)
        self.assertEqual(result, -1)

    def test_binary_search_empty_list(self):
        sorted_list = []
        target_element = 7
        result = binary_search(sorted_list, target_element)
        self.assertEqual(result, -1)

    def test_binary_search_duplicate_elements(self):
        sorted_list = [1, 2, 2, 3, 4, 5, 5, 6]
        target_element = 5
        result = binary_search(sorted_list, target_element)
        self.assertIn(result, [5, 6])

if __name__ == "__main__":
    unittest.main()