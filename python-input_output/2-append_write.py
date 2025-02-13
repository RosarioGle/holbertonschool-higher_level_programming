#!/usr/bin/python3
"""
appends a string at the end of a text file (UTF8) and returns
the number of characters added
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str): the name of the file to append
        text (str): the string to append to the file

    Returns:
        int: the number of characters added to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
