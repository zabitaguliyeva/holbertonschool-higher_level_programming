#!/usr/bin/python3
for ascii_code in range(ord('a'), ord('z')+1):
    alpha_letters = chr(ascii_code)
    if alpha_letters not in 'qe':
        print("{}".format(alpha_letters), end="")
