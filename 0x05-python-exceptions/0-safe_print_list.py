#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list = []
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
        except Exception:
            pass
        print("")
        return list
