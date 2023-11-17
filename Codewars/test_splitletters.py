import unittest
from splitletters import solution

class TestSplitLetters(unittest.TestCase):
    def test_camel_case(self):
        result = solution("camelCase")
        self.assertEqual(result, "camel Case")

    def test_three_string(self):
        result = solution("testThreeStrings")
        self.assertEqual(result, "test Three Strings")

    def test_null_string(self):
        result = solution("")
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()