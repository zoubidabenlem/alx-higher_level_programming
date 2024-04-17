#!/usr/bin/python3
""" student module
"""


class Student:
    """ defines a student
    """
    def __init__(self, first_name, last_name, age):
        """ initializes a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves the dictionary
        representation of a Student
        instance
        """
        if isinstance(attrs, list) and not len(attrs):
            return {}
        if attrs:
            inst_dict = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    inst_dict[att] = self.__dict__[att]
            return inst_dict
        return self.__dict__
