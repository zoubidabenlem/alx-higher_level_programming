#!/usr/bin/python3
'''attribute definition and error handling'''


class Square:
    '''square but with size and type exceptions'''
    def __init__(self, size=0):
        self.__size = size
    '''calculate square'''
    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
