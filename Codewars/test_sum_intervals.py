import unittest
from sum_intervals import sum_intervals

class TestSumIntervals(unittest.TestCase):
    def test_sum_intervals(self):
        # Test case 1
        intervals1 = [[1, 2], [6, 10], [11, 15]]
        self.assertEqual(sum_intervals(intervals1), 9)

        # Test case 2
        intervals2 = [[1, 4], [7, 10], [3, 5]]
        self.assertEqual(sum_intervals(intervals2), 7)

        # Test case 3
        intervals3 = [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]
        self.assertEqual(sum_intervals(intervals3), 19)

        # Test case 4
        intervals4 = [[0, 20], [-100000000, 10], [30, 40]]
        self.assertEqual(sum_intervals(intervals4), 100000030)

if __name__ == "__main__":
    unittest.main()