#!/usr/bin/python3
"""Function definition"""


def add_attribute(obj, att, value):
    """
    Raise:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
