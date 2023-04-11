#!/usr/bin/python3
"""
Module for Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height
        """
        self.__width = width
        self.__height = height
        super().__init__()

    def __str__(self):
        """
        Returns a string representation of the Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area of the Rectangle instance
        """
        return self.__width * self.__height
    
    @property
    def width(self):
        """
        Returns the width of the Rectangle
        """
        return self.__width
    
    @property
    def height(self):
        """
        Returns the height of the Rectangle
        """
        return self.__height
    
    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle
        """
        self.integer_validator("width", value)
        self.__width = value
    
    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle
        """
        self.integer_validator("height", value)
        self.__height = value
    
    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer
        """
        if type(value) != int or value <= 0:
            raise ValueError("{} must be an integer greater than 0".format(name))
