#!/usr/bin/python3

"""create an empty class"""


class Square:
    """Define the classe square."""
    def __init__(self, size=0):
        """Initialize the new Square.

        Args:
        size: the size
        """
        self.__size = size

    @property
    def size(self):
        """the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """the value is the square length"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print a square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
