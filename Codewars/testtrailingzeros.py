import unittest
from trailingzeros import zeros

class TestTrailingZerosFunction(unittest.TestCase):

    def test_zeros(self):
        self.assertEqual(zeros(6), 1)
        self.assertEqual(zeros(12), 2)
        self.assertEqual(zeros(25), 6)  # 25! has 6 trailing zeros (25, 20, 15, 10, 5, 1)

    def test_zeros_large_input(self):
        # Test with a larger input to check performance
        self.assertEqual(zeros(1000), 249)

if __name__ == '__main__':
    unittest.main()
