#!/usr/bin/python3
def no_c(my_string):
    strl = list(my_string)

    for ch in strl:
        if ch == 'c' or ch == 'C':
            strl.remove(ch)

    new_string = ''.join(strl)
    return new_string
