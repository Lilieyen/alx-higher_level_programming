#!/usr/bin/pythoniii3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    newList = my_list[::-1]
    for x in newList:
        print("{:d}".format(x))
        return my_list
