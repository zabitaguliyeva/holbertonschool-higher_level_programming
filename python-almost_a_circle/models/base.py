#!/usr/bin/python3
"""Base class"""
import json


class Base():
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Json to string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
