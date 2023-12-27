import unittest
from rgb import rgb

class TestRGBConversion(unittest.TestCase):
    def test_valid_rgb_values(self):
        self.assertEqual(rgb(255, 0, 0), 'FF0000')
        self.assertEqual(rgb(0, 255, 0), '00FF00')
        self.assertEqual(rgb(0, 0, 255), '0000FF')
        self.assertEqual(rgb(255, 255, 255), 'FFFFFF')

    def test_out_of_range_values(self):
        # Values below 0 should be rounded to 0
        self.assertEqual(rgb(-10, 128, 200), '000080')

        # Values above 255 should be rounded to 255
        self.assertEqual(rgb(300, 150, 500), 'FF96FF')

    def test_rounding_values(self):
        # Rounding to the closest valid values
        self.assertEqual(rgb(123.4, 234.8, 78.2), '7BEA4E')

if __name__ == '__main__':
    unittest.main()
