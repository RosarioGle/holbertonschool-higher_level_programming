#!/usr/bin/python3
"""
creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename (str): the name of the JSON file to read from

    Returns:
        object: the python object represented be the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
