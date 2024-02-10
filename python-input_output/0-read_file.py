#!/usr/bin/python3

import sys
def read_file(filename=""):

    with open("my_file_0.txt", "r") as filename:
        print(filename.read(), end ="")
