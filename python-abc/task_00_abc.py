#!/usr/bin/python3
"""
abstract class named Animal using the ABC package
"""
from abc import *


class Animal(ABC):
    """
    define Animal class
    """
    @abstractmethod
    def sound(self):
        """
        abstract method named sound using the @abstractmethod decorator
        """
        pass

class Dog(Animal):
    """
    define Dog class inheriting from Animal
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    define Cat class inheriting from Animal
    """
    def sound(self):
        return "Meow"