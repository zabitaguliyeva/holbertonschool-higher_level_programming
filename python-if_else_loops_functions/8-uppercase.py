#!/usr/bin/python3
def uppercase(str):
    g = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = ord(i) - 32
            g = g + chr(i)
        else:
            g += i

    print(g)
