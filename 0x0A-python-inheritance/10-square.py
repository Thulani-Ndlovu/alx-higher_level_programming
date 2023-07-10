#!/usr/bin/python3
"""subclass definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square implementation"""

    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
