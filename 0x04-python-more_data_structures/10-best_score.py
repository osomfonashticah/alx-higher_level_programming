#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    max = 0
    for key in a_dictionary:
        if a_dictionary[key] > max:
            max = dic[key]
    return key
