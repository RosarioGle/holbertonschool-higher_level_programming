#!/usr/bin/python3

def add_integer(a, b=98):

    """
    Return the sum of two integer.
    The arguments in float are converted to ints before the addition.
    
    Taises:
    TypeError: If either of Arguments are non-integer and non-float.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
