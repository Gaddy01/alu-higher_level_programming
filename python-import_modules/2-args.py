#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        print("{} arguments".format(len(agv)))
    else:
        print("{} argument".format(len(agv)))

    for i in (1, len(argv)):
        print("{}: {}".format(i, argv[i]))
