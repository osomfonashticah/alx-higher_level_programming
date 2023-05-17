#!/usr/bin/python3

def search_replace(my_list, search, replace):
    lists = my_list[:]
    for i in range(len(lists)):
        if lists[i] == search:
            lists[i] = replace
    return lists
