#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)+1):
        if i == len(str):
            print("\n")
            break
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            print("{}".format(chr(ord(str[i])-32)),end="")
        elif ord(str[i]) == 32:
            print(" ",end="")
        else:
            print(str[i],end="")  
