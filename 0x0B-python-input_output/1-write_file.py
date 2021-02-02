#!/usr/bin/python3
"""write to a file"""


def write_file(filename="", text=""):
    """writing to a file"""
    with open("filename", "w", encoding='utf-8') as myfile:
        myfile.write(text)
        return len(text)
