#!/usr/bin/python3
"""finding area of class square"""


class Square:
    """representing a square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

                def area(self):
                    """getting area of square"""
                    return (self.__size) ** 2
