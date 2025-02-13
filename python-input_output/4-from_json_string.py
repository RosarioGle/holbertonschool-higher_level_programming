#!/usr/bin/python3
"""
returns an object (Python data structure) represented by a
JSON string
"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str (str): the JSON string to convert

    Returns:
        object: the python data structure represented be the
        JSON string    
    """
    return json.loads(my_str)
