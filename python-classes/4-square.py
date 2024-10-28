#!/usr/bin/python3


 """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square's side.
"""


class Square:
    """
    This is an empty class
    """
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except Exception as e:
            raise e
   @property
    def size(self):
        """Getter for the private attribute __size."""
        return self.__size

    def area(self):
        """Calculate and return the area of the square."""
        return self.size**2
