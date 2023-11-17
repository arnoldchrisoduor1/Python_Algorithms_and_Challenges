import unittest
from camelcase import split_camel_case

class TestSplitCamelCase(unittest.TestCase):
    def test_hello_world(self):
        result = split_camel_case("helloWorld")
        self.assertEqual(result, "hello World")

    def test_camel_case(self):
        result = split_camel_case("camelCase")
        self.assertEqual(result, "camel Case")

    def test_break_camel_case(self):
        result = split_camel_case("breakCamelCase")
        self.assertEqual(result, "break Camel Case")

if __name__ == "__main__":
    unittest.main()