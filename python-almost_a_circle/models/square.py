#!/usr/bin/python3
"""
This is the module documentation. The module create a class square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (same for width and height).
            x (int): The x-coordinate (default: 0).
            y (int): The y-coordinate (default: 0).
            id (int): An optional ID for the instance.
        """
        super().__init__(size, size, x, y, id)

        def __str__(self):
            """
            Return a string representation of the Square.
            """
            return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
