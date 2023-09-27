#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_args(self):
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        test = []
        self.assertIsNone(max_integer(test))

    def test_non_int(self):
        test = [1, '2', 3, 4]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_single_element(self):
        test = [10]
        self.assertEqual(max_integer(test), 10)


if __name__ == '__main__':
    unittest.main()
