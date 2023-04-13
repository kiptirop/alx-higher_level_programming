#!/usr/bin/python3
# 8-class_to_json.py
"""Defines a function that converts a class instance to a JSON serializable dictionary."""


def class_to_json(obj):
    """Convert a class instance to a JSON serializable dictionary.
    Args:
        obj: An instance of a Python class.
    Returns:
        A dictionary representation of the class instance that can be serialized to JSON.
    Raises:
        TypeError: If the input object is not an instance of a class.
    """
    if not isinstance(obj, object):
        raise TypeError("Input must be an instance of a class")
    return obj.__dict__
