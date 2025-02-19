#!/usr/bin/python3
"""
Write a class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    define Square class
    """
    def __init__(self, size):
        """
        Args:
            size (int): size of the Square
        """
        if size is not None:
            self.__size = self.integer_validator("size", size)

    def area(self):
        """
        Returns:
            int: the square of the size
        """
        return self.__size ** 2
