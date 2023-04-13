#!/usr/bin/python3

"""Defines a function that reads a text file"""

def read_file(filename=""):
    """Reads UTF8 and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
