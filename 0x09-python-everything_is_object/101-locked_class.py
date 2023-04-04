#!/usr/bin/python3
# 101-locked_class.py

"""Defines a locked class."""

class LockedClass:
    __slots__ = ['first_name']

    """
    does not allow setting new attributes but attributes called 'first_name'.

    """
