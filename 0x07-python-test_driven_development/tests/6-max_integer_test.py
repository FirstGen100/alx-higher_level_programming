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

    def test_max_at_end(self):
        test = [1,2,3,4,5]
        self.assertEqual(max_integer(test), 5)

    def test_max_at_beginning(self):
            test = [10, 9, 8, 7]
            self.assertEqual(max_integer(test), 10)

    def test_max_at_middle(self):
        test = [1,2,5,4,3]
        self.assertEqual(max_integer(test), 5)

    def test_one_negative_number(self):
        test = [10, -1, 3, 5]
        self.assertEqual(max_integer(test), 10)

    def test_all_negative_numbers(self):
        test = [-1, -2, -3, -4]
        self.assertEqual(max_integer(test), -1)


if __name__ == '__main__':
    unittest.main()
