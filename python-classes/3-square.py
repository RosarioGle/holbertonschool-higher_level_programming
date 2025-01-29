#!/usr/bin/python3

"""Create an empty class"""


class Square:
    """Define the class square"""
    def __init__(self, size=0):
        """Initialize the new Square

        Args:

        size: the size
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Return the square area"""
        return self.__size * self.__size
