#!/usr/bin/python3


def uppercase(str):
    NUM1 = ord('a')
    NUM2 = ord('z')
    for char in str:
        # Check if the character is a lowercase letter
        if NUM1 <= ord(char) <= NUM2:
            #Convert to uppercase by subtracting 32 from its ASCII value
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
