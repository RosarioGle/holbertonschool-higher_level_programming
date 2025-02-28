#!/usr/bin/python3
"""
Write a class BaseGeometry
"""


class BaseGeometry:
    """
    the class BaseGeometry
    """

    def area(self):
        """
        raises an Exception with the
        message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Verify if the value is an integer and superior to 0

        Args:
            name(str): name of the form
            value(int): the value

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
