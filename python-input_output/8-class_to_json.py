#!/usr/bin/python3
"""
returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON
serialization of an object
"""


def class_to_json(obj):
    """
    Args:
        obj: an instance of a class

    Returns:
        dict: a dictionary containing all serializable attributes
        of the objet's instance
    """
    return obj.__dict__
