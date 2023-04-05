#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle
"""

class Rectangle:
    """Defines a Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """"getter for the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the instance height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns the printable representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            rect += "#" * self.width + "\n"
        return rect[:-1]

    def __repr__(self):
        """returns the string rep of the rect reproduction"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """prints a message after every deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
