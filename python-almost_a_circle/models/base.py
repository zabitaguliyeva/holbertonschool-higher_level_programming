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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json to string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        data = []
        filename = f"{cls.__name__}.json"
        if list_objs is not None:
            for obj in list_objs:
                data.append(obj.to_dictionary())
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(data))
