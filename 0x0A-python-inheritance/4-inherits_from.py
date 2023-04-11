#!/usr/bin/python3
"""0-inherits_from module"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited (directly
    or indirectly) from a_class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a class that inherited (directly
        or indirectly) from a_class; otherwise False.
    """
    return isinstance(obj, type) and issubclass(type(obj), a_class) and type(obj) != a_class
