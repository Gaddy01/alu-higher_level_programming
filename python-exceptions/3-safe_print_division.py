#!/usr/bin/python3


def safe_print_division(a, b):
    result = None
    try:
        result = a / b  # Perform the division
    except ZeroDivisionError:
        result = None  # Set result to None if division by zero occurs
    finally:
        print("Inside result: {}".format(result))  # Print the result in the finally block
    return result  # Return the result (either the division or None)
