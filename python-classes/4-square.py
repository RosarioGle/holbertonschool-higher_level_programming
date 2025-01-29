#!/usr/bin/python3

"""create an empty class"""


class Square:
    """define the class square"""
    def __init__(self, size):
        """Initialize the new Square

        Args:

        size: the size
        """
        self.__size = size

    @property
    def size(self):
        """The size od the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """The value is the square length"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)
