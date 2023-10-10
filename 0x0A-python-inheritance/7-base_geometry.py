#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """A class with Public instance methods area and integer_validator"""
    def area(self):
        """Raise an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer and > 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
