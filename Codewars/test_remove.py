import unittest
from remov import remov_nb

class TestRemovNB(unittest.TestCase):
    def test_remov_nb(self):
        result = remov_nb(26)
        expected_result = [(15, 21), (21, 15)]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()