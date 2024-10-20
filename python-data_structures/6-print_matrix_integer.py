#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for liste in matrix:
        for i in liste:
            if i == liste[-1]:
                print("{}".format(i), end="\n")
            else:
                print("{}".format(i), end=" ")
