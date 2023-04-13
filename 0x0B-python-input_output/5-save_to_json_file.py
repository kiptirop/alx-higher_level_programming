#!/usr/bin/python3

"""Defines a function that writes an Object to a text file, using a JSON rep"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes the JSON representation of an object to a file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

