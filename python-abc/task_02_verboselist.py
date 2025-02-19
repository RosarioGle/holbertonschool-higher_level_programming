#!/usr/bin/python3
"""
class named VerboseList that extends the Python list class
"""


class VerboseList(list):
    """
    define VerboseList class
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)
        else:
            print("Item [{}] not found in the list.".format(item))

    def pop(self, index=-1):
        if self:
            item = self[index]
            print("Popped [{}] from the list.".format(item))
            return super().pop(index)
        else:
            print("Cannot pop from an empty list.")
            return None
