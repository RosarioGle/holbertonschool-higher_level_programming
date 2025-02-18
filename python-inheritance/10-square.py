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
        super().__init__(size, size)
        self.__size = self.integer_validator("size", size)

    def area(self):
        """
        Returns:
            int: square of the size
        """
        return self.__size ** 2
