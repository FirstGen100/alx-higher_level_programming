#!/usr/bin/python3
'''making a unittest for max_integer(list[])'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''unittest for max_integer'''
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_singleinput(self):
        self.assertEqual(max_integer([4]), 4)

    def test_error(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 2, 4])

    def test_negative(self):
        self.assertEqual(max_integer([1, 2, 3, 5, -6]), 5)

    def test_maxbeginning(self):
        self.assertEqual(max_integer([7, 6, 5, 1]), 7)
