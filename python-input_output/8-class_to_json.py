#!/usr/bin/python3
"""Class to JSON"""
import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)
