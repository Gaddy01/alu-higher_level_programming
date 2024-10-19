#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        print("{} arguments".format(len(argv)))
    else:
        print("{} argument".format(len(argv)))

    for i in (1, len(argv)):
        print("{}: {}".format(i, argv[i]))
