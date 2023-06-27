#!/usr/bin/python3
'''Class Square declaration'''


class Square:
    '''Square constructor'''
    def __init__(self, size=0, position=(0, 0)):
        '''
            Args:
                size (int): integer value
                position (int, int): tuple
            '''

        self.__size = size
        self.__position = position

    '''Area of the square'''
    def area(self):
        return self.__size * self.__size

    '''Size Getter'''
    @property
    def size(self):
        return self.__size

    '''Size Setter'''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    '''Position Getter'''
    @property
    def position(self):
        return self.__position

    '''Position Setter'''
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(val, int) for val in value) or not
                all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    '''Print Square characters'''
    def my_print(self):
        if self.__size > 0:
            [print("") for i in range(self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for j in range(self.__size)]
                print("")
        elif self.__size == 0:
            print("")
