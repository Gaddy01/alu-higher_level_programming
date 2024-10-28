#!/usr/bin/python3


def safe_print_integer(value):
    try:
        str(value).isdigit()
        print("{:d}".format())
        return True
    except:
        return False
