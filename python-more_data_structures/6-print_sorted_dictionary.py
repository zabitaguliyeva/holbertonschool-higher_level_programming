#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = dict(sorted(a_dictionary.items()))
    for i in new_dict.keys():
        print("{}: {}".format(i, new_dict[i]))
