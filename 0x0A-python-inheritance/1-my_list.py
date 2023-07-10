#!/usr/bin/python3
"""Class inheritance"""
list = __import__('0-lookup').lookup


class MyList(list):
    def print_sorted(self):
        '''prints sorted list in ascending order'''
        print(sorted(self))
