#!/usr/bin/python3
"""Private instance attribute: size
   Instantiation with optional size: def __init__(self, size=0):
   size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
   if size is less than 0, raise a ValueError exception with the message size must be >= 0"""


class Square:
    """Size validation"""
    def __init__(self, size=0):
        self.__size = size
