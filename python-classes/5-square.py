#!/usr/bin/python3
"""Access and update private attribute"""


class Square:
    """Why a getter and setter?"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """Getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
