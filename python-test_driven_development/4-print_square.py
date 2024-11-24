#!/usr/bin/python3
"""
This module writes a function that prints a square with the character #
"""

def print_square(size):
    """The function that prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
