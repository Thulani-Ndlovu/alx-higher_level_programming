#!/usr/bin/python3
'''Class inheritance'''
from models.base import Base


class Rectangle(Base):
    '''private attributes'''
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    '''Class constructor'''
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    '''height getter'''
    @property
    def height(self):
        return self.__height

    '''height setter'''
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    '''x getter'''
    @property
    def x(self):
        return self.__x

    '''x setter'''
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    '''y getter'''
    @property
    def y(self):
        return self.__y

    '''y setter'''
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    '''Area'''
    def area(self):
        '''returns the area'''
        return self.__width * self.__height

    '''Display function'''
    def display(self):
        '''print rectangle with # characters'''
        count = 0
        for a in range(self.__y):
            print("")
        for i in range(self.__height):
            for j in range(self.__x+self.__width):
                if (count < self.__x):
                    print(" ", end="")
                    count += 1
                else:
                    print("#", end="")
            count = 0
            print("")

    '''Overriding __str__ method'''
    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    '''Update function'''
    def update(self, *vals):
        '''assigns an valument to each attribute'''
        if vals and len(vals) != 0:
            count = 0
            for val in vals:
                if count == 0:
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif count == 1:
                    self.width = val
                elif count == 2:
                    self.height = val
                elif count == 3:
                    self.x = val
                elif count == 4:
                    self.y = val
                count += 1
