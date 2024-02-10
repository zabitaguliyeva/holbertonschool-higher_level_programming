#!/usr/bin/python3
"""Geometry module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is not a Sparta"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        c = __class__.__name__
        return ("[{}] {}/{}".format(c, self.__size, self.__size))
