import unittest
from gap import gap

class TestGap(unittest.TestCase):
    def test_gap(self):
        result = gap(2, 3, 50)
        self.assertEqual(result, [3, 5])

        # Test case for a valid gap of 2 between 5 and 7
        result = gap(2, 5, 7)
        self.assertEqual(result, [5, 7])

        # Test case for no valid gap between 5 and 5
        result = gap(2, 5, 5)
        self.assertIsNone(result)

        # Test case for a valid gap of 4 between 130 and 200
        result = gap(4, 130, 200)
        self.assertEqual(result, [163, 167])

        # Test case for no valid gap between 100 and 110
        result = gap(6, 100, 110)
        self.assertIsNone(result)

        # Test case for no valid gap between 30000 and 100000
        result = gap(11, 30000, 100000)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()