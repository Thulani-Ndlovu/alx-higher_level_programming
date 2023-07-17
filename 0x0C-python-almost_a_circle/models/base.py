#!/bin/python3
'''Class definition'''


class Base:

    __nb_objects = 0
    '''Class constructor'''
    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
