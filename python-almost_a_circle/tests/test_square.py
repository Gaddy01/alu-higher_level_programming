#!/usr/bin/python3


import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_str(self):
        s = Square(3, x=1, y=2, id=5)
        self.assertEqual(str(s), "[Square] (5) 1/2 - 3")

if __name__ == "__main__":
    unittest.main()
