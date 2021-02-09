#!/usr/bin/python3
"""returning an object represented by a Json string"""

import json


def from_json_string(my_str):
    """return an object from a JSON formatted string"""
    return json.loads(my_str)
