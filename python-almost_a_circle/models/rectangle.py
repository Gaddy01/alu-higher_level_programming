#!/usr/bin/python3
"""
This is the module documentation. The module create a class Base
"""


from models.base import Base

class Rectangle(Base):
    """Represents a rectangle, inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate (default: 0).
            y (int): The y-coordinate (default: 0).
            id (int): An optional ID for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the `#` character."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
