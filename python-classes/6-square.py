#!/usr/bin/python3


"""
This code create an empty class.
"""


class Square:
    """
    A class to represent a square.
    """

    def __init__(self, size=0, position=(0,0)):
        self.size = size  # This will use the setter
        self.position = position

    @property
    def size(self):
        """Getter for the private attribute __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private attribute __size with validation.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.size == 0:
            print("")  # Print an empty line
        else:
            for _ in range(self.size):
                print("#" * self.size)
