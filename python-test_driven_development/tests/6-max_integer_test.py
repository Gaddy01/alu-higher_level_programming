#!/usr/bin/python3


import unittest
max_integer = __import__('6-max_integer').max_integer

class TextMaxInteger(unittest.TestCase):
    def test_integer(self):
        # Test if the list is empty
        self.assertAlmostEqual(max_integer([]), None)
