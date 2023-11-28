import unittest
from twosum import twosum

class TestTwoSumFunction(unittest.TestCase):
    def test_two_sum(self):
        #test case with a valid pair.
        numbers1 = [2, 7, 11, 15]
        target1 = 9
        self.assertEqual(twosum(numbers1, target1), (0,1))

        #test with different valid pair.
        numbers2 = [3, 2, 4]
        target2 = 6
        self.assertEqual(twosum(numbers2, target2), (1, 2))

        #test case where there are multiple valid pairs
        number3 = [3, 3]
        target3 = 6
        self.assertIn(twosum(number3, target3), [(0,1), (1, 0)])

        #test case where no valid pair exists.
        numbers4 = [1, 2, 3, 4]
        target4 = 10
        self.assertIsNone(twosum(numbers4, target4))

if __name__ == "__main__":
    unittest.main()