#!/usr/bin/python3
"""write an object to a text file using JSON"""

import json


def save_to_json_file(my_obj, filename):
    """object to text file using with statement"""
    with open(filename, mode="w", encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
