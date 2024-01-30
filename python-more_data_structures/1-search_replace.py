#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    new_list.append(list(map(lambda replace: i == replace if i == search, my_list)))
    return new_list
