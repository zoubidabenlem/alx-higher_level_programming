#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    rN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    prev = 0
    for letter in (reversed(roman_string)):
        val = rN[letter]
        if val < prev:
            number -= val
        else:
            number += val
        prev = val
    return number
