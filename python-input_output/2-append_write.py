#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Function"""
    with open(filename, "a") as f:
        return f.write(text)
