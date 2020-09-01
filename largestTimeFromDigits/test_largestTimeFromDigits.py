#test_largestTimeFromDigits.py
import unittest
from largestTimeFromDigits import LargestTimeFromDigits

class LargestTimeFromDigitsTests(unittest.TestCase):
    def setUp(self):
        self.lt = LargestTimeFromDigits()
    def test_one(self):
        self.assertEqual(self.lt.largest_time([1,2,3,4]), "23:41")
    def test_two(self):
        self.assertEqual(self.lt.largest_time([1,2,2,1]), "22:11")
    def test_invalid(self):
        self.assertEqual(self.lt.largest_time([5,5,5,5]), "")

if __name__ == '__main__':
    unittest.main()