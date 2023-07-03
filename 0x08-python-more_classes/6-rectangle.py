#!/usr/bin/python3
'''Reactangle Class Definition'''


class Rectangle:

    '''Number of instances'''
    number_of_instances = 0

    '''Class Constructor'''
    def __init__(self, width=0, height=0):
        '''
            Args:
                width (int): integer value
                height (int): integer value
        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height
            type(self).number_of_instances += 1

    '''width getter'''
    @property
    def width(self):
        return self.__width

    '''width setter'''
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    '''height getter'''
    @property
    def height(self):
        return self.__height

    '''height setter'''
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    '''Area of a rectangle'''
    def area(self):
        return self.__height * self.__width

    '''Perimeter of a rectangle'''
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    '''Printing rectangle with # character'''
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i != self.__height - 1:
                rectangle.append("\n")
        return ''.join(rectangle)

    '''String representation of the Rectangle'''
    def __repr__(self):
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    '''Printing a message at every delete instance of Rectangle'''
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
