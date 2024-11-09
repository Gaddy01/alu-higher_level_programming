#!/usr/bin/python3
""" This module creates a class, 'myList'
    This module creates a class, 'myList'
    This module creates a class, 'myList'
"""


class MyList(list):
    """
    MyList class that inherits from the built-in list class and .
    This class is designed to represent a list with an added met.
    """

    def __init__(self):
        """
        Initializes an instance of the MyList class.

        Inherits from the built-in list class and does not require
        """
        super().__init__()  # Initialize the parent class (list)

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        Uses Python's built-in sorted() function to sort ult
        without modifying the original list order.
        """
        print(sorted(self))

    def __str__(self):
        """
        Returns a string representation of the MyList object.
        
        This method returns the list as a string, making it easy to print
        the MyList instance directly.
        """
        return str(self)  # Return the string representation of the list
