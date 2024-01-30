#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = max(zip(a_dictionary.keys(), a_dictionary.values()))[0]
    return max_key
