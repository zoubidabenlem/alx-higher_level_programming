#!/bin/usr/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    rN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    prev = False
    prevLet = False

    for letter in (reversed(roman_string)):
        for k, v in rN.items():
            if letter == k:
                if letter == 'I' and prev and not prevLet:
                    number -= 1
                else:
                    number += v
                    prev = True
                    if letter == 'I':
                        prevLet = True
    return number
