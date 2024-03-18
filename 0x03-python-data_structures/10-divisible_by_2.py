#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    stuff = []
    for item in my_list:
        if item % 2 == 0:
            stuff.append(True)
        else:
            stuff.append(False)
    return stuff
