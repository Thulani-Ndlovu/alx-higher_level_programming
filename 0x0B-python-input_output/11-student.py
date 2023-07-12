#!/usr/bin/python3
'''Class definition'''


class Student:
    '''Constructor'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        if (type(attrs) == list and
                all(type(a) == str for a in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replace all attributes of the Student.'''
        for i, j in json.items():
            setattr(self, i, j)
