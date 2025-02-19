#!/usr/bin/python3
"""
Design two mixin classes, SwimMixin and FlyMixin, each
equipped with methods swim and fly respectively
"""


class SwimMixin:
    """
    define SwimMixin class
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    define FlyMixin class
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    define Dragon class
    """
    def roar(self):
        print("The dragon roars!")
