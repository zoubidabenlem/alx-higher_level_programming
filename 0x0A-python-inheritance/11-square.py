#!/usr/bin/python3
""" Rectangle Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a square
    """
    def __init__(self, size):
        """ Initializes a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """ Returns a string representation
        of a square
        """
        return f"[Square] {self.__size}/{self.__size}"
