#!/usr/bin/python3

"""Defines a function that returns an object reoresented by JSON string"""

import json

def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.
    """
    return json.loads(my_str)
