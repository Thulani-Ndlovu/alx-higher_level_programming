#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    uniqueTally = 0
    for i in unique:
        uniqueTally += i
    return uniqueTally
