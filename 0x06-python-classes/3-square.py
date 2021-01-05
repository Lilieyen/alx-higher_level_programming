#!/usr/bin/python3
"""finding area of class square"""


class Square:
    """private instance attribute"""
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length
        """getting area"""
        def area(self):
            return self.breadth * self.length
