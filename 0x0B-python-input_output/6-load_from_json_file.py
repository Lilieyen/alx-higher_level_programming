#!/usr/bin/python3
"""create an object from a JSON file"""

import json


def load_from_json_file(filename):
    """object from json file using with statement"""
    with open(filename, mode="r", encoding="utf-8") as myfile:
        return json.load(myfile)
