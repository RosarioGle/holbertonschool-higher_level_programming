#!/usr/bin/python3
"""
returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj (any): the objext to be serialized

    Returns:
        str: JSON representation of my_obj
    """
    return json.dumps(my_obj)
