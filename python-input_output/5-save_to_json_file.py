#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj (any): the object to be serialized and writen to
        the file
        filename (str): the name of the file to write the JSON data to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
