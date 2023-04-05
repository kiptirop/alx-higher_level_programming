#!/usr/bin/python3

"""Defines a Rectangle"""

class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rect"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """returns the rectangles printable print rep"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.height):
                rect += "#" * self.width
                if i != self.height - 1:
                    rect += "\n"
            return rect

    def __repr__(self):
        """returns the recs printable rep for reproduction"""
        return f"Rectangle({self.width}, {self.height})"

