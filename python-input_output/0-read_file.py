#!/usr/bin/python3
"""Read file"""

def read_file(filename=""):
    """Function"""
    with open("my_file_0.txt", "r") as filename:
        print(filename.read(), end ="")
