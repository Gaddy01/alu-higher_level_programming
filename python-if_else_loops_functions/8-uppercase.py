#!/usr/bin/python3


def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char):
            if ord(char) <= ord('z'):
                # Convert lowercase to uppercase by subtracting 32 from its ASCII value
                char = chr(ord(char) - 32)
                print("{}".format(char), end="")
    print()
