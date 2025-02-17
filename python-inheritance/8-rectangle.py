#!/usr/bin/python3
"""
Rectangle module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """Rectangle constructor

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
