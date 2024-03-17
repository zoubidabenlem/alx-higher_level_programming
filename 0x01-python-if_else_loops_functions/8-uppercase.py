#!/usr/bin/python3
def uppercase(str):
    result=""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            result+=(chr(ord(str[i])-32))
        elif ord(str[i]) == 32:
            result+=" "
        else:
            result+=str[i]
    print(result)
