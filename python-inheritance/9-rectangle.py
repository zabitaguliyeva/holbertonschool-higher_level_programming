#!/usr/bin/python3
"""Geometry module"""


BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """This is spartaaa..."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        c = __class__.__name__
        return ("[{}] {}/{}".format(c, self.__width, self.__height))
