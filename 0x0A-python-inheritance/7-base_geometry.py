#!/usr/bin/python3
""" base_geometry module
"""


class BaseGeometry:
    """ BaseGeometry class
    """
    def area(self):
        """ raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if "value" is an integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
