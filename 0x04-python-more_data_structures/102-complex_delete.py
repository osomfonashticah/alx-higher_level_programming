#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if not isinstance(a_dictionary, dict):
        return a_dictionary

    delete_keys = []

    for key, val in a_dictionary.items():
        if val == value:
            delete_keys.append(key)

    for key in delete_keys:
        del a_dictionary[key]

    return a_dictionary
