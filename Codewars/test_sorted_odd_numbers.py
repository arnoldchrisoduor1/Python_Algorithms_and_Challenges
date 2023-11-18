import unittest
from sort_the_odd import sort_odd_numbers

class TestSortOddNumbers():
    #test with only odd numbers.
    def test_1(self):
        input_array = [1,5,9,33,45,7]
        result = sort_odd_numbers(input_array)
        self.assertEqual(result, [1,5,7,33,45])

    #test for the even numebsr only
    def test_2(self):
        input_array = [2,8,4,12,86,32]
        result = sort_odd_numbers(input_array)
        self.assertEqual(result, [2,8,4,12,86,32])

    def test_3(self):
        input_array = []
        result = sort_odd_numbers(input_array)
        self.assertEqual(result, [])

    def test_4(self):
        input_array = [3,2,77,44,99,22]
        result = sort_odd_numbers(input_array)
        self.assertEqual(result, [3,2,77, 44, 99, 22])

    if __name__ == "__main__":
        unittest.main()