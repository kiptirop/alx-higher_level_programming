#!/usr/bin/python3

"""A function that adds 2 integers"""

def add_integer(a, b=98):
    """Returns the addition of integers a and b
    Float arguments are typecasted to ints before addition is performed.
    
    Raises:
        TypeError: If a/b is a non-integer and non-float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float.")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float.")
    a = int(a)
    b = int(b)
    return a + b
