#!/usr/bin/python3
"""Class Inheritance"""


def inherits_from(obj, a_class):
    """checks for inheritance"""
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
