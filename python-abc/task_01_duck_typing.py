#!/usr/bin/python3
"""
class named Shape with two abstract methods: area and perimeter
"""
from abc import *
import math


class Shape(ABC):
    """
    define Shape class
    """
    @abstractmethod
    def area(self):
        """
        abstract base class representing a geometric area
        """
        pass

    def perimeter(self):
        """
        abstarct base class representing a geometric perimeter
        """
        pass

class Circle(Shape):
    """
    define Circle class
    """
    def __init__(self, radius):
        """
        initialize Circle with a radius
        """
        self.radius = radius

    def area(self):
        """
        calculate and return the area of the circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        calculate and return the perimeter of the circle
        """
        return abs(2 * self.radius * math.pi)

class Rectangle(Shape):
    """
    define Rectangle class
    """
    def __init__(self, width, height):
        """
        initialize Rectangle with width and height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        calculate and return the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        calculate and return the parimeter of the rectangle
        """
        return abs(2 * (self.width + self.height))

def shape_info(shape):
    """
    print the area and the perimeter
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))