#!/usr/bin/python3
"""
Write a class Rectangle who inherit
from BaseGeometry (7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a Rectangle"""

    def __init__(self, width, height):
        """Instantiation with width and height
    Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle

    Raises:
        TypeError: If width or height is not an integer
        ValueError: If width or height is less than or equal to 0
    """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
