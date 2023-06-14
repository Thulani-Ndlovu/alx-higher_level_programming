#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    Keys = list(a_dictionary.keys())
    Keys.sort()
    sortedDict = {i: a_dictionary[i] for i in Keys}
    for i, j in sortedDict.items():
        print("{}: {}".format(i, j))
