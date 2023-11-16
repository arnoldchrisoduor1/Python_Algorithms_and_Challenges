import unittest
from split_strings import split_string_into_pairs

class TestSplitStringIntoPairs(unittest.TestCase):

    def test_even_length_string(self):
        result = split_string_into_pairs('abcdefgh')
        self.assertEqual(result, ['ab', 'cd', 'ef', 'gh'])

    def test_odd_length_string(self):
        result = split_string_into_pairs('asdfadsf')
        self.assertEqual(result, ['as', 'df', 'ad', 'sf'])

    def test_empty_string(self):
        result = split_string_into_pairs('')
        self.assertEqual(result, [])

    def test_single_character_string(self):
        result = split_string_into_pairs('x')
        self.assertEqual(result, ['x_'])

    def test_two_characters_string(self):
        result = split_string_into_pairs('ab')
        self.assertEqual(result, ['ab'])

if __name__ == '__main__':
    unittest.main()