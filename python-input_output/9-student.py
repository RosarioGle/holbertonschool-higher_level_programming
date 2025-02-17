#!/usr/bin/python3
"""
define a student class
"""


class Student:
    """
    the student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the sutdent
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns:
            dict: a dictionary containing the student's attributes
        """
        return self.__dict__
