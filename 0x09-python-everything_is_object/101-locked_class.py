#!/usr/bin/python3
# 101-locked_class.py

"""Defines a locked class."""

class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} does not allow setting new attributes")
        super().__setattr__(name, value)

