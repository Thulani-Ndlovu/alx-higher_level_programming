#!/usr/bin/python3
"""Function Definition"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
