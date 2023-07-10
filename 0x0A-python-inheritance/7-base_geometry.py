#!/usr/bin/python3
'''Class definition'''


class BaseGeometry:
    '''class implementation'''
    def area(self):
        """Raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raise:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
