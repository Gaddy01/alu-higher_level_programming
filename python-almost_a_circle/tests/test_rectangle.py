#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)

    def test_str(self):
        r = Rectangle(2, 4, id=1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 2/4")

if __name__ == "__main__":
    unittest.main()
