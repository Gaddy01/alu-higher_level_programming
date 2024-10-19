#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_arg = len(argv)-1
    if num_arg > 1:
        print("{} arguments".format(num_arg))
    else:
        print("{} argument".format(num_arg))

    for i in (1, num_arg):
        print("{}: {}".format(i, argv[i]))
