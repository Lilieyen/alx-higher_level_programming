#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for lst in matrix:
        for x in lst:
            l = len(lst) - 1
            if lst.index(x) == l:
                print("{:d}".format(x))
            else:
                print("{:d}".format(x), end=' ')
