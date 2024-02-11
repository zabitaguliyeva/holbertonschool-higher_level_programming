#!/usr/bin/python3
"""Load, add, save"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
    my_list.extend(args[1:])
except FileNotFoundError:
    my_list = []
save_to_json_file(my_list, filename)
