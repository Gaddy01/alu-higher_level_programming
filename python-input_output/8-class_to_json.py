#!/usr/bin/python3
"""
fijeuf89iewfew ewf32wf32wefsc
wqfc8w9qf c2eiuqwifh9wq fqi1qeu90
dh8buiwqgfb32 qwfuyuyqwh qweiq
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
