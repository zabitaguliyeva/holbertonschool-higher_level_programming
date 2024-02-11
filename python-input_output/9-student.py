#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """init module"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To json function"""
        return vars(self)
