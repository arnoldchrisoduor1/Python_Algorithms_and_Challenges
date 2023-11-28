import unittest
from findit import find_it

class TestFindOddOccurrence(unittest.TestCase):

    def test_find_odd_occurrence(self):
        self.assertEqual(find_it([7]), 7)
        self.assertEqual(find_it([0]), 0)
        self.assertEqual(find_it([1, 1, 2]), 2)
        self.assertEqual(find_it([0, 1, 0, 1, 0]), 0)
        self.assertEqual(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]), 4)

    def test_empty_sequence(self):
        # Test with an empty sequence
        self.assertIsNone(find_it([]))

if __name__ == '__main__':
    unittest.main()
