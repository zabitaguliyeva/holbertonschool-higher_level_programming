#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    original_list_copy = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return original_list_copy
    else:
        original_list_copy[idx] = element
        return original_list_copy
