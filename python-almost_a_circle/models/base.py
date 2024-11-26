#!/usr/bin/python3
"""
This is the module documentation. The module create a class Base
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries
            or "[]" if None or empty.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = f"{cls.__name__}.json"  # File name based on class name
        list_dicts = []

        if list_objs is not None:
            """Convert each object in list_objs
            to a dictionary using to_dictionary()"""
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert list of dictionaries to JSON string
        json_string = cls.to_json_string(list_dicts)

        # Write JSON string to the file
        with open(filename, "w") as file:
            file.write(json_string)
