#!/usr/bin/python3

'''
########################################## TEST 0
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
'''

######################################### TEST 1
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
