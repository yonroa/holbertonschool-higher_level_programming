#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class with different methods to prove the function"""

    def test_numbers(self):
        """Test the function with a list of numbers"""
        self.assertEqual(max_integer([3, 5, 7, 2]), 7)
        self.assertEqual(max_integer([-8, -10, -100, -1]), -1)
        self.assertEqual(max_integer([-7, 0, 7]), 7)
        self.assertEqual(max_integer([-5.5, 0.3, 7.5722]), 7.5722)
        self.assertEqual(max_integer([-3.7, -0.6, -105, -33.3]), -0.6)

    def test_types(self):
        """Test the function whit a list with strings"""
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 4, "cinco"])
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 'cuatro', 5])
        self.assertRaises(TypeError, max_integer, [1, 2, "3", 4, 5])
        self.assertEqual(max_integer(["hello", "hi", "hey", "ey!"]), "hi")

    def test_lists(self):
        """Test the function whit type no-list"""
        self.assertRaises(TypeError, max_integer, 8)
        self.assertRaises(TypeError, max_integer, 3.5)
        self.assertRaises(TypeError, max_integer, -2)
        self.assertRaises(TypeError, max_integer((3, 7, 4)))
        self.assertRaises(TypeError, max_integer("matrix"))
        self.assertRaises(TypeError, max_integer, True)

    def test_void(self):
        """Test the function with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Test the function with just one number"""
        self.assertEqual(max_integer([3]), 3)

    def test_identic(self):
        """Test the function with the same number"""
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)

    def test_none(self):
        """Test the function with None"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == "__main__":
    unittest.main()
