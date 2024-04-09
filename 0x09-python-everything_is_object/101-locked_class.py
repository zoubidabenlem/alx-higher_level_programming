#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, name))
        object.__setattr__(self, name, value)
