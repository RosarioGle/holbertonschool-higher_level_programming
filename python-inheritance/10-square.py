#!/usr/bin/python3
"""Write a class Square who inherit
from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a Square"""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): size of the square"""
        self.__size = self.integer_validator("size", size)

    def area(self):
        """
        area of the square

        Returns:
            int: square of the size
        """
        return self.__size ** 2
