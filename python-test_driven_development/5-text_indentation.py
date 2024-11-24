#!/usr/bin/python3
"""
This module writes a function that prints a text with
2 new lines after each of these characters: . ? and :
"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after
     each of these characters: . ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a buffer to hold the current line
    result = ""
    for char in text:
        result += char
        if char in ".:?":
            print(result.strip())
            print()  # Add the required 2 new lines
            result = ""  # Reset the buffer
    if result.strip():  # Print any remaining text
        print(result.strip())
