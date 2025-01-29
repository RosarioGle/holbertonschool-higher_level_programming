#!/usr/bin/python3

"""create an empty class"""


class Square:
    """define the class square"""
    def __init__(self, size=0):
        """Initialize the new Square

        Args:

        size: the size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
