#!/usr/bin/python3
"""
This is the module documentation. The module create a class Base
"""


class Base:
    """Base class for managing IDs."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int): An optional ID for the instance. If not provided,
            an ID is automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
