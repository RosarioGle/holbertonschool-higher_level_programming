#!/usr/nin/python3
"""
writes a string to a text file (UTF8) and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number
    of characters written

    Args:
        filename (str): the name/path of the file to write
        text (str): the string to write to the file

    Returns:
        int: the number of characters written to the file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
