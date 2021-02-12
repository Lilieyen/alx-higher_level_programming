#!/usr/bin/python3
"""
printing Square based off of 4-square.py
"""


class Square():
    """
    This is the Square class
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returning  area of a square.
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        for x in range(0, self.__size):
            for y in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
