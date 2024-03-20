#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = [replace if ele == search else ele for ele in my_list ]
    return newList
