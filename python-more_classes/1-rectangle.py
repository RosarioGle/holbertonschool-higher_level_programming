#!/usr/bin/python3

"""create an empty class"""


class Rectangle:
    """define the rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the new rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """value is the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """value is the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
