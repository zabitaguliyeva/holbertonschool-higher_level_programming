#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        self.__width.integer_validator(value, "width", False)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height.integer_validator(value, "height", False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x.integer_validator(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y.integer_validator(value, "y")
        self.__y = value

    def integer_validator(self, value, name, equal=True):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif equal and value < 0:
            raise ValueError("{} must be > 0".format(name))
        elif not equal and value <= 0:
            raise ValueError("{} must be >= 0".format(name))
