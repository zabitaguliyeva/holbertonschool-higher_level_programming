#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return max(zip(a_dictionary.keys(), a_dictionary.values()))[0]
    else:
        return None
