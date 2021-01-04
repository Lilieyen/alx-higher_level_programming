#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            printed += 1
        except Exception:
            pass
    print("")
    return printed
