#!/usr/bin/python3
"""
uhvbeijdskvniusahfwe ewijfewuhoiew
wefwefhiewojfwpefwe
wefwoeijfiweojfewf weofijwef
"""


class BaseGeometry:
    """
    dwuq bfyiuhowqNHDCFEWD SGFQVEWR F
    Fqnfveusaifov dsg
    efasvfgjriospgbewa
    fewvgkvoprj5eoqwinrvfmoqpewb
    """
    def __init__(self, width, height):
        # Validate width and height using integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Initialize width and height as private attributes
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <=0:
            raise ValueError(f"{name} must be greater than 0")
