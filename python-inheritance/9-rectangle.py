#!/usr/bin/python3
"""Write a class Rectangle who inherit
from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a Rectangle."""

    def __init__(self, width, height):
        """Initialize a new rectangle.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """print Rectangle with the width and height"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
