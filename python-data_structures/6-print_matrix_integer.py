#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        return "\n"
    else:
        for liste in matrix:
            for i in liste:
                if i == liste[-1]:
                    print("{:d}".format(i), end="\n")
                else:
                    print("{:d}".format(i), end=" ")
