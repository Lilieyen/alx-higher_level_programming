#!/usr/bin/python3
"""defining a square"""


class Square:
    """private instance attribute"""
    def __init__(self, size=0):
        """initializing size"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
