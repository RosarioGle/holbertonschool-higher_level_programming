#!/usr/bin/python3

"""create an empty class"""


class Rectangle:
    """define the rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize the new rectangle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """value is the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """value is the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print the rectangle with #"""
        empty = ""
        result = []
        if self.__width == 0 or self.__height == 0:
            return empty
        return "\n".join(
            [str(self.print_symbol) * self.width for _ in range(self.height)]
            )

    def __repr__(self):
        """return a representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print a sentence after deleting the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """define the new rectangle

        Args:
            rect_1(rectangle): rectangle 1
            rect_2(rectangle): rectangle 2"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """return the new square with width == height == size

        Args:
            size(int): the size"""
        return cls(size, size)
