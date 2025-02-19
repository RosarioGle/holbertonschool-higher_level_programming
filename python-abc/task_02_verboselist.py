#!/usr/bin/python3
"""
class named VerboseList that extends the Python list class
"""


class VerboseList(list):
    """
    define VerboseList class
    """
    def append(self, item):
        """
        Adds an item to the end of the list
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Adds several items to the list in a single operation
        """
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """
        Deletes a specific item from the list
        """
        if item in self:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)
        else:
            print("Item [{}] not found in the list.".format(item))

    def pop(self, index=-1):
        """
        Deletes and returns an element to a given position
        (by default, the last one)
        """
        if self:
            item = self[index]
            print("Popped [{}] from the list.".format(item))
            return super().pop(index)
        else:
            print("Cannot pop from an empty list.")
            return None
