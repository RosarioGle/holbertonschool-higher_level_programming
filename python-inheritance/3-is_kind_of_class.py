#!/usr/bin/python3
"""Function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class, ohterwise False"""


def is_kind_of_class(obj, a_class):
    """function that return True or False if object is an instance"""
    return isinstance(obj, a_class)
