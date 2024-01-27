#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    elif idx > len(my_list):
        return
    else:
        for i in my_list:
            if idx == i:
                return i + 1
