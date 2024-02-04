#!/usr/bin/python3
"""Area of a square"""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """size must be an integer, otherwise raise a TypeError exception
        with the message size must be an integer
        if size is less than 0, raise a ValueError exception with
        the message size must be >= 0"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
