#!/usr/bin/python3
"""
class named CountedIterator that extends the built-in
iterator obtained from the iter function
"""


class CountedIterator:
    """
    define CounterIterator class
    """
    def __init__(self, iterable):
        """
        initialize the CountedIterator
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        return the iterator itself
        """
        return self

    def __next__(self):
        """
        return the next item and increment the counter
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
        return the number of items iterated over
        """
        return self.count
