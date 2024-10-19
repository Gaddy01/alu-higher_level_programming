#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_arg = len(argv)-1
    if num_arg == 0: 
        print("{} arguments".format(num_arg))
        exit()
    elif num_arg == 1:
        print("{} argument".format(num_arg))
    else:
        print("{} arguments".format(num_arg))

    for i in range(1, num_arg):
        print("{}: {}".format(i, argv[i]))
