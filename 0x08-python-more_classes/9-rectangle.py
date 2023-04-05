#!/usr/bin/python3

"""
a class Rectangle that defines a rectangle
"""

class Rectangle:
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string once deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """returns a printable string"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """returns a printable string representation of the rec for reproduction"""
        return "Rectangle({}, {})".format(self.width, self.height)

    @property
    def width(self):
        """getter for the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area for the rec"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rect based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 >= area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rect instance that is a square"""
        return cls(size, size)
