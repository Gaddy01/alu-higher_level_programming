#!/usr/bin/python3

from calculator_1.py import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    some = add(a, b)
    substr = sub(a, b)
    multip = mul(a, b))
    divis = div(a, b)
    print("{} + {} = {}".format(a, b, some))
    print("{} - {} = {}".format(a, b, substr))
    print("{} * {} = {}".format(a, b, multip))
    print("{} / {} = {}".format(a, b, divis))
