#!/usr/bin/python3

for i in range(1, 89):
    if i / 10 < i % 10:
        print("{0:0=2d}".format(i), end=", ")
print("89")
