#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for i in range(len(row)):
            if (i + 1) % 3 != 0:
                print("{} ".format(row[i]), end="")
            else:
                print("{}".format(row[i]), end="")
        print()
