#!/usr/bin/python3
"""Creating rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ the init function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area function """
        return self.__width * self.__height

    def display(self):
        """ display function """
        if self.__y > 0:
            print("\n" * (self.__y), end="")
        for c in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """output"""
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def update(self, *args, **kwargs):
        """instance attributes"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """attributes to dictionary"""
        """output"""
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return {'x': x, 'y': y, 'id': id, 'height': h, 'width': w}
