import unittest
from linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
    def test_linear_search_found(self):
        my_list = [1, 2, 3, 5, 7, 9]
        target_element = 5
        result = linear_search(my_list, target_element)
        self.assertEqual(result, 2)

    def test_linear_search_not_found(self):
        my_list = [1, 3, 5, 7, 9]
        target_element = 4
        result = linear_search(my_list, target_element)
        self.assertEqual(result, -1)

    def test_linear_search_empty_list(self):
        my_list = []
        target_element = 7
        result = linear_search(my_list, target_element)
        self.assertEqual(result, -1)

    if __name__ == '__main__':
        unittest.main()