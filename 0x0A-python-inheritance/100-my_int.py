#!/usr/bin/python3
"""class inheriting from int"""


class MyInt(int):
    """Invert the operators == , and !="""

    def __eq__(self, value):
        """Overrides  the  == operator with !=. operator"""
        return self.real != value

    def __ne__(self, value):
        """Overrides the != operator with == operator."""
        return self.real == value
