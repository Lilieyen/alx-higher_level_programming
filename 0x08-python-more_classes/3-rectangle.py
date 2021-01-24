#!/usr/bin/python3
"""
Define a class rectangle
"""


class Rectangle:
    """
    attribute instantiation
    """
    def __init__(self, width=0, height=0):
        """
        intialzie height and width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0')
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('width must be >=0')
        self.__height = value

    def area(self):
        """get area of rectangle"""
        rec_area = self.__height * self.__width
        return rec_area

    def perimeter(self):
        """get perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2*self.height + 2*self.width)

    def __str__(self):
        """prints rectangle"""
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            rect += '#' * self.__width
            if i != self.__height - 1:
                rect += '\n'
        return rect