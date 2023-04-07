#!/usr/bin/python3

"""A function that adds 2 integers"""

def add_integer(a, b=98):
    """Returns the addition of integers a and b"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float.")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float.")
    a = int(a)
    b = int(b)
    return a + b
