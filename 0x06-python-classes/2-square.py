#!/usr/bin/python3
'''A class named Square is defined below'''


class Square:
    '''Square constructor'''
    def __init__(self, size=0):
        '''
            Args:
                size (int): integer value
            '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
