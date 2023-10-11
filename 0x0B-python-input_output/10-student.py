#!/usr/bin/python3
"""
Contains the Class Student
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation
        of a Student instance with specified attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for x in attrs:
            try:
                new_dict[x] = self.__dict__[x]
            except:
                pass
        return new_dict
