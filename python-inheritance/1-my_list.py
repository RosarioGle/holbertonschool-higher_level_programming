#!/usr/bin/python3
"""MyList that inherits from list"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
