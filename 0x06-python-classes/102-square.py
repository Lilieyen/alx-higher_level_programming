#!/usr/bin/python3
"""
class square
"""


class Square():
    """
    instantiation of class square
    """
    def __init__(self, size=0):
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        """
        return area of a sq
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

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.__size == other.__size
        return False

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.__size != other.__size
        return False

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.__size < other.__size
        return False

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.__size > other.__size
        return False

    def __le__(self, other):
        if isinstance(other, Square):
            return self.__size <= other.__size
        return False

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.__size >= other.__size
        return False
