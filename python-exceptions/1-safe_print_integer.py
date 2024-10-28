#!/usr/bin/python3


def safe_print_integer(value):
    try:
        int(value)
        return True
    except:
        return False
