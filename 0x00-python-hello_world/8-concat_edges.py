#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("object-oriented programming "):str.find("object-oriented programming ")+28] + str[str.find("with"):str.find("with")+5] + str[str.find("Python"):str.find("Python")+6]
print(str)
