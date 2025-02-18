#!/usr/bin/python3
"""
Square module.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Args:
            size (int): size of the Square
        """
        self.__size = self.integer_validator("size", size)

    def area(self):
        """
        Returns:
            int: square of the size
        """
        return self.__size ** 2

    def __str__(self):
        """print Rectangle with the width and height"""
        return ("[{}] {}/{}".format(__class__.__name__,
                                    self.__size, self.__size))
