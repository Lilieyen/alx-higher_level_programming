#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """private instance attribute width"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            """instantiation of width"""
            return (self.__width)
            @width.setter
            def width(self, value):
                self.__width = value
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            elif value < 0:
                raise ValueError('width must be >= 0')

            @property
            def height(self):
                """instantiation of height"""
                return (self.__height)

            @height.setter
            def height(self, value):
                self.__height = value
                if not isinstance(value, int):
                    raise TypeError('height must be an integer')
                elif value < 0:
                    raise ValueError('height must be >= 0')
