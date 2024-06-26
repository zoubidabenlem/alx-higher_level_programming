#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle:
    """Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes an instance of the
        Rectangle class
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the private instance
        variable "width"
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance
        variable "width"
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the private instance
        variable "height"
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance
        variable "height"
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle
        """
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation
        of an instance of the class Rectangle
        """
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) *
                self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Returns a string representation of
        the rectangle to be able to recreate
        a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes an instance of the Rectangle
        class and prints a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the largest area
        or rect_1 if they are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_1 if rect_1.area() > rect_2.area() else rect_2
