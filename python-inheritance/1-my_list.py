#!/usr/bin/python3
"""MyList that inherits from list"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
