#!/usr/bin/python3
"""
reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    reads and print the content of a text file
    
    Args:
        filename (str): the name/path of the file
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
