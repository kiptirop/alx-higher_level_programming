#!/usr/bin/python3

"""Returns True if the object is an instance"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or its subclasses; otherwise False.
    """
    return isinstance(obj, a_class)
