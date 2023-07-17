#!/usr/bin/python3
'''Class inheritance'''
from models.base import Base


class Rectangle(Base):
    '''Private attributes'''
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    '''Class constructor'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    '''width getter'''
    @property
    def width(self):
        return self.__width

    '''width setter'''
    @width.setter
    def width(self, value):
        self.__width = value

    '''height getter'''
    @property
    def height(self):
        return self.__height

    '''height setter'''
    @height.setter
    def height(self, value):
        self.__height = value

    '''x getter'''
    @property
    def x(self):
        return self.__x

    '''x setter'''
    @x.setter
    def x(self, value):
        self.__x = value

    '''y getter'''
    @property
    def y(self):
        return self.__y

    '''y setter'''
    @y.setter
    def y(self, value):
        self.__y = value
