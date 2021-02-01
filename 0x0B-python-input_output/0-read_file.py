#!/usr/bin/python3
"""encoding with UTF8"""


def read_file(filename=""):
    """read whole file"""
    with open(filename, encoding='utf-8') as myfile:
        print(myfile.read(), end="")
