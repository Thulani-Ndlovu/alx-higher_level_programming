#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    Keys = list(a_dictionary.keys())
    for x in Keys:
        if value == a_dictionary.get(x):
            del a_dictionary[x]
    return (a_dictionary)
