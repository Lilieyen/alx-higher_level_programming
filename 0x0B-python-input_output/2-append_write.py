#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """appending to file then returning num of chars"""
    with open(filename, mode="a", encoding="utf-8") as myfile:
        myfile.write(text)
        return len(text)
