#!/usr/bin/python3
"""Subclass definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implementation of square."""

    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
