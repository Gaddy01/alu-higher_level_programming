#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    # Check if the matrix is truly empty or has empty sub-lists
    # if len(matrix) == 0 or (len(matrix) == 1 and len(matrix[0]) == 0):
    if matrix == [[]] or matrix == []:
        print(" ")
        return
    else:
        for liste in matrix:
            for i in liste:
                if i == liste[-1]:
                    print("{:d}".format(i), end="\n")
                else:
                    print("{:d}".format(i), end=" ")
