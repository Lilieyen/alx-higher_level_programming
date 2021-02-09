#!/usr/bin/python3
"""write an object to a text file using JSON"""


def save_to_json_file(my_obj, filename):
    """object to text file using with statement"""
    with open(filename, mode="w") as myfile:
        myfile.write(my_obj)
