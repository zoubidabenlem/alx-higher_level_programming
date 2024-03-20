#!/bin/usr/python3
def multiply_list_map(my_list=[], number=0):
    list_mul = list(map(lambda v : v * number, my_list))
    return list_mul
