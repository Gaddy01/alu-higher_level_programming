#!/usr/bin/python3
"""
uhvbeijdskvniusahfwe ewijfewuhoiew
wefwefhiewojfwpefwe
wefwoeijfiweojfewf weofijwef
"""


class BaseGeometry:
    """
    Empty class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
