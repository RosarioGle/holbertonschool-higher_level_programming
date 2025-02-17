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
            height (height): height of the Rectangle

        Raises:
            AttributeError: if missing width arg
            AttributeError: if missing height arg
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
