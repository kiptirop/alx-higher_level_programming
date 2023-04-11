#!/usr/bin/python3
"""
Module for Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a Square instance with size
        """
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    @property
    def size(self):
        """
        Returns the size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the Square
        """
        self.integer_validator("size", value)
        self.__size = value
        self.__width = value
        self.__height = value

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer
        """
        if type(value) != int or value <= 0:
            raise ValueError("{} must be an integer greater than 0".format(name))

    def area(self):
        """
        Returns the area of the Square instance
        """
        return self.__size ** 2
